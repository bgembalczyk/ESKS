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
    return

def inputStudents(path: str) -> list:
    file = open(path, "r")
    students = []
    for line in file:
        tmp = line.split()
        students.append(Student(int(tmp[0]), int(tmp[1]), tmp[2], int(tmp[3])))
    file.close()
    return students

