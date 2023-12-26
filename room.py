from segment import Segment

class Room:
    def __init__(self, dorm, number: int, type=None):
        self._dorm = dorm
        self._number = number
        self._type = type
        self.segments = []

    def __str__(self):
        res = f"\tNumer pokoju: {self.number()}\n" \
               f"\tLiczba łóżek: {self.beds()}\n" \
               f"\tLiczba mieszkańców: {self.tenantsNum()}\n" \
               f"\tLiczba segmentów: {len(self.segments)}\n"
        return res

    def __lt__(self, other):
        return self.number() < other.number()

    def dorm(self):
        return self._dorm

    def number(self) -> int:
        return self._number

    def type(self) -> None | str:
        return self._type

    def beds(self) -> int:
        res = 0
        for segmentIter in self.segments:
            res += segmentIter.beds
        return res

    def tenantsNum(self) -> int:
        res = 0
        for segment in self.segments:
            res += len(segment.tenants)
        return res

    def segment(self, segmentSymbol: str) -> Segment | None:
        for i in self.segments:
            if i.symbol() == segmentSymbol:
                return i
        return None

    def inputSegments(self, tab: list) -> None:
        for i in range(len(tab)):
            self.segments.append(Segment(self, f"{chr(ord('A') + i)}", int(tab[i])))
