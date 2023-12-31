import json

dorms_data = [
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
     "rooms": [({"segments": [1, 1, 2], "shower": True}, 40)]
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
     "rooms": [({"segments": [1], "bathroom": True, "kitchen": True}, 210),
               ({"segments": [2], "bathroom": True, "kitchen": True}, 105),
               ({"segments": [2, 2], "bathroom": True, "kitchen": True}, 70)]
     }
]

dorms = {
    "dorms": []
}

for dorm in dorms_data:
    tmp_dorm = {"name": dorm["name"],
                "location": dorm["location"],
                "habitable": True,
                "rooms": []}
    room_number = 1
    for room in dorm["rooms"]:
        room_type, n = room
        for i in range(n):
            tmp_room = {"number": room_number, "habitable": True}
            if "old" in room_type and room_type["old"]:
                tmp_room["condition"] = "old"
            elif "renovated" in room_type and room_type["renovated"]:
                tmp_room["condition"] = "renovated"
            else:
                tmp_room["condition"] = "normal"
            if "bathroom" in room_type and room_type["bathroom"]:
                tmp_room["bathroom"] = "full"
            elif "shower" in room_type and room_type["shower"]:
                tmp_room["bathroom"] = "shower"
            else:
                tmp_room["bathroom"] = "none"
            tmp_room["kitchen"] = "kitchen" in room_type and room_type["kitchen"]
            tmp_room["ad"] = "ad" in room_type and room_type["ad"]
            tmp_room["segments"] = []
            for j, segment in enumerate(room_type["segments"]):
                tmp_segment = {"symbol": chr(ord("A") + j), "habitable": True, "beds": segment, "tenants": []}
                tmp_room["segments"].append(tmp_segment)
            tmp_dorm["rooms"].append(tmp_room)
            room_number += 1
    dorms["dorms"].append(tmp_dorm)

with open("dorms.json", "w", encoding='utf-8') as file:
    json.dump(dorms, file, ensure_ascii=False, indent=4)
