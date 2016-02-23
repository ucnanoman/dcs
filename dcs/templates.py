from .countries import *
from .group import VehicleGroup
from .vehicle import Vehicle
from .mission import Mission


class VehicleTemplate:
    class Russia:
        @staticmethod
        def sa10_site(mission: Mission, x, y, heading, prefix=""):
            russia = mission.country("Russia")
            vg = mission.vehicle_group(russia, prefix + "SA10 site", Russia.Vehicle.S_300PS_5P85C_ln, x, y, heading)

            vg.units[0].name = mission.string("launcher")
            vg.add_unit(mission.vehicle("radar", Russia.Vehicle.S_300PS_40B6M_tr))
            vg.add_unit(mission.vehicle("Command post", Russia.Vehicle.S_300PS_54K6_cp))
            vg.add_unit(mission.vehicle("radar", Russia.Vehicle.S_300PS_64H6E_sr))

            vg.formation(vg.Formation.Star)

            return vg
