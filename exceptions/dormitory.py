class WrongName(ValueError):
    def __init__(self):
        dorms = ["Akademik", "Babilon", "Bratniak", "Mikrus", "Muszelka", "Riviera", "Tatrzańska", "Tulipan",
                 "Ustronie", "Żaczek"]
        message = "Dormitory: dorm must be one of %r." % dorms
        super().__init__(message)

class WrongLocation(ValueError):
    def __init__(self):
        locations = ["Ochota", "Kampus Centralny", "Mokotów", "Wola", "Kampus Południowy"]
        message = "Dormitory: location must be one of %r." % locations
        super().__init__(message)

class WrongHabitable(TypeError):
    pass

class RoomNotFound(Exception):
    pass
