from segment import Segment

class Room:
    def __init__(self, dorm, number: int, habitable: bool, condition: str, bathroom: str, kitchen: bool, ad: bool):
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

    def __str__(self):
        res = f"\tNumer pokoju: {self.number}\n" \
               f"\tLiczba łóżek: {self.beds()}\n" \
               f"\tLiczba mieszkańców: {self.tenants_num()}\n" \
               f"\tLiczba segmentów: {len(self.segments)}\n"
        return res

    def __lt__(self, other):
        return self.number < other.number

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

    def get_segment(self, segment_symbol: str) -> Segment | None:
        for segment_iter in self.segments:
            if segment_iter.symbol == segment_symbol:
                return segment_iter
        return None

    def input_segments(self, tab: list):
        for segment in tab:
            new_segment = Segment(self, segment["symbol"], segment["habitable"], segment["beds"])
            self.segments.append(new_segment)
