import seks
from dormitory import Dormitory
from importFile import *
from accommodationAction import *

# 1. Studenci, którzy wskazali dorm i segment
# 2. Studenci, dla których istnieje dokładny typ segmentu
# 3. Studenci, dla których istnieje strictly better typ segmentu
# 4. jak 2, ale tam gdzie location nie odpowiada dorm
# 5. analogicznie do 4 dla 3

if __name__ == '__main__':
#    seks.seks()
    dorms = input_dorms("pliki do testów/dorms.json")
    students = input_students("pliki do testów/students.txt")
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
                print(student.id)
                print(student.preference)
                for bet_seg in better_segments:
                    print(bet_seg)
                print("\n")
