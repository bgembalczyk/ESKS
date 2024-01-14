from graphs import *
from funcDorms import *
from segmentType import SegmentType

def get_student(USOSid, students):
    for student in students:
        if student.id == USOSid:
            return student
    return None

def students_roommates_pairs(students):
    result = []
    for student in students:
        if student.pref_roommate is not None:
            student_pair = [get_student(student.id, students), get_student(student.pref_roommate, students)]
            if student_pair[1] is not None:
                if student_pair[0].city == student_pair[1].city:
                    result.append(student_pair)
    return result

def students_live_together(students):
    result = []
    edges = students_roommates_pairs(students)
    nodes = all_nodes(edges)
    for node in nodes:
        tmp = find_connected_subgraph(node, edges)
        tmp.sort()
        if tmp not in result:
            result.append(tmp)
    return result

def students_exact_segment(students, dorms):
    result = []
    for student in students:
        if None not in student.pref_segment:
            chosen_segment = get_specific_segment(dorms, student.pref_segment)
            if chosen_segment is not None:
                if chosen_segment.habitable and chosen_segment.beds > chosen_segment.tenants_num():
                    result.append([student, chosen_segment.type()])
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
                if student.preference.dorm in [seg_conf.dorm, None] and student.preference.location in [seg_conf.location, None]:
                    if student.preference < seg_conf:
                        better_segments.append(seg_conf)
            if len(better_segments) > 0:
                result.append([student, better_segments])
    return result

def students_that_dont_know_where_dorms_are(students, dorms):
    result = []
    segment_configs_counts = available_configurations(dorms)
    segment_configs = [segment_configuration["configuration"] for segment_configuration in segment_configs_counts]
    for student in students:
        if not is_correct_location(student.preference.dorm, student.preference.location):
            matching_segment_types = []
            new_student_preference = student.preference.correct_location()
            for seg_conf in segment_configs:
                for stud_pref in new_student_preference:
                    if stud_pref == seg_conf:
                        matching_segment_types.append(seg_conf)
            if len(matching_segment_types) == 0:
                for seg_conf in segment_configs:
                    if student.preference.dorm == seg_conf.dorm or student.preference.location == seg_conf.location or student.preference.dorm is None or student.preference.location is None:
                        if student.preference < seg_conf:
                            matching_segment_types.append(seg_conf)
            if len(matching_segment_types) > 0:
                result.append([student, matching_segment_types])
    return result

def find_best_segment_type(students, dorms):
    result = []
    segment_configs_counts = available_configurations(dorms)
    segment_configs = [segment_configuration["configuration"] for segment_configuration in segment_configs_counts]
    for student in students:
        best_match = []
        min_tmp = 9999999
        for seg_conf in segment_configs:
            tmp = student.preference - seg_conf
            if tmp < min_tmp:
                min_tmp = tmp
        for seg_conf in segment_configs:
            tmp = student.preference - seg_conf
            if tmp == min_tmp:
                best_match.append(seg_conf)
        result.append([student, best_match])
    return result

def add_to_seg_conf_from_cat(students, students_to_accommodate, available_configs, flexible_students):
    for referral in students_to_accommodate:
        if type(referral[1]) is list and len(referral[1]) == 1:
            referral[1] = referral[1][0]
        if type(referral[1]) is not list:
            for config in available_configs:
                if referral[1] == config["configuration"] and len(config["students"]) < config["beds"]:
                    config["students"].append(referral[0])
                    students.remove(referral[0])
        else:
            flexible_students.append(referral)
            students.remove(referral[0])

def divide_into_segment_configurations(students, dorms):
    available_configs = available_configurations(dorms)
    flexible_students = []

    add_to_seg_conf_from_cat(students, students_exact_segment(students, dorms), available_configs, flexible_students)

    add_to_seg_conf_from_cat(students, students_exact_segment_type(students, dorms), available_configs, flexible_students)

    add_to_seg_conf_from_cat(students, students_better_segment_type(students, dorms), available_configs, flexible_students)

    add_to_seg_conf_from_cat(students, students_that_dont_know_where_dorms_are(students, dorms), available_configs, flexible_students)

    add_to_seg_conf_from_cat(students, find_best_segment_type(students, dorms), available_configs, flexible_students)

    for referral in flexible_students:
        min_segs = 1000
        for seg_conf in referral[1]:
            for conf_div in available_configs:
                if seg_conf == conf_div["configuration"]:
                    if min_segs > conf_div["beds"]:
                        min_segs = conf_div["beds"]
        for conf_div in available_configs:
            if min_segs == conf_div["beds"]:
                referral[1] = conf_div["configuration"]
                students.append(referral[0])
                break

    add_to_seg_conf_from_cat(students, flexible_students, available_configs, flexible_students)
