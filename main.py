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
    divided_segments_conf = divide_into_segment_configurations(students, dorms)
    for item in divided_segments_conf:
        if len(item["students"]) != 0:
            print(item["configuration"])
            print(len(item["students"]))
            print()
            if item["configuration"].tenants_num_segment > 1:
                roommates_groups = divide_into_segments(item["students"], item["configuration"].tenants_num_segment)
                for roommates in roommates_groups:
                    for roommate in roommates:
                        print(roommate)
                        print()
                    print()
                print("\n")
