import lua
import os


class FlyingType:
    id = ""
    group_size_max = 4
    large_parking_slot = False
    helicopter = False
    fuel_max = 0
    max_speed = 500
    ammo_type = None
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Air"

    tacan = False
    eplrs = False

    pylons = {}
    payloads = None
    payload_dirs = [
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "payloads"),
        "C:\\Program Files\\Eagle Dynamics\\DCS World\\MissionEditor\\data\\scripts\\UnitPayloads"
    ]

    tasks = ['Nothing']

    @classmethod
    def load_payloads(cls):
        if cls.payloads:
            return cls.payloads

        for payload_dir in FlyingType.payload_dirs:
            payload_filename = os.path.join(payload_dir, cls.id + ".lua")
            if os.path.exists(payload_filename):
                with open(payload_filename, 'r') as payload:
                    pays = lua.loads(payload.read())
                    cls.payloads = pays[list(pays.keys())[0]]
                    return cls.payloads

    @classmethod
    def loadout(cls, _task):
        if cls.payloads:
            for p in cls.payloads["payloads"]:
                payload = cls.payloads["payloads"][p]
                tasks = [payload["tasks"][x] for x in payload["tasks"]]
                if _task.id in tasks:
                    pylons = payload["pylons"]
                    r = [(pylons[x]["num"], {"clsid": pylons[x]["CLSID"]}) for x in pylons]
                    return r
        return None

    @classmethod
    def loadout_by_name(cls, loadout_name):
        if cls.payloads:
            for p in cls.payloads["payloads"]:
                payload = cls.payloads["payloads"][p]
                if payload["name"] == loadout_name:
                    pylons = payload["pylons"]
                    r = [(pylons[x]["num"], {"clsid": pylons[x]["CLSID"]}) for x in pylons]
                    return r
        return None
