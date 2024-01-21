import pytest
import exceptions.room
from exceptions.dormitory import *
from dormitory import Dormitory
from room import Room
from segment import Segment
from student import Student
from segmentType import SegmentType

def test_dorm():
    dormitory = Dormitory("Akademik", True, "Ochota")
    assert dormitory

def test_dorm_miss_arg():
    with pytest.raises(TypeError):
        Dormitory()

def test_dorm_name():
    dormitory = Dormitory("Akademik", True, "Ochota")
    assert dormitory.name == "Akademik"

def test_dorm_wrong_name():
    with pytest.raises(WrongName):
        Dormitory("Sezam", True, "Ochota")

def test_dorm_location():
    dormitory = Dormitory("Akademik", True, "Ochota")
    assert dormitory.location == "Ochota"

def test_dorm_wrong_location():
    with pytest.raises(WrongLocation):
        Dormitory("Akademik", True, "Ursynów")

def test_dorm_habitable():
    dormitory = Dormitory("Akademik", True, "Ochota")
    assert dormitory.habitable

def test_dorm_wrong_habitable():
    with pytest.raises(WrongHabitable):
        Dormitory("Akademik", 1, "Ochota")

def test_dorm_rooms():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    dormitory.rooms.append(room)
    assert dormitory.rooms[0] is room

def test_dorm__str__():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room1 = Room(dormitory, 1, True, "renovated", "full", True, False)
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment1A = Segment(room1, "A", True, 1)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room1.segments.append(segment1A)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room1)
    dormitory.rooms.append(room2)
    string = f"Dom Studencki Akademik\nLiczba pokoi: 2\nLiczba łóżek: 6\nLiczba mieszkańców: 0\n"
    assert str(dormitory) == string

def test_dorm_beds():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room1 = Room(dormitory, 1, True, "renovated", "full", True, False)
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment1A = Segment(room1, "A", True, 1)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room1.segments.append(segment1A)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room1)
    dormitory.rooms.append(room2)
    assert dormitory.beds() == 6

def test_dorm_tenants_num():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room1 = Room(dormitory, 1, True, "renovated", "full", True, False)
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment1A = Segment(room1, "A", True, 1)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room1.segments.append(segment1A)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room1)
    dormitory.rooms.append(room2)
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(320684, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student3 = Student(320685, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student4 = Student(320686, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student5 = Student(320687, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student6 = Student(320688, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student1.accommodate(segment2A)
    student2.accommodate(segment2A)
    student3.accommodate(segment2B)
    student4.accommodate(segment2B)
    student5.accommodate(segment2B)
    student6.accommodate(segment1A)
    assert dormitory.tenants_num() == 6


def test_dorm_get_room():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room2)
    assert dormitory.get_room(2) is room2

def test_dorm_get_room_none():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room2)
    with pytest.raises(RoomNotFound):
        dormitory.get_room(1)

def test_dorm_get_room_non_int():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room2)
    with pytest.raises(exceptions.room.NumberNotInt):
        dormitory.get_room(True)

def test_dorm_get_room_wrong_room_number():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room2 = Room(dormitory, 2, True, "renovated", "full", True, False)
    segment2A = Segment(room2, "A", True, 2)
    segment2B = Segment(room2, "B", True, 3)
    room2.segments.append(segment2A)
    room2.segments.append(segment2B)
    dormitory.rooms.append(room2)
    with pytest.raises(exceptions.room.WrongNumber):
        dormitory.get_room(-2)

def test_dorm_input_rooms():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room_tab = [
        {"number": 1, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": True, "beds": 1},
                      {"symbol": "B", "habitable": False, "beds": 2}]},
        {"number": 2, "habitable": True, "condition": "normal", "bathroom": "null", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": True, "beds": 1},
                      {"symbol": "B", "habitable": False, "beds": 2}]}]
    dormitory.input_rooms(room_tab)
    assert len(dormitory.rooms) == 2 and dormitory.beds() == 6

def test_dorm_segment_types():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room_tab = [
        {"number": 1, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": True, "beds": 1}]},
        {"number": 2, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": True, "beds": 1},
                      {"symbol": "B", "habitable": True, "beds": 2}]},
        {"number": 3, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": False, "beds": 1},
                      {"symbol": "B", "habitable": True, "beds": 2}]},
        {"number": 4, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": True, "beds": 1},
                      {"symbol": "B", "habitable": True, "beds": 2}]}]
    dormitory.input_rooms(room_tab)
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student.accommodate(dormitory.get_room(4).get_segment("A"))
    seg_types = [
        SegmentType("Akademik", "Ochota", 1, 1, "normal", "full", True, False),
        SegmentType("Akademik", "Ochota", 3, 1, "normal", "full", True, False),
        SegmentType("Akademik", "Ochota", 3, 2, "normal", "full", True, False)
    ]
    assert dormitory.segment_types() == seg_types

def test_dorm_segment_types_repeating():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room_tab = [
        {"number": 1, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": True, "beds": 1}]},
        {"number": 2, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": True, "beds": 1},
                      {"symbol": "B", "habitable": True, "beds": 2}]},
        {"number": 3, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": False, "beds": 1},
                      {"symbol": "B", "habitable": True, "beds": 2}]},
        {"number": 4, "habitable": True, "condition": "normal", "bathroom": "full", "kitchen": True, "ad": False,
         "segments": [{"symbol": "A", "habitable": True, "beds": 1},
                      {"symbol": "B", "habitable": True, "beds": 2}]}]
    dormitory.input_rooms(room_tab)
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student.accommodate(dormitory.get_room(4).get_segment("A"))
    seg_types = [
        SegmentType("Akademik", "Ochota", 1, 1, "normal", "full", True, False),
        SegmentType("Akademik", "Ochota", 3, 1, "normal", "full", True, False),
        SegmentType("Akademik", "Ochota", 3, 2, "normal", "full", True, False),
        SegmentType("Akademik", "Ochota", 3, 2, "normal", "full", True, False),
        SegmentType("Akademik", "Ochota", 3, 2, "normal", "full", True, False)
    ]
    assert dormitory.segment_types(True) == seg_types
