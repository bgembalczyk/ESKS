class StudentError(Exception):
    pass

class StudentIdNotInt(StudentError, TypeError):
    pass

class StudentYearNotInt(StudentError, TypeError):
    pass

class StudentWrongYear(StudentError, ValueError):
    def __init__(self):
        message = "Student: year must between 1900 and 2010"
        super().__init__(message)

class StudentWrongSex(StudentError, ValueError):
    def __init__(self):
        sex = ["M", "F", "O"]
        message = "Student: sex must be one of %r." % sex
        super().__init__(message)

class StudentWrongFaculty(StudentError, ValueError):
    def __init__(self):
        faculties = ["Administracji i Nauk Społecznych", "Architektury", "Budownictwa, Mechaniki i Petrochemii",
                     "Chemiczny", "Elektroniki i Technik Informacyjnych", "Elektryczny", "Fizyki",
                     "Geodezji i Kartografii", "Instalacji Budowlanych, Hydrotechniki i Inżynierii Środowiska",
                     "Inżynierii Chemicznej i Procesowej", "Inżynierii Lądowej", "Inżynierii Materiałowej",
                     "Kolegium Nauk Ekonomicznych i Społecznych", "Matematyki i Nauk Informacyjnych",
                     "Mechaniczny Energetyki i Lotnictwa", "Mechaniczny Technologiczny", "Mechatroniki",
                     "Samochodów i Maszyn Roboczych", "Transportu", "Zarządzania"]
        message = "Student: faculty must be one of %r." % faculties
        super().__init__(message)

class StudentWrongMajor(StudentError, ValueError):
    def __init__(self):
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
        message = "Student: major must be one of %r." % majors
        super().__init__(message)

class StudentWrongCity(StudentError, ValueError):
    def __init__(self):
        cites = ["Warszawa", "Płock"]
        message = "Student: city must be one of %r." % cites
        super().__init__(message)

class StudentWrongLang(StudentError, ValueError):
    def __init__(self):
        langs = ["polski", "angielski"]
        message = "Student: lang must be one of %r." % langs
        super().__init__(message)
