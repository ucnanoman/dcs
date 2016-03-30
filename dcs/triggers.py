import copy
from typing import List
from enum import Enum

from dcs import mapping
from dcs import action
from dcs import condition


class TriggerZone:
    def __init__(self, _id, position: mapping.Point, radius=1500, hidden=False, name=""):
        self.id = _id
        self.radius = radius
        self.position = copy.copy(position)
        self.hidden = hidden
        self.name = name
        self.color = {1: 1, 2: 1, 3: 1, 4: 0.15}  # TODO color attributes

    def dict(self):
        return {
            "name": self.name,
            "hidden": self.hidden,
            "x": self.position.x,
            "y": self.position.y,
            "zoneId": self.id,
            "radius": self.radius,
            "color": self.color
        }

    def __repr__(self):
        return "TriggerZone({id}, {x}, {y}, {r}, '{n}')".format(
            id=self.id, x=self.position.x, y=self.position.y, r=self.radius, n=self.name
        )


class Triggers:
    def __init__(self):
        self.current_zone_id = 0
        self._zones = []  # type: List[TriggerZone]

    def load_from_dict(self, data):
        self.current_zone_id = 0
        self._zones = []
        for x in data["zones"]:
            imp_zone = data["zones"][x]
            tz = TriggerZone(
                imp_zone["zoneId"],
                mapping.Point(imp_zone["x"], imp_zone["y"]),
                imp_zone["radius"],
                imp_zone["hidden"],
                imp_zone["name"]
            )
            tz.color = imp_zone["color"]
            self._zones.append(tz)
            self.current_zone_id = max(self.current_zone_id, tz.id)

    def add_triggerzone(self, position: mapping.Point, radius=1500, hidden=False, name="") -> TriggerZone:
        self.current_zone_id += 1
        tz = TriggerZone(self.current_zone_id, position, radius, hidden, name)
        self._zones.append(tz)
        return tz

    def zones(self) -> List[TriggerZone]:
        return self._zones

    def dict(self):
        return {
            "zones": {i + 1: self._zones[i].dict() for i in range(0, len(self._zones))}
        }


class Event(Enum):
    NoEvent = ""
    Destroy = "dead"
    Shot = "shot"
    Crash = "crash"
    Eject = "eject"
    Refuel = "refuel"
    PilotDead = "pilot dead"
    BaseCaptured = "base captured"
    TookControl = "took control"
    RefuelStop = "refuel stop"
    Failure = "failure"


class TriggerRule:
    predicate = None

    def __init__(self, event, comment):
        self.comment = comment
        self.eventlist = event
        self.rules = []  # type: List[condition.Condition]
        self.actions = []  # type: List[action.Action]

    def dict(self):
        return {
            "comment": self.comment,
            "eventlist": self.eventlist.value,
            "predicate": self.predicate,
            "rules": {i + 1: self.rules[i].dict() for i in range(0, len(self.rules))},
            "actions": {i + 1: self.actions[i].dict() for i in range(0, len(self.actions))}
        }


class TriggerOnce(TriggerRule):
    predicate = "triggerOnce"

    def __init__(self, event: Event=Event.NoEvent, comment=""):
        super(TriggerOnce, self).__init__(event, comment)


class TriggerContinious(TriggerRule):
    predicate = "triggerContinious"

    def __init__(self, event: Event=Event.NoEvent, comment=""):
        super(TriggerContinious, self).__init__(event, comment)


class TriggerStart(TriggerRule):
    predicate = "triggerStart"

    def __init__(self, comment=""):
        super(TriggerStart, self).__init__(Event.NoEvent, comment)


class TriggerCondition(TriggerRule):
    predicate = "triggerFront"

    def __init__(self, comment=""):
        super(TriggerCondition, self).__init__(Event.NoEvent, comment)


class Rules:
    def __init__(self):
        self.triggers = []  # type: List[TriggerRule]

    def trig(self):
        return {}  # TODO

    def trigrules(self):
        return {i + 1: self.triggers[i].dict() for i in range(0, len(self.triggers))}
