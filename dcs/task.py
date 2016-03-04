from typing import List


class Task:
    def __init__(self, _id):
        self.id = _id
        self.params = {}
        self.auto = False
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

    @staticmethod
    def create_from_dict(d):
        _id = d["id"]
        t = None
        if _id == "WrappedAction":
            actionid = d["params"]["action"]["id"]
            if actionid == "EPLRS":
                t = EPLRS(None)
            if actionid == "SetFrequency":
                t = SetFrequencyCommand(1)
            if actionid == "ActivateBeacon":
                t = ActivateBeaconCommand(10)
            if actionid == "Option":
                t = OptDisparseUnderFire()
        elif _id == "EngageTargets":
            t = engagetargets_tasks[d["key"]]()
        elif _id == OrbitAction.Id:
            t = OrbitAction(0, 0)
        elif _id == AttackGroup.Id:
            t = AttackGroup(0)
        elif _id == Bombing.Id:
            t = Bombing(0, 0)
        elif _id == EngageTargetsInZone.Id:
            t = EngageTargetsInZone(0, 0)
        elif _id == EngageGroup.Id:
            t = EngageGroup(0)
        elif _id == EngageUnit.Id:
            t = EngageUnit(0)
        else:
            t = tasks_map[_id]()

        t.auto = d["auto"]
        t.enabled = d["enabled"]
        t.number = d["number"]
        t.params = d["params"]
        return t


# TODO check
class AntishipStrikeTaskAction(Task):
    Id = "EngageTargets"
    Key = "AntishipStrike"

    def __init__(self):
        super(AntishipStrikeTaskAction, self).__init__(AntishipStrikeTaskAction.Id)

    def dict(self):
        d = super(AntishipStrikeTaskAction, self).dict()
        d["key"] = AntishipStrikeTaskAction.Key
        return d


class CASTaskAction(Task):
    Id = "EngageTargets"
    Key = "CAS"

    def __init__(self):
        super(CASTaskAction, self).__init__(CASTaskAction.Id)
        self.params = {
            "targetTypes": {1: "Helicopters", 2: "Ground Units", 3: "Light armed ships"},
            "priority": 0
        }

    def dict(self):
        d = super(CASTaskAction, self).dict()
        d["key"] = CASTaskAction.Key
        return d


class SEADTaskAction(Task):
    Id = "EngageTargets"
    Key = "SEAD"

    def __init__(self):
        super(SEADTaskAction, self).__init__(SEADTaskAction.Id)
        self.params = {
            "targetTypes": {1: "Air Defence"},
            "priority": 0
        }

    def dict(self):
        d = super(SEADTaskAction, self).dict()
        d["key"] = SEADTaskAction.Key
        return d


class CAPTaskAction(Task):
    Id = "EngageTargets"
    Key = "CAP"

    def __init__(self):
        super(CAPTaskAction, self).__init__(CAPTaskAction.Id)
        self.params = {
            "targetTypes": {1: "Air"},
            "priority": 0
        }

    def dict(self):
        d = super(CAPTaskAction, self).dict()
        d["key"] = CAPTaskAction.Key
        return d


class FighterSweepTaskAction(Task):
    Id = "EngageTargets"
    Key = "FighterSweep"

    def __init__(self):
        super(FighterSweepTaskAction, self).__init__(FighterSweepTaskAction.Id)
        self.params = {
            "targetTypes": {1: "Planes"},
            "priority": 0
        }

    def dict(self):
        d = super(FighterSweepTaskAction, self).dict()
        d["key"] = FighterSweepTaskAction.Key
        return d

engagetargets_tasks = {
    AntishipStrikeTaskAction.Key: AntishipStrikeTaskAction,
    CASTaskAction.Key: CASTaskAction,
    CAPTaskAction.Key: CAPTaskAction,
    SEADTaskAction.Key: SEADTaskAction,
    FighterSweepTaskAction.Key: FighterSweepTaskAction
}


class EscortTaskAction(Task):
    Id = "Escort"

    def __init__(self, group_id=None, engagement_max_dist=60000, lastwpt=None):
        super(EscortTaskAction, self).__init__(EscortTaskAction.Id)
        self.params = {
            "lastWptIndexFlagChangedManually": False,
            "lastWptIndexFlag": False,
            "engagementDistMax": engagement_max_dist,
            "targetTypes": {1: "Planes"},
            "pos": {"x": -200, "y": -500, "z": 0}
        }
        if group_id:
            self.params["groupId"] = group_id
        if lastwpt:
            self.params["lastWptIndexFlagChangedManually"] = True
            self.params["lastWptIndexFlag"] = True
            self.params["lastWptIndex"] = lastwpt


class AttackGroup(Task):
    Id = "AttackGroup"

    def __init__(self, group_id):
        super(AttackGroup, self).__init__(AttackGroup.Id)
        self.params = {
            "groupId": group_id,
            "weaponType": 1069547520
        }


class Bombing(Task):
    Id = "Bombing"

    def __init__(self, x, y):
        super(Bombing, self).__init__(Bombing.Id)
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
    Id = "EngageTargetsInZone"

    def __init__(self, x, y, radius=5000):
        super(EngageTargetsInZone, self).__init__(EngageTargetsInZone.Id)
        self.params = {
            "targetTypes": {1: "Air Defence"},
            "priority": 0,
            "x": x,
            "y": y,
            "zoneRadius": radius
        }


class EngageGroup(Task):
    Id = "EngageGroup"

    def __init__(self, group_id, visible=False):
        super(EngageGroup, self).__init__(EngageGroup.Id)
        self.auto = False
        self.params = {
            "visible": visible,
            "groupId": group_id,
            "priority": 1,
            "weaponType": 1073741822
        }

# weapontype 14 => guided bombs


class EngageUnit(Task):
    Id = "EngageUnit"

    def __init__(self, unit_id, visible=False):
        super(EngageUnit, self).__init__(EngageUnit.Id)
        self.auto = False
        self.params = {
            "visible": visible,
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
    Id = "AWACS"

    def __init__(self):
        super(AWACSTaskAction, self).__init__(AWACSTaskAction.Id)


class RefuelingTaskAction(Task):
    Id = "Tanker"

    def __init__(self):
        super(RefuelingTaskAction, self).__init__(RefuelingTaskAction.Id)


class OrbitAction(Task):
    Id = "Orbit"
    Pattern_RaceTrack = "Race-Track"
    Pattern_Circle = "Circle"
    supported_pattern = [Pattern_RaceTrack, Pattern_Circle]

    def __init__(self, altitude, speed, pattern=Pattern_RaceTrack):
        super(OrbitAction, self).__init__(OrbitAction.Id)
        if pattern not in OrbitAction.supported_pattern:
            raise RuntimeError("Orbit patter '{pattern}' unknown. Use one of {patterns}.".format(
                pattern=pattern, patterns=','.join(OrbitAction.supported_pattern)))
        self.params = {
            "altitude": altitude,
            "pattern": pattern,
            "speed": speed / 3.6,
            "speedEdited": True
        }

tasks_map = {
    EscortTaskAction.Id: EscortTaskAction,
    AttackGroup.Id: AttackGroup,
    Bombing.Id: Bombing,
    EngageTargetsInZone.Id: EngageTargetsInZone,
    EngageGroup.Id: EngageGroup,
    EngageUnit.Id: EngageUnit,
    AWACSTaskAction.Id: AWACSTaskAction,
    RefuelingTaskAction.Id: RefuelingTaskAction,
    OrbitAction.Id: OrbitAction
}


class WrappedAction(Task):
    Id = "WrappedAction"

    def __init__(self):
        super(WrappedAction, self).__init__(WrappedAction.Id)


class EPLRS(WrappedAction):
    Key = "EPLRS"

    def __init__(self, group_id):
        super(EPLRS, self).__init__()
        self.params = {
            "action": {"id": EPLRS.Key, "params": {"value": True, "groupId": group_id}}
        }


class ActivateBeaconCommand(WrappedAction):
    Key = "ActivateBeacon"

    @staticmethod
    def calc_tacan_frequency(mode_channel, channel, aa=True):
        if not aa and mode_channel == "X":
            if channel < 64:
                freq = 962 + channel - 1
            else:
                freq = 1151 + channel - 64
        else:
            if channel < 64:
                freq = 1088 + channel - 1
            else:
                freq = 1025 + channel - 64

        return freq * 1000000

    def __init__(self, channel, modechannel="X", callsign="TKR", bearing=True):
        super(ActivateBeaconCommand, self).__init__()
        self.params = {
            "action": {
                "id": ActivateBeaconCommand.Key,
                "params": {
                    "type": 4,
                    "frequency": self.calc_tacan_frequency(modechannel, channel),
                    "callsign": callsign,
                    "channel": channel,
                    "modeChannel": modechannel,
                    "bearing": bearing,
                    "system": 4
                }
            }
        }


class SetFrequencyCommand(WrappedAction):
    Key = "SetFrequency"
    Modulation_AM = 0
    Modulation_FM = 1

    def __init__(self, frequency, modulation=Modulation_AM):
        super(SetFrequencyCommand, self).__init__()
        self.params = {
            "action": {
                "id": SetFrequencyCommand.Key,
                "params": {"modulation": modulation, "frequency": frequency * 1000000}
            }
        }


class MainTask:
    name = None
    sub_tasks = []
    perform_task = []  # type: List[Task]


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

class Option(Task):
    Id = "WrappedAction"

    def __init__(self):
        super(Option, self).__init__(Option.Id)


class OptDisparseUnderFire(Option):
    Key = 8

    def __init__(self, value=None):
        super(OptDisparseUnderFire, self).__init__()
        self.params = {
            "action": {"id": "Option", "params": {"name": OptDisparseUnderFire.Key}}
        }
        if value:
            self.params["action"]["params"]["value"] = value
