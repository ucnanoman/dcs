class GoalRule:
    def __init__(self, predicate):
        self.coalitionlist = ""
        self.zone = None
        self.group = None
        self.predicate = predicate
        self.unit = None
        self.altitude = None

    def load_from_dict(self, data):
        self.zone = data.get("zone")
        self.group = data.get("group")
        self.predicate = data.get("predicate")
        self.unit = data.get("unit")
        self.coalitionlist = data.get("coalitionlist")
        self.altitude = data.get("altitude")

    def dict(self):
        d = {
            "predicate": self.predicate
        }
        if self.zone:
            d["zone"] = self.zone
        if self.group:
            d["group"] = self.group
        if self.unit:
            d["unit"] = self.unit
        if self.altitude:
            d["altitude"] = self.altitude
        if self.coalitionlist:
            d["coalitionlist"] = self.coalitionlist
        return d


class UnitInZone(GoalRule):
    def __init__(self, unitid, zoneid):
        super(UnitInZone, self).__init__("c_unit_in_zone")
        self.unit = unitid
        self.zone = zoneid


class UnitAltitudeLower(GoalRule):
    def __init__(self, unitid, zoneid):
        super(UnitAltitudeLower, self).__init__("c_unit_altitude_lower")
        self.unit = unitid
        self.zone = zoneid


class Goal:
    def __init__(self, comment="", side="OFFLINE", score=100):
        self.rules = []  # type: list[GoalRule]
        self.side = side
        self.score = score
        self.predicate = "score"
        self.comment = comment

    def load_from_dict(self, data):
        self.side = data["side"]
        self.score = data["score"]
        self.predicate = data["predicate"]
        self.comment = data["comment"]
        self.rules = []
        for x in data["rules"]:
            gr = GoalRule(x["predicate"])
            gr.load_from_dict(x)
            self.rules.append(gr)

    def dict(self):
        return {
            "side": self.side,
            "score": self.score,
            "predicate": self.predicate,
            "comment": self.comment,
            "rules": {i+1: self.rules[i].dict() for i in range(0, len(self.rules))}
        }


class Goals:
    def __init__(self):
        self.goals = []  # type list[Goal]

    def load_from_dict(self, data):
        for x in data:
            g = Goal()
            g.load_from_dict(data)
            self.goals.append(g)

    def dict(self):
        return {i+1: self.goals[i].dict() for i in range(0, len(self.goals))}
