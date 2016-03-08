from .unitgroup import VehicleGroup, ShipGroup, PlaneGroup, StaticGroup
from typing import List, Dict


class Country:
    callsign = {}
    planes = []
    helicopters = []

    def __init__(self, _id, name):
        self.id = _id
        self.name = name
        self.vehicle_group = []  # type: List[VehicleGroup]
        self.ship_group = []  # type: List[ShipGroup]
        self.plane_group = []  # type: List[PlaneGroup]
        self.helicopter_group = []  # type: List[HelicopterGroup]
        self.static_group = []  # type: List[StaticGroup]
        self.current_callsign_id = 99
        self.current_callsign_category = {}  # type: Dict[str,int]

    def add_vehicle_group(self, vgroup):
        self.vehicle_group.append(vgroup)

    def add_ship_group(self, sgroup):
        self.ship_group.append(sgroup)

    def add_plane_group(self, pgroup):
        self.plane_group.append(pgroup)

    def add_helicopter_group(self, hgroup):
        self.helicopter_group.append(hgroup)

    def add_static_group(self, sgroup):
        self.static_group.append(sgroup)

    def find_vehicle_group(self, name: str):
        for vgroup in self.vehicle_group:
            if name in vgroup.name.str():
                return vgroup

    def find_ship_group(self, name: str):
        for sgroup in self.ship_group:
            if name in sgroup.name.str():
                return sgroup

    def find_plane_group(self, name: str):
        for group in self.plane_group:
            if name in group.name.str():
                return group

    def find_helicopter_group(self, name: str):
        for group in self.helicopter_group:
            if name in group.name.str():
                return group

    def find_static_group(self, name: str):
        for group in self.static_group_group:
            if name in group.name.str():
                return group

    def next_callsign_id(self):
        self.current_callsign_id += 1
        return self.current_callsign_id

    def next_callsign_category(self, category):
        if category not in self.current_callsign_category:
            self.current_callsign_category[category] = 0
            return self.callsign.get(category)[0]

        self.current_callsign_category[category] += 1
        if self.current_callsign_category[category] >= len(self.callsign[category]):
            self.current_callsign_category[category] = 0
        return self.callsign.get(category)[self.current_callsign_category[category]]

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

        if self.ship_group:
            d["ship"] = {"group": {}}
            i = 1
            for group in self.ship_group:
                d["ship"]["group"][i] = group.dict()
                i += 1

        if self.plane_group:
            d["plane"] = {"group": {}}
            i = 1
            for plane_group in self.plane_group:
                d["plane"]["group"][i] = plane_group.dict()
                i += 1

        if self.helicopter_group:
            d["helicopter"] = {"group": {}}
            i = 1
            for group in self.helicopter_group:
                d["helicopter"]["group"][i] = group.dict()
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
