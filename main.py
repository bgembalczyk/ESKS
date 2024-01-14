import seks
from dormitory import Dormitory
from importFile import *
from funcStudents import *
from funcDorms import *
from segmentType import SegmentType

# 1. Studenci, którzy wskazali dorm i segment
# 2. Studenci, dla których istnieje dokładny typ segmentu
# 3. Studenci, dla których istnieje strictly better typ segmentu
# 4. jak 2, ale tam gdzie location nie odpowiada dorm
# 5. analogicznie do 4 dla 3
# 6. najbardziej zbliżony segment
#   dorm >> num_segment >> num_room >> condition >> bathroom >> kitchen >> ad

if __name__ == '__main__':
#    seks.seks()
    dorms = input_dorms("pliki do testów/dorms.json")
    students = input_students("pliki do testów/students.txt")
    segment_configs_counts = available_configurations(dorms)
    segment_configs = [segment_configuration["configuration"] for segment_configuration in segment_configs_counts]
    stud_cat0 = students_live_together(students)
    stud_cat2 = students_exact_segment_type(students, dorms)
    stud_cat3 = students_better_segment_type(students, dorms)
    stud_cat4 = students_that_dont_know_where_dorms_are(students, dorms)
    acc_studs = []
    for roommates in stud_cat0:
        for student in roommates:
            if student not in acc_studs:
                acc_studs.append(student)
    for student_pair in stud_cat2:
        if student_pair[0] not in acc_studs:
            acc_studs.append(student_pair[0])
    for student_pair in stud_cat3:
        if student_pair[0] not in acc_studs:
            acc_studs.append(student_pair[0])
    for student_pair in stud_cat4:
        if student_pair[0] not in acc_studs:
            acc_studs.append(student_pair[0])
    # def find_best_segment_type(students, dorms):
    for student in students:
        if student not in acc_studs:
            best_match = []
            min_tmp = 9999999
            for seg_conf in segment_configs:
                tmp = student.preference - seg_conf
                if tmp < min_tmp:
                    min_tmp = tmp
            if min_tmp == 1000000:
                print(student)
                print(student.preference)
                print(min_tmp)
                for seg_conf in segment_configs:
                    tmp = student.preference - seg_conf
                    if tmp == min_tmp:
                        print(f"test: {student.preference < seg_conf}")
                        best_match.append(seg_conf)
                        print(seg_conf)
                print()
