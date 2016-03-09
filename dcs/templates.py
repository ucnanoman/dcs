from .countries import Russia, USA
from . import unit
from .mission import Mission
from . import mapping


class VehicleTemplate:
    class Russia:
        @staticmethod
        def sa10_site(mission: Mission, x, y, heading, prefix="", skill=unit.Skill.AVERAGE):
            russia = mission.country("Russia")
            vg = mission.vehicle_group(russia, prefix + "SA10 site",
                                       Russia.Vehicle.AirDefence.SAM_SA_10_S_300PS_CP_54K6, x, y, heading)
            u = mission.vehicle("Operator 1", Russia.Vehicle.Infantry.Infantry_Soldier_Rus)
            vx, vy = mapping.point_from_heading(x, y, heading + 180, 10)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 3):  # 3 launchers
                vx, vy = mapping.point_from_heading(x, y, heading + hdg, 50)
                u = mission.vehicle("launcher #" + str(i+1), Russia.Vehicle.AirDefence.SAM_SA_10_S_300PS_LN_5P85C)
                u.x = vx
                u.y = vy
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            vx, vy = mapping.point_from_heading(x, y, heading, 80)
            u = mission.vehicle("radar", Russia.Vehicle.AirDefence.SAM_SA_10_S_300PS_TR_30N6)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 100)
            u = mission.vehicle("radar", Russia.Vehicle.AirDefence.SAM_SA_10_S_300PS_SR_64H6E)
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
            vg = mission.vehicle_group(usa, prefix + "Patriot site", USA.Vehicle.AirDefence.SAM_Patriot_ICC, x, y, heading)
            u = mission.vehicle("Operator 1", USA.Vehicle.Infantry.Infantry_M4)
            vx, vy = mapping.point_from_heading(x, y, heading + 180, 5)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 2):  # 2 launchers
                vx, vy = mapping.point_from_heading(x, y, heading + hdg, 50)
                u = mission.vehicle("launcher #" + str(i+1), USA.Vehicle.AirDefence.SAM_Patriot_LN_M901)
                u.x = vx
                u.y = vy
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 20)
            u = mission.vehicle("Electronic power plant", USA.Vehicle.AirDefence.SAM_Patriot_EPP_III)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading, 80)
            u = mission.vehicle("radar", USA.Vehicle.AirDefence.SAM_Patriot_STR_AN_MPQ_53)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            inf = mission.vehicle("Operator 2", USA.Vehicle.Infantry.Infantry_M4)
            vx, vy = mapping.point_from_heading(u.x, u.y, heading + 270, 5)
            inf.x = vx
            inf.y = vy
            vg.add_unit(inf)

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 100)
            u = mission.vehicle("Antenna", USA.Vehicle.AirDefence.SAM_Patriot_AMG_AN_MRC_137)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading + 120, 80)
            u = mission.vehicle("ECS", USA.Vehicle.AirDefence.SAM_Patriot_ECS_AN_MSQ_104)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            for u in vg.units:
                u.skill = skill

        @staticmethod
        def hawk_site(mission: Mission, x, y, heading, prefix="", skill=unit.Skill.AVERAGE):
            usa = mission.country("USA")
            vg = mission.vehicle_group(usa, prefix + "Hawk site", USA.Vehicle.AirDefence.SAM_Hawk_PCP, x, y, heading)

            u = mission.vehicle("Operator 1", USA.Vehicle.Infantry.Infantry_M4)
            vx, vy = mapping.point_from_heading(x, y, heading + 180, 5)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 2):  # 2 launchers
                vx, vy = mapping.point_from_heading(x, y, heading + hdg, 50)
                u = mission.vehicle("launcher #" + str(i+1), USA.Vehicle.AirDefence.SAM_Hawk_LN_M192)
                u.x = vx
                u.y = vy
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 20)
            u = mission.vehicle("Radar", USA.Vehicle.AirDefence.SAM_Hawk_SR_AN_MPQ_50)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            inf = mission.vehicle("Operator 2", USA.Vehicle.Infantry.Infantry_M4)
            vx, vy = mapping.point_from_heading(u.x, u.y, heading + 270, 5)
            inf.x = vx
            inf.y = vy
            vg.add_unit(inf)

            vx, vy = mapping.point_from_heading(x, y, heading, 80)
            u = mission.vehicle("Tower", USA.Vehicle.AirDefence.SAM_Hawk_TR_AN_MPQ_46)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            vx, vy = mapping.point_from_heading(x, y, heading + 180, 100)
            u = mission.vehicle("Wave Radar", USA.Vehicle.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55)
            u.x = vx
            u.y = vy
            u.heading = heading
            vg.add_unit(u)

            for u in vg.units:
                u.skill = skill
