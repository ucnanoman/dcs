from .countries import *
from . import unit
from .mission import Mission
from . import mapping


class VehicleTemplate:
    class Russia:
        @staticmethod
        def sa10_site(mission: Mission, x, y, heading, prefix="", skill=unit.Skill.AVERAGE):
            russia = mission.country("Russia")
            vg = mission.vehicle_group(russia, prefix + "SA10 site", Russia.Vehicle.S_300PS_54K6_cp, x, y, heading)
            u = mission.vehicle("Operator 1", Russia.Vehicle.Paratrooper_AKS_74)
            vx, vy = mapping.point_from_heading(x, y, heading + 180, 10)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 3):  # 3 launchers
                vx, vy = mapping.point_from_heading(x, y, heading + hdg, 50)
                u = mission.vehicle("launcher #" + str(i+1), Russia.Vehicle.S_300PS_5P85C_ln)
                u.x = vx
                u.y = vy
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            vx, vy = mapping.point_from_heading(x, y, heading, 80)
            u = mission.vehicle("radar", Russia.Vehicle.S_300PS_40B6M_tr)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 100)
            u = mission.vehicle("radar", Russia.Vehicle.S_300PS_64H6E_sr)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            for u in vg.units:
                u.skill = skill

            return vg

    class USA:
        @staticmethod
        def patriot_site(mission: Mission, x, y, heading, prefix="", skill=unit.Skill.AVERAGE):
            usa = mission.country("USA")
            vg = mission.vehicle_group(usa, prefix + "Patriot site", USA.Vehicle.Patriot_cp, x, y, heading)
            u = mission.vehicle("Operator 1", USA.Vehicle.Soldier_M4)
            vx, vy = mapping.point_from_heading(x, y, heading + 180, 5)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 2):  # 2 launchers
                vx, vy = mapping.point_from_heading(x, y, heading + hdg, 50)
                u = mission.vehicle("launcher #" + str(i+1), USA.Vehicle.Patriot_ln)
                u.x = vx
                u.y = vy
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 20)
            u = mission.vehicle("Electronic power plant", USA.Vehicle.Patriot_EPP)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading, 80)
            u = mission.vehicle("radar", USA.Vehicle.Patriot_str)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            inf = mission.vehicle("Operator 2", USA.Vehicle.Soldier_M4)
            vx, vy = mapping.point_from_heading(u.x, u.y, heading + 270, 5)
            inf.x = vx
            inf.y = vy
            vg.add_unit(inf)

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 100)
            u = mission.vehicle("Antenna", USA.Vehicle.Patriot_AMG)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading + 120, 80)
            u = mission.vehicle("ECS", USA.Vehicle.Patriot_ECS)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            for u in vg.units:
                u.skill = skill

        @staticmethod
        def hawk_site(mission: Mission, x, y, heading, prefix="", skill=unit.Skill.AVERAGE):
            usa = mission.country("USA")
            vg = mission.vehicle_group(usa, prefix + "Hawk site", USA.Vehicle.Hawk_pcp, x, y, heading)

            u = mission.vehicle("Operator 1", USA.Vehicle.Soldier_M4)
            vx, vy = mapping.point_from_heading(x, y, heading + 180, 5)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 2):  # 2 launchers
                vx, vy = mapping.point_from_heading(x, y, heading + hdg, 50)
                u = mission.vehicle("launcher #" + str(i+1), USA.Vehicle.Hawk_ln)
                u.x = vx
                u.y = vy
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 20)
            u = mission.vehicle("Radar", USA.Vehicle.Hawk_sr)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            inf = mission.vehicle("Operator 2", USA.Vehicle.Soldier_M4)
            vx, vy = mapping.point_from_heading(u.x, u.y, heading + 270, 5)
            inf.x = vx
            inf.y = vy
            vg.add_unit(inf)

            vx, vy = mapping.point_from_heading(x, y, heading, 80)
            u = mission.vehicle("Tower", USA.Vehicle.Hawk_tr)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 100)
            u = mission.vehicle("Wave Radar", USA.Vehicle.Hawk_cwar)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            for u in vg.units:
                u.skill = skill
