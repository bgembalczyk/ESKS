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
