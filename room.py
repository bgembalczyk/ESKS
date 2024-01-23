import exceptions.segment
import exceptions.room as error
from segment import Segment

class Room:
    def __init__(self, dorm, number, habitable, condition, bathroom, kitchen, ad):
        from dormitory import Dormitory
        conditions = ["normal", "renovated", "old"]
        bathrooms = ["full", "shower", "null"]

        # Validate input parameters
        if type(dorm) is not Dormitory:
            raise error.WrongDorm
        if type(number) is not int:
            raise error.NumberNotInt
        if number <= 0:
            raise error.WrongNumber
        if type(habitable) is not bool:
            raise error.WrongHabitable
        if condition not in conditions:
            raise error.WrongCondition
        if bathroom not in bathrooms:
            raise error.WrongBathroom
        if type(kitchen) is not bool:
            raise error.WrongKitchen
        if type(ad) is not bool:
            raise error.WrongAd

        # Assign values to instance variables
        self._dorm = dorm
        self._number = number
        self._bathroom = bathroom
        self._kitchen = kitchen
        self._ad = ad
        self.habitable = habitable
        self.condition = condition
        self.segments = []

    @property
    def dorm(self):
        return self._dorm

    @property
    def number(self):
        return self._number

    @property
    def bathroom(self):
        return self._bathroom

    @property
    def kitchen(self):
        return self._kitchen

    @property
    def ad(self):
        return self._ad

    def beds(self) -> int:
        # Calculate the total number of beds in all segments of the room
        res = 0
        for segment_iter in self.segments:
            res += segment_iter.beds
        return res

    def tenants_num(self) -> int:
        # Calculate the total number of tenants in all segments of the room
        res = 0
        for segment in self.segments:
            res += len(segment.tenants)
        return res

    def __str__(self):
        # Generate a formatted string representation of the Room object
        res = f"\tNumer pokoju: {self.number}\n" \
               f"\tLiczba łóżek: {self.beds()}\n" \
               f"\tLiczba mieszkańców: {self.tenants_num()}\n" \
               f"\tLiczba segmentów: {len(self.segments)}\n"
        return res

    def __lt__(self, other):
        # Compare Room objects based on their room numbers
        return self.number < other.number

    def get_segment(self, segment_symbol) -> Segment | None:
        # Retrieve a segment based on its symbol
        if type(segment_symbol) is not str:
            raise exceptions.segment.SymbolNotStr
        if len(segment_symbol) != 1 or segment_symbol not in "QWERTYUIOPASDFGHJKLZXCVBNM":
            raise exceptions.segment.WrongSymbol

        for segment_iter in self.segments:
            if segment_iter.symbol == segment_symbol:
                return segment_iter
        raise error.SegmentNotFound

    def input_segments(self, tab: list):
        # Add segments to the room based on the input data
        for segment in tab:
            new_segment = Segment(self, segment["symbol"], segment["habitable"], segment["beds"])
            self.segments.append(new_segment)
