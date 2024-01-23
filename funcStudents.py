from graphs import *
from funcDorms import *
from exceptions.rest import *
from exceptions.segmentType import Incomparable
from segmentType import SegmentType
from itertools import combinations

def get_student(USOSid, students):
    for student in students:
        if student.id == USOSid:
            return student
    raise NotFound

def students_roommates_pairs(students):
    result = []
    for student in students:
        if student.pref_roommate is not None:
            try:
                student_pair = [get_student(student.id, students), get_student(student.pref_roommate, students)]
                if student_pair[0].city == student_pair[1].city:
                    student_pair.sort()
                    result.append(student_pair)
            except NotFound:
                pass
    return result

def students_live_together(students):
    result = []
    edges = students_roommates_pairs(students)
    nodes = all_nodes(edges)
    for node in nodes:
        subgraph = find_connected_subgraph(node, edges)
        subgraph.sort()
        if subgraph not in result:
            result.append(subgraph)
    return result

def students_exact_segment(students, dorms):
    result = []
    for student in students:
        if None not in student.pref_segment:
            try:
                chosen_segment = get_specific_segment(dorms, student.pref_segment)
                if chosen_segment is not None:
                    if chosen_segment.habitable and chosen_segment.beds > chosen_segment.tenants_num():
                        result.append([student, chosen_segment.type()])
            except NotFound:
                pass
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
        min_conf = None
        for seg_conf in referral[1]:
            for conf_div in available_configs:
                if seg_conf == conf_div["configuration"]:
                    if min_segs > conf_div["beds"]:
                        min_segs = conf_div["beds"]
                        min_conf = seg_conf
        for conf_div in available_configs:
            if conf_div["configuration"] == min_conf:
                referral[1] = conf_div["configuration"]
                students.append(referral[0])
                break

    add_to_seg_conf_from_cat(students, flexible_students, available_configs, flexible_students)

    return available_configs

def compare_students(potential_roommates):
    result = 0
    for student_i in potential_roommates:
        for student_j in potential_roommates:
            if student_i != student_j:
                if student_i.pref_segment[1] is not None and student_j.pref_segment[1] is not None:
                    if student_i.pref_segment[0] == student_j.pref_segment[0] and student_i.pref_segment[1] != student_j.pref_segment[1]:
                        result += 500
                if student_i.sex != student_j.sex:
                    return 1000
                if student_i.city != student_j.city:
                    result += 100
                if student_i.lang != student_j.lang:
                    result += 100
                result += abs(student_i.year - student_j.year)
                if student_i.faculty != student_j.faculty:
                    result += 25
                if student_i.major == student_j.major:
                    result += 10
    return result

def find_best_roommates(potential_roommates, potential_combs):
    min_fit = 10000
    for comb in potential_combs:
        if compare_students(comb) < min_fit:
            min_fit = compare_students(comb)
    for comb in potential_combs:
        if compare_students(comb) == min_fit:
            for student in comb:
                potential_roommates.remove(student)
            print(min_fit)
            return comb
    return None

def divide_into_segments(potential_roommates, tenant_num_segment):
    result = []
    students_to_match = []
    for student in potential_roommates:
        if student.pref_segment[1] is not None:
            result.append([student])
        else:
            students_to_match.append(student)
    while len(students_to_match) > 0:
        min_fit = 1000
        min_seg = None
        for roommates in result:
            for student in students_to_match:
                if len(roommates) < tenant_num_segment:
                    tmp_fit = compare_students([student] + roommates)
                    if tmp_fit < min_fit:
                        min_fit = tmp_fit
                        min_seg = roommates
        if min_fit == 1000:
            result.append([students_to_match[0]])
            students_to_match.pop(0)
        else:
            for roommates in result:
                for student in students_to_match:
                    tmp_fit = compare_students([student] + roommates)
                    if tmp_fit == min_fit and min_seg == roommates:
                        roommates.append(student)
                        students_to_match.remove(student)
                        break
    return result

def students_live_together_into_segments(students, dorms):
    segment_configurations_tmp = available_configurations(dorms)
    segment_configurations = [seg_conf["configuration"] for seg_conf in segment_configurations_tmp]
    result = []
    roommates_groups = students_live_together(students)
    for roommates in roommates_groups:
        best_segment_type = []

        for student in roommates:
            if student.pref_segment[1] is not None:
                chosen_segment = get_specific_segment(dorms, student.pref_segment)
                if chosen_segment is not None:
                    if chosen_segment.habitable and chosen_segment.beds >= chosen_segment.tenants_num() + len(roommates):
                        best_segment_type.append(chosen_segment.type())

        combined_segment_type = combined_segment_types(roommates)
        correct_combined = []
        for seg_conf in combined_segment_type:
            if not is_correct_location(seg_conf.dorm, seg_conf.location):
                correct_combined += seg_conf.correct_location()
            else:
                correct_combined.append(seg_conf)
        if len(best_segment_type) == 0:
            for seg_conf_i in correct_combined:
                for seg_conf_j in segment_configurations:
                    if seg_conf_i == seg_conf_j:
                        if seg_conf_j not in best_segment_type:
                            best_segment_type.append(seg_conf_j)

        if len(best_segment_type) == 0:
            for seg_conf_i in correct_combined:
                for seg_conf_j in segment_configurations:
                    try:
                        if seg_conf_i < seg_conf_j:
                            if seg_conf_j not in best_segment_type:
                                best_segment_type.append(seg_conf_j)
                    except Incomparable:
                        pass

        if len(best_segment_type) == 0:
            for seg_conf_i in correct_combined:
                min_seg_conf = 1000000000
                for seg_conf_j in segment_configurations:
                    tmp = seg_conf_i - seg_conf_j
                    if seg_conf_j.tenants_num_segment >= len(roommates) and tmp < min_seg_conf:
                        min_seg_conf = tmp
            for seg_conf_i in correct_combined:
                for seg_conf_j in segment_configurations:
                    tmp = seg_conf_i - seg_conf_j
                    if seg_conf_j.tenants_num_segment >= len(roommates) and tmp == min_seg_conf:
                        if seg_conf_j not in best_segment_type:
                            best_segment_type.append(seg_conf_j)

        min_seg = 1000
        for best_seg_conf in best_segment_type:
            for seg_conf in segment_configurations_tmp:
                if best_seg_conf == seg_conf["configuration"] and seg_conf["beds"] < min_seg:
                    min_seg = seg_conf["beds"]
        for best_seg_conf in best_segment_type:
            for seg_conf in segment_configurations_tmp:
                if best_seg_conf == seg_conf["configuration"] and seg_conf["beds"] == min_seg:
                    result.append([roommates, best_seg_conf])
                    break
        for student in roommates:
            students.remove(student)
    return result
