from room import Room
from segment import Segment
from student import Student

class Dormitory:
    def __init__(self, name: str, location, habitable):
        self._name = name
        self._location = location
        self.habitable = habitable
        self.rooms = []

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def __str__(self):
        resStr = f"Dom Studencki {self.name}\n" \
                 f"Liczba pokoi: {len(self.rooms)}\n" \
                 f"Liczba łóżek: {self.beds()}\n" \
                 f"Liczba mieszkańców: {self.tenantsNum()}\n"
        return resStr

    def beds(self) -> int:
        res = 0
        for room in self.rooms:
            res += room.beds()
        return res

    def tenantsNum(self) -> int:
        res = 0
        for room in self.rooms:
            res += room.tenants_num()
        return res

    def room(self, roomNum: int) -> Room | None:
        for i in self.rooms:
            if i.number() == roomNum:
                return i
        return None

    def inputRooms(self, tab: list) -> None:
        if tab[1] or tab[3] == "separated":
            roomTmp = Room(self, int(tab[0]), "separated")
        elif tab[2] == "kitchen":
            roomTmp = Room(self, int(tab[0]), "kitchen")
        elif tab[3] == "renovated":
            roomTmp = Room(self, int(tab[0]), "renovated")
        else:
            roomTmp = Room(self, int(tab[0]))
        roomTmp.inputSegments(tab[-1])
        self.rooms.append(roomTmp)

    # TODO
    # nie ma już Student.prefTenantsNum
    def findPlace(self, student: Student) -> Segment | None:
        prefMatesNum = student.prefTenantsNum
        for room in self.rooms:
            for segment in room.segments:
                if segment.beds == prefMatesNum and len(segment.tenants) < segment.beds:
                    return segment
        for room in self.rooms:
            for segment in room.segments:
                if len(segment.tenants) < segment.beds:
                    return segment
        return None

