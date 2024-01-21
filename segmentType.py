from exceptions.segmentType import *

class SegmentType:
    def __init__(self, dorm, location, tenants_num_room, tenants_num_segment, condition, bathroom, kitchen, ad):
        dorms = [None, "Akademik", "Babilon", "Bratniak", "Mikrus", "Muszelka", "Riviera", "Tatrzańska", "Tulipan",
                 "Ustronie", "Żaczek"]
        locations = [None, "Ochota", "Kampus Centralny", "Mokotów", "Wola", "Kampus Południowy"]
        conditions = [None, "normal", "renovated", "old"]
        bathrooms = [None, "full", "shower", "null"]

        if dorm not in dorms:
            raise WrongDorm
        if location not in locations:
            raise WrongLocation
        if tenants_num_room is not None:
            if type(tenants_num_room) is not int:
                raise TenantsNumNotInt
            else:
                if tenants_num_room < 1:
                    raise WrongTenantsNumRoom
        if tenants_num_segment is not None:
            if type(tenants_num_segment) is not int:
                raise TenantsNumNotInt
            else:
                if tenants_num_segment < 1:
                    raise WrongTenantsNumSegment("SegmentType: tenants_num_segment must be greater than 0")
        if tenants_num_room is not None and tenants_num_segment is not None:
            if tenants_num_segment > tenants_num_room:
                raise WrongTenantsNumSegment("SegmentType: tenants_num_segment must be lower than or equal to tenants_num_room")
        if condition not in conditions:
            raise WrongCondition
        if bathroom not in bathrooms:
            raise WrongBathroom
        if type(kitchen) is not bool and kitchen is not None:
            raise WrongKitchen
        if type(ad) is not bool and ad is not None:
            raise WrongAd

        self._dorm = dorm
        self._location = location
        self._tenants_num_room = tenants_num_room
        self._tenants_num_segment = tenants_num_segment
        self._condition = condition
        self._bathroom = bathroom
        self._kitchen = kitchen
        self._ad = ad

    @property
    def dorm(self):
        return self._dorm

    @property
    def location(self):
        return self._location

    @property
    def tenants_num_room(self):
        return self._tenants_num_room

    @property
    def tenants_num_segment(self):
        return self._tenants_num_segment

    @property
    def condition(self):
        return self._condition

    @property
    def bathroom(self):
        return self._bathroom

    @property
    def kitchen(self):
        return self._kitchen

    @property
    def ad(self):
        return self._ad

    def __eq__(self, other):
        if self.dorm is not None and other.dorm is not None:
            if self.dorm != other.dorm:
                return False

        if self.location is not None and other.location is not None:
            if self.location != other.location:
                return False

        if self.tenants_num_room is not None and other.tenants_num_room is not None:
            if self.tenants_num_room != other.tenants_num_room:
                return False

        if self.tenants_num_segment is not None and other.tenants_num_segment is not None:
            if self.tenants_num_segment != other.tenants_num_segment:
                return False

        if self.condition is not None and other.condition is not None:
            if self.condition != other.condition:
                return False

        if self.bathroom is not None and other.bathroom is not None:
            if self.bathroom != other.bathroom:
                return False

        if self.kitchen is not None and other.kitchen is not None:
            if self.kitchen != other.kitchen:
                return False

        if self.ad is not None and other.ad is not None:
            if self.ad != other.ad:
                return False

        return True

    def __lt__(self, other):
        if not (self.dorm == other.dorm or self.dorm is None or self.location == other.location or self.location is None):
            raise Incomparable
        if self.tenants_num_segment is not None and other.tenants_num_segment is not None:
            if self.tenants_num_segment < other.tenants_num_segment:
                return False
            elif self.tenants_num_segment == other.tenants_num_segment:
                if self.tenants_num_room is not None and other.tenants_num_room is not None:
                    if self.tenants_num_room < other.tenants_num_room:
                        return False
        else:
            if self.tenants_num_room is not None and other.tenants_num_room is not None:
                if self.tenants_num_room < other.tenants_num_room:
                    return False

        if self.condition is not None and other.condition is not None:
            if (self.condition == "renovated" and other.condition != "renovated") or (self.condition == "normal" and other.condition == "old"):
                return False

        if self.bathroom is not None and other.bathroom is not None:
            if (self.bathroom == "full" and other.bathroom != "full") or (self.bathroom == "shower" and other.bathroom == "null"):
                return False

        if self.kitchen is not None and other.kitchen is not None:
            if self.kitchen and not other.kitchen:
                return False

        if self.ad is not None and other.ad is not None:
            if not self.ad and other.ad:
                return False

        if self.tenants_num_segment != other.tenants_num_segment:
            return True
        if self.tenants_num_room != other.tenants_num_room:
            return True
        if self.condition != other.condition:
            return True
        if self.bathroom != other.bathroom:
            return True
        if self.kitchen != other.kitchen:
            return True
        if self.ad != other.ad:
            return True
        return False

    def __sub__(self, other):
        # dorm >> num_segment >> num_room >> condition >> bathroom >> kitchen >> ad
        result = 1000000
        if self.dorm is not None and self.location is not None:
            if self.dorm != other.dorm:
                if self.location != other.location:
                    result += 3000000
                else:
                    result += 1000000
            elif self.location != other.location:
                result += 2000000
        elif self.dorm is not None:
            if self.dorm != other.dorm:
                result += 1000000
        elif self.location is not None:
            if self.location != other.location:
                result += 2000000
        res_tent = 0
        if self.tenants_num_room is not None:
            tmp = (other.tenants_num_room - self.tenants_num_room)
            if tmp > 0:
                res_tent += tmp
        if self.tenants_num_segment is not None:
            tmp = (other.tenants_num_segment - self.tenants_num_segment) * 2
            if tmp > 0:
                res_tent += tmp
        result += res_tent * 10000
        if self.condition is not None:
            if self.condition != other.condition:
                if self.condition == "renovated":
                    if other.condition == "normal":
                        result += 1000
                    elif other.condition == "old":
                        result += 2000
                elif self.condition == "normal":
                    if other.condition == "old":
                        result += 1000
        if self.bathroom is not None:
            if self.bathroom != other.bathroom:
                if self.bathroom == "full":
                    if other.bathroom == "shower":
                        result += 100
                    elif other.bathroom == "null":
                        result += 200
                elif self.bathroom == "shower":
                    if other.bathroom == "null":
                        result += 100
        if self.kitchen is not None:
            if self.kitchen and not other.kitchen:
                result += 10
        if self.ad is not None:
            if not self.ad and other.ad:
                result += 1
        return result

    def copy(self):
        return SegmentType(self.dorm, self.location, self.tenants_num_room, self.tenants_num_segment, self.condition, self.bathroom, self.kitchen, self.ad)

    def correct_location(self):
        tmp1 = SegmentType(None, self.location, self.tenants_num_room, self.tenants_num_segment, self.condition, self.bathroom, self.kitchen, self.ad)
        tmp2 = SegmentType(self.dorm, None, self.tenants_num_room, self.tenants_num_segment, self.condition, self.bathroom, self.kitchen, self.ad)
        return tmp1, tmp2
