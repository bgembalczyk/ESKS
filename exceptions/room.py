class WrongDorm(TypeError):
    pass

class NumberNotInt(TypeError):
    pass

class WrongNumber(ValueError):
    def __init__(self):
        message = "Room: number must be positive int"
        super().__init__(message)

class WrongHabitable(TypeError):
    pass

class WrongCondition(ValueError):
    def __init__(self):
        conditions = ["normal", "renovated", "old"]
        message = "Room: condition must be one of %r." % conditions
        super().__init__(message)

class WrongBathroom(ValueError):
    def __init__(self):
        bathrooms = ["full", "shower", "null"]
        message = "Room: bathroom must be one of %r." % bathrooms
        super().__init__(message)

class WrongKitchen(TypeError):
    pass

class WrongAd(TypeError):
    pass
