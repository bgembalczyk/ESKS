class NotFound(Exception):
    pass

class WrongSegmentReference(Exception):
    def __init__(self):
        message = "Preferred segment must be tuple with (str, [int][char.upper])"
        super().__init__(message)
