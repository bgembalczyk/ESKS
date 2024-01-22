import pytest
from exceptions.rest import *
from student import Student
from funcStudents import *
from importFile import input_dorms

def test_get_student():
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(320684, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, None, "shower", True, False))
    student3 = Student(320685, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "normal", "full", False, True))
    students = [student1, student2, student3]
    assert get_student(320683, students) == student1

def test_get_student_fail():
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(320684, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, None, "shower", True, False))
    student3 = Student(320685, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "normal", "full", False, True))
    students = [student1, student2, student3]
    with pytest.raises(NotFound):
        get_student(320680, students)

def test_students_roommates_pairs():
    student1 = Student(320683, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(320684, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", 320683, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, None, "shower", True, False))
    student3 = Student(320685, 2002, "M", "Elektroniki i Technik Informacyjnych", "Informatyka", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "normal", "full", False, True))
    students = [student1, student2, student3]
    assert students_roommates_pairs(students) == [[student1, student2]]

def test_students_live_together():
    student1 = Student(1, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", 2, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(2, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student3 = Student(3, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    students = [student1, student2, student3]
    assert students_live_together(students) == [[student1, student2]]

def test_students_exact_segment():
    student1 = Student(1, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(2, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", "36A"), SegmentType("Akademik", "Ochota", 2, 2, "renovated", "null", False, False))
    student3 = Student(3, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 3, 3, "renovated", "null", False, False))
    students = [student1, student2, student3]
    dorms = input_dorms("test_dorms.json")
    assert students_exact_segment(students, dorms)[0][0] == student2

def test_students_exact_segment_type():
    student1 = Student(1, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(2, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 2, 2, "renovated", "null", False, False))
    student3 = Student(3, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 3, 3, "renovated", "null", False, False))
    students = [student1, student2, student3]
    dorms = input_dorms("test_dorms.json")
    assert students_exact_segment_type(students, dorms)[0][0] == student1

def test_students_better_segment_type():
    student1 = Student(1, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 1, 1, "renovated", "null", False, False))
    student2 = Student(2, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Babilon", None), SegmentType("Babilon", "Ochota", 2, 2, "renovated", "null", False, False))
    student3 = Student(3, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 3, 3, "renovated", "null", False, False))
    students = [student1, student2, student3]
    dorms = input_dorms("test_dorms.json")
    assert students_exact_segment_type(students, dorms)[0][0] == student1

def test_students_that_dont_know_where_dorms_are():
    student1 = Student(1, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Mokotów", 1, 1, "renovated", "null", False, False))
    student2 = Student(2, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Babilon", None), SegmentType("Babilon", "Ochota", 2, 2, "renovated", "null", False, False))
    student3 = Student(3, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 3, 3, "renovated", "null", False, False))
    students = [student1, student2, student3]
    dorms = input_dorms("test_dorms.json")
    assert students_that_dont_know_where_dorms_are(students, dorms)[0][0] == student1

def test_find_best_segment_type():
    dorms = input_dorms("test_dorms.json")
    student1 = Student(1, 2000, "M", "Fizyki", "Fotonika", "Warszawa", "polski", None, ("Akademik", None), SegmentType("Akademik", "Ochota", 2, 2, "renovated", "full", True, False))
    students = [student1]
    assert find_best_segment_type(students, dorms) == [[student1, [SegmentType("Akademik", "Ochota", 1, 1, "renovated", "full", True, False)]]]
