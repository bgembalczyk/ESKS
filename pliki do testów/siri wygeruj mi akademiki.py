dormsData = [
    {"name": "Akademik", "beds": 800,
     "rooms": [([{"beds": 1, "floor": [2], "separate": False}], 0.5 / 6),
               ([{"beds": 2, "floor": [2], "separate": False}], 0.5 / 6),
               ([{"beds": 1, "floor": [3], "separate": False}], 0.2 / 6),
               ([{"beds": 2, "floor": [3], "separate": False}], 0.2 / 6),
               ([{"beds": 2, "floor": [3], "separate": True}], 0.2 / 6),
               ([{"beds": 3, "floor": [3], "separate": False}], 0.2 / 6),
               ([{"beds": 4, "floor": [3], "separate": False}], 0.2 / 6),
               ([{"beds": 1, "floor": [4, 5, 6, 7, 8], "separate": False}], 0.25 / 6),
               ([{"beds": 2, "floor": [4, 5, 6, 7, 8], "separate": False}], 0.25 / 6),
               ([{"beds": 3, "floor": [4, 5, 6, 7, 8], "separate": False}], 0.25 / 6),
               ([{"beds": 4, "floor": [4, 5, 6, 7, 8], "separate": False}], 0.25 / 6)]},
    {"name": "Babilon", "beds": 800,
     "rooms": [([{"beds": 1, "kitchen": False}], 0.25 / 7),
               ([{"beds": 2, "kitchen": False}], 0.25 / 7),
               ([{"beds": 2, "kitchen": True}], 0.25 / 7),
               ([{"beds": 3, "kitchen": False}], 0.25 / 7),
               ([{"beds": 2, "kitchen": False}, {"beds": 2, "kitchen": False}], 0.25),
               ([{"beds": 1, "kitchen": False}, {"beds": 3, "kitchen": False}], 0.25 / 7),
               ([{"beds": 2, "kitchen": False}, {"beds": 3, "kitchen": False}], 0.25 / 7),
               ([{"beds": 3, "kitchen": False}, {"beds": 3, "kitchen": False}], 0.25 / 7)]
     },
    {"name": "Bratniak", "beds": 200,
     "rooms": [([{"beds": 2}], 0.4),
               ([{"beds": 3}], 0.4),
               ([{"beds": 4}], 0.1),
               ([{"beds": 5}], 0.1)]
     },
    {"name": "Mikrus", "beds": 490,
     "rooms": [([{"beds": 1}], 1 / 25),
               ([{"beds": 2}], 24 / 25)]
     },
    {"name": "Muszelka", "beds": 150,
     "rooms": [([{"beds": 1}], 0.25),
               ([{"beds": 1}, {"beds": 1}], 0.25),
               ([{"beds": 1}, {"beds": 2}], 0.25),
               ([{"beds": 2}, {"beds": 2}], 0.25)]
     },
    {"name": "Riviera", "beds": 700,
     "rooms": [([{"beds": 2, "floor": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}], 1 / 28),
               ([{"beds": 2, "floor": [15, 16]}], 1 / 28),
               ([{"beds": 3, "floor": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}, {"beds": 3, "floor": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}], 1 / 28),
               ([{"beds": 3, "floor": [15, 16]}, {"beds": 3, "floor": [15, 16]}], 1 / 28)]
     },
    {"name": "Tatrzańska", "beds": 200,
     "rooms": [([{"beds": 1}], 0.2),
               ([{"beds": 1}, {"beds": 1}], 0.2),
               ([{"beds": 1}, {"beds": 2}], 0.2),
               ([{"beds": 2}, {"beds": 2}], 0.4)]
     },
    {"name": "Tulipan", "beds": 150,
     "rooms": [([{"beds": 1}, {"beds": 2}], 1)]
     },
    {"name": "Ustronie", "beds": 340,
     "rooms": [([{"beds": 2, "type": "normal"}], 1 / 3),
               ([{"beds": 2, "type": "renovated"}], 1 / 3),
               ([{"beds": 2, "type": "separated"}], 1 / 3)]
     },
    {"name": "Żaczek", "beds": 700,
     "rooms": [([{"beds": 1}], 0.3),
               ([{"beds": 2}], 0.3),
               ([{"beds": 2}, {"beds": 2}], 0.4)]}
]

file = open("dorms.txt", "w")
# TODO
# Teraz jest już tylko mało czytelne
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
