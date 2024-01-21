import exceptions.segment
from segment import Segment
from exceptions.room import *

class Room:
    def __init__(self, dorm, number, habitable, condition, bathroom, kitchen, ad):
        from dormitory import Dormitory
        conditions = ["normal", "renovated", "old"]
        bathrooms = ["full", "shower", "null"]

        if type(dorm) is not Dormitory:
            raise WrongDorm
        if type(number) is not int:
            raise NumberNotInt
        if number <= 0:
            raise WrongNumber
        if type(habitable) is not bool:
            raise WrongHabitable
        if condition not in conditions:
            raise WrongCondition
        if bathroom not in bathrooms:
            raise WrongBathroom
        if type(kitchen) is not bool:
            raise WrongKitchen
        if type(ad) is not bool:
            raise WrongAd

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
        res = 0
        for segment_iter in self.segments:
            res += segment_iter.beds
        return res

    def tenants_num(self) -> int:
        res = 0
        for segment in self.segments:
            res += len(segment.tenants)
        return res

    def __str__(self):
        res = f"\tNumer pokoju: {self.number}\n" \
               f"\tLiczba łóżek: {self.beds()}\n" \
               f"\tLiczba mieszkańców: {self.tenants_num()}\n" \
               f"\tLiczba segmentów: {len(self.segments)}\n"
        return res

    def __lt__(self, other):
        return self.number < other.number

    def get_segment(self, segment_symbol) -> Segment | None:
        if type(segment_symbol) is not str:
            raise exceptions.segment.SymbolNotStr
        if len(segment_symbol) != 1 or segment_symbol not in "QWERTYUIOPASDFGHJKLZXCVBNM":
            raise exceptions.segment.WrongSymbol

        for segment_iter in self.segments:
            if segment_iter.symbol == segment_symbol:
                return segment_iter
        raise SegmentNotFound

    def input_segments(self, tab: list):
        for segment in tab:
            new_segment = Segment(self, segment["symbol"], segment["habitable"], segment["beds"])
            self.segments.append(new_segment)
