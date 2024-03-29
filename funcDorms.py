from segmentType import SegmentType
from exceptions.rest import WrongSegmentReference, NotFound
import exceptions.dormitory
import exceptions.room

def get_dorm(dorms, dorm_name):
    # Get a dormitory by name
    for dorm in dorms:
        if dorm.name == dorm_name:
            return dorm

def get_specific_segment(dorms, pref_seg_num):
    # Get a specific segment based on preferences
    try:
        pref_dorm = pref_seg_num[0]
    except (TypeError, ValueError):
        raise WrongSegmentReference
    try:
        pref_room = int(pref_seg_num[1][:-1])
    except (TypeError, ValueError):
        raise WrongSegmentReference
    try:
        pref_segment = pref_seg_num[1][-1]
    except (TypeError, ValueError):
        raise WrongSegmentReference
    for dorm in dorms:
        if dorm.name == pref_dorm:
            try:
                room = dorm.get_room(pref_room)
                try:
                    segment = room.get_segment(pref_segment)
                    return segment
                except exceptions.room.SegmentNotFound:
                    raise NotFound
            except exceptions.dormitory.RoomNotFound:
                raise NotFound

def available_configurations(dorms):
    # Find available configurations in dormitories
    all_configs = []
    result = []
    for dorm in dorms:
        all_configs += dorm.segment_types(True)
    for dorm in dorms:
        for config in dorm.segment_types():
            new_config = {
                "configuration": config,
                "beds": all_configs.count(config) * config.tenants_num_segment,
                "students": []
            }
            result.append(new_config)
    return result

def combined_segment_types(roommates):
    # Combine segment types based on roommate preferences
    new_dorm = []
    new_location = []
    new_tenants_num_room = []
    new_tenants_num_segment = []
    new_condition = None
    new_bathroom = None
    new_kitchen = None
    new_ad = None

    for student in roommates:
        roommate_pref = student.preference
        if roommate_pref.dorm is not None and roommate_pref.dorm not in new_dorm:
            new_dorm.append(roommate_pref.dorm)
        if roommate_pref.location is not None and roommate_pref.location not in new_location:
            new_location.append(roommate_pref.location)
        if roommate_pref.tenants_num_room is not None:
            new_tenants_num_room.append(roommate_pref.tenants_num_room)
        if roommate_pref.tenants_num_segment is not None:
            new_tenants_num_segment.append(roommate_pref.tenants_num_segment)
        if new_condition != "renovated":
            if roommate_pref.condition == "renovated":
                new_condition = "renovated"
            elif roommate_pref.condition == "normal" and new_condition != "normal":
                new_condition = "normal"
            elif roommate_pref.condition == "old" and new_condition is None:
                new_condition = "old"
        if new_bathroom != "full":
            if roommate_pref.bathroom == "full":
                new_bathroom = "full"
            elif roommate_pref.bathroom == "shower" and new_bathroom != "shower":
                new_bathroom = "shower"
            elif roommate_pref.bathroom == "null" and new_bathroom is None:
                new_bathroom = "null"
        if new_kitchen is not True:
            if roommate_pref.kitchen is not None:
                new_kitchen = roommate_pref.kitchen
        if new_ad is not False:
            if roommate_pref.ad is not None:
                new_ad = roommate_pref.ad

    if len(new_dorm) == 0:
        new_dorm = [None]
    if len(new_location) == 0:
        new_location = [None]
    if len(new_tenants_num_segment) == 0:
        new_tenants_num_segment = [0]
    if len(new_tenants_num_room) == 0:
        new_tenants_num_room = [0]
    new_tenants_num_segment = max(len(roommates), min(new_tenants_num_segment))
    new_tenants_num_room = max(len(roommates), min(new_tenants_num_room))

    result = []
    for dorm in new_dorm:
        for location in new_location:
            tenants_room = new_tenants_num_room
            tenants_segment = new_tenants_num_segment
            condition = new_condition
            bathroom = new_bathroom
            kitchen = new_kitchen
            ad = new_ad
            result.append(SegmentType(dorm, location, tenants_room, tenants_segment, condition, bathroom, kitchen, ad))
    return result

def is_correct_location(dorm_name, dorm_location):
    # Check if the dormitory location is correct based on dorm name
    if None in [dorm_name, dorm_location]:
        return True
    if dorm_location == "Ochota" and dorm_name not in ["Akademik", "Babilon", "Bratniak", "Muszelka", "Tulipan"]:
        return False
    if dorm_location == "Kampus Centralny" and dorm_name not in ["Mikrus", "Riviera"]:
        return False
    if dorm_location == "Mokotów" and dorm_name != "Tatrzańska":
        return False
    if dorm_location == "Wola" and dorm_name != "Ustronie":
        return False
    if dorm_location == "Kampus Południowy" and dorm_name != "Żaczek":
        return False
    return True

def find_segment_type(dorms, segment_type):
    # Find a segment type based on a given configuration in dormitories
    for dorm in dorms:
        for room in dorm.rooms:
            for segment in room.segments:
                if segment.type() == segment_type and segment.habitable and segment.tenants_num() < segment.beds:
                    return segment
    raise NotFound
