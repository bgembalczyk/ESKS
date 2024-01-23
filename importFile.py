from student import Student
from dormitory import Dormitory
from segmentType import SegmentType
import json

def input_dorms(path):
    with open(path, "r", encoding='utf-8') as file:
        dorms = []
        dorms_tmp = json.load(file)
        for dorm in dorms_tmp["dorms"]:
            new_dorm = Dormitory(dorm["name"], dorm["habitable"], dorm["location"])
            new_dorm.input_rooms(dorm["rooms"])
            dorms.append(new_dorm)
    return dorms

def input_students(path):
    with open(path, "r") as file:
        students = []
        for line in file:
            stud_tmp = line[:-1].split(";")
            stud_id, stud_year, stud_sex, stud_faculty, stud_major, stud_city, stud_lang, pref_roommate, pref_dorm, pref_segment, pref_location, pref_tenants_num_room, pref_tenants_num_segment, pref_condition, pref_bathroom, pref_kitchen, pref_ad = stud_tmp
            try:
                pref_roommate = eval(pref_roommate)
            except (NameError, SyntaxError):
                pass
            try:
                pref_dorm = eval(pref_dorm)
            except (NameError, SyntaxError):
                pass
            try:
                pref_segment = eval(pref_segment)
            except (NameError, SyntaxError):
                pass
            try:
                pref_location = eval(pref_location)
            except (NameError, SyntaxError):
                pass
            try:
                pref_tenants_num_room = eval(pref_tenants_num_room)
            except (NameError, SyntaxError):
                pass
            try:
                pref_tenants_num_segment = eval(pref_tenants_num_segment)
            except (NameError, SyntaxError):
                pass
            try:
                pref_condition = eval(pref_condition)
            except (NameError, SyntaxError):
                pass
            try:
                pref_bathroom = eval(pref_bathroom)
            except (NameError, SyntaxError):
                pass
            try:
                pref_kitchen = eval(pref_kitchen)
            except (NameError, SyntaxError):
                pass
            try:
                pref_ad = eval(pref_ad)
            except (NameError, SyntaxError):
                pass
            stud_pref = SegmentType(pref_dorm, pref_location, pref_tenants_num_room, pref_tenants_num_segment, pref_condition, pref_bathroom, pref_kitchen, pref_ad)
            new_stud = Student(int(stud_id), int(stud_year), stud_sex, stud_faculty, stud_major, stud_city, stud_lang, pref_roommate, (pref_dorm, pref_segment), stud_pref)
            students.append(new_stud)
        return students
