from .translation import String
from .task import Task


class Point:
    def __init__(self):
        self.alt = 0
        self.type = "Turning Point"
        self.name = String()
        self.x = 0
        self.y = 0
        self.speed = 0
        self.formation_template = ""
        self.action = ""

    def dict(self):
        return {
            "alt": self.alt,
            "type": self.type,
            "name": self.name.id,
            "x": self.x,
            "y": self.y,
            "speed": self.speed / 3.6,
            "formation_template": self.formation_template,
            "action": self.action
        }


class MovingPoint(Point):
    def __init__(self):
        super(MovingPoint, self).__init__()
        self.alt_type = "BARO"
        self.ETA = 0
        self.ETA_locked = True
        self.speed_locked = True
        self.tasks = []  # type: list[Task]
        self.properties = None
        self.airdrome_id = None
        self.action = "Off Road"

    def dict(self):
        d = super(MovingPoint, self).dict()
        d["alt"] = self.alt
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
