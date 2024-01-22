from importFile import *
from inputOutput import *
from accommodationAction import accommodation_action

def check_places(dorms: dict) -> int:
    beds_available = 0
    tenants_num = 0
    for dorm_name in dorms:
        beds_available += dorms[dorm_name].beds()
        tenants_num += dorms[dorm_name].tenants_num()
    return beds_available - tenants_num


def seks() -> None:
    dorms = {}
    students_to_accommodate = []

    print(f"Witaj w Systemie Elektronicznego Kwaterowania Studentów!")
    inputTmp = input(f"Naciśnij dowolny przycisk oraz Enter, żeby rozpocząć\n")
    while inputTmp:
        inputTmp = input(f"Naciśnij 0, żeby wczytać dane testowe\n"
                         f"Naciśnij 1, żeby sprawdzić informacje o danym akademiku\n"
                         f"Naciśnij 2, żeby sprawdzić informacje o oczekujących studentach\n"
                         f"Naciśnij 3, żeby zmieniać informacje o akademikach\n"
                         f"Naciśnij 4, żeby złożyć wniosek o miejsce w akademiku\n"
                         f"Naciśnij 5, żeby przeprowadzić akcje kwaterunkową\n")
        if inputTmp == "0":
            students_to_accommodate = input_students("generatory/students.txt")
            dorms = input_dorms("generatory/dorms.txt")
            students_to_accommodate.sort()
        elif inputTmp == "1":
            display_dorm(dorms)
        elif inputTmp == "2":
            display_stud(students_to_accommodate)
        elif inputTmp == "3":
            edit_dorms(dorms)
        elif inputTmp == "4":
            pass
        elif inputTmp == "5":
            accommodation_action(students_to_accommodate, dorms)

        print(f"Aktualnie posiadamy: {check_places(dorms)} miejsc w naszych akademikach\n"
              f"{len(students_to_accommodate)} studentów czeka na zakwaterowanie")
