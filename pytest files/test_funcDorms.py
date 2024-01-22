import pytest
from dormitory import Dormitory
from room import Room
from segment import Segment
from student import Student
from funcDorms import *
from exceptions.rest import *
from segmentType import SegmentType

def test_get_specific_segment():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    assert get_specific_segment(dorms, ("Akademik", "1A")) is segment

def test_get_specific_segment_fail_segment():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(NotFound):
        get_specific_segment(dorms, ("Akademik", "1B"))

def test_get_specific_segment_fail_room():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(NotFound):
        get_specific_segment(dorms, ("Akademik", "2A"))

def test_get_specific_fail1():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(WrongSegmentReference):
        get_specific_segment(dorms, True)

def test_get_specific_fail2():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(WrongSegmentReference):
        get_specific_segment(dorms, ("Akademik", True))

def test_get_specific_fail3():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(WrongSegmentReference):
        get_specific_segment(dorms, ("Akademik", "1"))

def test_available_configurations():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)

    test_segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert available_configurations(dorms)[0]["configuration"] == test_segment_type

def test_combined_segment_types():
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, None, "shower", True, False))
    student3 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "normal", "full", False, True))
    roommates = [student1, student2, student3]
    res_segment = combined_segment_types(roommates)
    assert res_segment[0] == SegmentType("Akademik", "Ochota", 3, 3, "renovated", "full", True, False)

def test_is_correct_location():
    assert is_correct_location("Akademik", "Ochota")

def test_is_correct_location_fail():
    assert not is_correct_location("Akademik", "Mokotów")

def test_find_segment_type():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    assert find_segment_type(dorms, SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)) == segment

def test_find_segment_type_fail1():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(NotFound):
        find_segment_type(dorms, SegmentType("Akademik", "Ochota", 2, 1, "renovated", "full", True, False))

def test_find_segment_type_fail2():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", False, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    with pytest.raises(NotFound):
        find_segment_type(dorms, SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False))

def test_find_segment_type_fail3():
    dorms = []
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    segment = Segment(room, "A", True, 1)
    dorms.append(dormitory)
    dormitory.rooms.append(room)
    room.segments.append(segment)
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student.accommodate(segment)
    with pytest.raises(NotFound):
        find_segment_type(dorms, SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False))

