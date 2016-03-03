from .terrain import ParkingSlot
from .translation import String
from .flyingtype import FlyingType
import json
import copy
import math


class Skill:
    AVERAGE = "Average"
    GOOD = "Good"
    HIGH = "High"
    EXCELLENT = "Excellent"
    RANDOM = "Random"
    PLAYER = "Player"
    CLIENT = "Client"


class Unit:
    def __init__(self, _id, name=None, type=""):
        self.type = type
        self.x = 0
        self.y = 0
        self.heading = 0
        self.id = _id
        self.skill = Skill.AVERAGE
        self.name = name if name else String()

    def set_position(self, pos):
        self.x = pos.x()
        self.y = pos.y()

    def clone(self, _id):
        new = copy.copy(self)
        new.id = _id
        return new

    def dict(self):
        d = {
            "type": self.type,
            "x": self.x,
            "y": self.y,
            "heading": math.radians(self.heading),
            "skill": self.skill,
            "unitId": self.id,
            "name": self.name.id
        }
        return d


class FlyingUnit(Unit):
    def __init__(self, _id=None, name=None, _type: FlyingType=None):
        super(FlyingUnit, self).__init__(_id, name, _type.id)
        self.unit_type = _type  # for loadout validation
        self.unit_type.load_payloads()
        self.livery_id = None
        self.parking = None
        self.psi = 0
        self.onboard_num = "010"
        self.alt = 0
        self.alt_type = "BARO"
        self.flare = _type.flare
        self.chaff = _type.chaff
        self.fuel = _type.fuel_max
        self.gun = 100
        self.ammo_type = _type.ammo_type
        self.pylons = {}
        self.callsign = None
        self.callsign_dict = {1: 1, 2: 1, 3: 1, "name": ""}
        self.speed = 0
        self.radio = None
        self.hardpoint_racks = True

    def load_from_dict(self, dict):
        self.x = dict["x"]
        self.y = dict["y"]
        self.heading = math.degrees(dict["heading"])
        self.type = dict["type"]
        self.skill = dict["skill"]
        self.livery_id = dict.get("livery_id")
        self.x = dict["x"]
        self.y = dict["y"]
        self.alt_type = dict["alt_type"]
        self.alt = dict["alt"]
        self.psi = dict["psi"]
        self.speed = dict["speed"]
        self.fuel = dict["payload"]["fuel"]
        self.gun = dict["payload"]["gun"]
        self.flare = dict["payload"]["flare"]
        self.chaff = dict["payload"]["chaff"]
        self.ammo_type = dict["payload"].get("ammo_type")
        self.pylons = dict["payload"]["pylons"]
        self.onboard_num = dict["onboard_num"]
        if isinstance(dict["callsign"], int):
            self.callsign = dict["callsign"]
        else:
            self.callsign_dict = dict["callsign"]
        self.parking = dict.get("parking", None)
        self.radio = dict.get("Radio")
        self.hardpoint_racks = dict.get("hardpoint_racks", True)
        return True

    def set_parking(self, parking_slot: ParkingSlot):
        parking_slot.unit_id = self.id
        self.parking = parking_slot.id

    def load_pylon(self, weapon, pylon=None):
        if pylon is None:
            pylon = weapon[0]
        if pylon not in self.unit_type.pylons:
            raise RuntimeError("Plane {pn} has no pylon {p}.".format(pn=self.unit_type.id, p=pylon))
        if weapon is None:
            return self.pylons.pop(pylon, None)
        self.pylons[pylon] = {"CLSID": weapon[1]["clsid"]}
        return True

    def store_loadout(self, filename):
        with open(filename, 'w') as loadout:
            json.dump(self.pylons, loadout)

        return True

    def load_loadout(self, filename):
        with open(filename, 'r') as loadout:
            self.pylons = json.load(loadout)

        return True

    def reset_loadout(self):
        self.pylons = {}

    def set_default_preset_channel(self, freq):
        if self.radio:
            self.radio[1]["channels"][1] = freq

    def set_radio_preset(self):
        if self.unit_type.panel_radio:
            self.radio = self.unit_type.panel_radio

    def set_player(self):
        self.skill = Skill.PLAYER
        self.set_radio_preset()

    def set_client(self):
        self.skill = Skill.CLIENT
        self.set_radio_preset()

    def dict(self):
        d = super(FlyingUnit, self).dict()
        d["alt"] = self.alt
        d["alt_type"] = self.alt_type
        if self.parking is not None:
            d["parking"] = self.parking
        if self.livery_id:
            d["livery_id"] = self.livery_id
        d["psi"] = self.psi
        d["onboard_num"] = self.onboard_num
        d["speed"] = self.speed
        if self.unit_type.pylons:
            d["hardpoint_racks"] = self.hardpoint_racks
        d["payload"] = {
            "flare": self.flare,
            "chaff": self.chaff,
            "fuel": self.fuel,
            "gun": self.gun,
            "pylons": self.pylons
        }
        if self.ammo_type:
            d["payload"]["ammo_type"] = self.ammo_type
        if self.callsign:
            d["callsign"] = self.callsign
        else:
            d["callsign"] = self.callsign_dict
        if self.radio:
            d["Radio"] = self.radio
        return d
