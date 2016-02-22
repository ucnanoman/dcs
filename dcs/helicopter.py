from .unit import FlyingUnit
from .helicopters import HelicopterType, Ka_50


class Helicopter(FlyingUnit):
    def __init__(self, _id=None, name=None, _type: HelicopterType=Ka_50):
        super(Helicopter, self).__init__(_id, name, _type)
