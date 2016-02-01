from .unit import Unit


class StaticType:
    AMMUNITION_DEPOT = ".Ammunition depot"


class Static(Unit):
    def __init__(self, id=None, name=None, type=""):
        super(Static, self).__init__(id, name, type)
        self.category = "Warehouses"
        self.can_cargo = False
        self.shape_name = ""

    def dict(self):
        d = super(Static, self).dict()
        d["category"] = self.category
        d["canCargo"] = self.can_cargo
        d["shape_name"] = self.shape_name
        return d