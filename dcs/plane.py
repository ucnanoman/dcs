from .unit import Unit
from .terrain import ParkingSlot


class PlaneType:
    id = ""
    group_size_max = 4
    large_parking_slot = False
    fuel_max = 0
    ammo_type = 1
    gun_max = 100
    chaff = 0
    flare = 0
    role = "air"


class A10C(PlaneType):
    id = "A-10C"
    fuel_max = 5029  # kg
    ammo_type = 1
    gun_max = 100  # %
    chaff_max = 480
    chaff = 240
    flare_max = 240
    flare = 120
    role = "air"


class M2000C(PlaneType):
    id = "M-2000C"
    fuel_max = 3165
    chaff_max = 112
    chaff = 112
    flare_max = 16
    flare = 16


class Plane(Unit):
    def __init__(self, _id=None, name=None, _type: PlaneType=A10C):
        super(Plane, self).__init__(_id, name, _type.id)
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
        self.callsign_name = ""
        self.callsign = [1, 1, 1]
        self.speed = 0

    def set_parking(self, parking_slot: ParkingSlot):
        parking_slot.unit_id = self.id
        self.parking = parking_slot.id

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
        d["callsign"] = {
            "name": self.callsign_name,
            1: self.callsign[0],
            2: self.callsign[1],
            3: self.callsign[2]
        }
        return d
