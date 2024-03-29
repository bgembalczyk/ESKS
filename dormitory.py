import exceptions.room
import exceptions.dormitory as error
from room import Room

class Dormitory:
    def __init__(self, name, habitable, location):
        dorms = ["Akademik", "Babilon", "Bratniak", "Mikrus", "Muszelka", "Riviera", "Tatrzańska", "Tulipan",
                 "Ustronie", "Żaczek"]
        locations = ["Ochota", "Kampus Centralny", "Mokotów", "Wola", "Kampus Południowy"]

        # Validate input parameters
        if name not in dorms:
            raise error.WrongName
        if location not in locations:
            raise error.WrongLocation
        if type(habitable) is not bool:
            raise error.WrongHabitable

        # Assign values to instance variables
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
        # Generate a formatted string representation of the Dormitory object
        resStr = f"Dom Studencki {self.name}\n" \
                 f"Liczba pokoi: {len(self.rooms)}\n" \
                 f"Liczba łóżek: {self.beds()}\n" \
                 f"Liczba mieszkańców: {self.tenants_num()}\n"
        return resStr

    def beds(self) -> int:
        # Calculate the total number of beds in all rooms of the dormitory
        res = 0
        for room in self.rooms:
            res += room.beds()
        return res

    def tenants_num(self) -> int:
        # Calculate the total number of tenants in all rooms of the dormitory
        res = 0
        for room in self.rooms:
            res += room.tenants_num()
        return res

    def get_room(self, roomNum) -> Room:
        # Retrieve a room based on its number
        if type(roomNum) is not int:
            raise exceptions.room.NumberNotInt
        if roomNum <= 0:
            raise exceptions.room.WrongNumber

        for room_iter in self.rooms:
            if room_iter.number == roomNum:
                return room_iter
        raise error.RoomNotFound

    def input_rooms(self, tab: list) -> None:
        # Add rooms to the dormitory based on the input data
        for room in tab:
            new_room = Room(self, room["number"], room["habitable"], room["condition"], room["bathroom"],
                            room["kitchen"], room["ad"])
            new_room.input_segments(room["segments"])
            self.rooms.append(new_room)

    def segment_types(self, repeating=False):
        # Generate a list of unique or not SegmentType objects based on the dormitory's rooms and segments
        result = []
        if not self.habitable or self.beds() == self.tenants_num():
            return result
        for room in self.rooms:
            if room.habitable and room.beds() > room.tenants_num():
                for segment in room.segments:
                    if segment.habitable and segment.beds > segment.tenants_num():
                        seg_type = segment.type()
                        if (seg_type not in result) or repeating:
                            result.append(seg_type)
        return result
