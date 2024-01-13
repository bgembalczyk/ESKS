from graphs import *

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

def available_configurations(dorms):
    all_configs = []
    result = []
    for dorm in dorms:
        all_configs += dorm.segment_types(True)
    for dorm in dorms:
        for config in dorm.segment_types():
            result.append({"configuration": config, "count": all_configs.count(config)})
    return result

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
