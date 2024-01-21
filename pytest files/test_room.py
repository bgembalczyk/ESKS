import pytest
import exceptions.segment
from exceptions.room import *
from segment import Segment
from room import Room
from dormitory import Dormitory
from student import Student
from segmentType import SegmentType

def test_room():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    assert room

def test_room_miss_arg():
    with pytest.raises(TypeError):
        Room()

def test_room_dorm():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    assert room.dorm == dormitory

def test_room_wrong_dorm():
    with pytest.raises(WrongDorm):
        Room(True, 1, True, "renovated", "full", True, False)

def test_room_number():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    assert room.number == 1

def test_room_number_not_int():
    dormitory = Dormitory("Akademik", True, "Ochota")
    with pytest.raises(NumberNotInt):
        Room(dormitory, True, True, "renovated", "full", True, False)

def test_room_wrong_number():
    dormitory = Dormitory("Akademik", True, "Ochota")
    with pytest.raises(Exception):
        Room(dormitory, -1, True, "renovated", "full", True, False)

def test_room_habitable():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    assert room.habitable

def test_room_wrong_habitable():
    dormitory = Dormitory("Akademik", True, "Ochota")
    with pytest.raises(WrongHabitable):
        Room(dormitory, 1, 1, "renovated", "full", True, False)

def test_room_condition():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    assert room.condition == "renovated"

def test_room_wrong_condition():
    dormitory = Dormitory("Akademik", True, "Ochota")
    with pytest.raises(WrongCondition):
        Room(dormitory, 1, True, "new", "full", True, False)

def test_room_bathroom():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    assert room.bathroom == "full"

def test_room_wrong_bathroom():
    dormitory = Dormitory("Akademik", True, "Ochota")
    with pytest.raises(Exception):
        Room(dormitory, 1, True, "renovated", "bathtub", True, False)

def test_room_kitchen():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    assert room.kitchen

def test_room_wrong_kitchen():
    dormitory = Dormitory("Akademik", True, "Ochota")
    with pytest.raises(Exception):
        Room(dormitory, 1, True, "renovated", "full", 1, False)

def test_room_ad():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    assert not room.ad

def test_room_wrong_ad():
    dormitory = Dormitory("Akademik", True, "Ochota")
    with pytest.raises(Exception):
        Room(dormitory, 1, True, "renovated", "full", True, 1)

def test_room_beds():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room2)
    assert room2.beds() == 5

def test_room_tenants_num():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room2)
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(320684, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student3 = Student(320685, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student4 = Student(320686, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student5 = Student(320687, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student1.accommodate(segment2A)
    student2.accommodate(segment2A)
    student3.accommodate(segment2B)
    student4.accommodate(segment2B)
    student5.accommodate(segment2B)
    assert room2.tenants_num() == 5

def test_room__str__():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 2, True, "renovated", "full", True, False)
    segmentA = Segment(room, "A", True, 2)
    segmentB = Segment(room, "B", True, 3)
    room.segments.append(segmentA)
    room.segments.append(segmentB)
    dormitory.rooms.append(room)
    string = f"\tNumer pokoju: 2\n\tLiczba łóżek: 5\n\tLiczba mieszkańców: 0\n\tLiczba segmentów: 2\n"
    assert str(room) == string

def test_room__lt__():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room1 = Room(dormitory, 1, True, "renovated", "full", True, False)
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    assert room1 < room2

def test_room__lt__fail():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room1 = Room(dormitory, 1, True, "renovated", "full", True, False)
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    assert not room2 < room1

def test_room_get_segments():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    assert room.get_segment("A") is segment

def test_room_get_segments_symbol_not_str():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(exceptions.segment.SymbolNotStr):
        room.get_segment(1)

def test_room_get_segments_symbol_too_long():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(exceptions.segment.WrongSymbol):
        room.get_segment("AB")

def test_room_get_segments_wrong_symbol():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(exceptions.segment.WrongSymbol):
        room.get_segment("#")

def test_room_input_segments():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segments_tab = [{"symbol": "A", "habitable": True, "beds": 1}, {"symbol": "B", "habitable": False, "beds": 2}]
    room.input_segments(segments_tab)
    assert len(room.segments) == len(segments_tab)
