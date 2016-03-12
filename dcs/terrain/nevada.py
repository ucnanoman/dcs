from .terrain import Terrain, Airport, Runway, ParkingSlot
from .. import mapping


class Nevada(Terrain):
    bounds = mapping.Rectangle(-497177.656250, -329334.875000, -166934.953125, 209836.890625)
    map_view_default = {
        "center": mapping.Point(-340928.57142857, -55928.571428568),
        "zoom": 1000000
    }

    def __init__(self):
        super(Nevada, self).__init__("Nevada")
        # nttr center MGRS
        # 11SPE9400410022
        self.center = {"lat": 39.81806, "long": -114.73333}
        self.bullseye_blue = {"x": -409931.344, "y": -14024.097}
        self.bullseye_red = {"x": -288293.969, "y": -88022.641}