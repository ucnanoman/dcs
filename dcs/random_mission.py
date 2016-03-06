import sys
import dcs
import dcs.mission
import dcs.task
import random
import argparse
import os


class USPlatoon:
    units = [
        dcs.countries.USA.Vehicle.M1043_HMMWV_Armament,
        dcs.countries.USA.Vehicle.M1043_HMMWV_Armament,
        dcs.countries.USA.Vehicle.M1126_Stryker_ICV,
        dcs.countries.USA.Vehicle.Vulcan
    ]
    maybe = [
        dcs.countries.USA.Vehicle.M1097_Avenger
    ]


class BasicScenario:
    def __init__(self):
        self.m = dcs.mission.Mission()

        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus

        self.m.coalition["red"].swap_country(self.m.coalition["blue"], "Ukraine")

        self.red_airports = caucasus.default_red_airports()
        for a in self.red_airports:
            self.setup_airport_red(a)

    def setup_airport_red(self, airport: dcs.terrain.Airport):
        airport.set_red()
        if not airport.civilian:
            dcs.templates.VehicleTemplate.Russia.sa10_site(self.m, airport.x + 500, airport.y, 180)
        else:
            slots = len(airport.parking_slots)
            airdef = int(round(random.random() + slots/20, 0))
            if airdef:
                vg = self.m.vehicle_group(
                    self.m.country("Russia"),
                    airport.name + " Air Defense",
                    dcs.countries.Russia.Vehicle._2S6_Tunguska,
                    airport.x + 500, airport.y + 100, 180)

                for i in range(1, airdef):
                    _type = dcs.countries.Russia.Vehicle._2S6_Tunguska if random.random() > 0.5 else dcs.countries.Russia.Vehicle.ZSU_23_4_Shilka
                    u = self.m.vehicle(airport.name + " Air Defense #" + str(i), _type)
                    vg.add_unit(u)
                vg.formation_scattered(180)

        return airport

    def save(self, filename):
        self.m.save(filename)


class Refueling(BasicScenario):
    def __init__(self, aircraft_type:str, playercount: int, start:str):
        super(Refueling, self).__init__()

        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus

        usa = self.m.country("USA")
        ukraine = self.m.country("Ukraine")

        batumi = caucasus.airport_batumi()
        vaziani = caucasus.airport_vaziani()

        x1 = random.randrange(int(batumi.x), int(batumi.x) + 120 * 1000)
        sy = int(batumi.y) - 100 * 1000
        y1 = random.randrange(sy, int(vaziani.y))
        heading = 90 if y1 < (sy + (vaziani.y - sy) / 2) else 270
        heading = random.randrange(heading - 20, heading + 20)
        race_dist = random.randrange(80*1000, 120*1000)
        #awacs = self.m.awacs_flight(usa, "AWACS", dcs.planes.E_3A, soganlug, soganlug.x - 5000, soganlug.y - 70000, race_distance=120 * 1000, heading=270)
        refuel = self.m.refuel_flight(ukraine, "Tanker", dcs.planes.IL_78M, None, x1, y1, race_distance=race_dist, heading=heading)


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
            dcs.countries.Russia.Vehicle.T_80UD: 8,
            dcs.countries.Russia.Vehicle.BMP_3: 10,
            dcs.countries.Russia.Vehicle.Strela_1_9P31: 6
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
        ukraine = self.m.coalition["red"].swap_country(self.m.coalition["blue"], "Ukraine")

        nalchik = self.m.terrain.airport_nalchik()
        beslan = self.m.terrain.airport_beslan()
        mozdok = caucasus.airport_mozdok()
        sochi = caucasus.airport_sochi()
        self.setup_airport_red(beslan)
        self.setup_airport_red(nalchik)
        self.setup_airport_red(mozdok)

        senaki = self.m.terrain.airport_senaki()
        batumi = self.m.terrain.airport_batumi()
        soganlug = self.m.terrain.airport_soganlug()
        #self.setup_airport_blue(senaki)
        self.setup_airport_blue(batumi)
        self.setup_airport_blue(soganlug)
        usa = self.m.country("USA")
        self.distribute_ground(usa, senaki.x, senaki.y, senaki.x + 20*1000, senaki.y - 30*1000, self.blue_ground)

        awacs = self.m.awacs_flight(usa, "AWACS", dcs.planes.E_3A, soganlug, soganlug.x - 5000, soganlug.y - 70000, race_distance=120 * 1000, heading=270)
        refuel = self.m.refuel_flight(ukraine, "Tanker", dcs.planes.IL_78M, batumi, batumi.x + 40000, batumi.y + 30000, race_distance=80*1000, heading=90)

        pg = self.m.plane_group_from_parking(usa, "Airgroup", dcs.planes.M_2000C, batumi)
        pg.units[0].set_player()
        pg.load_loadout("air2air")

        russia = self.m.country("Russia")
        self.distribute_air(russia, [sochi, mozdok, nalchik], self.red_airforce, self.red_airforce_escort)

    def setup_sochi(self):
        sochi = self.m.terrain.airports["Sochi"]
        sochi.set_red()
        sa10 = dcs.templates.VehicleTemplate.Russia.sa10_site(self.m, sochi.x - 500, sochi.y, 180)

        return sochi

    def setup_airport_blue(self, airport: dcs.terrain.Airport):
        airport.set_blue()
        posx = airport.x - 1100
        posy = airport.y
        bullsheading = dcs.mapping.heading_between_points(posx, posy, self.m.terrain.bullseye_blue["x"], self.m.terrain.bullseye_blue["y"])
        airdef = dcs.templates.VehicleTemplate.USA.hawk_site(self.m, posx, posy, bullsheading)
        return airport

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
                    sochi = self.m.terrain.airport_sochi()
                    x = random.randrange(int(sochi.x + 20*1000), -10000)
                    y = sochi.y + random.randrange(20000, 50000)

                awacs = self.m.awacs_flight(_country, "AWACS", _type, airport, x, y, random.randrange(30*1000, 120*1000), random.randrange(60, 110), random.randrange(3800, 5000))

                if escort_distr:
                    escort_type = escort_distr.pop()
                    eg = self.m.plane_group_from_parking(_country, "AWACS escort", escort_type, airport, dcs.task.Escort, group_size=2)
                    eg.add_runway_waypoint(airport)
                    wp = eg.add_waypoint(awacs.points[2].x, awacs.points[2].y, awacs.points[2].alt)
                    wp.tasks.append(dcs.task.EscortTaskAction(awacs.id, lastwpt=len(eg.points)+1))
            elif _type.task_default in [dcs.task.CAS, dcs.task.GroundAttack]:
                target = ground_targets[random.randrange(0, len(ground_targets))]

                if True:
                    if airport.runway_free:
                        pg = self.m.plane_group_from_runway(_country, "Airgroup " + str(i), _type, airport, task=dcs.task.CAS, group_size=2)
                    else:
                        pg = self.m.plane_group_from_parking(_country, "Airgroup " + str(i), _type, airport, task=dcs.task.CAS, group_size=2)
                    last_wp = pg.add_runway_waypoint(airport)
                else:
                    heading = int(dcs.mapping.heading_between_points(target.x(), target.y(), airport.x, airport.y) + 360)
                    heading = random.randrange(heading - 20, heading + 20) - 360
                    x, y = dcs.mapping.point_from_heading(target.x(), target.y(), heading, random.randrange(50, 80)*1000)
                    pg = self.m.plane_group_inflight(_country, "Airgroup " + str(i), _type, x, y, 1000, task=dcs.task.CAS, group_size=2)
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
                    pg.points[0].tasks.append(dcs.task.CAP.EnrouteTasks.EngageTargets(50*1000))

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

    parser = argparse.ArgumentParser(description="Random DCS mission generator")

    parser.add_argument("-a", "--aircrafttype", default=dcs.planes.Su_25T.id,
                        choices=[
                            dcs.planes.A_10C.id,
                            dcs.planes.Su_25T.id,
                            dcs.planes.M_2000C.id,
                            dcs.helicopters.Ka_50.id],
                        help="Player aircraft type")
    parser.add_argument("-p", "--playercount", default=1, type=int)
    parser.add_argument("-s", "--start", default="inflight", choices=["inflight", "runway", "warm", "cold"])
    parser.add_argument("-t", "--missiontype", default="main", choices=["main", "CAS", "CAP", "refuel"])
    parser.add_argument("-o", "--output", default=os.path.join(os.path.expanduser("~"), "Saved Games\\DCS\\Missions\\random.miz"))

    args = parser.parse_args()
    missiontype = args.missiontype
    if args.aircrafttype in [dcs.planes.Su_25T.id, dcs.helicopters.Ka_50.id]:
        missiontype = "CAS"
    if args.aircrafttype == dcs.planes.A_10C.id:
        if args.missiontype not in ["CAS", "refuel"]:
            missiontype = "CAS"

    if missiontype == "refuel":
        s = Refueling(args.aircrafttype, args.playercount, args.start)
    else:
        s = Scenario()

    s.save(args.output)


if __name__ == '__main__':
    sys.exit(main())