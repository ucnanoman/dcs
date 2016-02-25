import math
from .unit import Unit
from .point import Point, MovingPoint
from .translation import String
from .terrain import Airport
from . import mapping


class Group:
    def __init__(self, _id: int, name=None):
        if not isinstance(_id, int):
            raise TypeError("id must be an integer")
        self.id = _id
        self.hidden = False
        self.units = []  # type: list[Unit]
        self.spans = []
        self.points = []  # type: list[MovingPoint]
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
            d["route"] = {"points": {}}
            i = 1
            for point in self.points:
                d["route"]["points"][i] = point.dict()
                i += 1

        if self.spans is not None:
            # spans
            d["route"]["spans"] = {}
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
        if self.task:
            d["task"] = self.task
        d["tasks"] = self.tasks
        d["start_time"] = self.start_time
        d["visible"] = self.visible
        if self.frequency:
            d["frequency"] = self.frequency
        return d


class VehicleGroup(MovingGroup):
    class Formation:
        Line = 1
        Star = 2
        Rectangle = 3

    def __init__(self, _id, name=None, start_time=0):
        super(VehicleGroup, self).__init__(_id, name, start_time)
        self.modulation = 0
        self.communication = True

    def add_waypoint(self, x, y, _type="Off Road", speed=32) -> MovingPoint:
        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = _type
        mp.x = x
        mp.y = y
        mp.speed = speed / 3.6
        mp.ETA_locked = False

        self.add_point(mp)
        return mp

    def formation_line(self, heading, distance=20):
        x = self.units[0].x
        y = self.units[0].y
        for i in range(0, len(self.units)):
            unit = self.units[i]
            unit.x = x
            unit.y = y + i * distance

            #unit.x = x + i * distance
            #unit.y = y

            unit.heading = heading

    def formation_star(self, heading, distance=20):
        x = self.units[0].x
        y = self.units[0].y
        units_count = len(self.units)
        iterations = math.ceil(units_count / 8)
        u_idx = 1
        for i in range(0, iterations):
            sx = x - (i+1) * distance
            sy = y - (i+1) * distance
            for j in range(0, 3):
                dx = distance * (i + 1) * j
                for k in range(0, 3):
                    dy = distance * (i + 1) * k
                    if u_idx >= units_count:
                        break
                    u = self.units[u_idx]
                    u.x = sx + dx
                    u.y = sy + dy
                    u.heading = heading

                    if not (j == 1 and k == 1):
                        u_idx += 1

    def formation_rectangle(self, heading, distance=20):
        units_count = len(self.units)
        size = math.ceil(math.sqrt(units_count))
        sx = self.units[0].x
        sy = self.units[0].y
        u_idx = 0
        for i in range(0, size):
            dx = distance * i
            for j in range(0, size):
                dy = distance * j
                if u_idx >= units_count:
                    break
                u = self.units[u_idx]
                u.x = sx - dx
                u.y = sy + dy
                u.heading = heading
                u_idx += 1

    def formation(self, _type=Formation.Line, heading=0):
        form_map = {
            VehicleGroup.Formation.Line: self.formation_line,
            VehicleGroup.Formation.Star: self.formation_star,
            VehicleGroup.Formation.Rectangle: self.formation_rectangle
        }

        form_map[_type](heading)

        return True

    def dict(self):
        d = super(VehicleGroup, self).dict()
        d["modulation"] = self.modulation
        d["communication"] = self.communication
        return d


class FlyingGroup(MovingGroup):
    def __init__(self, _id, name=None, start_time=0):
        super(FlyingGroup, self).__init__(_id, name, start_time)
        self.modulation = 0
        self.communication = True
        self.uncontrolled = False
        self.task = "CAS"

    def add_waypoint(self, x, y, altitude, speed=600, name=String()) -> MovingPoint:
        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = mp.type
        mp.name = name
        mp.x = x
        mp.y = y
        mp.alt = altitude
        mp.speed = speed / 3.6
        mp.ETA_locked = False

        self.add_point(mp)
        return mp

    def add_runway_waypoint(self, airport: Airport, runway_heading: float, distance=6000) -> MovingPoint:
        """
        Adds a waypoint parallel to the given runway heading, for start or approach.
        :param airport: start airport object
        :param runway_heading: degress of the runway
        :param distance: distance of the waypoint from the airport
        :return:
        """

        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = mp.type
        mp.alt_type = "RADIO"
        mp.x, mp.y = mapping.point_from_heading(airport.x, airport.y, runway_heading, distance)
        mp.alt = 300
        mp.speed = 200 / 3.6
        mp.ETA_locked = False

        self.add_point(mp)
        return mp

    def land_at(self, airport: Airport) -> MovingPoint:
        mp = MovingPoint()
        mp.type = "Land"
        mp.action = "Landing"
        mp.x = airport.x
        mp.y = airport.y
        mp.airdrome_id = airport.id
        mp.alt = 0
        mp.speed = 0
        mp.ETA_locked = False

        self.add_point(mp)
        return mp

    def load_task_default_loadout(self, task):
        task_payload = self.units[0].unit_type.loadout(task)
        if task_payload:
            for p in self.units:
                for x in task_payload:
                    p.load_pylon(x)

    def load_pylon(self, weapon, pylon=None):
        for u in self.units:
            u.load_pylon(weapon, pylon)

        return True

    def load_loadout(self, filename):
        for u in self.units:
            u.load_loadout(filename)

        return True

    def dict(self):
        d = super(FlyingGroup, self).dict()
        d["modulation"] = self.modulation
        d["communication"] = self.communication
        d["uncontrolled"] = self.uncontrolled
        return d


class PlaneGroup(FlyingGroup):
    def __init__(self, _id, name=None, start_time=0):
        super(PlaneGroup, self).__init__(_id, name, start_time)


class HelicopterGroup(FlyingGroup):
    def __init__(self, _id, name=None, start_time=0):
        super(HelicopterGroup, self).__init__(_id, name, start_time)


class ShipGroup(MovingGroup):
    def __init__(self, _id, name=None, start_time=0):
        super(ShipGroup, self).__init__(_id, name, start_time)
        self.task = None
        self.frequency = None
        self.spans = None

    def add_waypoint(self, x, y, speed=20) -> MovingPoint:
        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = "Turning Point"
        mp.x = x
        mp.y = y
        mp.speed = speed / 3.6
        mp.ETA_locked = False

        self.add_point(mp)
        return mp

    def dict(self):
        d = super(ShipGroup, self).dict()
        return d


class StaticGroup(Group):
    def __init__(self, _id, name=None):
        super(StaticGroup, self).__init__(_id, name)
        self.dead = False
        self.heading = 0

    def dict(self):
        d = super(StaticGroup, self).dict()
        d["dead"] = self.dead
        d["heading"] = math.radians(self.heading)
        return d
