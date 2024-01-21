class WrongDorm(ValueError):
    def __init__(self):
        dorms = [None, "Akademik", "Babilon", "Bratniak", "Mikrus", "Muszelka", "Riviera", "Tatrzańska", "Tulipan",
                 "Ustronie", "Żaczek"]
        message = "SegmentType: dorm must be one of %r." % dorms
        super().__init__(message)

class WrongLocation(ValueError):
    def __init__(self):
        locations = [None, "Ochota", "Kampus Centralny", "Mokotów", "Wola", "Kampus Południowy"]
        message = "SegmentType: location must be one of %r." % locations
        super().__init__(message)

class WrongCondition(ValueError):
    def __init__(self):
        conditions = [None, "normal", "renovated", "old"]
        message = "SegmentType: condition must be one of %r." % conditions
        super().__init__(message)

class WrongBathroom(ValueError):
    def __init__(self):
        bathrooms = [None, "full", "shower", "null"]
        message = "SegmentType: bathroom must be one of %r." % bathrooms
        super().__init__(message)

class WrongKitchen(TypeError):
    pass

class WrongAd(TypeError):
    pass

class TenantsNumNotInt(TypeError):
    pass

class WrongTenantsNumRoom(ValueError):
    def __init__(self):
        message = "SegmentType: tenants_num_room must be greater than 0"
        super().__init__(message)

class WrongTenantsNumSegment(ValueError):
    pass

class Incomparable(Exception):
    pass
