from student import Student
from dormitory import Dormitory
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

def input_students(path: str) -> list:
    with open(path, "r") as file:
        students = []
        for line in file:
            tmp = line[:-1].split(";")
            stud_tmp = tmp[:7]
            stud_id, stud_year, stud_sex, stud_faculty, stud_major, stud_city, stud_lang = stud_tmp
            preference = tmp[7:]
            new_stud = Student(stud_id, stud_year, stud_sex, stud_faculty, stud_major, stud_city, stud_lang, preference)
            print(new_stud)
            students.append(new_stud)
        file.close()
        return students
