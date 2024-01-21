class WrongRoom(TypeError):
    pass

class SymbolNotStr(ValueError):
    def __init__(self):
        message = "Segment: symbol must be single uppercase letter"
        super().__init__(message)

class WrongSymbol(TypeError):
    pass

class WrongHabitable(TypeError):
    pass

class BedsNotInt(TypeError):
    pass

class WrongBeds(ValueError):
    def __init__(self):
        message = "Segment: Number of beds must be positive int"
        super().__init__(message)
