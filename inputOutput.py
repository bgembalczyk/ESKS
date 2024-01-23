from dormitory import Dormitory
from room import Room
from segment import Segment
from student import Student
from segmentType import SegmentType
from funcDorms import get_dorm
from exceptions.student import *
import exceptions.dormitory
import exceptions.room


def display_dorm(dorms):
    dorm_names = []
    for dorm in dorms:
        dorm_names.append(dorm.name)
    dorm_input = input("Podaj nazwę akademika: [/all] ")
    if dorm_input in dorm_names:
        print(get_dorm(dorms, dorm_input))
        tmp_room_input = input("Czy chcesz wyświetlić informacje o pokoju? [T/N] ").upper()
        while tmp_room_input == "T":
            if tmp_room_input == "T":
                room_input = input("Podaj numer pokoju: ")
            for room in dorm.rooms:
                if tmp_room_input == "T":
                    if room.number() == int(room_input):
                        print(room)
                        break
            tmp_segment_input = input("Czy chcesz wyświetlić informacje o segmencie? [T/N] ").upper()
            while tmp_segment_input == "T":
                segment_input = input("Podaj symbol segmentu: ")
                for segment in room.segments:
                    if segment.symbol() == segment_input:
                        print(segment)
                        break
    elif dorm_input == "all":
        for dorm in dorms:
            print(dorm)
            for room in dorm.rooms:
                print(room)
                for segment in room.segments:
                    print(segment)
    else:
        print("Nie ma takiego akademika, akademiki PW to: ")
        tmp = ""
        for dorm in dorms:
            tmp += f"{dorm.name}, "
        if len(dorms):
            tmp = tmp[:-2]
        print(tmp)

def print_to_file(dorms):
    students = []
    for dorm in dorms:
        for room in dorm.rooms:
            for segment in room.segments:
                for tenant in segment.tenants:
                    students.append(tenant)
    students.sort()
    with open("raport.txt", "w") as file:
        for student in students:
            file.write(f"{student.id} -> {student.segment.room.dorm.name} {student.segment.room.number}{student.segment.symbol}")

def display_stud(dorms):
    students = []
    for dorm in dorms:
        for room in dorm.rooms:
            for segment in room.segments:
                for tenant in segment.tenants:
                    students.append(tenant)
    students.sort()
    for student in students:
        print(f"{student.id} -> {student.segment.room.dorm.name} {student.segment.room.number}{student.segment.symbol}")

def edit(dorms):
    dorm_input = input("Podaj nazwę akademika, w którym chcesz wprowadzić zmiany: ")
    for dorm in dorms:
        if dorm.name == dorm_input:
            tmp_input = input(f"Czy chcesz włączyć lub wyłączyć z kwaterowania DS {dorm.name}? [T/N] ").upper()
            if tmp_input == "T":
                tmp_input = input(f"Ustaw aktualny status kwaterowania w DS {dorm.name}: [T/N] ").upper()
                if tmp_input == "T":
                    dorm.habitable = True
                elif tmp_input == "N":
                    dorm.habitable = False
            while tmp_input:
                tmp_input = input(f"Podaj numer pokoju w DS {dorm.name}, który chcesz włączyć lub wyłączyć z kwaterowania: ")
                try:
                    room = dorm.get_room(int(tmp_input))
                    tmp_input = input(f"Czy chcesz włączyć lub wyłączyć z kwaterowania pokój {room.number}? [T/N] ").upper()
                    if tmp_input == "T":
                        tmp_input = input(f"Ustaw aktualny status kwaterowania w pokoju {room.number}: [T/N] ").upper()
                        if tmp_input == "T":
                            room.habitable = True
                        elif tmp_input == "N":
                            room.habitable = False
                    while tmp_input:
                        tmp_input = input(f"Podaj symbol segmentu w pokoju {room.number}, który chcesz włączyć lub wyłączyć z kwaterowania: ")
                        try:
                            segment = room.get_segment(tmp_input)
                            tmp_input = input(f"Czy chcesz włączyć lub wyłączyć z kwaterowania segment {segment.symbol}? [T/N] ").upper()
                            if tmp_input == "T":
                                tmp_input = input(f"Ustaw aktualny status kwaterowania w segmencie {segment.symbol}: [T/N] ").upper()
                                if tmp_input == "T":
                                    segment.habitable = True
                                elif tmp_input == "N":
                                    segment.habitable = False
                        except (TypeError, ValueError):
                            print("Spróbuj jeszcze raz")
                        except exceptions.room.SegmentNotFound:
                            print(f"W pokoju {room.number} nie ma takiego segmentu\n"
                                  f"Segmenty w pokoju {room.number} mają symbole od {room.segments[0].symbol} do {room.segments[-1].symbol}")
                except (TypeError, ValueError):
                    print("Spróbuj jeszcze raz")
                except exceptions.dormitory.RoomNotFound:
                    print(f"W DS {dorm.name} nie ma takiego pokoju\n"
                          f"Pokoje w DS {dorm.name} mają numery od {dorm.rooms[0].number} do {dorm.rooms[-1].number}")

def input_single_student():
    while True:
        USOSid = input("Podaj swój numer USOSid: ")
        year = input("Podaj swój rok urodzenia: ")
        sex = input("Podaj swoją płeć: [M/F/O] ")
        faculty = input("Podaj wydział, na którym studiujesz: ")
        major = input("Podaj swój kierunek studiów: ")
        lang = input("Podaj język, w którym studiujesz: [polski/angielski] ")
        pref_dorm = input("Podaj preferowany akademik: ")
        try:
            student = Student(int(USOSid), int(year), sex, faculty, major, "Warszawa", lang, None, (pref_dorm, None), SegmentType(pref_dorm, None, None, None, None, None, None, None))
            return [student]
        except WrongId:
            print("Spróbuj jeszcze raz")
        except YearNotInt:
            print("Spróbuj jeszcze raz")
        except WrongSex:
            print("Spróbuj jeszcze raz")
        except WrongFaculty:
            print("Spróbuj jeszcze raz")
        except WrongMajor:
            print("Spróbuj jeszcze raz")
        except WrongLang:
            print("Spróbuj jeszcze raz")
        except WrongPrefDorm:
            print("Spróbuj jeszcze raz")
        except ValueError:
            print("Spróbuj jeszcze raz")
        except TypeError:
            print("Spróbuj jeszcze raz")

