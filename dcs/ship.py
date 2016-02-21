from .unit import Unit


class Ship(Unit):
    def __init__(self, id=None, name=None, _type="speedboat"):
        super(Ship, self).__init__(id, name, _type)
        self.transportable = {"randomTransportable": False}

    def dict(self):
        d = super(Ship, self).dict()
        d["transportable"] = self.transportable
        return d
