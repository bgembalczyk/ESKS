from segment import Segment

class Student:
    def __init__(self, USOSid: int, year: int, sex: str, faculty: str, major: str, city: str, lang: str, preference):
        self._id = USOSid
        self._year = year
        self._sex = sex
        self._faculty = faculty
        self._major = major
        self._city = city
        self._lang = lang
        self._preference = preference
        self.segment = None

    @property
    def id(self):
        return self._id

    @property
    def year(self):
        return self._year

    @property
    def sex(self):
        return self._sex

    @property
    def faculty(self):
        return self._faculty

    @property
    def major(self):
        return self._major

    @property
    def city(self):
        return self._city

    @property
    def lang(self):
        return self._lang

    @property
    def preference(self):
        return self._preference

    def __str__(self):
        return f"USOSid: {self.id}\n" \
               f"Birth year: {self.year}\n" \
               f"Sex: {self.sex}\n" \
               f"Student is studying: {self.major} in {self.lang} at The Faculty {self.faculty} in {self.city}\n" \
               f"Student's accommodation preferences: {self.preference}\n"

    def __lt__(self, other):
        return self.id < other.id

    def accommodate(self, segment_var: Segment):
        segment_var.tenants.append(self)
        self.segment = segment_var
        return
