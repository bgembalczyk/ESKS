import exceptions.student as error
from segmentType import SegmentType
from segment import Segment

class Student:
    def __init__(self, USOSid, year, sex, faculty, major, city, lang, pref_roommate, pref_segment, preference):
        sexes = ["M", "F", "O"]
        faculties = ["Administracji i Nauk Społecznych", "Architektury", "Budownictwa, Mechaniki i Petrochemii",
                     "Chemiczny", "Elektroniki i Technik Informacyjnych", "Elektryczny", "Fizyki",
                     "Geodezji i Kartografii", "Instalacji Budowlanych, Hydrotechniki i Inżynierii Środowiska",
                     "Inżynierii Chemicznej i Procesowej", "Inżynierii Lądowej", "Inżynierii Materiałowej",
                     "Kolegium Nauk Ekonomicznych i Społecznych", "Matematyki i Nauk Informacyjnych",
                     "Mechaniczny Energetyki i Lotnictwa", "Mechaniczny Technologiczny", "Mechatroniki",
                     "Samochodów i Maszyn Roboczych", "Transportu", "Zarządzania"]
        majors = ["Administracja", "Aerospace Engineering", "Architecture", "Architektura", "Automatyka i robotyka",
                  "Automatyka i robotyka stosowana", "Automatyka, robotyka i informatyka  przemysłowa",
                  "Automatyzacja i robotyzacja procesów produkcyjnych", "Biotechnologia", "Budownictwo",
                  "Civil Engineering", "Computer Science", "Computer Science and Information Systems",
                  "Cyberbezpieczeństwo", "Ekonomia", "Electric and Hybrid Vehicles Engineering",
                  "Electrical Engineering", "Elektromobilność", "Elektronika", "Elektrotechnika", "Energetyka",
                  "Environmental Engineering", "Fizyka techniczna", "Fotonika", "Geodezja i kartografia",
                  "Geoinformatyka", "Gospodarka przestrzenna", "Informatyka", "Informatyka i systemy informacyjne",
                  "Informatyka stosowana", "Inżynieria biomedyczna", "Inżynieria chemiczna i procesowa",
                  "Inżynieria i analiza danych", "Inżynieria Internetu rzeczy", "Inżynieria materiałowa",
                  "Inżynieria mechaniczna", "Inżynieria pojazdów elektrycznych i hybrydowych", "Inżynieria środowiska",
                  "Inżynieria zarządzania", "Lotnictwo i kosmonautyka", "Matematyka", "Matematyka i analiza danych",
                  "Mechanika i budowa maszyn", "Mechanika i projektowanie maszyn", "Mechatronics",
                  "Mechatronics of Vehicles and Construction Machinery", "Mechatronika",
                  "Mechatronika pojazdów i maszyn roboczych", "Ochrona środowiska", "Papiernictwo i poligrafia",
                  "Power Engineering", "Przemysłowe zastosowania informatyki", "Robotyka i automatyka",
                  "Technologia chemiczna", "Telecommunications", "Telekomunikacja", "Transport", "Zarządzanie",
                  "Zarządzanie i inżynieria produkcji"]
        cites = ["Warszawa"]
        langs = ["polski", "angielski"]
        dorms = [None, "Akademik", "Babilon", "Bratniak", "Mikrus", "Muszelka", "Riviera", "Tatrzańska", "Tulipan",
                 "Ustronie", "Żaczek"]

        # Validate input parameters
        if type(USOSid) is not int:
            raise error.IdNotInt
        if USOSid <= 0:
            raise error.WrongId
        if type(year) is not int:
            raise error.YearNotInt
        if not 1900 < year < 2010:
            raise error.WrongYear
        if sex not in sexes:
            raise error.WrongSex
        if faculty not in faculties:
            raise error.WrongFaculty
        if major not in majors:
            raise error.WrongMajor
        if city not in cites:
            raise error.WrongCity
        if lang not in langs:
            raise error.WrongLang
        if type(pref_roommate) is not int and pref_roommate is not None:
            raise error.IdNotInt
        if pref_roommate is not None:
            if pref_roommate <= 0:
                raise error.WrongId
        if type(preference) is not SegmentType:
            raise error.WrongPreference
        try:
            len(pref_segment)
        except TypeError:
            raise error.WrongPrefSegment
        if len(pref_segment) != 2:
            raise error.WrongPrefSegment
        if pref_segment[1] is not None and pref_segment[0] is None:
            raise error.PrefDormMissing
        if pref_segment[0] not in dorms:
            raise error.WrongPrefDorm
        if pref_segment[1] is not None:
            if pref_segment[1][-1] not in "QWERTYUIOPASDFGHJKLZXCVBNM":
                raise error.WrongPrefSegment
        try:
            int(pref_segment[1][:-1])
        except ValueError:
            raise error.WrongPrefSegment
        except TypeError:
            pass

        # Assign values to instance variables
        self._id = USOSid
        self._year = year
        self._sex = sex
        self._faculty = faculty
        self._major = major
        self._city = city
        self._lang = lang
        self._pref_roommate = pref_roommate
        self._pref_segment = pref_segment
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
    def pref_roommate(self):
        return self._pref_roommate

    @property
    def pref_segment(self):
        return self._pref_segment

    @property
    def preference(self):
        return self._preference

    def __str__(self):
        # Generate a formatted string representation of the Student object
        return f"USOSid: {self.id}\n" \
               f"Birth year: {self.year}\n" \
               f"Sex: {self.sex}\n" \
               f"Student is studying: {self.major} in {self.lang} at The Faculty {self.faculty} in {self.city}\n" \
               f"Student's preferred roommate: {self.pref_roommate}\n" \
               f"Student's preferred segment is {self.pref_segment[1]} in {self.pref_segment[0]}"

    def __lt__(self, other):
        # Implement the less-than comparison for Student objects based on their IDs
        return self.id < other.id

    def __eq__(self, other):
        # Implement the equality comparison for Student objects based on their IDs
        return self.id == other.id

    def accommodate(self, segment_var: Segment):
        # Accommodate the student in the specified segment
        if self.segment is not None:
            raise error.AlreadyAccommodated
        if not segment_var.habitable or not segment_var.room.habitable or not segment_var.room.dorm.habitable:
            raise error.NonHabitable
        if segment_var.tenants_num() >= segment_var.beds:
            raise error.TooManyTenants
        segment_var.tenants.append(self)
        self.segment = segment_var
        return
