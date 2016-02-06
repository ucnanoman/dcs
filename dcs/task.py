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


class CAS(Task):
    def __init__(self):
        super(CAS, self).__init__("EngageTargets")
        self.params = {
            "targetTypes": {1: "Helicopters", 2: "Ground Units", 3: "Light armed ships"},
            "priority": 0
        }
        self.key = "CAS"

    def main_task_name(self):
        return self.key

    def dict(self):
        d = super(CAS, self).dict()
        d["key"] = self.key
        return d


class AWACS(Task):
    def __init__(self):
        super(AWACS, self).__init__("AWACS")


class EPLRS(Task):
    def __init__(self, group_id):
        super(EPLRS, self).__init__("WrappedAction")
        self.params = {
            "action": {"id": "EPLRS", "params": {"value": True, "groupId": group_id}}
        }
