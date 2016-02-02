from .unit import Unit
from .point import Point
from .translation import String


class Group:
    def __init__(self, _id: int, name=None):
        if not isinstance(_id, int):
            raise TypeError("id must be an integer")
        self.id = _id
        self.hidden = False
        self.units = []  # type: List[Unit]
        self.spans = []
        self.points = []  # type: List[MovingPoint]
        self.name = name if name else String()

    def add_unit(self, unit: Unit):
        self.units.append(unit)

    def add_point(self, point: Point):
        self.points.append(point)

    def add_span(self, pos):
        self.spans.append({"x": pos.x, "y": pos.y})

    def x(self):
        if len(self.units) > 0:
            return self.units[0].x
        return None

    def y(self):
        if len(self.units) > 0:
            return self.units[0].y
        return None

    def dict(self):
        d = {}
        d["hidden"] = self.hidden
        d["name"] = self.name.id
        d["groupId"] = self.id
        if self.units:
            d["x"] = self.units[0].x
            d["y"] = self.units[0].y
            d["units"] = {}
            i = 1
            for unit in self.units:
                d["units"][i] = unit.dict()
                i += 1
        if self.points:
            d["route"] = {"points": {}, "spans": {}}
            i = 1
            for point in self.points:
                d["route"]["points"][i] = point.dict()
                i += 1

            # spans
            i = 1
            for spawn in self.spans:
                d["route"]["spans"][i] = spawn
                i += 1
        return d


class MovingGroup(Group):
    def __init__(self, _id, name=None, start_time=0):
        super(MovingGroup, self).__init__(_id, name)
        self.task = ""
        self.tasks = {}
        self.start_time = start_time
        self.visible = False
        self.frequency = 251

    def dict(self):
        d = super(MovingGroup, self).dict()
        d["task"] = self.task
        d["tasks"] = self.tasks
        d["start_time"] = self.start_time
        d["visible"] = self.visible
        d["frequency"] = self.frequency
        return d


class VehicleGroup(MovingGroup):
    class Task:
        GROUND = "Ground Nothing"

    def __init__(self, _id, name=None, start_time=0):
        super(VehicleGroup, self).__init__(_id, name, start_time)
        self.modulation = 0
        self.communication = True
        self.task = VehicleGroup.Task.GROUND

    def dict(self):
        d = super(VehicleGroup, self).dict()
        d["modulation"] = self.modulation
        d["communication"] = self.communication
        return d


class PlaneGroup(MovingGroup):
    class Task:
        CAS = "CAS"
        CAP = "CAP"

    def __init__(self, _id, name=None, start_time=0):
        super(PlaneGroup, self).__init__(_id, name, start_time)
        self.modulation = 0
        self.communication = True
        self.uncontrolled = False
        self.task = ""

    def dict(self):
        d = super(PlaneGroup, self).dict()
        d["modulation"] = self.modulation
        d["communication"] = self.communication
        d["uncontrolled"] = self.uncontrolled
        return d


class StaticGroup(Group):
    def __init__(self, _id, name=None):
        super(StaticGroup, self).__init__(_id, name)
        self.dead = False
        self.heading = 0

    def dict(self):
        d = super(StaticGroup, self).dict()
        d["dead"] = self.dead
        d["heading"] = self.heading
        return d