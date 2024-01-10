import seks
from dormitory import Dormitory
from importFile import *

if __name__ == '__main__':
    # seks.seks()
    dorms = input_dorms("pliki do testów/dorms.json")
    for dorm in dorms:
        print(dorm.name)
        segment_types = dorm.segment_types()
        for seg_type in segment_types:
            print(seg_type)
        print()
