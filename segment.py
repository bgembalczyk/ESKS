from segmentType import SegmentType
from exceptions.segment import *

class Segment:
    def __init__(self, room, symbol, habitable, beds):
        from room import Room

        if type(room) is not Room:
            raise WrongRoom
        if type(symbol) is not str:
            raise SymbolNotStr
        if len(symbol) != 1 or symbol not in "QWERTYUIOPASDFGHJKLZXCVBNM":
            raise WrongSymbol
        if type(habitable) is not bool:
            raise WrongHabitable
        if type(beds) is not int:
            raise BedsNotInt
        if beds <= 0:
            raise WrongBeds

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
                       f"\t\tLiczba mieszkańców: {self.tenants_num()}\n"

    def __lt__(self, other):
        return self.symbol < other.symbol

    def tenants_num(self):
        return len(self.tenants)

    def type(self):
        result = SegmentType(self.room.dorm.name, self.room.dorm.location, self.room.beds(), self.beds, self.room.condition, self.room.bathroom, self.room.kitchen, self.room.ad)
        return result

