import sys
import dcs
import dcs.mission
import dcs.task
import dcs.mapping
from dcs.mapping import Point, Polygon
import dcs.terrain
import dcs.unittype
import dcs.vehicles
from dcs.countries import USA, Russia
import random
import argparse
import os
import datetime
from typing import List, Dict, Tuple


class USPlatoon:
    units = [
        dcs.countries.USA.Vehicle.Armor.APC_M1043_HMMWV_Armament,
        dcs.countries.USA.Vehicle.Armor.APC_M1043_HMMWV_Armament,
        dcs.countries.USA.Vehicle.Armor.APC_M1126_Stryker_ICV,
        dcs.countries.USA.Vehicle.AirDefence.AAA_Vulcan_M163
    ]
    maybe = [
        dcs.countries.USA.Vehicle.AirDefence.SAM_Avenger_M1097
    ]


class BasicScenario:
    battle_zones = [
        Polygon([Point(-270285.71428571, 609257.14285714), Point(-264342.85714286, 614142.85714286),
                 Point(-257428.57142857, 619485.71428571), Point(-250857.14285714, 625171.42857143),
                 Point(-248342.85714286, 627457.14285714), Point(-244600, 628800),
                 Point(-238685.71428571, 635371.42857143), Point(-235257.14285714, 639942.85714285),
                 Point(-238685.71428571, 640771.42857143), Point(-239342.85714286, 642714.28571428),
                 Point(-235971.42857143, 644742.85714285), Point(-236600, 646142.85714285),
                 Point(-234085.71428571, 650142.85714285), Point(-239200, 656428.57142857),
                 Point(-249828.57142857, 653000), Point(-264400, 650000), Point(-264828.57142857, 644171.42857142),
                 Point(-269885.71428571, 634542.85714285), Point(-273600, 635428.57142857),
                 Point(-273657.14285714, 642571.42857142), Point(-285771.42857143, 640828.57142857),
                 Point(-285800, 625514.28571428), Point(-279771.42857143, 625285.71428571),
                 Point(-273942.85714286, 629371.42857142), Point(-272428.57142857, 624828.57142857),
                 Point(-273342.85714286, 612285.71428571)])
    ]

    red_force = {
        "Armor": {
            "Tank Platoon": (Russia.name, [
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90
            ]),
            "Tank Platoon 2": (Russia.name, [
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90
            ])
        },
        "LightArmor": {
            "Light Armor 01": (Russia.name, [
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3
            ]),
            "Light Armor 02": (Russia.name, [
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3
            ]),
            "Light Armor 03": (Russia.name, [
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3
            ])
        },
        "Artillery": {
            "Artillery": (Russia.name, [
                Russia.Vehicle.Artillery.SPH_2S1_Gvozdika,
                Russia.Vehicle.Artillery.SPH_2S1_Gvozdika,
                Russia.Vehicle.Artillery.SPH_2S1_Gvozdika,
                Russia.Vehicle.Artillery.SPH_2S1_Gvozdika,
                Russia.Vehicle.Unarmed.Transport_Ural_4320T,
                Russia.Vehicle.AirDefence.SAM_SA_19_Tunguska_2S6
            ])
        },
        "AirDefence": {
            "Air Defense": (Russia.name, [
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_LN_2P25,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_STR_9S91,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_LN_2P25,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_STR_9S91,
                Russia.Vehicle.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            ])
        },
        "Supply": {
            "Russia Supply": (Russia.name, [
                Russia.Vehicle.Unarmed.Transport_GAZ_66,
                Russia.Vehicle.Unarmed.Fuel_Truck_ATZ_10,
                Russia.Vehicle.Unarmed.Transport_ZIU_9,
                Russia.Vehicle.Unarmed.Transport_ZIU_9,
                Russia.Vehicle.Unarmed.Transport_ZIU_9
            ])
        }
    }


    blue_force = {
        "Armor": {
            "1st Tank Platoon 01": (USA.name, [
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams
            ]),
            "1st Tank Platoon 02": (USA.name, [
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams
            ])
        },
        "LightArmor": {
            "1st Light Armor Brigade 01": (USA.name, [
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
            ]),
            "1st Light Armor Brigade 02": (USA.name, [
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
            ])
        },
        "Artillery": {
            "1st Artillery Corps 01": (USA.name, [
                USA.Vehicle.Artillery.SPH_M109_Paladin,
                USA.Vehicle.Artillery.SPH_M109_Paladin,
                USA.Vehicle.Artillery.SPH_M109_Paladin,
                USA.Vehicle.Artillery.SPH_M109_Paladin,
                USA.Vehicle.Unarmed.HEMTT_TFFT,
                USA.Vehicle.AirDefence.SAM_Stinger_comm,
                USA.Vehicle.AirDefence.SAM_Stinger_MANPADS
            ])
        },
        "AirDefence": {
            "Air Defense Battery 01": (USA.name, [
                USA.Vehicle.Unarmed.APC_M1025_HMMWV,
                USA.Vehicle.Unarmed.APC_M1025_HMMWV,
                USA.Vehicle.AirDefence.SAM_Avenger_M1097,
                USA.Vehicle.AirDefence.SAM_Avenger_M1097,
                USA.Vehicle.AirDefence.SAM_Avenger_M1097,
                USA.Vehicle.AirDefence.SAM_Avenger_M1097
            ])
        },
        "Supply": {
            "US Supply": (USA.name, [
                USA.Vehicle.Unarmed.Transport_M818,
                USA.Vehicle.Unarmed.Transport_M818,
                USA.Vehicle.Unarmed.Tanker_M978_HEMTT,
                USA.Vehicle.Unarmed.HEMTT_TFFT
            ])
        }
    }

    def __init__(self):
        self.m = dcs.mission.Mission()

        self.m.coalition["red"].swap_country(self.m.coalition["blue"], dcs.countries.Ukraine.name)

        self.red_airports = []  # type: List[dcs.terrain.Airport]
        self.blue_airports = []  # type: List[dcs.terrain.Airport]
        self.setup_airports()

    def dynamic_weather(self):
        self.m.weather.dynamic_weather(random.randrange(1, 2))

    def daytime(self, period):
        self.m.start_time -= datetime.timedelta(hours=-12)
        self.m.start_time += datetime.timedelta(days=random.randrange(0, 365))
        map = {
            "day": datetime.timedelta(minutes=random.randrange(480, 960)),
            "night": datetime.timedelta(minutes=random.randrange(-120, 240)),
            "dusk": datetime.timedelta(minutes=random.randrange(960, 1100)),
            "dawn": datetime.timedelta(minutes=random.randrange(240, 480))
        }
        if period == "random":
            k = list(map.keys())
            period = k[random.randrange(0, len(k))]
        self.m.start_time += map[period]

    def setup_airports(self):
        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus
        self.red_airports = caucasus.default_red_airports()
        for a in self.red_airports:
            self.setup_airport(a, "red", [dcs.vehicles.AirDefence.SAM_SA_19_Tunguska_2S6,
                                          dcs.vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka])

        self.blue_airports = caucasus.default_blue_airports()
        for a in self.blue_airports:
            self.setup_airport(a, "blue", [dcs.vehicles.AirDefence.SAM_Avenger_M1097,
                                                dcs.vehicles.AirDefence.AAA_Vulcan_M163])

    def setup_airport(self, airport: dcs.terrain.Airport, side: str, air_def_units: List[dcs.unittype.VehicleType]):
        airport.set_coalition(side)

        if not airport.civilian:
            if airport.is_red():
                dcs.templates.VehicleTemplate.Russia.sa10_site(self.m, airport.random_unit_zone().center(), 180)
            elif airport.is_blue():
                dcs.templates.VehicleTemplate.USA.patriot_site(self.m, airport.random_unit_zone().center(), 330)
        else:
            slots = len(airport.parking_slots)
            airdef = int(round(random.random() + slots/20, 0))
            if airdef:
                vg = self.m.vehicle_group(
                    self.m.country("Russia") if airport.is_red() else self.m.country("USA"),
                    airport.name + " Air Defense",
                    air_def_units[random.randrange(0, len(air_def_units))],
                    airport.random_unit_zone().random_point(), 180)

                for i in range(1, airdef):
                    _type = air_def_units[random.randrange(0, len(air_def_units))]
                    u = self.m.vehicle(airport.name + " Air Defense #" + str(i), _type)
                    vg.add_unit(u)
                vg.formation_scattered(random.randrange(0, 359))

        return airport

    def add_civil_airtraffic(self, planes=(10, 20), helicopters=(0, 10), hidden=True):
        p_count = random.randrange(planes[0], planes[1])
        h_count = random.randrange(helicopters[0], helicopters[1])

        c_count = 1

        def civil_flight(countries, airports):
            country_str = countries[random.randrange(0, len(countries))]
            country = self.m.country(country_str)

            airport = airports[random.randrange(0, len(airports))]

            transports = [x for x in country.planes if dcs.planes.plane_map[x].task_default == dcs.task.Transport]
            ptype = dcs.planes.plane_map[transports[random.randrange(0, len(transports))]]

            slots = airport.free_parking_slot(ptype.large_parking_slot, False)

            x = random.randrange(dcs.terrain.Caucasus.bounds.bottom+100*1000, dcs.terrain.Caucasus.bounds.top-100*1000)
            y = random.randrange(dcs.terrain.Caucasus.bounds.left+600*1000, dcs.terrain.Caucasus.bounds.right-130*1000)

            pos = dcs.mapping.Point(x, y)
            name = "Civil " + str(c_count)
            rand = random.random()
            if 0.3 < rand < 0.5 and slots:
                pg = self.m.plane_group_from_parking(country, name, ptype, airport, coldstart=random.getrandbits(1))
                pg.add_runway_waypoint(airport, distance=random.randrange(6000, 8000, 100))
                pg.add_waypoint(pos, random.randrange(5000, 8000, 100), 400)
            elif 0.5 < rand and slots:
                pg = self.m.plane_group_from_parking(country, name, ptype, airport)
                pg.uncontrolled = True
            else:
                bound = dcs.mapping.Rectangle(dcs.terrain.Caucasus.bounds.top-100*1000,
                                              dcs.terrain.Caucasus.bounds.left+200*1000,
                                              dcs.terrain.Caucasus.bounds.bottom+100*1000,
                                              dcs.terrain.Caucasus.bounds.right-130*1000)
                point = bound.random_point()

                pg = self.m.plane_group_inflight(
                    country, name, ptype, point, random.randrange(5000, 8000, 100), 400)
                tmp = pg.add_waypoint(dcs.mapping.Point(0, 0), pg.points[0].alt)
                wp = pg.add_runway_waypoint(airport, distance=random.randrange(6000, 8000, 100))
                heading = wp.position.heading_between_point(point)
                tmp.position = wp.position.point_from_heading(heading, 30*1000)
                pg.land_at(airport)
            pg.set_frequency(240)
            return pg

        def heli_transport_flight(countries, airports: List[dcs.terrain.Airport]):
            country_str = countries[random.randrange(0, len(countries))]
            country = self.m.country(country_str)

            transports = [x for x in country.helicopters
                          if dcs.helicopters.helicopter_map[x].task_default == dcs.task.Transport]
            htype = dcs.helicopters.helicopter_map[transports[random.randrange(0, len(transports))]]

            start_airport = airports[random.randrange(0, len(airports))]
            rand = random.random()
            name = "Helicopter Transport " + str(c_count)
            if 0.7 < rand:
                bound = dcs.mapping.Rectangle.from_point(start_airport.position, 100*1000)
                pos = bound.random_point()
                hg = self.m.helicopter_group_inflight(
                    country, name, htype, pos, random.randrange(800, 1500, 100), 200)
                hg.add_runway_waypoint(start_airport)
                hg.land_at(start_airport)
            elif 0.4 < rand < 0.7:
                hg = self.m.helicopter_group_from_parking(country, name, htype, start_airport)
                hg.uncontrolled = True
            else:
                dest_airport = None
                while True:
                    dest_airport = airports[random.randrange(0, len(airports))]
                    if dest_airport != start_airport:
                        break

                hg = self.m.helicopter_group_from_parking(
                    country, name, htype, start_airport, coldstart=random.getrandbits(1))
                hg.add_runway_waypoint(start_airport)
                hg.add_runway_waypoint(dest_airport)
                hg.land_at(dest_airport)
            return hg

        # red
        red_countries = [dcs.countries.Russia.name]
        for i in range(0, int(p_count / 2)):
            cf = civil_flight(red_countries, self.red_airports)
            cf.hidden = hidden
            cf.points[0].tasks.append(dcs.task.SetInvisibleCommand())
            c_count += 1

        for i in range(0, int(h_count / 2)):
            hf = heli_transport_flight(red_countries, self.red_airports)
            hf.hidden = hidden
            hf.points[0].tasks.append(dcs.task.SetInvisibleCommand())
            c_count += 1

        # blue
        blue_countries = [dcs.countries.USA.name, dcs.countries.Ukraine.name, dcs.countries.Georgia.name]
        for i in range(0, int(p_count / 2)):
            cf = civil_flight(blue_countries, self.blue_airports)
            cf.hidden = hidden
            cf.points[0].tasks.append(dcs.task.SetInvisibleCommand())
            c_count += 1

        for i in range(0, int(h_count / 2)):
            hf = heli_transport_flight(blue_countries, self.blue_airports)
            hf.hidden = hidden
            hf.points[0].tasks.append(dcs.task.SetInvisibleCommand())
            c_count += 1

    def add_uncontrolled_military_planes(self, airports: List[dcs.terrain.Airport],
                                         planes: List[Tuple[str, str, int]], hidden=True):

        g_idx = 1
        while planes:
            country, strtype, group_size = planes.pop()

            while True:
                airport = airports[random.randrange(0, len(airports))]

                ptype = dcs.planes.plane_map[strtype]
                slots = airport.free_parking_slots(ptype.large_parking_slot, False)
                if len(slots) >= group_size:
                    break

            c = self.m.country(country)
            pg = self.m.plane_group_from_parking(c, strtype + " Flight #" + str(g_idx),
                                                 ptype, airport, parking_slots=slots, group_size=group_size)
            pg.uncontrolled = True
            pg.hidden = hidden
            g_idx += 1

    def place_players(self, start, aircraft_types: List[Tuple[str, str]],
                      airports: List[dcs.terrain.Airport],
                      group_size,
                      maintask,
                      placement_rect=None) -> List[dcs.unitgroup.FlyingGroup]:

        aircraft_groups = []  # type: List[dcs.unitgroup.FlyingGroup]
        name = "Airmaster "
        c = 1
        for _type in aircraft_types:
            country = self.m.country(_type[0])
            aircraft_type = _type[1]
            plane_type = dcs.planes.plane_map.get(aircraft_type, None)
            if plane_type:
                airport = airports[random.randrange(0, len(airports))]

                if start == "inflight":
                    rp = placement_rect.random_point if placement_rect else dcs.mapping.Rectangle.from_point(
                        airport.position, 20*1000).from_point()
                    pg = self.m.plane_group_inflight(
                        country, name + str(c), plane_type, rp, random.randrange(2000, 5000, 100), maintask=maintask, group_size=group_size)
                elif start == "runway":
                    pg = self.m.plane_group_from_runway(country, name + str(c), plane_type, airport, maintask=maintask, group_size=group_size)
                else:
                    pg = self.m.plane_group_from_parking(
                        country, name + str(c), plane_type, airport, coldstart=start == "cold", maintask=maintask, group_size=group_size)
                aircraft_groups.append(pg)
            else:
                heli_type = dcs.helicopters.helicopter_map[aircraft_type]
                airport = airports[random.randrange(0, len(airports))]

                if start == "inflight":
                    rp = placement_rect.random_point if placement_rect else dcs.mapping.Rectangle.from_point(
                        airport.position, 20*1000).from_point()
                    pg = self.m.helicopter_group_inflight(
                        country, name + str(c), heli_type, rp, random.randrange(300, 1000, 100), maintask=maintask, group_size=group_size)
                elif start == "runway":
                    pg = self.m.helicopter_group_from_runway(country, name + str(c), heli_type, airport, maintask=maintask, group_size=group_size)
                else:
                    pg = self.m.helicopter_group_from_parking(
                        country, name + str(c), heli_type, airport, coldstart=start == "cold", maintask=maintask, group_size=group_size)
                aircraft_groups.append(pg)

            for u in pg.units:
                u.set_client()
            c += 1

        if group_size == 1:
            aircraft_groups[0].units[0].set_player()

        return aircraft_groups

    def save(self, filename, stats):
        self.m.save(filename, show_stats=stats)


class Refueling(BasicScenario):
    def __init__(self, aircraft_types: List[Tuple[str,str]], playercount: int, start: str):
        super(Refueling, self).__init__()

        self.add_civil_airtraffic(hidden=False)

        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus

        usa = self.m.country(dcs.countries.USA.name)
        ukraine = self.m.country(dcs.countries.Ukraine.name)

        batumi = caucasus.batumi()
        vaziani = caucasus.vaziani()

        kutaisi = caucasus.kutaisi()
        kobuleti = caucasus.kobuleti()
        blue_military = [kutaisi, kobuleti]

        planes = [
            (dcs.countries.USA.name, dcs.countries.USA.Plane.F_16C_bl_52d, 4),
            (dcs.countries.USA.name, dcs.countries.USA.Plane.F_15E, 2),
            (dcs.countries.USA.name, dcs.countries.USA.Plane.F_A_18C, 4),
            (dcs.countries.Georgia.name, dcs.countries.Georgia.Plane.Su_25T, 4)
        ]

        self.add_uncontrolled_military_planes(blue_military, planes, False)

        frequency = 140
        orbit_rect = dcs.mapping.Rectangle(
            int(batumi.position.x + 120*1000), int(batumi.position.y - 100 * 1000), int(batumi.position.x), int(vaziani.position.y))

        pos, heading, race_dist = Refueling.random_orbit(orbit_rect)
        awacs = self.m.awacs_flight(
            usa,
            "AWACS",
            plane_type=dcs.planes.E_3A,
            airport=None,
            position=pos,
            race_distance=race_dist, heading=heading,
            altitude=random.randrange(4000, 5500, 100), frequency=frequency)

        self.m.escort_flight(usa, "AWACS Escort", dcs.planes.plane_map[dcs.countries.USA.Plane.F_15E], None, awacs, 2)

        pos, heading, race_dist = Refueling.random_orbit(orbit_rect)
        refuel_net = self.m.refuel_flight(
            ukraine,
            "Tanker IL",
            dcs.planes.IL_78M,
            airport=None,
            position=pos,
            race_distance=race_dist, heading=heading,
            altitude=random.randrange(4000, 5500, 100), frequency=frequency)

        pos, heading, race_dist = Refueling.random_orbit(orbit_rect)
        refuel_rod = self.m.refuel_flight(
            usa,
            "Tanker KC",
            dcs.planes.KC_135,
            airport=None,
            position=pos,
            race_distance=race_dist, heading=heading,
            altitude=random.randrange(4000, 5500, 100), frequency=frequency)

        player_groups = self.place_players(start, aircraft_types, blue_military, orbit_rect, playercount, None)

        if start == "inflight":
            fuel_percent = 0.2
        else:
            fuel_percent = 0.3

        for pg in player_groups:
            airport = caucasus.airport_by_id(pg.points[0].airdrome_id)
            airport = airport if airport else blue_military[random.randrange(0, len(blue_military))]
            if start != "inflight":
                pg.add_runway_waypoint(airport)

            for u in pg.units:
                u.fuel *= fuel_percent

            if pg.units[0].unit_type in [dcs.planes.A_10C]:
                pg.add_waypoint(refuel_rod.points[1].position, 4000)
            else:
                pg.add_waypoint(refuel_net.points[1].position, 4000)

            pg.add_runway_waypoint(airport)
            pg.land_at(airport)
            pg.load_loadout("Combat Air Patrol")

        goal = dcs.goals.Goal("home and alive")
        goal.rules.append(dcs.goals.UnitAlive(pg.units[0].id))
        tz = self.m.triggers.add_triggerzone(pg.units[0].position, 30, name="home")
        goal.rules.append((dcs.goals.UnitInZone(pg.units[0].id, tz.id)))
        self.m.goals.add_offline(goal)

        self.m.set_description_text("""Random generated refueling test mission.
{count} {type} are/is prepared for a refueling training mission.""".format(
            count=playercount, type=", ".join(aircraft_types)))
        self.m.set_description_bluetask_text("""Find your tanker and do a full refuel.
Afterwards land at your designated homebase.

AWACS and Tankers are reachable on {freq} Mhz VHF-AM.""".format(freq=frequency))

    @staticmethod
    def random_orbit(rect: dcs.mapping.Rectangle):
        x1 = random.randrange(rect.bottom, rect.top)
        sy = rect.left
        y1 = random.randrange(sy, rect.right)
        heading = 90 if y1 < (sy + (rect.right - sy) / 2) else 270
        heading = random.randrange(heading - 20, heading + 20)
        race_dist = random.randrange(80*1000, 120*1000)
        return dcs.mapping.Point(x1, y1), heading, race_dist


class CAS(BasicScenario):
    blue_plane_force = {
        "SEAD": {
            "SEAD 01": (USA.name, 2, dcs.planes.F_16C_bl_52d)
        },
        "CAP": {
            "Air Patrol": (USA.name, 2, dcs.planes.F_15C)
        }
    }

    def __init__(self, aircraft_types: List[Tuple[str,str]], playercount: int, start: str):
        super(CAS, self).__init__()

        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus

        usa = self.m.country(dcs.countries.USA.name)
        kutaisi = caucasus.kutaisi()
        kobuleti = caucasus.kobuleti()
        blue_military_airport = [kutaisi, kobuleti]

        battle_point = BasicScenario.battle_zones[0].random_point()

        front_hdg = 30
        i = 0
        for force in [self.blue_force, self.red_force]:
            attack_hdg = (300 + (180 if i > 0 else 0)) % 360
            defense_hdg = (attack_hdg + 180) % 360
            rp = battle_point.point_from_heading(defense_hdg, 3*1000)
            for force_type in force:
                for conf in force[force_type]:
                    dist_hdg = front_hdg if random.getrandbits(1) else front_hdg + 180
                    rp = rp.point_from_heading(dist_hdg, random.randrange(100, 1000))
                    if force_type in ["Artillery", "Supply"]:
                        rp = rp.point_from_heading(random.randrange(defense_hdg-30, defense_hdg+30), random.randrange(500, 3000))
                    else:
                        rp = rp.point_from_heading(random.randrange(attack_hdg-30, attack_hdg+30), random.randrange(0, 500))

                    plat = force[force_type][conf]
                    c = self.m.country(plat[0])
                    g = self.m.vehicle_group_platoon(c, conf, plat[1], rp)
                    g.formation_scattered(attack_hdg)

                    if force_type not in ["Artillery", "Supply", "AirDefence"]:
                        wp = g.add_waypoint(g.position.point_from_heading(attack_hdg, 3000))
                        wp.action = "Vee"
                        g.add_waypoint(wp.position.point_from_heading(random.randrange(attack_hdg-30, attack_hdg+30), 3000))
            i += 1

        for plane_force in [self.blue_plane_force]:
            for force_type in plane_force:
                for conf in plane_force[force_type]:
                    conf_data = plane_force[force_type][conf]
                    airport = blue_military_airport[random.randrange(0, len(blue_military_airport))]
                    country = self.m.country(conf_data[0])
                    if force_type == "CAP":
                        self.m.patrol_flight(country, conf, conf_data[2], airport,
                                             caucasus.batumi().position, caucasus.lochini().position,
                                             group_size=conf_data[1])
                    else:
                        pg = self.m.plane_group_from_runway(country, conf, conf_data[2], airport,
                                                        dcs.task.MainTask.map[force_type], group_size=conf_data[1])
                        pg.add_runway_waypoint(airport)

                        if force_type in ["SEAD"]:
                            pg.add_waypoint(battle_point, 1000)


        player_groups = self.place_players(start, aircraft_types, blue_military_airport, playercount, dcs.task.CAS)
        for pg in player_groups:
            pg.add_runway_waypoint(caucasus.airport_by_id(pg.points[0].airdrome_id))
            pg.add_waypoint(battle_point, 0)


class Scenario(BasicScenario):

    def __init__(self):
        super(Scenario, self).__init__()

        self.red_airforce = {
            dcs.planes.MiG_29A.id: 1,
            dcs.planes.Su_24M.id: 1,
            dcs.planes.Su_25T.id: 1,
            dcs.planes.A_50.id: 1}

        self.red_airforce_escort = [
            dcs.planes.MiG_29S
        ]

        self.red_helicopter = [
            dcs.helicopters.Mi_24V.id
        ]

        self.red_ground = {
            dcs.countries.Russia.Vehicle.Armor.MBT_T_80U: 8,
            dcs.countries.Russia.Vehicle.Armor.IFV_BMP_3: 10,
            dcs.countries.Russia.Vehicle.AirDefence.SAM_SA_9_Strela_1_9P31: 6
        }

        self.blue_ground = [
            USPlatoon,
            USPlatoon,
            USPlatoon,
            USPlatoon,
            USPlatoon,
            USPlatoon
        ]

        self.blue_targets = []  # list[dcs.group.VehicleGroup]

        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus
        ukraine = self.m.country(dcs.countries.Ukraine.name)

        nalchik = self.m.terrain.nalchik()
        beslan = self.m.terrain.beslan()
        mozdok = caucasus.mozdok()
        sochi = caucasus.sochi()

        senaki = self.m.terrain.senaki()
        batumi = self.m.terrain.batumi()
        soganlug = self.m.terrain.soganlug()
        vaziani = caucasus.vaziani()

        usa = self.m.country("USA")
        self.distribute_ground(usa, senaki.x, senaki.y, senaki.x + 20*1000, senaki.y - 30*1000, self.blue_ground)

        awacs = self.m.awacs_flight(usa, "AWACS", dcs.planes.E_3A, vaziani, vaziani.x - 5000, vaziani.y - 70000, race_distance=120 * 1000, heading=270)
        self.m.escort_flight(usa, str(awacs.name) + " escort us", dcs.planes.F_16C_bl_52d, vaziani, awacs)
        refuel = self.m.refuel_flight(ukraine, "Tanker", dcs.planes.IL_78M, batumi, batumi.x + 40000, batumi.y + 30000, race_distance=80*1000, heading=90)

        patrol = self.m.patrol_flight(usa, "patrolium", dcs.planes.F_15C, soganlug,
                                      soganlug.x, soganlug.y - 20*1000, soganlug.x + 20*1000, soganlug.y - 200*1000)

        pg = self.m.plane_group_from_parking(usa, "Airgroup", dcs.planes.M_2000C, batumi)
        pg.units[0].set_player()
        pg.load_loadout("air2air")

        russia = self.m.country("Russia")
        self.distribute_air(russia, [sochi, mozdok, nalchik, caucasus.mineralnye()], self.red_airforce, self.red_airforce_escort)

    def distribute_ground(self, _country, x1, y1, x2, y2, groundforce):
        xmin = int(min(x1, x2))
        xmax = int(max(x1, x2))
        ymin = int(min(y1, y2))
        ymax = int(max(y1, y2))
        i = 0
        isblue = self.m.is_blue(_country)
        side = "Blue" if isblue else "Red"
        for uname in groundforce:
            x = random.randrange(xmin, xmax, 10)
            y = random.randrange(ymin, ymax, 10)
            units = list(uname.units)
            if random.randrange(0, 100) > 80:
                units += uname.maybe
            vg = self.m.vehicle_group_platoon(_country, side + " " + str(uname.__name__) + " " + str(i), units, x, y, random.randrange(0, 359))
            vg.formation_scattered()
            if isblue:
                self.blue_targets.append(vg)
            i += 1

    def distribute_air(self, _country, airports, airforce, escort):
        air_distr = dict(airforce)
        escort_distr = list(escort)

        isblue = self.m.is_blue(_country)
        if isblue:
            ground_targets = self.red_targets
        else:
            ground_targets = self.blue_targets
        i = 100
        while sum([air_distr[x] for x in air_distr]) > 0:
            port = random.randrange(len(airports))

            types = [x for x in airforce if air_distr[x] > 0]

            print(types)
            _type_id = types[random.randrange(len(types))]

            _type = dcs.planes.plane_map[_type_id]
            if not airports[port].free_parking_slot(_type.large_parking_slot, False):
                continue

            airport = airports[port]
            if airport.name == "Nalchik":
                airports.pop(port)

            if _type.task_default == dcs.task.AWACS:
                if self.m.is_red(_country):
                    sochi = self.m.terrain.sochi()
                    x = random.randrange(int(sochi.x + 20*1000), -10000)
                    y = sochi.y + random.randrange(20000, 50000)

                awacs = self.m.awacs_flight(_country, "AWACS", _type, airport, x, y, random.randrange(30*1000, 120*1000), random.randrange(60, 110), random.randrange(3800, 5000))

                if escort_distr:
                    escort_type = escort_distr.pop()
                    self.m.escort_flight(_country, str(awacs.name) + " escort", escort_type, airport, awacs, group_size=2)
            elif _type.task_default in [dcs.task.CAS, dcs.task.GroundAttack]:
                target = ground_targets[random.randrange(0, len(ground_targets))]

                if True:
                    if airport.runway_free:
                        pg = self.m.plane_group_from_runway(_country, "Airgroup " + str(i), _type, airport, maintask=dcs.task.CAS, group_size=2)
                    else:
                        pg = self.m.plane_group_from_parking(_country, "Airgroup " + str(i), _type, airport, maintask=dcs.task.CAS, group_size=2)
                    last_wp = pg.add_runway_waypoint(airport)
                else:
                    heading = int(dcs.mapping.heading_between_points(target.x(), target.y(), airport.x, airport.y) + 360)
                    heading = random.randrange(heading - 20, heading + 20) - 360
                    x, y = dcs.mapping.point_from_heading(target.x(), target.y(), heading, random.randrange(50, 80)*1000)
                    pg = self.m.plane_group_inflight(_country, "Airgroup " + str(i), _type, x, y, 1000, maintask=dcs.task.CAS, group_size=2)
                    last_wp = pg.points[0]
                pg.points[0].tasks.clear()
                pg.points[0].tasks.append(dcs.task.EngageTargets(20*1000, [dcs.task.Targets.All.GroundUnits.GroundVehicles]))

                if _type == dcs.planes.Su_25T:
                    pg.load_loadout("APU-8 Vikhr-M*2,S-25L*2,R-73*2,SPPU-22*2,Mercury LLTV Pod,MPS-410")

                heading = dcs.mapping.heading_between_points(last_wp.x, last_wp.y, target.x(), target.y())
                distance = dcs.mapping.distance(last_wp.x, last_wp.y, target.x(), target.y())
                x, y = dcs.mapping.point_from_heading(last_wp.x, last_wp.y, heading, distance - 5000)
                last_wp = pg.add_waypoint(x, y, 4000)
                last_wp.tasks.append(dcs.task.CAS.EnrouteTasks.EngageGroup(target.id))
                pg.add_waypoint(last_wp.x + 1000 * 10, last_wp.y, 4000)
                pg.add_runway_waypoint(airport)
                pg.land_at(airport)
            else:
                pg = self.m.plane_group_from_parking(_country, "Airgroup " + str(i), _type, airport, group_size=2)
                if pg.task == dcs.task.CAP.name:
                    pg.points[0].tasks.clear()
                    pg.points[0].tasks.append(dcs.task.CAP.EnrouteTasks.EngageTargets(50*1000, [dcs.task.Targets.All.Air.Planes]))

                last_wp = pg.add_runway_waypoint(airport)

                hdg = 230
                waypoints = 5
                for i in range(0, waypoints):
                    if i > waypoints - 3:
                        hdg = (hdg + 180) % 360
                    hdg = random.randrange(hdg - 70, hdg + 70)
                    x, y = dcs.mapping.point_from_heading(last_wp.x, last_wp.y, hdg, random.randrange(10*1000, 60*1000, 1000))
                    last_wp = pg.add_waypoint(x, y, 4000)

                pg.add_runway_waypoint(airport)
                pg.land_at(airport)

            air_distr[_type_id] -= 1
            i += 1


def main():

    types = [
        (dcs.countries.USA.name, dcs.planes.A_10C.id),
        (dcs.countries.Georgia.name, dcs.planes.Su_25T.id),
        (dcs.countries.USA.name, dcs.planes.M_2000C.id),
        (dcs.countries.USA.name, dcs.helicopters.Ka_50.id)
    ]
    aircraft_types = [x[1] for x in types]
    parser = argparse.ArgumentParser(description="Random DCS mission generator")

    parser.add_argument("-a", "--aircrafttype", default=dcs.planes.Su_25T.id,
                        choices=aircraft_types,
                        help="Player aircraft type")
    parser.add_argument("-p", "--playercount", default=1, type=int)
    parser.add_argument("-s", "--start", default="inflight", choices=["inflight", "runway", "warm", "cold"])
    parser.add_argument("-t", "--missiontype", default="main", choices=["main", "CAS", "CAP", "refuel"])
    parser.add_argument("-d", "--daytime", choices=["random", "day", "night", "dusk", "dawn"], default="random")
    parser.add_argument("-w", "--weather", choices=["dynamic", "clear"], default="dynamic")
    parser.add_argument("--show-stats", action="store_true", default=False, help="Show generated missions stats")
    parser.add_argument("-o", "--output", default=os.path.join(os.path.expanduser("~"), "Saved Games\\DCS\\Missions\\random.miz"))

    args = parser.parse_args()
    missiontype = args.missiontype
    if args.aircrafttype in [
        dcs.planes.Su_25T.id,
        dcs.helicopters.Ka_50.id,
        dcs.planes.A_10C.id] and args.missiontype == "main":
        missiontype = "CAS"
    if args.aircrafttype == dcs.planes.A_10C.id:
        if args.missiontype not in ["CAS", "refuel"]:
            missiontype = "CAS"

    if missiontype == "refuel":
        supported = [dcs.planes.A_10C.id, dcs.planes.M_2000C.id]
        types = [x for x in types if x[1] in supported] if args.playercount > 1 else [x for x in types if x[1] == args.aircrafttype]
        s = Refueling(types, args.playercount, args.start)
    elif missiontype == "CAS":
        types = types if args.playercount > 1 else [x for x in types if x[1] == args.aircrafttype]
        s = CAS(types, args.playercount, args.start)
    else:
        s = Scenario()

    s.daytime(args.daytime)
    if args.weather == "dynamic":
        s.dynamic_weather()
    s.save(args.output, args.show_stats)


if __name__ == '__main__':
    sys.exit(main())
