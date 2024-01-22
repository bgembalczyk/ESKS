from dormitory import Dormitory
from room import Room
from segment import Segment


def display_dorm(dorms: dict) -> None:
    dorm_input = input("Podaj nazwę akademika: [/all] ")
    if dorm_input in dorms:
        print(dorms[dorm_input])
        tmp_room_input = input("Czy chcesz wyświetlić informacje o pokoju? [t/n] ")
        while tmp_room_input == "t":
            if tmp_room_input == "t":
                room_input = input("Podaj numer pokoju: ")
            for room in dorms[dorm_input].rooms:
                if tmp_room_input == "t":
                    if room.number() == int(room_input):
                        print(room)
                        break
            tmp_segment_input = input("Czy chcesz wyświetlić informacje o segmencie? [t/n]")
            while tmp_segment_input == "t":
                segment_input = input("Podaj symbol segmentu: ")
                for segment in room.segments:
                    if segment.symbol() == segment_input:
                        print(segment)
                        break
    elif dorm_input == "all":
        for dorm_name in dorms:
            print(dorms[dorm_name])
            for room in dorms[dorm_name].rooms:
                print(room)
                for segment in room.segments:
                    print(segment)
    else:
        print("Nie ma takiego akademika, akademiki PW to: ")
        tmp = ""
        for dorm_name in dorms:
            tmp += f"{dorm_name}, "
        if len(dorms):
            tmp = tmp[:-2]
        print(tmp)

def display_stud(students: list) -> None:
    N = int(input("Podaj dla ilu studentów chcesz wypisać informacje: "))
    for i in range(min(len(students), N)):
        print(students[i])

def edit_dorms(dorms: dict):
    tmp_input = input("Naciśnij 0, żeby wrócić\n"
                     "Naciśnij 1, żeby dodać akademik\n"
                     "Naciśnij 2, żeby edytować akademik\n"
                     "Naciśnij 3, żeby usunąć akademik\n")
    while tmp_input != "0":
        dorm_input = input("Podaj nazwę akademika: ")
        if dorm_input in dorms:
            if tmp_input == "1":
                print("Już jest akademik o takiej nazwie!")
            elif tmp_input == "2":
                edit_room(dorms[dorm_input])
            elif tmp_input == "3":
                dorms.pop(dorm_input)
        else:
            if tmp_input == "1":
                dorms[dorm_input] = Dormitory(dorm_input)
            else:
                print("Nie ma takiego akademika, akademiki PW to: ")
                tmp = ""
                for dorm_name in dorms:
                    tmp += f"{dorm_name}, "
                if len(dorms):
                    tmp = tmp[:-2]
                print(tmp)

        tmp_input = input("Naciśnij 0, żeby wrócić\n"
                         "Naciśnij 1, żeby dodać akademik\n"
                         "Naciśnij 2, żeby edytować akademik\n"
                         "Naciśnij 3, żeby usunąć akademik\n")

def edit_room(dorm_name: Dormitory):
    tmp_input = input("Naciśnij 0, żeby wrócić\n"
                     "Naciśnij 1, żeby dodać pokój\n"
                     "Naciśnij 2, żeby edytować pokój\n"
                     "Naciśnij 3, żeby usunąć pokój\n")
    while tmp_input != "0":
        int_input = int(input("Podaj numer pokoju: "))
        room_input = dorm_name.get_room(int_input)
        if room_input:
            if tmp_input == "1":
                print("Już jest pokój o takim numerze!")
            elif tmp_input == "2":
                edit_segment(room_input)
            elif tmp_input == "3":
                dorm_name.rooms.remove(room_input)
        else:
            if tmp_input == "1":
                dorm_name.rooms.append(Room(dorm_name, int_input))
            else:
                print(f"Nie ma takiego pokoju.\n"
                      f"Pokoje w Domu Studenckim {dorm_name.name()} mają numery od {dorm_name.rooms[0].number()} do {dorm_name.rooms[-1].number()}")

        tmp_input = input("Naciśnij 0, żeby wrócić\n"
                         "Naciśnij 1, żeby dodać pokój\n"
                         "Naciśnij 2, żeby edytować pokój\n"
                         "Naciśnij 3, żeby usunąć pokój\n")

def edit_segment(room: Room):
    tmp_input = input("Naciśnij 0, żeby wrócić\n"
                     "Naciśnij 1, żeby dodać segment\n"
                     "Naciśnij 2, żeby edytować segment\n"
                     "Naciśnij 3, żeby usunąć segment\n")
    while tmp_input != "0":
        chr_input = input("Podaj symbol segmentu: ")
        segment_input = room.get_segment(chr_input)
        if segment_input:
            if tmp_input == "1":
                print("Już jest segment o takim symbolu!")
            elif tmp_input == "2":
                if input("Czy chcesz zmienić liczbę łóżek? [t/n]") == "t":
                    beds = int(input("Podaj nową liczbę łóżek w segmencie: "))
                    while beds < len(segment_input.tenants):
                        print("Liczba łóżek nie może być mniejsza od ilości mieszkańców!")
                        beds = int(input("Podaj nową liczbę łóżek w segmencie: "))
            elif tmp_input == "3":
                room.segments.remove(segment_input)
        else:
            if tmp_input == "1":
                beds = int(input("Ile łóżek w segmencie? "))
                room.segments.append(Segment(room, chr(ord(room.segments[-1].symbol()) + 1), beds))
            else:
                print(f"Nie ma takiego segmentu.\n"
                      f"Segmenty w pokoju {room.segments} mają symbole od {room.segments[0].symbol()} do {room.segments[-1].symbol()}")

        tmp_input = input("Naciśnij 0, żeby wrócić\n"
                         "Naciśnij 1, żeby dodać pokój\n"
                         "Naciśnij 2, żeby edytować pokój\n"
                         "Naciśnij 3, żeby usunąć pokój\n")

