# from dormitory import Dormitory
# from room import Room
# from segment import Segment
#
#
# def displayDorm(dorms: dict) -> None:
#     dormInput = input("Podaj nazwę akademika: [/all] ")
#     if dormInput in dorms:
#         print(dorms[dormInput])
#         tmpRoomInput = input("Czy chcesz wyświetlić informacje o pokoju? [t/n] ")
#         while tmpRoomInput == "t":
#             if tmpRoomInput == "t":
#                 roomInput = input("Podaj numer pokoju: ")
#             for room in dorms[dormInput].rooms:
#                 if tmpRoomInput == "t":
#                     if room.number() == int(roomInput):
#                         print(room)
#                         break
#             tmpSegmentInput = input("Czy chcesz wyświetlić informacje o segmencie? [t/n]")
#             while tmpSegmentInput == "t":
#                 segmentInput = input("Podaj symbol segmentu: ")
#                 for segment in room.segments:
#                     if segment.symbol() == segmentInput:
#                         print(segment)
#                         break
#     elif dormInput == "all":
#         for dorm_name in dorms:
#             print(dorms[dorm_name])
#             for room in dorms[dorm_name].rooms:
#                 print(room)
#                 for segment in room.segments:
#                     print(segment)
#     else:
#         print("Nie ma takiego akademika, akademiki PW to: ")
#         tmp = ""
#         for dorm_name in dorms:
#             tmp += f"{dorm_name}, "
#         if len(dorms):
#             tmp = tmp[:-2]
#         print(tmp)
#
# def displayStud(students: list) -> None:
#     N = int(input("Podaj dla ilu studentów chcesz wypisać informacje: "))
#     for i in range(min(len(students), N)):
#         print(students[i])
#
# def editDorms(dorms: dict):
#     tmpInput = input("Naciśnij 0, żeby wrócić\n"
#                      "Naciśnij 1, żeby dodać akademik\n"
#                      "Naciśnij 2, żeby edytować akademik\n"
#                      "Naciśnij 3, żeby usunąć akademik\n")
#     while tmpInput != "0":
#         dormInput = input("Podaj nazwę akademika: ")
#         if dormInput in dorms:
#             if tmpInput == "1":
#                 print("Już jest akademik o takiej nazwie!")
#             elif tmpInput == "2":
#                 editRoom(dorms[dormInput])
#             elif tmpInput == "3":
#                 dorms.pop(dormInput)
#         else:
#             if tmpInput == "1":
#                 dorms[dormInput] = Dormitory(dormInput)
#             else:
#                 print("Nie ma takiego akademika, akademiki PW to: ")
#                 tmp = ""
#                 for dorm_name in dorms:
#                     tmp += f"{dorm_name}, "
#                 if len(dorms):
#                     tmp = tmp[:-2]
#                 print(tmp)
#
#         tmpInput = input("Naciśnij 0, żeby wrócić\n"
#                          "Naciśnij 1, żeby dodać akademik\n"
#                          "Naciśnij 2, żeby edytować akademik\n"
#                          "Naciśnij 3, żeby usunąć akademik\n")
#
# def editRoom(dorm_name: Dormitory):
#     tmpInput = input("Naciśnij 0, żeby wrócić\n"
#                      "Naciśnij 1, żeby dodać pokój\n"
#                      "Naciśnij 2, żeby edytować pokój\n"
#                      "Naciśnij 3, żeby usunąć pokój\n")
#     while tmpInput != "0":
#         intInput = int(input("Podaj numer pokoju: "))
#         roomInput = dorm_name.get_room(intInput)
#         if roomInput:
#             if tmpInput == "1":
#                 print("Już jest pokój o takim numerze!")
#             elif tmpInput == "2":
#                 editSegment(roomInput)
#             elif tmpInput == "3":
#                 dorm_name.rooms.remove(roomInput)
#         else:
#             if tmpInput == "1":
#                 dorm_name.rooms.append(Room(dorm_name, intInput))
#             else:
#                 print(f"Nie ma takiego pokoju.\n"
#                       f"Pokoje w Domu Studenckim {dorm_name.name()} mają numery od {dorm_name.rooms[0].number()} do {dorm_name.rooms[-1].number()}")
#
#         tmpInput = input("Naciśnij 0, żeby wrócić\n"
#                          "Naciśnij 1, żeby dodać pokój\n"
#                          "Naciśnij 2, żeby edytować pokój\n"
#                          "Naciśnij 3, żeby usunąć pokój\n")
#
# def editSegment(room: Room):
#     tmpInput = input("Naciśnij 0, żeby wrócić\n"
#                      "Naciśnij 1, żeby dodać segment\n"
#                      "Naciśnij 2, żeby edytować segment\n"
#                      "Naciśnij 3, żeby usunąć segment\n")
#     while tmpInput != "0":
#         chrInput = input("Podaj symbol segmentu: ")
#         segmentInput = room.get_segment(chrInput)
#         if segmentInput:
#             if tmpInput == "1":
#                 print("Już jest segment o takim symbolu!")
#             elif tmpInput == "2":
#                 if input("Czy chcesz zmienić liczbę łóżek? [t/n]") == "t":
#                     beds = int(input("Podaj nową liczbę łóżek w segmencie: "))
#                     while beds < len(segmentInput.tenants):
#                         print("Liczba łóżek nie może być mniejsza od ilości mieszkańców!")
#                         beds = int(input("Podaj nową liczbę łóżek w segmencie: "))
#             elif tmpInput == "3":
#                 room.segments.remove(segmentInput)
#         else:
#             if tmpInput == "1":
#                 beds = int(input("Ile łóżek w segmencie? "))
#                 room.segments.append(Segment(room, chr(ord(room.segments[-1].symbol()) + 1), beds))
#             else:
#                 print(f"Nie ma takiego segmentu.\n"
#                       f"Segmenty w pokoju {room.segments} mają symbole od {room.segments[0].symbol()} do {room.segments[-1].symbol()}")
#
#         tmpInput = input("Naciśnij 0, żeby wrócić\n"
#                          "Naciśnij 1, żeby dodać pokój\n"
#                          "Naciśnij 2, żeby edytować pokój\n"
#                          "Naciśnij 3, żeby usunąć pokój\n")
#
