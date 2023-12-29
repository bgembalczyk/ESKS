dormsData = [
    {"name": "Akademik", "location": "Ochota",
     "rooms": [({"segments": [1], "old": True}, 65),
               ({"segments": [2], "old": True}, 30),
               ({"segments": [1], "renovated": True}, 25),
               ({"segments": [2], "renovated": True}, 15),
               ({"segments": [2], "renovated": True, "bathroom": True}, 15),
               ({"segments": [3], "renovated": True}, 10),
               ({"segments": [4], "renovated": True}, 5),
               ({"segments": [1]}, 165),
               ({"segments": [2]}, 85),
               ({"segments": [3]}, 55),
               ({"segments": [4]}, 40)]
     },
    {"name": "Babilon", "location": "Ochota",
     "rooms": [({"segments": [1], "bathroom": True}, 30),
               ({"segments": [2], "bathroom": True}, 15),
               ({"segments": [2], "bathroom": True, "kitchen": True}, 15),
               ({"segments": [3], "bathroom": True}, 10),
               ({"segments": [2, 2], "bathroom": True}, 50),
               ({"segments": [1, 3], "bathroom": True}, 10),
               ({"segments": [2, 3], "bathroom": True}, 7),
               ({"segments": [3, 3], "bathroom": True}, 5)]
     },
    {"name": "Bratniak", "location": "Ochota",
     "rooms": [({"segments": [2]}, 40),
               ({"segments": [3]}, 25),
               ({"segments": [4]}, 5),
               ({"segments": [5]}, 4)]
     },
    {"name": "Mikrus", "location": "Kampus Centralny",
     "rooms": [({"segments": [1]}, 20),
               ({"segments": [2]}, 235)]
     },
    {"name": "Muszelka", "location": "Ochota",
     "rooms": [({"segments": [1]}, 38),
               ({"segments": [1, 1]}, 19),
               ({"segments": [1, 2]}, 13),
               ({"segments": [2, 2]}, 9)]
     },
    {"name": "Riviera", "location": "Kampus Centralny",
     "rooms": [({"segments": [2], "bathroom": True, "ad": True}, 75),
               ({"segments": [2], "bathroom": True}, 100),
               ({"segments": [3, 3], "bathroom": True, "ad": True}, 25),
               ({"segments": [3, 3], "bathroom": True}, 35)]
     },
    {"name": "Tatrzańska", "location": "Mokotów",
     "rooms": [({"segments": [1]}, 40),
               ({"segments": [1, 1]}, 20),
               ({"segments": [1, 2]}, 15),
               ({"segments": [2, 2]}, 20)]
     },
    {"name": "Tulipan", "location": "Ochota",
     "rooms": [({"segments": [1, 2], "shower": True}, 50)]
     },
    {"name": "Ustronie", "location": "Wola",
     "rooms": [({"segments": [2]}, 115),
               ({"segments": [2], "renovated": True}, 115),
               ({"segments": [2], "bathroom": True}, 115)]
     },
    {"name": "Wcześniak", "location": "Płock",
     "rooms": [({"segments": [1, 1, 2, 2], "bathroom": True}, 40),
               ({"segments": [2, 2, 2, 2], "bathroom": True}, 45)]
     },
    {"name": "Żaczek", "location": "Kampus Południowy",
     "rooms": [({"beds": [1], "bathroom": True, "kitchen": True}, 210),
               ({"beds": [2], "bathroom": True, "kitchen": True}, 105),
               ({"beds": [2, 2], "bathroom": True, "kitchen": True}, 70)]
     }
]

file = open("dorms.txt", "w")
# TODO
# Totalnie do przerobienia
for dorm in dormsData:
    if dorm['name'] == "Akademik" or dorm['name'] == "Riviera":
        roomNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
        roomNum = [0]
    for room in dorm['rooms']:
        bedNum = 0
        for segment in room[0]:
            bedNum += segment['beds']
        for i in range(int(room[1] * dorm['beds'] / bedNum)):
            if dorm['name'] == "Akademik" or dorm['name'] == "Riviera":
                for floor in room[0][0]['floor']:
                    roomNum[floor - 2] += 1
                    file.write(f"{dorm['name']};")
                    file.write(f"{floor * 100 + roomNum[floor - 2]};")
                    if dorm['name'] == "Akademik":
                        file.write(f"{room[0][0]['separate']};")
                    else:
                        file.write(";")
                    if dorm['name'] == "Babilon":
                        file.write(f"{room[0][0]['kitchen']};")
                    else:
                        file.write(";")
                    if dorm['name'] == "Ustronie":
                        file.write(f"{room[0][0]['type']};")
                    else:
                        file.write(";")
                    tmp = ""
                    for segment in room[0]:
                        tmp += f"{segment['beds']},"
                    file.write(f"{tmp[:-1]}\n")
            else:
                roomNum[0] += 1
                file.write(f"{dorm['name']};")
                file.write(f"{roomNum[0]};")
                if dorm['name'] == "Akademik":
                    file.write(f"{room[0][0]['separate']};")
                else:
                    file.write(";")
                if dorm['name'] == "Babilon":
                    file.write(f"{room[0][0]['kitchen']};")
                else:
                    file.write(";")
                if dorm['name'] == "Ustronie":
                    file.write(f"{room[0][0]['type']};")
                else:
                    file.write(";")
                tmp = ""
                for segment in room[0]:
                    tmp += f"{segment['beds']},"
                file.write(f"{tmp[:-1]}\n")

file.close()
