class SegmentTypeError(Exception):
    pass

class SegmentTypeWrongDorm(SegmentTypeError, ValueError):
    def __init__(self):
        dorms = [None, "Akademik", "Babilon", "Bratniak", "Mikrus", "Muszelka", "Riviera", "Tatrzańska", "Tulipan",
                 "Ustronie", "Żaczek"]
        message = "SegmentType: dorm must be one of %r." % dorms
        super().__init__(message)

class SegmentTypeWrongLocation(SegmentTypeError, ValueError):
    def __init__(self):
        locations = [None, "Ochota", "Kampus Centralny", "Mokotów", "Wola", "Kampus Południowy"]
        message = "SegmentType: location must be one of %r." % locations
        super().__init__(message)

class SegmentTypeWrongCondition(SegmentTypeError, ValueError):
    def __init__(self):
        conditions = [None, "normal", "renovated", "old"]
        message = "SegmentType: condition must be one of %r." % conditions
        super().__init__(message)

class SegmentTypeWrongBathroom(SegmentTypeError, ValueError):
    def __init__(self):
        bathrooms = [None, "full", "shower", "null"]
        message = "SegmentType: bathroom must be one of %r." % bathrooms
        super().__init__(message)

class SegmentTypeWrongKitchen(SegmentTypeError, TypeError):
    pass

class SegmentTypeWrongAd(SegmentTypeError, TypeError):
    pass

class SegmentTypeTenantsNumNotInt(SegmentTypeError, TypeError):
    pass

class SegmentTypeWrongTenantsNumRoom(SegmentTypeError, ValueError):
    def __init__(self):
        message = "SegmentType: tenants_num_room must be greater than 0"
        super().__init__(message)

class SegmentTypeWrongTenantsNumSegment(SegmentTypeError, ValueError):
    pass

class SegmentTypesIncomparable(SegmentTypeError):
    pass
