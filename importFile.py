from student import Student
from dormitory import Dormitory

def inputDorms(path: str) -> dict:
    file = open(path, "r")
    dorms = {}
    dormNames = []
    for line in file:
        tmp = line.split(";")
        tmp[-1] = tmp[-1][:-1].split(',')
        if tmp[0] not in dormNames:
            dorms[tmp[0]] = Dormitory(tmp[0])
            dormNames.append(tmp[0])
        dorms[tmp[0]].inputRooms(tmp[1:])
    file.close()
    return dorms

def inputStudents(path: str) -> list:
    file = open(path, "r")
    students = []
    for line in file:
        tmp = line.split()
        students.append(Student(int(tmp[0]), int(tmp[1]), tmp[2], int(tmp[3])))
    file.close()
    return students

