from segment import Segment

class Student:
    def __init__(self, id: int, applicationTime: int, prefDorm, prefTenantsNum):
        self.id = id
        self.applicationTime = applicationTime
        self.prefDorm = prefDorm
        self.prefTenantsNum = prefTenantsNum
        self.dorm = None

    def __str__(self):
        return f"ID: {self.id}\n" \
               f"Application time: {self.applicationTime}\n" \
               f"Chosen dorm: {self.prefDorm}\n" \
               f"Lives in: {self.dorm}"

    def __lt__(self, other):
        return self.applicationTime < other.applicationTime

    def accommodate(self, segmentVar: Segment) -> None:
        segmentVar.tenants.append(self)
        self.dorm = segmentVar.room().dorm()
