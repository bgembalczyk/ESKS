from student import Student
from segment import Segment

id = 320683
year = 2002
sex = "M"
faculty = "Elektroniki i Technik Informacyjnych"
major = "Informatyka"
city = "Warszawa"
lang = "polski"
pref_roommate = 297777
pref_segment = ("Akademik", "307A")
preference = ("Akademik", "Ochota", 1, 1, "renovated", "null", False, False)

def test_student_id():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.id == 320683

def test_student_year():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.year == 2002

def test_student_sex():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.sex == "M"

def test_student_faculty():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.faculty == "Elektroniki i Technik Informacyjnych"

def test_student_major():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.major == "Informatyka"

def test_student_city():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.city == "Warszawa"

def test_student_lang():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.lang == "polski"

def test_student_pref_roommate():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.pref_roommate == 297777

def test_student_pref_segment():
    student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
    assert student.segment == ("Akademik", "307A")

# def test_student_preference():
#     student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
#     assert student.preference == ("Akademik", "Ochota", 1, 1, "renovated", "null", False, False)

# def test_accommodate():
#     student = Student(id, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference)
#     assert False
