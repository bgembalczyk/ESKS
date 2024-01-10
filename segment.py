class Segment:
    def __init__(self, room, symbol: str, habitable: bool, beds: int):
        self._room = room
        self._symbol = symbol
        self.beds = beds
        self.habitable = habitable
        self.tenants = []

    @property
    def room(self):
        return self._room

    @property
    def symbol(self):
        return self._symbol

    def __str__(self):
        return f"\t\tSegment {self.symbol}\n" \
                       f"\t\tLiczba łóżek: {self.beds}\n" \
                       f"\t\tLiczba mieszkańców: {len(self.tenants)}\n"

    def __lt__(self, other):
        return self.symbol < other.symbol

    def tenants_num(self):
        return len(self.tenants)

    def type(self):
        return (self.room.dorm.name, )
