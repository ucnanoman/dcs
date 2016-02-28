from .countries import *
from .group import VehicleGroup
from .vehicle import Vehicle
from .mission import Mission
from . import mapping


class VehicleTemplate:
    class Russia:
        @staticmethod
        def sa10_site(mission: Mission, x, y, heading, prefix=""):
            russia = mission.country("Russia")
            vg = mission.vehicle_group(russia, prefix + "SA10 site", Russia.Vehicle.S_300PS_54K6_cp, x, y, heading)

            hdg = 90
            for i in range(0, 3):  # 3 launchers
                vx, vy = mapping.point_from_heading(x, y, heading + hdg, 50)
                u = mission.vehicle("launcher #" + str(i), Russia.Vehicle.S_300PS_5P85C_ln)
                u.x = vx
                u.y = vy
                vg.add_unit(u)
                hdg += 90

            vx, vy = mapping.point_from_heading(x, y, heading, 80)
            u = mission.vehicle("radar", Russia.Vehicle.S_300PS_40B6M_tr)
            u.x = vx
            u.y = vy
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 100)
            u = mission.vehicle("radar", Russia.Vehicle.S_300PS_64H6E_sr)
            u.x = vx
            u.y = vy
            vg.add_unit(u)

            return vg
