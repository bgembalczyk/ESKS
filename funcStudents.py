from graphs import *
from funcDorms import *
from segmentType import SegmentType

def get_student(USOSid, students):
    for student in students:
        if student.id == USOSid:
            return student
    return None

def student_pairs(students):
    result = []
    for student in students:
        if student.pref_roommate is not None:
            student_pair = [get_student(student.id, students), get_student(student.pref_roommate, students)]
            if student_pair[1] is not None:
                if student_pair[0].city == student_pair[1].city:
                    result.append(student_pair)
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

    for roommate in roommates:
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

def students_live_together(students):
    result = []
    edges = student_pairs(students)
    nodes = all_nodes(edges)
    for node in nodes:
        tmp = find_connected_subgraph(node, edges)
        tmp.sort()
        if tmp not in result:
            result.append(tmp)
    return result

def students_exact_segment_type(students, dorms):
    result = []
    segment_configs_counts = available_configurations(dorms)
    segment_configs = [segment_configuration["configuration"] for segment_configuration in segment_configs_counts]
    for student in students:
        student_acceptable_configs = []
        if student.preference in segment_configs:
            for seg_conf in segment_configs:
                if student.preference == seg_conf:
                    student_acceptable_configs.append(seg_conf)
            result.append([student, student_acceptable_configs])
    return result

def students_better_segment_type(students, dorms):
    result = []
    segment_configs_counts = available_configurations(dorms)
    segment_configs = [segment_configuration["configuration"] for segment_configuration in segment_configs_counts]
    for student in students:
        if student.preference not in segment_configs:
            better_segments = []
            for seg_conf in segment_configs:
                if student.preference.dorm == seg_conf.dorm and student.preference.location == seg_conf.location:
                    if student.preference < seg_conf:
                        better_segments.append(seg_conf)
            if len(better_segments) > 0:
                result.append([student, better_segments])
    return result
