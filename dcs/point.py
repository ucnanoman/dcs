from .translation import String
from . import task
from . import mapping
from typing import List
from enum import Enum


class PointAction(Enum):
    None_ = ""
    TurningPoint = "Turning Point"
    FlyOverPoint = "Fly Over Point"
    FromParkingArea = "From Parking Area"
    FromParkingAreaHot = "From Parking Area Hot"
    FromRunway = "From Runway"
    Landing = "Landing"
    OnRoad = "On Road"
    OffRoad = "Off Road"
    LineAbreast = "Rank"
    Cone = "Cone"
    Vee = "Vee"
    Diamond = "Diamond"
    EchelonLeft = "EchelonL"
    EchelonRight = "EchelonR"
    Custom = "Custom"


class StaticPoint:
    def __init__(self):
        self.alt = 0
        self.type = "Turning Point"
        self.name = String()
        self.position = mapping.Point(0, 0)
        self.speed = 0
        self.formation_template = ""
        self.action = PointAction.TurningPoint  # type: PointAction

    def load_from_dict(self, d, translation):
        self.alt = d["alt"]
        self.type = d["type"]
        self.position.x = d["x"]
        self.position.y = d["y"]
        self.action = PointAction(d["action"])
        self.formation_template = d["formation_template"]
        self.speed = d["speed"]
        self.name = translation.get_string(d["name"])

    def dict(self):
        return {
            "alt": self.alt,
            "type": self.type,
            "name": self.name.id,
            "x": self.position.x,
            "y": self.position.y,
            "speed": round(self.speed, 13),
            "formation_template": self.formation_template,
            "action": self.action.value
        }


class MovingPoint(StaticPoint):
    def __init__(self):
        super(MovingPoint, self).__init__()
        self.alt_type = "BARO"
        self.ETA = 0
        self.ETA_locked = True
        self.speed_locked = True
        self.tasks = []  # type: List[task.Task]
        self.properties = None
        self.airdrome_id = None

    def load_from_dict(self, d, translation):
        super(MovingPoint, self).load_from_dict(d, translation)
        self.alt_type = d.get("alt_type", None)
        self.ETA_locked = d["ETA_locked"]
        self.ETA = d["ETA"]
        self.speed_locked = d["speed_locked"]
        for t in d["task"]["params"]["tasks"]:
            self.tasks.append(task._create_from_dict(d["task"]["params"]["tasks"][t]))
        self.airdrome_id = d.get("airdromeId", None)
        self.properties = d.get("properties", None)

    def find_task(self, task_type):
        """Searches tasks in this point for the given task class

        :param task_type: task class to search, :py:mod:`dcs.task`
        :return: task instance if found, else None
        """
        for t in self.tasks:
            if isinstance(t, task_type):
                return t
        return None

    def dict(self):
        d = super(MovingPoint, self).dict()
        d["alt_type"] = self.alt_type
        d["ETA"] = self.ETA
        d["ETA_locked"] = self.ETA_locked
        d["speed_locked"] = self.speed_locked
        tasks = {}
        for i in range(0, len(self.tasks)):
            self.tasks[i].number = i+1
            tasks[i+1] = self.tasks[i].dict()
        d["task"] = {
            "id": "ComboTask",
            "params": {
                "tasks": {i+1: self.tasks[i].dict() for i in range(0, len(self.tasks))}
            }
        }
        if self.airdrome_id is not None:
            d["airdromeId"] = self.airdrome_id
        if self.properties is not None:
            d["properties"] = self.properties
        return d
