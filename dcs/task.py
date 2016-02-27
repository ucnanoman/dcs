class Task:
    def __init__(self, _id):
        self.id = _id
        self.params = {}
        self.auto = True
        self.number = 1
        self.enabled = True

    def main_task_name(self) -> str:
        return self.id

    def dict(self):
        return {
            "id": self.id,
            "auto": self.auto,
            "enabled": self.enabled,
            "params": self.params,
            "number": self.number
        }


# TODO check
class AntishipStrikeTaskAction(Task):
    def __init__(self):
        super(AntishipStrikeTaskAction, self).__init__("EngageTargets")
        self.key = "AntishipStrike"

    def dict(self):
        d = super(AntishipStrikeTaskAction, self).dict()
        d["key"] = self.key
        return d


class CASTaskAction(Task):
    def __init__(self):
        super(CASTaskAction, self).__init__("EngageTargets")
        self.params = {
            "targetTypes": {1: "Helicopters", 2: "Ground Units", 3: "Light armed ships"},
            "priority": 0
        }
        self.key = "CAS"

    def dict(self):
        d = super(CASTaskAction, self).dict()
        d["key"] = self.key
        return d


class SEADTaskAction(Task):
    def __init__(self, group_id):
        super(SEADTaskAction, self).__init__("EngageTargets")
        self.params = {
            "targetTypes": {1: "Air Defence"},
            "priority": 0
        }
        self.key = "SEAD"

    def dict(self):
        d = super(SEADTaskAction, self).dict()
        d["key"] = self.key
        return d


class CAPTaskAction(Task):
    def __init__(self):
        super(CAPTaskAction, self).__init__("EngageTargets")
        self.params = {
            "targetTypes": {1: "Air"},
            "priority": 0
        }
        self.key = "CAP"

    def dict(self):
        d = super(CAPTaskAction, self).dict()
        d["key"] = self.key
        return d


class FighterSweepTaskAction(Task):
    def __init__(self):
        super(FighterSweepTaskAction, self).__init__("EngageTargets")
        self.params = {
            "targetTypes": {1: "Planes"},
            "priority": 0
        }
        self.key = "FighterSweep"

    def dict(self):
        d = super(FighterSweepTaskAction, self).dict()
        d["key"] = self.key
        return d


class EscortTaskAction(Task):
    def __init__(self, group_id, engagement_max_dist=60000):
        super(EscortTaskAction, self).__init__("Escort")
        self.params = {
            "lastWptIndexFlagChangedManually": True,
            "groupId": group_id,
            "lastWptIndexFlag": False,
            "engagementDistMax": engagement_max_dist,
            "targetTypes": {1: "Planes"},
            "pos": {"x": -200, "y": -500, "z": 0}
        }


class AttackGroup(Task):
    def __init__(self, group_id):
        super(AttackGroup, self).__init__("AttackGroup")
        self.params = {
            "groupId": group_id,
            "weaponType": 1069547520
        }


class Bombing(Task):
    def __init__(self, x, y):
        super(Bombing, self).__init__("Bombing")
        self.params = {
            "directionEnabled": False,
            "direction": 0,
            "attackQtyLimit": False,
            "attackQty": 1,
            "expend": "Auto",
            "y": y,
            "groupAttack": False,
            "altitude": 88,
            "altitudeEnabled": False,
            "weaponType": 1073741822,
            "x": x
        }


class EngageTargetsInZone(Task):
    def __init__(self, x, y, radius=5000):
        super(EngageTargetsInZone, self).__init__("EngageTargetsInZone")
        self.params = {
            "targetTypes": {1: "Air Defence"},
            "priority": 0,
            "x": x,
            "y": y,
            "zoneRadius": radius
        }


class EngageGroup(Task):
    def __init__(self, group_id):
        super(EngageGroup, self).__init__("EngageGroup")
        self.auto = False
        self.params = {
            "visible": False,
            "groupId": group_id,
            "priority": 1,
            "weaponType": 1073741822
        }

# weapontype 14 => guided bombs


class EngageUnit(Task):
    def __init__(self, unit_id):
        super(EngageUnit, self).__init__("EngageUnit")
        self.auto = False
        self.params = {
            "visible": False,
            "groupAttack": False,
            "unitId": unit_id,
            "priority": 1,
            "weaponType": 1073741822,
            "directionEnabled": False,
            "direction": 0,
            "altitudeEnabled": False,
            "attackQtyLimit": False,
            "attackQty": 0
        }


class AWACSTaskAction(Task):
    def __init__(self):
        super(AWACSTaskAction, self).__init__("AWACS")


class RefuelingTaskAction(Task):
    def __init__(self):
        super(RefuelingTaskAction, self).__init__("Tanker")


class EPLRS(Task):
    def __init__(self, group_id):
        super(EPLRS, self).__init__("WrappedAction")
        self.params = {
            "action": {"id": "EPLRS", "params": {"value": True, "groupId": group_id}}
        }


class SetFrequencyCommand(Task):
    Modulation_AM = 0
    Modulation_FM = 1

    def __init__(self, frequency, modulation=Modulation_AM):
        super(SetFrequencyCommand, self).__init__("WrappedAction")
        self.params = {
            "action": {"id": "SetFrequency", "params": {"modulation": modulation, "frequency": frequency * 1000000}}
        }


class OrbitAction(Task):
    supported_pattern = ["Race-Track", "Circle"]

    def __init__(self, altitude, speed, pattern="Race-Track"):
        super(OrbitAction, self).__init__("Orbit")
        if pattern not in OrbitAction.supported_pattern:
            raise RuntimeError("Orbit patter '{pattern}' unknown. Use one of {patterns}.".format(
                pattern=pattern, patterns=','.join(OrbitAction.supported_pattern)))
        self.params = {
            "altitude": altitude,
            "pattern": pattern,
            "speed": speed / 3.6,
            "speedEdited": True
        }


class MainTask:
    name = None
    sub_tasks = []
    perform_task = []


class Nothing(MainTask):
    id = 15
    name = "Nothing"
    sub_tasks = ["Orbit", "Follow", "Aerobatics"]


class AFAC(MainTask):
    id = 16
    name = "AFAC"
    sub_tasks = ["Orbit", "Follow", "AttackGroup", "AttackUnit", "Bombing", "AttackMapObject"]


class AWACS(MainTask):
    id = 14
    name = "AWACS"
    sub_tasks = ["Orbit", "Follow", "Refueling"]
    perform_task = [AWACSTaskAction]


class AntishipStrike(MainTask):
    id = 30
    name = "AntishipStrike"
    sub_tasks = ["Orbit", "Follow", "AttackGroup", "AttackUnit"]
    perform_task = [AntishipStrikeTaskAction]


class CAS(MainTask):
    id = 31
    name = "CAS"
    sub_tasks = ["Orbit", "Follow", "AttackGroup", "AttackUnit", "Aerobatics", "Refueling"]
    perform_task = [CASTaskAction]

    class EnrouteTasks:
        EngageGroup = EngageGroup
        EngageTargetsInZone = EngageTargetsInZone
        EngageUnit = EngageUnit


class CAP(MainTask):
    id = 11
    name = "CAP"
    sub_tasks = ["Orbit", "Follow", "Aerobatics"]
    perform_task = [CAPTaskAction]


class Escort(MainTask):
    id = 18
    name = "Escort"
    sub_tasks = ["Orbit", "Follow", "Escort"]
    perform_task = [EscortTaskAction]


class FighterSweep(MainTask):
    id = 19
    name = "Fighter Sweep"
    sub_tasks = ["Orbit", "Follow", "Aerobatics"]
    perform_task = [FighterSweepTaskAction]


class GroundAttack(MainTask):
    id = 32
    name = "Ground Attack"
    sub_tasks = ["Orbit", "Follow", "Bombing", "AttackMapObject", "Aerobatics"]


class Intercept(MainTask):
    id = 10
    name = "Intercept"
    sub_tasks = ["Orbit", "Follow", "AttackGroup", "AttackUnit", "Aerobatics"]


class PinpointStrike(MainTask):
    id = 33
    name = "Pinpoint Strike"
    sub_tasks = ["Orbit", "Follow", "Bombing", "AttackMapObject"]


class Reconnaissance(MainTask):
    id = 17
    name = "Reconnaissance"
    sub_tasks = ["Orbit", "Follow", "Aerobatics"]
    perform_task = []


class Refueling(MainTask):
    id = 13
    name = "Refueling"
    sub_tasks = ["Orbit", "Follow"]
    perform_task = [RefuelingTaskAction]


class RunwayAttack(MainTask):
    id = 34
    name = "Ground Attack"
    sub_tasks = ["Orbit", "Follow", "Bombing", "BombingRunway", "AttackMapObject"]
    perform_task = []


class SEAD(MainTask):
    id = 29
    name = "SEAD"
    sub_tasks = ["Orbit", "Follow", "AttackGroup", "AttackUnit", "Escort"]
    perform_task = [SEADTaskAction]


class Transport(MainTask):
    id = 35
    name = "Transport"
    sub_tasks = ["Orbit", "Follow", "Aerobatics"]
    perform_task = []


# options

class OptDisparseUnderFire(Task):
    def __init__(self, value=None):
        super(OptDisparseUnderFire, self).__init__("WrappedAction")
        self.params = {
            "action": {"id": "Option", "params": {"name": 8}}
        }
        if value:
            self.params["action"]["params"]["value"] = value
