from .unit import Unit
from .terrain import ParkingSlot
from .planes import PlaneType, A_10C


class Plane(Unit):
    def __init__(self, _id=None, name=None, _type: PlaneType=A_10C):
        super(Plane, self).__init__(_id, name, _type.id)
        self.plane_type = _type  # for loadout validation
        self.livery_id = None
        self.parking = None
        self.psi = ""
        self.onboard_num = "010"
        self.alt = 0
        self.alt_type = "BARO"
        self.flare = _type.flare
        self.chaff = _type.chaff
        self.fuel = _type.fuel_max
        self.gun = _type.gun_max
        self.ammo_type = _type.ammo_type
        self.pylons = {}
        self.callsign = None
        self.callsign_dict = {1: 1, 2: 1, 3: 1, "name": ""}
        self.speed = 0

    def set_parking(self, parking_slot: ParkingSlot):
        parking_slot.unit_id = self.id
        self.parking = parking_slot.id

    def load_pylon(self, pylon, weapon):
        if pylon not in self.plane_type.pylons:
            raise RuntimeError("Plane {pn} has no pylon {p}.".format(pn=self.plane_type.id, p=pylon))
        self.pylons[pylon] = weapon["clsid"]
        return True

    def dict(self):
        d = super(Plane, self).dict()
        d["alt"] = self.alt
        d["alt_type"] = self.alt_type
        if self.parking is not None:
            d["parking"] = self.parking
        if self.livery_id:
            d["livery_id"] = self.livery_id
        d["psi"] = self.psi
        d["onboard_num"] = self.onboard_num
        d["speed"] = self.speed
        d["payload"] = {
            "flare": self.flare,
            "chaff": self.chaff,
            "fuel": self.fuel,
            "gun": self.gun,
            "ammo_type": self.ammo_type,
            "pylons": self.pylons
        }
        if self.callsign:
            d["callsign"] = self.callsign
        else:
            d["callsign"] = self.callsign_dict
        return d
