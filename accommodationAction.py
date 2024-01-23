from importFile import *
from funcStudents import *
from funcDorms import *
from exceptions.student import *

def accommodation_action(students, dorms):
    students_to_accommodation = students_live_together_into_segments(students, dorms)
    for student_seg in students_to_accommodation:
        chosen_segment = None
        for student in student_seg[0]:
            if student.pref_segment[1] is not None:
                if get_specific_segment(dorms, student.pref_segment) is not None and student_seg[1] == get_specific_segment(dorms, student.pref_segment).type():
                    chosen_segment = get_specific_segment(dorms, student.pref_segment)
        if chosen_segment is None:
            chosen_segment = find_segment_type(dorms, student_seg[1])
        for student in student_seg[0]:
            student.accommodate(chosen_segment)

    segment_types_with_students = divide_into_segment_configurations(students, dorms)
    for type_students in segment_types_with_students:
        students_with_accommodation = divide_into_segments(type_students["students"], type_students["configuration"].tenants_num_segment)
        for roommates in students_with_accommodation:
            chosen_segment = None
            for student in roommates:
                if student.pref_segment[1] is not None:
                    try:
                        if type_students["configuration"] == get_specific_segment(dorms, student.pref_segment).type():
                            chosen_segment = get_specific_segment(dorms, student.pref_segment)
                    except NotFound:
                        pass
            if chosen_segment is None:
                chosen_segment = find_segment_type(dorms, type_students["configuration"])
            for student in roommates:
                try:
                    student.accommodate(chosen_segment)
                except TooManyTenants:
                    students.append(student)

    segment_types_with_students = divide_into_segment_configurations(students, dorms)
    for type_students in segment_types_with_students:
        students_with_accommodation = divide_into_segments(type_students["students"], type_students["configuration"].tenants_num_segment)
        for roommates in students_with_accommodation:
            chosen_segment = None
            for student in roommates:
                if student.pref_segment[1] is not None:
                    if get_specific_segment(dorms, student.pref_segment) is not None and type_students["configuration"] == get_specific_segment(dorms, student.pref_segment).type():
                        chosen_segment = get_specific_segment(dorms, student.pref_segment)
            if chosen_segment is None:
                chosen_segment = find_segment_type(dorms, type_students["configuration"])
            for student in roommates:
                student.accommodate(chosen_segment)
    return
