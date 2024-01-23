from segmentType import SegmentType
import exceptions.segment as Error

class Segment:
    def __init__(self, room, symbol, habitable, beds):
        from room import Room

        # Validate input parameters
        if type(room) is not Room:
            raise Error.WrongRoom
        if type(symbol) is not str:
            raise Error.SymbolNotStr
        if len(symbol) != 1 or symbol not in "QWERTYUIOPASDFGHJKLZXCVBNM":
            raise Error.WrongSymbol
        if type(habitable) is not bool:
            raise Error.WrongHabitable
        if type(beds) is not int:
            raise Error.BedsNotInt
        if beds <= 0:
            raise Error.WrongBeds

        # Assign values to instance variables
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
        # Generate a formatted string representation of the Segment object
        return f"\t\tSegment {self.symbol}\n" \
                       f"\t\tLiczba łóżek: {self.beds}\n" \
                       f"\t\tLiczba mieszkańców: {self.tenants_num()}\n"

    def __lt__(self, other):
        # Compare Segment objects based on their symbols
        return self.symbol < other.symbol

    def tenants_num(self):
        # Return the number of tenants in the segment
        return len(self.tenants)

    def type(self):
        # Create a SegmentType object based on the Segment's characteristics
        dorm = self.room.dorm.name
        location = self.room.dorm.location
        room_beds = self.room.beds()
        segment_beds = self.beds
        condition = self.room.condition
        bathroom = self.room.bathroom
        kitchen = self.room.kitchen
        ad = self.room.ad
        result = SegmentType(dorm, location, room_beds, segment_beds, condition, bathroom, kitchen, ad)
        return result

