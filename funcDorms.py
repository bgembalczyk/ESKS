from segmentType import SegmentType

# def accommodationAction(studentsToAccommodate: list, dorms: dict) -> None:
#     while studentsToAccommodate:
#         tmpStudent = studentsToAccommodate[0]
#         tmpSegment = dorms[tmpStudent.prefDorm].find_place(tmpStudent)
#         if not tmpSegment:
#             for dorm_name in dorms:
#                 tmpSegment = dorms[dorm_name].find_place(tmpStudent)
#                 if tmpSegment:
#                     break
#         if not tmpSegment:
#             print("There's not enough places in dorms!!!")
#             print(len(studentsToAccommodate))
#             print(studentsToAccommodate)
#             break
#         tmpStudent.accommodate(tmpSegment)
#         studentsToAccommodate.pop(0)

def get_specific_segment(dorms, pref_seg_num):
    pref_dorm = pref_seg_num[0]
    pref_room = int(pref_seg_num[1][:-1])
    pref_segment = pref_seg_num[1][-1]
    for dorm in dorms:
        if dorm.name == pref_dorm:
            room = dorm.get_room(pref_room)
            if room is not None:
                segment = room.get_segment(pref_segment)
                return segment
    return None

def available_configurations(dorms):
    all_configs = []
    result = []
    for dorm in dorms:
        all_configs += dorm.segment_types(True)
    # TODO
    # zliczanie wolnych miejsc w przypadku w części zajętego pokoju bardziej nie działa niż działa
    for dorm in dorms:
        for config in dorm.segment_types():
            result.append({"configuration": config, "beds": all_configs.count(config) * config.tenants_num_segment, "students": []})
    return result

def combined_segment_types(roommates):
    new_dorm = []
    new_location = []
    new_tenants_num_room = []
    new_tenants_num_segment = []
    new_condition = None
    new_bathroom = None
    new_kitchen = None
    new_ad = None

    for student in roommates:
        roommate = student.preference
        if roommate.dorm is not None and roommate.dorm not in new_dorm:
            new_dorm.append(roommate.dorm)
        if roommate.location is not None and roommate.location not in new_location:
            new_location.append(roommate.location)
        if roommate.tenants_num_room is not None:
            new_tenants_num_room.append(roommate.tenants_num_room)
        if roommate.tenants_num_segment is not None:
            new_tenants_num_segment.append(roommate.tenants_num_segment)
        if new_condition != "renovated":
            if roommate.condition == "renovated":
                new_condition = "renovated"
            elif roommate.condition == "normal" and new_condition != "normal":
                new_condition = "normal"
            elif roommate.condition == "old" and new_condition is None:
                new_condition = "old"
        if new_bathroom != "full":
            if roommate.bathroom == "full":
                new_bathroom = "full"
            elif roommate.bathroom == "shower" and new_bathroom != "shower":
                new_bathroom = "shower"
            elif roommate.bathroom == "null" and new_bathroom is None:
                new_bathroom = "null"
        if new_kitchen is not True:
            if roommate.kitchen is not None:
                new_kitchen = roommate.kitchen
        if new_ad is not False:
            if roommate.ad is not None:
                new_ad = roommate.ad

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
            result.append(SegmentType(dorm, location, new_tenants_num_room, new_tenants_num_segment, new_condition, new_bathroom, new_kitchen, new_ad))
    return result

def is_correct_location(dorm_name, dorm_location):
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
    for dorm in dorms:
        for room in dorm.rooms:
            for segment in room.segments:
                if segment.type() == segment_type and segment.habitable and segment.tenants_num() < segment.beds:
                    return segment
    return None
