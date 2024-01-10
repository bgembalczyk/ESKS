from room import Room
from segment import Segment
from student import Student


class Dormitory:
    def __init__(self, name: str, habitable: bool, location: str):
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
                 f"Liczba mieszkańców: {self.tenants_num()}\n"
        return resStr

    def beds(self) -> int:
        res = 0
        for room in self.rooms:
            res += room.beds()
        return res

    def tenants_num(self) -> int:
        res = 0
        for room in self.rooms:
            res += room.tenants_num()
        return res

    def get_room(self, roomNum: int) -> Room | None:
        for room_iter in self.rooms:
            if room_iter.number() == roomNum:
                return room_iter
        return None

    def input_rooms(self, tab: list) -> None:
        for room in tab:
            new_room = Room(self, room["number"], room["habitable"], room["condition"], room["bathroom"],
                            room["kitchen"], room["ad"])
            new_room.input_segments(room["segments"])
            self.rooms.append(new_room)

    def segment_types(self):
        result = []
        if not self.habitable:
            return result
        for room in self.rooms:
            if room.habitable:
                for segment in room.segments:
                    if segment.habitable:
                        seg_type = (self.name, self.location, room.beds(), segment.beds, room.condition, room.bathroom, room.kitchen, room.ad)
                        if seg_type not in result:
                            result.append(seg_type)
        return result

    # TODO
    # nie ma już Student.prefTenantsNum
    def find_place(self, student: Student) -> Segment | None:
        pref_mates_num = student.prefTenantsNum
        for room in self.rooms:
            for segment in room.segments:
                if segment.beds == pref_mates_num and len(segment.tenants) < segment.beds:
                    return segment
        for room in self.rooms:
            for segment in room.segments:
                if len(segment.tenants) < segment.beds:
                    return segment
        return None
