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
    # to chyba nie działa tak jak chciałem -> sprawdź screeny
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

def students_that_dont_know_where_dorms_are(students, dorms):
    result = []
    segment_configurations_count = available_configurations(dorms)
    segment_configurations = []
    for seg_conf in segment_configurations_count:
        segment_configurations.append(seg_conf["configuration"])
    for student in students:
        if not is_correct_location(student.preference.dorm, student.preference.location):
            matching_segment_types = []
            new_student_preference = student.preference.correct_location()
            for seg_conf in segment_configurations:
                for stud_pref in new_student_preference:
                    if stud_pref == seg_conf:
                        matching_segment_types.append(seg_conf)
            if len(matching_segment_types) == 0:
                for seg_conf in segment_configurations:
                    if student.preference.dorm == seg_conf.dorm or student.preference.location == seg_conf.location:
                        if student.preference < seg_conf:
                            matching_segment_types.append(seg_conf)
            result.append([student, matching_segment_types])
    return result
