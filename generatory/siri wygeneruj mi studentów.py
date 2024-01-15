import random

def random_segment(dorm):
    match dorm:
        case "Akademik":
            max_room, max_seg = 510, 1
        case "Babilon":
            max_room, max_seg = 142, 2
        case "Bratniak":
            max_room, max_seg = 74, 1
        case "Mikrus":
            max_room, max_seg = 255, 1
        case "Muszelka":
            max_room, max_seg = 79, 2
        case "Riviera":
            max_room, max_seg = 235, 2
        case "Tatrzańska":
            max_room, max_seg = 95, 2
        case "Tulipan":
            max_room, max_seg = 40, 3
        case "Ustronie":
            max_room, max_seg = 345, 1
        case "Wcześniak":
            max_room, max_seg = 85, 4
        case "Żaczek":
            max_room, max_seg = 385, 2
        case _:
            return None
    return f"{random.randint(1, max_room)}{chr(ord('A') + random.randint(0, max_seg - 1))}"

def find_major(majors, n):
    for major in majors:
        if n <= int(major[-1]):
            return major[1], major[0], major[3], major[4]


N = 5000
max_stud = 5660
dorm_Wwa = ["Akademik", "Babilon", "Bratniak", "Mikrus", "Muszelka", "Riviera", "Tatrzańska", "Tulipan", "Ustronie",
             "Żaczek"]
majors = [
    ["Administracja", "Administracji i Nauk Społecznych", "200", "Warszawa", "polski", "200"],
    ["Architektura", "Architektury", "100", "Warszawa", "polski", "300"],
    ["Automatyka i robotyka", "Elektroniki i Technik Informacyjnych", "60", "Warszawa", "polski", "360"],
    ["Automatyka i robotyka stosowana", "Elektryczny", "48", "Warszawa", "polski", "408"],
    ["Automatyzacja i robotyzacja procesów produkcyjnych", "Mechaniczny Technologiczny", "120", "Warszawa", "polski",
     "528"],
    ["Automatyka, robotyka i informatyka  przemysłowa", "Mechatroniki", "70", "Warszawa", "polski", "598"],
    ["Biotechnologia", "Chemiczny", "90", "Warszawa", "polski", "688"],
    ["Budownictwo", "Inżynierii Lądowej", "270", "Warszawa", "polski", "958"],
    ["Cyberbezpieczeństwo", "Elektroniki i Technik Informacyjnych", "60", "Warszawa", "polski", "1018"],
    ["Elektromobilność", "Elektryczny", "24", "Warszawa", "polski", "1042"],
    ["Elektronika", "Elektroniki i Technik Informacyjnych", "150", "Warszawa", "polski", "1192"],
    ["Elektrotechnika", "Elektryczny", "120", "Warszawa", "polski", "1312"],
    ["Energetyka", "Mechaniczny Energetyki i Lotnictwa", "90", "Warszawa", "polski", "1402"],
    ["Fizyka techniczna", "Fizyki", "100", "Warszawa", "polski", "1502"],
    ["Fotonika", "Fizyki", "30", "Warszawa", "polski", "1532"],
    ["Geodezja i kartografia", "Geodezji i Kartografii", "150", "Warszawa", "polski", "1682"],
    ["Geoinformatyka", "Geodezji i Kartografii", "45", "Warszawa", "polski", "1727"],
    ["Gospodarka przestrzenna", "Geodezji i Kartografii", "120", "Warszawa", "polski", "1847"],
    ["Informatyka", "Elektroniki i Technik Informacyjnych", "150", "Warszawa", "polski", "1997"],
    ["Informatyka i systemy informacyjne", "Matematyki i Nauk Informacyjnych", "100", "Warszawa", "polski", "2097"],
    ["Informatyka stosowana", "Elektryczny", "120", "Warszawa", "polski", "2217"],
    ["Inżynieria biomedyczna", "Elektroniki i Technik Informacyjnych", "45", "Warszawa", "polski", "2262"],
    ["Inżynieria biomedyczna", "Mechatroniki", "45", "Warszawa", "polski", "2307"],
    ["Inżynieria chemiczna i procesowa", "Inżynierii Chemicznej i Procesowej", "120", "Warszawa", "polski", "2427"],
    ["Inżynieria i analiza danych", "Matematyki i Nauk Informacyjnych", "70", "Warszawa", "polski", "2497"],
    ["Inżynieria Internetu rzeczy", "Elektroniki i Technik Informacyjnych", "30", "Warszawa", "polski", "2527"],
    ["Inżynieria materiałowa", "Inżynierii Materiałowej", "100", "Warszawa", "polski", "2627"],
    ["Inżynieria mechaniczna", "Samochodów i Maszyn Roboczych", "50", "Warszawa", "polski", "2677"],
    ["Inżynieria pojazdów elektrycznych i hybrydowych", "Samochodów i Maszyn Roboczych", "100", "Warszawa", "polski",
     "2777"],
    ["Inżynieria środowiska", "Instalacji Budowlanych, Hydrotechniki i Inżynierii Środowiska", "240", "Warszawa",
     "polski", "3017"],
    ["Inżynieria zarządzania", "Zarządzania", "120", "Warszawa", "polski", "3137"],
    ["Lotnictwo i kosmonautyka", "Mechaniczny Energetyki i Lotnictwa", "90", "Warszawa", "polski", "3227"],
    ["Matematyka", "Matematyki i Nauk Informacyjnych", "80", "Warszawa", "polski", "3307"],
    ["Matematyka i analiza danych", "Matematyki i Nauk Informacyjnych", "60", "Warszawa", "polski", "3367"],
    ["Mechanika i budowa maszyn", "Mechaniczny Technologiczny", "140", "Warszawa", "polski", "3507"],
    ["Mechanika i projektowanie maszyn", "Mechaniczny Energetyki i Lotnictwa", "28", "Warszawa", "polski", "3535"],
    ["Mechatronika", "Mechatroniki", "180", "Warszawa", "polski", "3715"],
    ["Mechatronika pojazdów i maszyn roboczych", "Samochodów i Maszyn Roboczych", "50", "Warszawa", "polski", "3765"],
    ["Ochrona środowiska", "Instalacji Budowlanych, Hydrotechniki i Inżynierii Środowiska", "60", "Warszawa", "polski",
     "3825"],
    ["Papiernictwo i poligrafia", "Mechaniczny Technologiczny", "80", "Warszawa", "polski", "3905"],
    ["Robotyka i automatyka", "Mechaniczny Energetyki i Lotnictwa", "52", "Warszawa", "polski", "3957"],
    ["Technologia chemiczna", "Chemiczny", "195", "Warszawa", "polski", "4152"],
    ["Telekomunikacja", "Elektroniki i Technik Informacyjnych", "150", "Warszawa", "polski", "4302"],
    ["Transport", "Transportu", "280", "Warszawa", "polski", "4582"],
    ["Zarządzanie", "Zarządzania", "120", "Warszawa", "polski", "4702"],
    ["Zarządzanie i inżynieria produkcji", "Mechaniczny Technologiczny", "120", "Warszawa", "polski", "4822"],
    # ["Budownictwo", "Budownictwa, Mechaniki i Petrochemii", "80", "Płock", "polski", "4902"],
    # ["Ekonomia", "Kolegium Nauk Ekonomicznych i Społecznych", "90", "Płock", "polski", "4992"],
    # ["Inżynieria środowiska", "Budownictwa, Mechaniki i Petrochemii", "50", "Płock", "polski", "5042"],
    # ["Mechanika i budowa maszyn", "Budownictwa, Mechaniki i Petrochemii", "70", "Płock", "polski", "5112"],
    # ["Przemysłowe zastosowania informatyki", "Budownictwa, Mechaniki i Petrochemii", "40", "Płock", "polski", "5152"],
    # ["Technologia chemiczna", "Budownictwa, Mechaniki i Petrochemii", "80", "Płock", "polski", "5232"],
    ["Aerospace Engineering", "Mechaniczny Energetyki i Lotnictwa", "25", "Warszawa", "angielski", "5257"],
    ["Architecture", "Architektury", "50", "Warszawa", "angielski", "5307"],
    ["Civil Engineering", "Inżynierii Lądowej", "60", "Warszawa", "angielski", "5367"],
    ["Computer Science", "Elektroniki i Technik Informacyjnych", "30", "Warszawa", "angielski", "5397"],
    ["Computer Science and Information Systems", "Matematyki i Nauk Informacyjnych", "30", "Warszawa", "angielski",
     "5427"],
    ["Electric and Hybrid Vehicles Engineering", "Samochodów i Maszyn Roboczych", "50", "Warszawa", "angielski",
     "5477"],
    ["Electrical Engineering", "Elektryczny", "48", "Warszawa", "angielski", "5525"],
    ["Environmental Engineering", "Instalacji Budowlanych, Hydrotechniki i Inżynierii Środowiska", "30", "Warszawa",
     "angielski", "5555"],
    ["Mechatronics", "Mechatroniki", "30", "Warszawa", "angielski", "5585"],
    ["Mechatronics of Vehicles and Construction Machinery", "Samochodów i Maszyn Roboczych", "25", "Warszawa",
     "angielski", "5610"],
    ["Power Engineering", "Mechaniczny Energetyki i Lotnictwa", "20", "Warszawa", "angielski", "5630"],
    ["Telecommunications", "Elektroniki i Technik Informacyjnych", "30", "Warszawa", "angielski", "5660"]
]
students_id_pool = list(range(1000, 10000))


with open("students.txt", "w") as file:
    for i in range(N):
        sex = random.randint(0, 1)
        stud_id = random.choice(students_id_pool)
        students_id_pool.remove(stud_id)
        stud_faculty, stud_major, stud_city, stud_lang = find_major(majors, random.randint(0, max_stud - 1))
        if stud_city == "Płock":
            preference_dorm = "Wcześniak"
            preference_location = "Płock"
        else:
            if random.random() > 1 / 3:
                preference_dorm = random.choice(dorm_Wwa)
            else:
                preference_dorm = None
            if stud_faculty in ["Inżynierii Materiałowej", "Mechaniczny Technologiczny", "Mechatroniki", "Samochodów i Maszyn Roboczych", "Zarządzania"]:
                preference_location = "Kampus Południowy"
            else:
                if random.random() > 1 / 4:
                    preference_location = random.choice(["Ochota", "Kampus Centralny", "Mokotów", "Wola"])
                else:
                    preference_location = None
        if random.random() > 1 / 2:
            preference_segment = random_segment(preference_dorm)
        else:
            preference_segment = None
        if random.random() > 1 / 8:
            preference_tenants_num_room = random.randint(1, 8)
            if random.random() > 1 / 9:
                preference_tenants_num_segment = random.randint(1, min(6, preference_tenants_num_room))
            else:
                preference_tenants_num_segment = None
        else:
            preference_tenants_num_room = None
            preference_tenants_num_segment = None
        if random.random() > 1 / 5:
            preference_condition = random.choice(["normal", "renovated"])
        else:
            preference_condition = None
        if random.random() > 1 / 6:
            preference_bathroom = random.choice(["full", "shower", "null"])
        else:
            preference_bathroom = None
        if random.random() > 1 / 7:
            preference_kitchen = random.choice([True, False])
        else:
            preference_kitchen = None
        if preference_dorm == "Riviera" or preference_location == "Kampus Centralny":
            preference_ad = random.choice([True, False])
        else:
            preference_ad = False
        if random.random() < 1 / 4:
            preference_tenant = random.randint(1000, 10000)
        else:
            preference_tenant = None
        line = f"{stud_id};{random.randint(1997, 2005)};{sex * 'F' + (1 - sex) * 'M'};" \
               f"{stud_faculty};{stud_major};{stud_city};{stud_lang};{preference_tenant};{preference_dorm};" \
               f"{preference_segment};{preference_location};{preference_tenants_num_room};" \
               f"{preference_tenants_num_segment};{preference_condition};{preference_bathroom};{preference_kitchen};" \
               f"{preference_ad}\n"
        file.write(line)

