from segment import Segment

class Student:
    def __init__(self, id, year, sex, faculty, major, city, lang, preference):
        self.id = id
        self.year = year
        self.sex = sex
        self.faculty = faculty
        self.major = major
        self.city = city
        self.lang = lang
        self.preference = preference

    def __str__(self):
        return f"USOSid: {self.id}\n" \
               f"Birth year: {self.year}\n" \
               f"Sex: {self.prefDorm}\n" \
               f"Student is studying: {self.major} in {self.lang} at the faculty {self.faculty} in {self.city}\n" \
               f"Student's accommodation preferences: {self.preference}"

    def accommodate(self, segment_var: Segment) -> None:
        segment_var.tenants.append(self)
        self.dorm = segment_var.room().dorm()
