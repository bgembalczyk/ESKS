from segmentType import SegmentType
from exceptions import *
import pytest

def test_segment_type():
    segment_type = SegmentType("Akademik", "Ochota", 2, 1, "renovated", "full", True, False)
    assert segment_type

def test_segment_type_none():
    segment_type = SegmentType(None, None, None, None, None, None, None, None)
    assert segment_type

def test_segment_type_missing_arg():
    with pytest.raises(TypeError):
        SegmentType()

def test_segment_type_dorm():
    segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type.dorm == "Akademik"

def test_segment_type_dorm_wrong():
    with pytest.raises(ValueError):
        SegmentType("Sezam", "Ochota", 1, 1, "renovated", "full", True, False)

def test_segment_type_location():
    segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type.location == "Ochota"

def test_segment_type_location_wrong():
    with pytest.raises(ValueError):
        SegmentType("Akademik", "Ursynów", 1, 1, "renovated", "full", True, False)

def test_segment_type_tenants_num_room():
    segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type.tenants_num_room == 1

def test_segment_type_tenants_num_room_wrong_type():
    with pytest.raises(TypeError):
        SegmentType("Akademik", "Ochota", False, 1, "renovated", "full", True, False)

def test_segment_type_tenants_num_room_wrong_int():
    with pytest.raises(ValueError):
        SegmentType("Akademik", "Ochota", -1, -11, "renovated", "full", True, False)

def test_segment_type_tenants_num_segment():
    segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type.tenants_num_segment == 1

def test_segment_type_tenants_num_segment_wrong_type():
    with pytest.raises(TypeError):
        SegmentType("Akademik", "Ochota", 1, False, "renovated", "full", True, False)

def test_segment_type_tenants_num_segment_wrong_int():
    with pytest.raises(ValueError):
        SegmentType("Akademik", "Ochota", 1, -1, "renovated", "full", True, False)

def test_segment_type_tenants_num_wrong_int():
    with pytest.raises(ValueError):
        SegmentType("Akademik", "Ochota", 1, 2, "renovated", "full", True, False)

def test_segment_type_condition():
    segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type.condition == "renovated"

def test_segment_type_wrong_condition():
    with pytest.raises(ValueError):
        SegmentType("Akademik", "Ochota", 1, 1, "new", "full", True, False)

def test_segment_type_bathroom():
    segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type.bathroom == "full"

def test_segment_type_wrong_bathroom():
    with pytest.raises(ValueError):
        SegmentType("Akademik", "Ochota", 1, 1, "renovated", "renovated", True, False)

def test_segment_type_kitchen():
    segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type.kitchen

def test_segment_type_wrong_kitchen():
    with pytest.raises(TypeError):
        SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", "true", False)

def test_segment_type_ad():
    segment_type = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert not segment_type.ad

def test_segment_type_wrong_ad():
    with pytest.raises(TypeError):
        SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, "false")

def test_segment_type__eq__():
    segment_type1 = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    segment_type2 = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type1 == segment_type2

def test_segment_type__eq__fail():
    segment_type1 = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    segment_type2 = SegmentType("Akademik", "Ochota", 2, 1, "renovated", "full", True, False)
    assert segment_type1 != segment_type2

def test_segment_type__eq__none():
    segment_type1 = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    segment_type2 = SegmentType(None, None, None, None, None, None, None, None)
    assert segment_type1 == segment_type2

def test_segment_type__eq__none_none():
    segment_type1 = SegmentType(None, None, None, None, None, None, None, None)
    segment_type2 = SegmentType(None, None, None, None, None, None, None, None)
    assert segment_type1 == segment_type2

def test_segment_type__lt__():
    segment_type1 = SegmentType("Akademik", "Ochota", 4, 2, "normal", "null", False, True)
    segment_type2 = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert segment_type1 < segment_type2

def test_segment_type__lt__fail():
    segment_type1 = SegmentType("Akademik", "Ochota", 4, 2, "normal", "null", False, True)
    segment_type2 = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    assert not segment_type2 < segment_type1

def test_segment_type__lt__incomparable():
    segment_type1 = SegmentType("Akademik", "Ochota", 4, 2, "normal", "null", False, True)
    segment_type2 = SegmentType("Tatrzańska", "Mokotów", 1, 1, "renovated", "full", True, False)
    with pytest.raises(SegmentTypesIncomparable):
        segment_type1 < segment_type2

def test_segment_type__sub__():
    segment_type1 = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)
    segment_type2 = SegmentType("Akademik", "Ochota", 2, 1, "renovated", "full", True, False)
    assert segment_type1 - segment_type2 == 1010000

def test_segment_type__sub__2():
    segment_type1 = SegmentType("Akademik", "Ochota", 4, 2, "normal", "null", False, True)
    segment_type2 = SegmentType("Tatrzańska", "Mokotów", 1, 1, "renovated", "full", True, False)
    assert segment_type2 - segment_type1 == 4051211

def test_segment_type_copy():
    segment_type1 = SegmentType("Akademik", "Ochota", 4, 2, "normal", "null", False, True)
    segment_type2 = segment_type1.copy()
    assert (segment_type1 == segment_type2) and (segment_type1 is not segment_type2)

def test_segment_type_correct_location():
    segment_type1 = SegmentType("Akademik", "Mokotów", 4, 2, "normal", "null", False, True)
    # segment_type2 = SegmentType(None, "Mokotów", 4, 2, "normal", "null", False, True)
    # segment_type3 = SegmentType("Akademik", None, 4, 2, "normal", "null", False, True)
    assert segment_type1.correct_location() == (SegmentType(None, "Mokotów", 4, 2, "normal", "null", False, True), SegmentType("Akademik", None, 4, 2, "normal", "null", False, True))
