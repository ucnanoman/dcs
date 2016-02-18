from .group import VehicleGroup, PlaneGroup, StaticGroup


class Country:
    callsign = {}

    def __init__(self, _id, name):
        self.id = _id
        self.name = name
        self.vehicle_group = []  # type: list[VehicleGroup]
        self.plane_group = []  # type: list[PlaneGroup]
        self.static_group = []  # type: list[StaticGroup]

    def name(self):
        return self.name

    def add_vehicle_group(self, vgroup):
        self.vehicle_group.append(vgroup)

    def add_plane_group(self, pgroup):
        self.plane_group.append(pgroup)

    def add_static_group(self, sgroup):
        self.static_group.append(sgroup)

    def find_vehicle_group(self, name: str):
        for vgroup in self.vehicle_group:
            if name in vgroup.name.str():
                return vgroup

    def find_plane_group(self, name: str):
        for group in self.plane_group:
            if name in group.name.str():
                return group

    def find_static_group(self, name: str):
        for group in self.static_group_group:
            if name in group.name.str():
                return group

    def dict(self):
        d = {}
        d["name"] = self.name
        d["id"] = self.id

        if self.vehicle_group:
            d["vehicle"] = {"group": {}}
            i = 1
            for vgroup in self.vehicle_group:
                d["vehicle"]["group"][i] = vgroup.dict()
                i += 1
        if self.plane_group:
            d["plane"] = {"group": {}}
            i = 1
            for plane_group in self.plane_group:
                d["plane"]["group"][i] = plane_group.dict()
                i += 1

        if self.static_group:
            d["static"] = {"group": {}}
            i = 1
            for static_group in self.static_group:
                d["static"]["group"][i] = static_group.dict()
                i += 1
        return d

    def __str__(self):
        return str(self.id) + "," + self.name + "," + str(self.vehicle_group)
