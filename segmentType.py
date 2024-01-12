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

    def __mul__(self, other):
        # TODO
        # Przerobic na wersje dla dowolnej ilosci argumentów

        if None in [self.dorm, other.dorm]:
            tmp_dorm = [x for x in [self.dorm, other.dorm] if x is not None]
            if len(tmp_dorm) == 0:
                new_dorm = None
            else:
                new_dorm = tmp_dorm[0]
        else:
            # TODO
            pass

        if None in [self.location, other.location]:
            tmp_location = [x for x in [self.location, other.location] if x is not None]
            if len(tmp_location) == 0:
                new_location = None
            else:
                new_location = tmp_location[0]
        else:
            # TODO
            pass

        if None in [self.tenants_num_room, other.tenants_num_room]:
            tmp_tenants_num_room = [x for x in [self.tenants_num_room, other.tenants_num_room] if x is not None]
            if len(tmp_tenants_num_room) == 0:
                new_tenants_num_room = None
            else:
                new_tenants_num_room = tmp_tenants_num_room[0]
        else:
            new_tenants_num_room = min([self.tenants_num_room, other.tenants_num_room])

        if None in [self.tenants_num_segment, other.tenants_num_segment]:
            tmp_tenants_num_segment = [x for x in [self.tenants_num_segment, other.tenants_num_segment] if x is not None]
            if len(tmp_tenants_num_segment) == 0:
                new_tenants_num_segment = None
            else:
                new_tenants_num_segment = tmp_tenants_num_segment[0]
        else:
            new_tenants_num_segment = min([self.tenants_num_segment, other.tenants_num_segment])

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


