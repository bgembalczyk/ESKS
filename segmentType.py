from dataclasses import dataclass

@dataclass(eq=False)
class SegmentType:
    dorm: str | None
    location: str | None
    tenants_num_room: int | None
    tenants_num_segment: int | None
    condition: str | None   # "normal", "renovated", "old"
    bathroom: str | None    # "full", "shower", "null"
    kitchen: bool | None
    ad: bool | None

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

    # def __mul__(self, other):
    #     if None in [self.dorm, other.dorm]:
    #         tmp_dorm = [x for x in [self.dorm, other.dorm] if x is not None]
    #         if len(tmp_dorm) == 1:
    #             new_dorm = tmp_dorm[0]
    #         else:
    #             new_dorm = None
    #     else:
    #         if self.dorm == other.dorm:
    #             new_dorm = self.dorm
    #         elif other.dorm in self.dorm:
    #             new_dorm = self.dorm
    #         else:
    #             new_dorm = []
    #             for item in [self.dorm, other.dorm]:
    #                 if type(item) is list:
    #                     new_dorm += item
    #                 else:
    #                     new_dorm.append(item)
    #
    #     if None in [self.location, other.location]:
    #         tmp_location = [x for x in [self.location, other.location] if x is not None]
    #         if len(tmp_location) == 1:
    #             new_location = tmp_location[0]
    #         else:
    #             new_location = None
    #     else:
    #         if self.location == other.location:
    #             new_location = self.location
    #         elif other.location in self.location:
    #             new_location = self.location
    #         else:
    #             new_location = []
    #             for item in [self.location, other.location]:
    #                 if type(item) is list:
    #                     new_location += item
    #                 else:
    #                     new_location.append(item)
    #
    #     if None in [self.tenants_num_room, other.tenants_num_room]:
    #         tmp_tenants_num_room = [x for x in [self.tenants_num_room, other.tenants_num_room] if x is not None]
    #         if len(tmp_tenants_num_room) == 0:
    #             new_tenants_num_room = None
    #         else:
    #             new_tenants_num_room = tmp_tenants_num_room[0]
    #     else:
    #         new_tenants_num_room = min([self.tenants_num_room, other.tenants_num_room])
    #
    #     if None in [self.tenants_num_segment, other.tenants_num_segment]:
    #         tmp_tenants_num_segment = [x for x in [self.tenants_num_segment, other.tenants_num_segment] if x is not None]
    #         if len(tmp_tenants_num_segment) == 0:
    #             new_tenants_num_segment = None
    #         else:
    #             new_tenants_num_segment = tmp_tenants_num_segment[0]
    #     else:
    #         new_tenants_num_segment = min([self.tenants_num_segment, other.tenants_num_segment])
    #
    #     if "renovated" in [self.condition, other.condition]:
    #         new_condition = "renovated"
    #     elif "normal" in [self.condition, other.condition]:
    #         new_condition = "normal"
    #     elif "old" in [self.condition, other.condition]:
    #         new_condition = "old"
    #     else:
    #         new_condition = None
    #
    #     if "full" in [self.bathroom, other.bathroom]:
    #         new_bathroom = "full"
    #     elif "shower" in [self.bathroom, other.bathroom]:
    #         new_bathroom = "shower"
    #     elif "null" in [self.bathroom, other.bathroom]:
    #         new_bathroom = "null"
    #     else:
    #         new_bathroom = None
    #
    #     if self.kitchen is not None or other.kitchen is not None:
    #         new_kitchen = True in [self.kitchen, other.kitchen]
    #     else:
    #         new_kitchen = None
    #
    #     if self.ad is not None or other.ad is not None:
    #         new_ad = not (False in [self.ad, other.ad])
    #     else:
    #         new_ad = None
    #
    #     return SegmentType(new_dorm, new_location, new_tenants_num_room, new_tenants_num_segment, new_condition, new_bathroom, new_kitchen, new_ad)

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
            if not self.kitchen and other.ad:
                result += 1
        return result

    def copy(self):
        return SegmentType(self.dorm, self.location, self.tenants_num_room, self.tenants_num_segment, self.condition, self.bathroom, self.kitchen, self.ad)

    def correct_location(self):
        tmp1 = self.copy()
        tmp2 = self.copy()
        tmp1.dorm = None
        tmp2.location = None
        return tmp1, tmp2
