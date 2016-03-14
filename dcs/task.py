from typing import List, Dict


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


class TargetType(type):
    id = None

    def __str__(self):
        return '"{id}"'.format(id=self.id)


class Targets(metaclass=TargetType):
    class All(metaclass=TargetType):
        id = "All"
        class Air(metaclass=TargetType):
            id = "Air"
            class Planes(metaclass=TargetType):
                id = "Planes"
                class Fighters(metaclass=TargetType):
                    id = "Fighters"
                class Bombers(metaclass=TargetType):
                    id = "Bombers"
            class Helicopters(metaclass=TargetType):
                id = "Helicopters"

        class GroundUnits(metaclass=TargetType):
            id = "Ground Units"
            class Infantry(metaclass=TargetType):
                id = "Infantry"
            class Fortifications(metaclass=TargetType):
                id = "Fortifications"
            class GroundVehicles(metaclass=TargetType):
                id = "Ground vehicles"

                class ArmoredVehicles(metaclass=TargetType):
                    id = "Armored vehicles"
                    class Tanks(metaclass=TargetType):
                        id = "Tanks"
                    class IFV(metaclass=TargetType):
                        id = "IFV"
                    class APC(metaclass=TargetType):
                        id = "APC"
                class Artillery(metaclass=TargetType):
                    id = "Artillery"
                class UnarmedVehicles(metaclass=TargetType):
                    id = "Unarmed vehicles"
            class AirDefence(metaclass=TargetType):
                id = "Air Defence"
                class AAA(metaclass=TargetType):
                    id = "AAA"
                    class SAMRelated(metaclass=TargetType):
                        id = "SAM related"
                        class SRSAM(metaclass=TargetType):
                            id = "SR SAM"
                        class MRSAM(metaclass=TargetType):
                            id = "MR SAM"
                        class LRSAM(metaclass=TargetType):
                            id = "LR SAM"

        class Naval(metaclass=TargetType):
            id = "Naval"
            class Ships(metaclass=TargetType):
                id = "Ships"
                class ArmedShips(metaclass=TargetType):
                    id = "Armed ships"
                    class HeavyArmedShips(metaclass=TargetType):
                        id = "Heavy armed ships"
                        class AircraftCarriers(metaclass=TargetType):
                            id = "Aircraft Carriers"
                        class Cruisers(metaclass=TargetType):
                            id = "Cruisers"
                        class Destroyers(metaclass=TargetType):
                            id = "Destroyers"
                        class Frigates(metaclass=TargetType):
                            id = "Frigates"
                        class Corvettes(metaclass=TargetType):
                            id = "Corvettes"
                    class LightArmedShips(metaclass=TargetType):
                        id = "Light armed ships"
                class UnarmedShips(metaclass=TargetType):
                    id = "Unarmed ships"
            class Submarines(metaclass=TargetType):
                id = "Submarines"


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
            "targetTypes": {
                1: Targets.All.Air.Helicopters,
                2: Targets.All.GroundUnits,
                3: Targets.All.Naval.Ships.ArmedShips.LightArmedShips
            },
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
            "targetTypes": {1: Targets.All.GroundUnits.AirDefence},
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
            "targetTypes": {1: Targets.All.Air},
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
            "targetTypes": {1: Targets.All.Air.Planes},
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

    def __init__(self,
                 group_id=None,
                 engagement_max_dist=60000,
                 lastwpt=None,
                 targets: List[str]=None,
                 position: Dict[str, float]=None):
        super(EscortTaskAction, self).__init__(EscortTaskAction.Id)
        if targets is None:
            targets = [Targets.All.Air.Planes]
        if position is None:
            position = {"x": -200, "y": -100, "z": -500}
        self.params = {
            "lastWptIndexFlagChangedManually": False,
            "lastWptIndexFlag": False,
            "engagementDistMax": engagement_max_dist,
            "targetTypes": {i: targets[i-1] for i in range(1, len(targets)+1)},
            "pos": position
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


class EngageTargets(Task):
    Id = "EngageTargets"

    def __init__(self, max_distance=None, targets: List[str]=None):
        super(EngageTargets, self).__init__(EngageTargets.Id)
        if targets is None:
            targets = [Targets.All]
        self.params = {
            "targetTypes": {i: targets[i-1] for i in range(1, len(targets)+1)},
            "maxDistEnabled": True if max_distance else False,
            "maxDist": max_distance,
            "priority": 0
        }


class EngageTargetsInZone(Task):
    Id = "EngageTargetsInZone"

    def __init__(self, x, y, radius=5000, targets: List[str]=None):
        super(EngageTargetsInZone, self).__init__(EngageTargetsInZone.Id)
        if targets is None:
            targets = [Targets.All]
        self.params = {
            "targetTypes": {i: targets[i-1] for i in range(1, len(targets)+1)},
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


class SetInvisibleCommand(WrappedAction):
    Key = "SetInvisible"

    def __init__(self, value=True):
        super(SetInvisibleCommand, self).__init__()
        self.params = {
            "action": {
                "id": SetInvisibleCommand.Key,
                "params": {"value": value}
            }
        }


class SetImmortalCommand(WrappedAction):
    Key = "SetImmortal"

    def __init__(self, value=True):
        super(SetImmortalCommand, self).__init__()
        self.params = {
            "action": {
                "id": SetImmortalCommand.Key,
                "params": {"value": value}
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

    class EnrouteTasks:
        EngageTargets = EngageTargets
        EngageTargetsInZone = EngageTargetsInZone
        EngageGroup = EngageGroup
        EngageUnit = EngageUnit


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


MainTask.map = {
    SEAD.name: SEAD,
    CAP.name: CAP
}

# options

class Option(Task):
    Id = "WrappedAction"
    Key = None

    def __init__(self, value=None):
        super(Option, self).__init__(Option.Id)
        self.params = {
            "action": {"id": "Option", "params": {"name": self.Key}}
        }
        if value:
            self.params["action"]["params"]["value"] = value


class OptROE(Option):
    """
    Sets the groups rules of engagement.
    Ultimately defines whether or not the AI group is allowed to attack.
    This option can override all other tasking. With the 1.5 patch two of the values
    have different names in the mission editor.
    However the behavior is still exactly the same as before,
    its just labeled slightly different. The scripting engine still uses the previous values.
    """
    Key = 0

    class Values:
        WeaponFree = 0
        """
        AI will engage any enemy group it detects.
        Target prioritization is based based on the threat of the target.
        """
        OpenFireWeaponFree = 1
        """AI will engage any enemy group it detects, but will prioritize targets specified in the groups tasking."""
        OpenFire = 2
        """AI will engage only targets specified in its taskings."""
        ReturnFire = 3
        """AI will only engage threats that shoot first."""
        WeaponHold = 4
        """AI will hold fire under all circumstances."""

    def __init__(self, value=Values.WeaponFree):
        super(OptROE, self).__init__(value)


class OptReactOnThreat(Option):
    """
    Defines the allowable action for an airborne group to take in response to a threat.
    This option can have an effect on other tasking.
    """
    Key = 1

    class Values:
        NoReaction = 0
        """No defensive actions will take place to counter threats"""
        PassiveDefense = 1
        """
        AI will use jammers and other countermeasures in an attempt to defeat the threat.
        AI will not attempt a maneuver to defeat a threat.
        """
        EvadeFire = 2
        """
        AI will react by performing defensive maneuvers against incoming threats,
        AI will also use passive defense.
        """
        ByPassAndEscape = 3
        """
        AI will attempt to avoid enemy threat zones all together.
        This includes attempting to fly above or around threats.
        """
        AllowAbortMission = 4
        """If a threat is deemed severe enough the AI will abort its mission and return to base."""

    def __init__(self, value=Values.NoReaction):
        super(OptReactOnThreat, self).__init__(value)


class OptDisparseUnderFire(Option):
    Key = 8

    def __init__(self, value=None):
        super(OptDisparseUnderFire, self).__init__(value)
