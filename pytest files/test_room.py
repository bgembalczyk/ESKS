import pytest
import exceptions.segment
from exceptions.room import *
from segment import Segment
from room import Room
from dormitory import Dormitory

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

def test_room__str__():
    dormitory = Dormitory("Akademik", True, "Ochota")
    room = Room(dormitory, 1, True, "renovated", "full", True, False)
    string = f"\tNumer pokoju: 1\n\tLiczba łóżek: 0\n\tLiczba mieszkańców: 0\n\tLiczba segmentów: 0\n"
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
