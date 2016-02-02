from .unit import Unit


class PlaneType:
    A10C = "A-10C"


class Plane(Unit):
    def __init__(self, _id=None, name=None, type=""):
        super(Plane, self).__init__(_id, name, type)
        self.livery_id = None
        self.parking = None
        self.psi = ""
        self.onboard_num = "010"
        self.alt = 0
        self.alt_type = "BARO"
        self.flare = 0
        self.chaff = 0
        self.fuel = 0
        self.gun = 0
        self.ammo_type = 0
        self.pylons = {}
        self.callsign_name = ""
        self.callsign = [1, 1, 1]
        self.speed = 0

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
