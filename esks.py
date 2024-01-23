from importFile import *
from inputOutput import *
from accommodationAction import accommodation_action

def check_places(dorms) -> int:
    beds_available = 0
    tenants_num = 0
    for dorm in dorms:
        beds_available += dorm.beds()
        tenants_num += dorm.tenants_num()
    return beds_available - tenants_num

def esks() -> None:
    students_to_accommodate = []

    print(f"Witaj w Elektronicznym Systemie Kwaterowania Studentów!")
    inputTmp = True
    dorms = input_dorms("dorms.json")
    while inputTmp:
        print(f"\nAktualnie posiadamy: {check_places(dorms)} miejsc w naszych akademikach\n"
              f"{len(students_to_accommodate)} studentów czeka na zakwaterowanie")
        inputTmp = input(f"Naciśnij 0, żeby zmieniać dane w systemie\n"
                         f"Naciśnij 1, żeby sprawdzić informacje o akademikach\n"
                         f"Naciśnij 2, żeby wypisać informacje o studentach zakwaterowanych w akademikach\n"
                         f"Naciśnij 3, żeby złożyć wniosek o miejsce w akademiku\n"
                         f"Naciśnij 4, żeby przeprowadzić akcje kwaterunkową\n"
                         f"Naciśnij enter, żeby zakończyć\n")
        if inputTmp == "0":
            edit(dorms)
        elif inputTmp == "1":
            display_dorm(dorms)
        elif inputTmp == "2":
            answer = input("Czy zapisać informacje do pliku raport.txt? [T/N] ").upper()
            if answer == "T":
                print_to_file(dorms)
            display_stud(dorms)
        elif inputTmp == "3":
            students_to_accommodate = input_single_student()
            accommodation_action(students_to_accommodate, dorms)
            pass
        elif inputTmp == "4":
            path = input("Podaj ścieżkę do pliku ze studentami: ")
            students_to_accommodate = input_students(path)
            accommodation_action(students_to_accommodate, dorms)
