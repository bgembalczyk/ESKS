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
    for i in students_live_together(students):
        roommates = []
        for j in i:
            print(j)
            print(j.preference)
            print()
            roommates.append(j.preference)
        tmp = combined_segment_types(roommates)
        for j in tmp:
            print(j)
        print("\n")


