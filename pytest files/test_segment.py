import pytest
from segment import Segment
from room import Room
from dormitory import Dormitory
from student import Student
from segmentType import SegmentType
from exceptions.segment import *

def test_segment():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    assert segment

def test_segment_miss_arg():
    with pytest.raises(TypeError):
        Segment()

def test_segment_room():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    assert segment.room is room

def test_segment_wrong_room():
    with pytest.raises(WrongRoom):
        Segment(1, "A", True, 1)

def test_segment_symbol():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    assert segment.symbol == "A"

def test_segment_symbol_not_str():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    with pytest.raises(SymbolNotStr):
        Segment(room, 1, True, 1)

def test_segment_wrong_symbol():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    with pytest.raises(WrongSymbol):
        Segment(room, "?", True, 1)

def test_segment_habitable():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    assert segment.habitable

def test_segment_wrong_habitable():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    with pytest.raises(WrongHabitable):
        Segment(room, "A", 1, 1)

def test_segment_beds():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    pass

def test_segment_beds_not_int():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    with pytest.raises(BedsNotInt):
        Segment(room, "A", True, True)

def test_segment_wrong_beds():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    with pytest.raises(WrongBeds):
        Segment(room, "A", True, -1)

def test_segment_tenants():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student.accommodate(segment)
    assert segment.tenants[0] is student

def test_segment_tenants_num():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student.accommodate(segment)
    assert segment.tenants_num() == 1

def test_segment__str__():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    string = f"\t\tSegment A\n\t\tLiczba łóżek: 1\n\t\tLiczba mieszkańców: 0\n"
    assert str(segment) == string

def test_segment__lt__():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment1 = Segment(room, "A", True, 1)
    segment2 = Segment(room, "B", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment1)
    room.segments.append(segment2)
    assert segment1 < segment2

def test_segment__lt__fail():
    dormitory = Dormitory("Sezam", True, "Powiśle")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment1 = Segment(room, "A", True, 1)
    segment2 = Segment(room, "B", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment1)
    room.segments.append(segment2)
    assert not segment2 < segment1

def test_segment_type():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    assert segment.type() == SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
