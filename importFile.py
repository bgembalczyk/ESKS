from student import Student
from dormitory import Dormitory
from segmentType import SegmentType
import json

def input_dorms(path):
    # Reads dormitory information from a JSON file and returns a list of Dormitory objects.
    with open(path, "r", encoding='utf-8') as file:
        dorms = []
        dorms_tmp = json.load(file)
        for dorm in dorms_tmp["dorms"]:
            new_dorm = Dormitory(dorm["name"], dorm["habitable"], dorm["location"])
            new_dorm.input_rooms(dorm["rooms"])
            dorms.append(new_dorm)
    return dorms

def input_students(path):
    # Reads student information from a text file and returns a list of Student objects.
    with open(path, "r") as file:
        students = []
        for line in file:
            stud_tmp = line[:-1].split(";")
            stud_id, stud_year, stud_sex, stud_faculty, stud_major, stud_city, stud_lang, pref_roommate, pref_dorm, pref_segment, pref_location, pref_tenants_num_room, pref_tenants_num_segment, pref_condition, pref_bathroom, pref_kitchen, pref_ad = stud_tmp

            def eval_pref(pref):
                # Helper function to evaluate preferences or set to None if evaluation fails
                try:
                    return eval(pref)
                except (NameError, SyntaxError):
                    return None

            stud_pref = SegmentType(
                eval_pref(pref_dorm),
                eval_pref(pref_location),
                eval_pref(pref_tenants_num_room),
                eval_pref(pref_tenants_num_segment),
                eval_pref(pref_condition),
                eval_pref(pref_bathroom),
                eval_pref(pref_kitchen),
                eval_pref(pref_ad)
            )

            new_stud = Student(
                int(stud_id),
                int(stud_year),
                stud_sex,
                stud_faculty,
                stud_major,
                stud_city,
                stud_lang,
                eval_pref(pref_roommate),
                (eval_pref(pref_dorm), eval_pref(pref_segment)),
                stud_pref
            )
            students.append(new_stud)
        return students
