# from importFile import *
# from inputOutput import *
# from accommodationAction import accommodationAction
#
# def checkPlaces(dorms: dict) -> int:
#     bedsAvailable = 0
#     tenantsNum = 0
#     for dorm_name in dorms:
#         bedsAvailable += dorms[dorm_name].beds()
#         tenantsNum += dorms[dorm_name].tenants_num()
#     return bedsAvailable - tenantsNum
#
#
# def seks() -> None:
#     dorms = {}
#     studentsToAccommodate = []
#
#     print(f"Witaj w Systemie Elektronicznego Kwaterowania Studentów!")
#     inputTmp = input(f"Naciśnij dowolny przycisk oraz Enter, żeby rozpocząć\n")
#     while inputTmp:
#         inputTmp = input(f"Naciśnij 0, żeby wczytać dane testowe\n"
#                          f"Naciśnij 1, żeby sprawdzić informacje o danym akademiku\n"
#                          f"Naciśnij 2, żeby sprawdzić informacje o oczekujących studentach\n"
#                          f"Naciśnij 3, żeby zmieniać informacje o akademikach\n"
#                          f"Naciśnij 4, żeby złożyć wniosek o miejsce w akademiku\n"
#                          f"Naciśnij 5, żeby przeprowadzić akcje kwaterunkową\n")
#         if inputTmp == "0":
#             studentsToAccommodate = inputStudents("pliki do testów/students.txt")
#             dorms = inputDorms("pliki do testów/dorms.txt")
#             studentsToAccommodate.sort()
#         elif inputTmp == "1":
#             displayDorm(dorms)
#         elif inputTmp == "2":
#             displayStud(studentsToAccommodate)
#         elif inputTmp == "3":
#             editDorms(dorms)
#         elif inputTmp == "4":
#             pass
#         elif inputTmp == "5":
#             accommodationAction(studentsToAccommodate, dorms)
#
#         print(f"Aktualnie posiadamy: {checkPlaces(dorms)} miejsc w naszych akademikach\n"
#               f"{len(studentsToAccommodate)} studentów czeka na zakwaterowanie")
