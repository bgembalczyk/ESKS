import random

def genRoom():
    tmp = random.random()
    if tmp >= 0.5:
        return 2
    elif tmp >= 0.25:
        return 1
    elif tmp >= 0.125:
        return 3
    else:
        return 4

N = 4000
dormNames = ["Akademik", "Babilon", "Bratniak", "Mikrus", "Muszelka", "Riviera", "Tatrzańska", "Tulipan", "Ustronie", "Żaczek"]
file = open("students.txt", "w")

for i in range(N):
    file.write(f"{i} {random.randint(1688124089 - 60 * 60 * 24, 1688124089 + 60 * 60 * 24)} {dormNames[random.randint(0, len(dormNames) - 1)]} {genRoom()}\n")

file.close()
