import copy


class Skill:
    AVERAGE = "Average"
    GOOD = "Good"
    HIGH = "High"
    EXCELLENT = "Excellent"
    RANDOM = "Random"
    PLAYER = "Player"
    CLIENT = "Client"


class Unit:
    def __init__(self, _id, name=None, type=""):
        self.type = type
        self.x = 0
        self.y = 0
        self.heading = 0
        self.id = _id
        self.skill = Skill.AVERAGE
        self.name = name if name else String()

    def set_position(self, pos):
        self.x = pos.x()
        self.y = pos.y()

    def clone(self, _id):
        new = copy.copy(self)
        new.id = _id
        return new

    def dict(self):
        d = {
            "type": self.type,
            "x": self.x,
            "y": self.y,
            "heading": self.heading,
            "skill": self.skill,
            "unitId": self.id,
            "name": self.name.id
        }
        return d