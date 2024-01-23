# Importing functions and classes from other modules
from funcStudents import students_live_together_into_segments, divide_into_segment_configurations, divide_into_segments
from funcDorms import get_specific_segment, find_segment_type
from exceptions.rest import NotFound
from exceptions.student import TooManyTenants

def accommodation_action(students, dorms):
    # Perform accommodation actions for students in dorms

    # Students living together are accommodated into suitable segments
    students_to_accommodation = students_live_together_into_segments(students, dorms)
    for student_seg in students_to_accommodation:
        chosen_segment = None
        # Check if students have a specific preferred segment
        for student in student_seg[0]:
            if student.pref_segment[1] is not None:
                # If the preferred segment exists and matches the type, choose it
                if get_specific_segment(dorms, student.pref_segment) is not None:
                    if student_seg[1] == get_specific_segment(dorms, student.pref_segment).type():
                        chosen_segment = get_specific_segment(dorms, student.pref_segment)
        # If no specific segment is found, find a suitable segment type
        if chosen_segment is None:
            chosen_segment = find_segment_type(dorms, student_seg[1])
        # Accommodate all students in the group to the chosen segment
        for student in student_seg[0]:
            student.accommodate(chosen_segment)

    # Divide students into segment configurations and further into segments
    segment_types_with_students = divide_into_segment_configurations(students, dorms)
    for type_students in segment_types_with_students:
        pot_mates = type_students["students"]
        num_stud_in_segment = type_students["configuration"].tenants_num_segment
        students_with_accommodation = divide_into_segments(pot_mates, num_stud_in_segment)
        for roommates in students_with_accommodation:
            chosen_segment = None
            # Check if roommates have a specific preferred segment
            for student in roommates:
                if student.pref_segment[1] is not None:
                    try:
                        # If the preferred segment exists and matches the type, choose it
                        if type_students["configuration"] == get_specific_segment(dorms, student.pref_segment).type():
                            chosen_segment = get_specific_segment(dorms, student.pref_segment)
                    except NotFound:
                        pass
            # If no specific segment is found, find a suitable segment type
            if chosen_segment is None:
                chosen_segment = find_segment_type(dorms, type_students["configuration"])
            # Accommodate all roommates to the chosen segment
            for student in roommates:
                try:
                    student.accommodate(chosen_segment)
                except TooManyTenants:
                    # If too many tenants, return them to the students list
                    students.append(student)

    # Repeating the accommodation process for any remaining students
    segment_types_with_students = divide_into_segment_configurations(students, dorms)
    for type_students in segment_types_with_students:
        pot_mates = type_students["students"]
        num_stud_in_segment = type_students["configuration"].tenants_num_segment
        students_with_accommodation = divide_into_segments(pot_mates, num_stud_in_segment)
        for roommates in students_with_accommodation:
            chosen_segment = None
            # Check if roommates have a specific preferred segment
            for student in roommates:
                if student.pref_segment[1] is not None:
                    # If the preferred segment exists and matches the type, choose it
                    if get_specific_segment(dorms, student.pref_segment) is not None:
                        if type_students["configuration"] == get_specific_segment(dorms, student.pref_segment).type():
                            chosen_segment = get_specific_segment(dorms, student.pref_segment)
            # If no specific segment is found, find a suitable segment type
            if chosen_segment is None:
                chosen_segment = find_segment_type(dorms, type_students["configuration"])
            # Accommodate all roommates to the chosen segment
            for student in roommates:
                student.accommodate(chosen_segment)
    return
