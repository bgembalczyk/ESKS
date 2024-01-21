import pytest

from student import Student
from segmentType import SegmentType
from exceptions.student import *

def test_student():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student

def test_student_missing_arg():
    with pytest.raises(TypeError):
        Student()

def test_student_id():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.id == 320683

def test_student_id_not_int():
    with pytest.raises(IdNotInt):
        Student(True, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_wrong_id():
    with pytest.raises(WrongId):
        Student(-2137, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_year():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.year == 2002

def test_student_year_not_int():
    with pytest.raises(YearNotInt):
        Student(320683, False, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_wrong_year():
    with pytest.raises(WrongYear):
        Student(320683, -2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_sex():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.sex == "M"

def test_student_wrong_sex():
    with pytest.raises(WrongSex):
        Student(320683, 2002, "NB", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_faculty():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.faculty == "Elektroniki i Technik Informacyjnych"

def test_student_wrong_faculty():
    with pytest.raises(WrongFaculty):
        Student(320683, 2002, "M", "Elektroniki i Nauk Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_major():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.major == "Informatyka"

def test_student_wrong_major():
    with pytest.raises(WrongMajor):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka Społeczna", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_city():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.city == "Warszawa"

def test_student_wrong_city():
    with pytest.raises(WrongCity):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Katowice", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_lang():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.lang == "polski"

def test_student_wrong_lang():
    with pytest.raises(WrongLang):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "python", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_pref_roommate():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.pref_roommate == 297777

def test_student_pref_roommate_not_int():
    with pytest.raises(IdNotInt):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", True, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_wrong_pref_roommate():
    with pytest.raises(WrongId):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", -297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_pref_segment():
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.pref_segment == ("Akademik", "307A")

def test_student_wrong_pref_segment_dorm():
    with pytest.raises(WrongPrefDorm):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Sezam", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_wrong_pref_segment():
    with pytest.raises(WrongPrefSegment):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_wrong_pref_segment_len():
    with pytest.raises(WrongPrefSegment):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, False, SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_pref_segment_miss_dorm():
    with pytest.raises(PrefDormMissing):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, (None, "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))

def test_student_preference():
    preference = SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False)
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student.preference == preference

def test_student_wrong_pref():
    with pytest.raises(WrongPreference):
        Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), True)

def test_student__str__():
    string = f"USOSid: 320683\nBirth year: 2002\nSex: M\n" \
             f"Student is studying: Informatyka in polski at The Faculty Elektroniki i Technik Informacyjnych " \
             f"in Warszawa\nStudent's preferred roommate: 297777\nStudent's preferred segment is 307A in Akademik"
    student = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert str(student) == string

def test_student__eq__():
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(320683, 1999, "F", "Chemiczny", "Biotechnologia", "Płock", "angielski", 319000, ("Babilon", "2137Z"), SegmentType("Babilon", "Ochota", 2, 2, "normal", "full", True, False))
    assert student1 == student2

def test_student__eq__fail():
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(319000, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    assert student1 != student2

def test_student__lt__():
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(297777, 1999, "F", "Chemiczny", "Biotechnologia", "Płock", "angielski", 319000, ("Babilon", "2137Z"), SegmentType("Babilon", "Ochota", 2, 2, "normal", "full", True, False))
    assert student2 < student1

def test_student__lt__fail():
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 297777, ("Akademik", "307A"), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(297777, 1999, "F", "Chemiczny", "Biotechnologia", "Płock", "angielski", 319000, ("Babilon", "2137Z"), SegmentType("Babilon", "Ochota", 2, 2, "normal", "full", True, False))
    assert not student1 < student2

# TODO
# def test_accommodate():
#     student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
#     assert False
