import lua
import os


class FlyingType:
    id = ""
    group_size_max = 4
    large_parking_slot = False
    helicopter = False
    fuel_max = 0
    ammo_type = None
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Air"

    pylons = {}
    payloads = None

    tasks = ['Nothing']

    @classmethod
    def load_payloads(cls):
        if cls.payloads:
            return cls.payloads

        payload_filename = "payloads/" + cls.id + ".lua"
        payload_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), payload_filename)
        if os.path.exists(payload_filename):
            with open(payload_filename, 'r') as payload:
                pays = lua.loads(payload.read())
                cls.payloads = pays[list(pays.keys())[0]]

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
