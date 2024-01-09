class Segment:
    def __init__(self, room, symbol: str, beds: int):
        self._room = room
        self._symbol = symbol
        self.beds = beds
        self.tenants = []

    def __str__(self):
        return f"\t\tSegment {self.symbol()}\n" \
                       f"\t\tLiczba łóżek: {self.beds}\n" \
                       f"\t\tLiczba mieszkańców: {len(self.tenants)}\n"

    def __lt__(self, other):
        return self.symbol() < other.symbol()

    def symbol(self) -> str:
        return self._symbol

    def room(self):
        return self._room
