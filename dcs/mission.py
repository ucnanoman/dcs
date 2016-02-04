import zipfile
import lua
from .weather import *
from .group import *
from .country import Country
from . import country
from .point import Point, MovingPoint
from .vehicle import Vehicle
from .plane import Plane, PlaneType
from .static import Static
from .translation import Translation, String
from .terrain import Terrain, Caucasus, Nevada, ParkingSlot


class Options:
    def __init__(self, opts={}):
        self.options = opts

    def __str__(self):
        return lua.dumps(self.options, "options", 1)

    def __repr__(self):
        return repr(self.options)


class Warehouses:
    def __init__(self, terrain: Terrain):
        self.terrain = terrain
        self.warehouses = {}

    def load_dict(self, data):
        for x in data.get("airports", {}):
            self.terrain.airport_by_id(x).load_from_dict(data["airports"][x])

    def __str__(self):
        airports = self.terrain.airports
        d = {
            "warehouses": self.warehouses,
            "airports": {airports[x].id: airports[x].dict() for x in airports}
        }
        return lua.dumps(d, "warehouses", 1)


class MapPosition:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y


class Coalition:
    def __init__(self, name, bullseye=None):
        self.name = name
        self.countries = {}  # type: dict[str, Country]
        self.bullseye = bullseye
        self.nav_points = []  # TODO

    def set_bullseye(self, bulls):
        self.bullseye = bulls

    def add_country(self, country):
        self.countries[country.name] = country

    def remove_country(self, name):
        return self.countries.pop(name)

    def country(self, country_name: str):
        return self.countries[country_name]

    def dict(self):
        d = {}
        d["name"] = self.name
        if self.bullseye:
            d["bullseye"] = self.bullseye
        d["country"] = {}
        i = 1
        for country in self.countries.keys():
            d["country"][i] = self.country(country).dict()
            i += 1
        d["nav_points"] = {}
        return d


class Mission:
    COUNTRY_IDS = {x for x in range(0, 13)} | {x for x in range(15, 47)}

    def __init__(self, terrain: Terrain = Caucasus()):
        self.current_unit_id = 0
        self.current_group_id = 0

        self.translation = Translation()

        self.description_text = self.string("dcs mission")
        self.description_bluetask = self.string("blue task")
        self.description_redtask = self.string("red task")
        self.sortie = self.string("sortie text")
        self.pictureFileNameR = ""
        self.pictureFileNameB = ""
        self.version = 9
        self.currentKey = 0
        self.start_time = 43200
        self.terrain = terrain
        self.trigrules = {}
        self.triggers = {}
        self.options = Options()
        self.warehouses = Warehouses(self.terrain)
        self.mapresource = {}
        self.goals = {}
        blue = Coalition("blue")
        blue.add_country(country.Australia())
        blue.add_country(country.Belgium())
        blue.add_country(country.Canada())
        blue.add_country(country.Croatia())
        blue.add_country(country.CzechRepublic())
        blue.add_country(country.Denmark())
        blue.add_country(country.France())
        blue.add_country(country.Georgia())
        blue.add_country(country.Germany())
        blue.add_country(country.Israel())
        blue.add_country(country.Italy())
        blue.add_country(country.Norway())
        blue.add_country(country.Poland())
        blue.add_country(country.SouthKorea())
        blue.add_country(country.Spain())
        blue.add_country(country.Netherlands())
        blue.add_country(country.UK())
        blue.add_country(country.USA())
        blue.add_country(country.Turkey())

        red = Coalition("red")
        red.add_country(country.Abkhazia())
        red.add_country(country.Belarus())
        red.add_country(country.China())
        red.add_country(country.Iran())
        red.add_country(country.Kazakhstan())
        red.add_country(country.NorthKorea())
        red.add_country(country.Russia())
        red.add_country(country.Serbia())
        red.add_country(country.SouthOssetia())
        red.add_country(country.Syria())
        red.add_country(country.Ukraine())

        blue.bullseye = terrain.bullseye_blue
        red.bullseye = terrain.bullseye_red

        self.coalition = {"blue": blue, "red": red}  # type: dict[str, Coalition]

        self.map = {
            "zoom": 1000000,
            "centerY": 680000,
            "centerX": -250000
        }

        self.groundControl = {}
        self.failures = {}
        self.trig = {}
        self.result = {}
        self.groundControl = {}
        self.forcedOptions = {}
        self.resourceCounter = {}
        self.needModules = {}
        self.weather = Weather()
        self.usedModules = {
            'Su-25A by Eagle Dynamics': True,
            'MiG-21Bis AI by Leatherneck Simulations': True,
            'UH-1H Huey by Belsimtek': True,
            'Su-25T by Eagle Dynamics': True,
            'F-86F Sabre by Belsimtek': True,
            'Su-27 Flanker by Eagle Dynamics': True,
            'Hawk T.1A AI by VEAO Simulations': True,
            'MiG-15bis AI by Eagle Dynamics': True,
            'Ka-50 Black Shark by Eagle Dynamics': True,
            'Combined Arms by Eagle Dynamics': True,
            'L-39C/ZA by Eagle Dynamics': True,
            'A-10C Warthog by Eagle Dynamics': True,
            'F-5E/E-3 by Belsimtek': True,
            'C-101 Aviojet': True,
            'TF-51D Mustang by Eagle Dynamics': True,
            './CoreMods/aircraft/MQ-9 Reaper': True,
            'C-101 Aviojet by AvioDev': True,
            'P-51D Mustang by Eagle Dynamics': True,
            'A-10A by Eagle Dynamics': True,
            'World War II AI Units by Eagle Dynamics': True,
            'MiG-15bis by Belsimtek': True,
            'F-15C': True,
            'Flaming Cliffs by Eagle Dynamics': True,
            'Bf 109 K-4 by Eagle Dynamics': True,
            'Mi-8MTV2 Hip by Belsimtek': True,
            'MiG-21Bis by Leatherneck Simulations': True,
            'M-2000C by RAZBAM Sims': True,
            'FW-190D9 Dora by Eagle Dynamics': True,
            'Caucasus': True,
            'Hawk T.1A by VEAO Simulations': True,
            'F-86F Sabre AI by Eagle Dynamics': True
        }

    def _import_moving_point(self, group: Group, imp_group) -> Group:
        for imp_point_idx in imp_group["route"]["points"]:
            imp_point = imp_group["route"]["points"][imp_point_idx]
            point = MovingPoint()
            point.alt = imp_point["alt"]
            point.alt_type = imp_point.get("alt_type", None)
            point.type = imp_point["type"]
            point.x = imp_point["x"]
            point.y = imp_point["y"]
            point.action = imp_point["action"]
            point.ETA_locked = imp_point["ETA_locked"]
            point.ETA = imp_point["ETA"]
            point.formation_template = imp_point["formation_template"]
            point.speed_locked = imp_point["speed_locked"]
            point.speed = imp_point["speed"]
            point.name = self.translation.get_string(imp_point["name"])
            point.task = imp_point["task"]
            point.airdrome_id = imp_point.get("airdromeId", None)
            point.properties = imp_point.get("properties", None)
            group.add_point(point)
        return group

    def _import_static_point(self, group: Group, imp_group) -> Group:
        for imp_point_idx in imp_group["route"]["points"]:
            imp_point = imp_group["route"]["points"][imp_point_idx]
            point = Point()
            point.alt = imp_point["alt"]
            point.type = imp_point["type"]
            point.x = imp_point["x"]
            point.y = imp_point["y"]
            point.action = imp_point["action"]
            point.formation_template = imp_point["formation_template"]
            point.speed = imp_point["speed"]
            point.name = self.translation.get_string(imp_point["name"])
            group.add_point(point)
        return group

    def _imp_coalition(self, coalition, key):
        if key not in coalition:
            return None
        imp_col = coalition[key]
        col = Coalition(key, imp_col["bullseye"])
        for country_idx in imp_col["country"]:
            imp_country = imp_col["country"][country_idx]
            _country = country.get_by_id(imp_country["id"])

            if "vehicle" in imp_country:
                for vgroup_idx in imp_country["vehicle"]["group"]:
                    vgroup = imp_country["vehicle"]["group"][vgroup_idx]
                    vg = VehicleGroup(vgroup["groupId"], self.translation.get_string(vgroup["name"]), vgroup["start_time"])
                    vg.task = vgroup["task"]
                    self.current_group_id = max(self.current_group_id, vg.id)

                    self._import_moving_point(vg, vgroup)

                    # units
                    for imp_unit_idx in vgroup["units"]:
                        imp_unit = vgroup["units"][imp_unit_idx]
                        unit = Vehicle(id=imp_unit["unitId"], name=self.translation.get_string(imp_unit["name"]))
                        unit.set_position(MapPosition(imp_unit["x"], imp_unit["y"]))
                        unit.heading = imp_unit["heading"]
                        unit.type = imp_unit["type"]
                        unit.skill = imp_unit["skill"]
                        unit.x = imp_unit["x"]
                        unit.y = imp_unit["y"]
                        unit.player_can_drive = imp_unit["playerCanDrive"]
                        unit.transportable = imp_unit["transportable"]

                        self.current_unit_id = max(self.current_unit_id, unit.id)
                        vg.add_unit(unit)
                    _country.add_vehicle_group(vg)

            if "plane" in imp_country:
                for pgroup_idx in imp_country["plane"]["group"]:
                    pgroup = imp_country["plane"]["group"][pgroup_idx]
                    plane_group = PlaneGroup(pgroup["groupId"], self.translation.get_string(pgroup["name"]), pgroup["start_time"])
                    plane_group.task = pgroup["task"]
                    plane_group.frequency = pgroup["frequency"]
                    plane_group.modulation = pgroup["modulation"]
                    plane_group.communication = pgroup["communication"]
                    plane_group.uncontrolled = pgroup["uncontrolled"]
                    self.current_group_id = max(self.current_group_id, plane_group.id)

                    self._import_moving_point(plane_group, pgroup)

                    # units
                    for imp_unit_idx in pgroup["units"]:
                        imp_unit = pgroup["units"][imp_unit_idx]
                        plane = Plane(_id=imp_unit["unitId"], name=self.translation.get_string(imp_unit["name"]))
                        plane.set_position(MapPosition(imp_unit["x"], imp_unit["y"]))
                        plane.heading = imp_unit["heading"]
                        plane.type = imp_unit["type"]
                        plane.skill = imp_unit["skill"]
                        plane.livery_id = imp_unit.get("livery_id")
                        plane.x = imp_unit["x"]
                        plane.y = imp_unit["y"]
                        plane.alt_type = imp_unit["alt_type"]
                        plane.alt = imp_unit["alt"]
                        plane.psi = imp_unit["psi"]
                        plane.speed = imp_unit["speed"]
                        plane.fuel = imp_unit["payload"]["fuel"]
                        plane.gun = imp_unit["payload"]["gun"]
                        plane.flare = imp_unit["payload"]["flare"]
                        plane.chaff = imp_unit["payload"]["chaff"]
                        plane.ammo_type = imp_unit["payload"].get("ammo_type")
                        plane.pylons = imp_unit["payload"]["pylons"]
                        plane.callsign_name = imp_unit["callsign"]["name"]
                        plane.parking = imp_unit.get("parking", None)
                        plane.speed = imp_unit["speed"]
                        plane.callsign = [imp_unit["callsign"][1], imp_unit["callsign"][2], imp_unit["callsign"][3]]

                        self.current_unit_id = max(self.current_unit_id, plane.id)
                        plane_group.add_unit(plane)
                    _country.add_plane_group(plane_group)

            if "static" in imp_country:
                for sgroup_idx in imp_country["static"]["group"]:
                    sgroup = imp_country["static"]["group"][sgroup_idx]
                    static_group = StaticGroup(sgroup["groupId"], self.translation.get_string(sgroup["name"]))
                    static_group.heading = sgroup["heading"]
                    static_group.hidden = sgroup["hidden"]
                    static_group.dead = sgroup["dead"]
                    self.current_group_id = max(self.current_group_id, static_group.id)

                    self._import_static_point(static_group, sgroup)

                    # units
                    for imp_unit_idx in sgroup["units"]:
                        imp_unit = sgroup["units"][imp_unit_idx]
                        static = Static(id=imp_unit["unitId"], name=self.translation.get_string(imp_unit["name"]), type=imp_unit["type"])
                        static.can_cargo = imp_unit["canCargo"]
                        static.heading = imp_unit["heading"]
                        static.x = imp_unit["x"]
                        static.y = imp_unit["y"]
                        static.category = imp_unit["category"]
                        static.shape_name = imp_unit["shape_name"]

                        self.current_unit_id = max(self.current_unit_id, static.id)
                        static_group.add_unit(static)
                    _country.add_static_group(static_group)
            col.add_country(_country)
        return col

    def load_file(self, filename):
        mission_dict = {}
        options_dict = {}
        warehouse_dict = {}
        dictionary_dict = {}

        def loaddict(fname, miz):
            with miz.open(fname) as mfile:
                data = mfile.read()
                data = data.decode()
                return lua.loads(data)

        with zipfile.ZipFile(filename, 'r') as miz:
            mission_dict = loaddict('mission', miz)
            options_dict = loaddict('options', miz)
            warehouse_dict = loaddict('warehouses', miz)
            dictionary_dict = loaddict('l10n/DEFAULT/dictionary', miz)

        imp_mission = mission_dict["mission"]

        # import translations
        self.translation = Translation()
        translation_dict = dictionary_dict["dictionary"]
        for sid in translation_dict:
            self.translation.set_string(sid, translation_dict[sid], 'DEFAULT')

        self.translation.max_dict_id = imp_mission["maxDictId"]

        # print(self.translation)

        # setup terrain
        if imp_mission["theatre"] == 'Caucasus':
            self.terrain = Caucasus()
        elif imp_mission["theatre"] == 'Nevada':
            self.terrain = Nevada()
        else:
            raise RuntimeError("Unknown theatre: '{theatre}'".format(theatre=imp_mission["theatre"]))

        # import options
        self.options = Options(options_dict["options"])

        # import warehouses
        self.warehouses = Warehouses(self.terrain)
        self.warehouses.load_dict(warehouse_dict["warehouses"])

        # import base values
        self.description_text = self.translation.get_string(imp_mission["descriptionText"])
        self.description_bluetask = self.translation.get_string(imp_mission["descriptionBlueTask"])
        self.description_redtask = self.translation.get_string(imp_mission["descriptionRedTask"])
        self.sortie = self.translation.get_string(imp_mission["sortie"])
        self.pictureFileNameR = imp_mission["pictureFileNameR"]
        self.pictureFileNameB = imp_mission["pictureFileNameB"]
        self.version = imp_mission["version"]
        self.currentKey = imp_mission["currentKey"]
        self.start_time = imp_mission["start_time"]
        self.usedModules = imp_mission["usedModules"]

        # groundControl
        self.groundControl = imp_mission["groundControl"]  # TODO

        # result
        self.result = imp_mission["result"]  # TODO

        # goals
        self.goals = imp_mission["goals"]  # TODO

        # trig
        self.trig = imp_mission["trig"]  # TODO

        # triggers
        self.triggers = imp_mission["triggers"]  # TODO

        # trigrules
        self.trigrules = imp_mission["trigrules"]  # TODO

        # failures
        self.failures = imp_mission["failures"]  # TODO

        # forced options
        self.forcedOptions = imp_mission["forcedOptions"]  # TODO

        # map
        self.map = imp_mission["map"]

        # weather
        imp_weather = imp_mission["weather"]
        self.weather = Weather()
        self.weather.atmosphere_type = imp_weather["atmosphere_type"]
        wind = imp_weather.get("wind", {})
        wind_at_ground = wind.get("atGround", {})
        wind_at_2000 = wind.get("at2000", {})
        wind_at_8000 = wind.get("at8000", {})
        self.weather.wind_at_ground = Wind(wind_at_ground.get("dir", 0), wind_at_ground.get("speed", 0))
        self.weather.wind_at_2000 = Wind(wind_at_2000.get("dir", 0), wind_at_2000.get("speed", 0))
        self.weather.wind_at_8000 = Wind(wind_at_8000.get("dir", 0), wind_at_8000.get("speed", 0))
        self.weather.enable_fog = imp_weather["enable_fog"]
        turbulence = imp_weather.get("turbulence", {})
        self.weather.turbulence_at_ground = turbulence.get("atGround", 0)
        self.weather.turbulence_at_2000 = turbulence.get("at2000", 0)
        self.weather.turbulence_at_8000 = turbulence.get("at8000", 0)
        season = imp_weather.get("season", {})
        self.weather.season_temperature = season.get("temperature", 20)
        self.weather.season_iseason = season.get("iseason", 1)
        self.weather.type_weather = imp_weather.get("type_weather", 0)
        self.weather.qnh = imp_weather.get("qnh", 760)
        cyclones = imp_weather.get("cyclones", {})
        for x in cyclones:
            c = Cyclone()
            c.centerX = cyclones[x].get("centerX", 0)
            c.centerZ = cyclones[x].get("centerZ", 0)
            c.ellipticity = cyclones[x].get("ellipticity", 0)
            c.pressure_excess = cyclones[x].get("pressure_excess", 0)
            c.pressure_spread = cyclones[x].get("pressure_spread", 0)
            c.rotation = cyclones[x].get("rotation", 0)
            self.weather.cyclones.append(c)
        self.weather.name = imp_weather.get("name", "Summer, clean sky")
        fog = imp_weather.get("fog", {})
        self.weather.fog_thickness = fog.get("thickness", 0)
        self.weather.fog_visibility = fog.get("visibility", 25)
        self.weather.fog_density = fog.get("density", 7)
        visibility = imp_weather.get("visiblity", {})
        self.weather.visibility_distance = visibility.get("distance", 80000)
        clouds = imp_weather.get("clouds", {})
        self.weather.clouds_thickness = clouds.get("thickness", 200)
        self.weather.clouds_density = clouds.get("density", 0)
        self.weather.clouds_base = clouds.get("base", 300)
        self.weather.clouds_iprecptns = clouds.get("iprecptns", 0)

        # import coalition with countries and units
        self.coalition["blue"] = self._imp_coalition(imp_mission["coalition"], "blue")
        self.coalition["red"] = self._imp_coalition(imp_mission["coalition"], "red")
        neutral_col = self._imp_coalition(imp_mission["coalition"], "neutral")
        if neutral_col:
            self.coalition["neutral"] = neutral_col

        return True

    def description_text(self):
        return str(self.description_text)

    def set_description_text(self, text):
        self.description_text.set(text)

    def description_bluetask_text(self):
        return str(self.description_bluetask)

    def set_description_bluetask_text(self, text):
        self.description_bluetask.set(text)

    def description_redtask_text(self):
        return str(self.description_redtask)

    def set_description_redtask_text(self, text):
        self.description_redtask.set(text)

    def next_group_id(self):
        self.current_group_id += 1
        return self.current_group_id

    def next_unit_id(self):
        self.current_unit_id += 1
        return self.current_unit_id

    def string(self, s, lang='DEFAULT'):
        """Create a new String() object for translation"""
        return self.translation.create_string(s, lang)

    def vehicle_group(self, name) -> VehicleGroup:
        return VehicleGroup(self.next_group_id(), self.string(name))

    def vehicle(self, name, _type):
        return Vehicle(self.next_unit_id(), self.string(name), _type)

    def vehicle_group(self, _country, name, _type: str, x, y, heading=0, group_size=1, formation=None) -> VehicleGroup:
        vg = VehicleGroup(self.next_group_id(), self.string(name))

        for i in range(1, group_size + 1):
            v = self.vehicle(name + " Unit #{nr}".format(nr=i), _type)
            v.x = x
            v.y = y + (i-1) * 20
            v.heading = heading
            vg.add_unit(v)

        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = "On Road"
        mp.x = vg.units[0].x
        mp.y = vg.units[0].y

        vg.add_point(mp)

        _country.add_vehicle_group(vg)
        return vg

    def plane_group(self, name):
        return PlaneGroup(self.next_group_id(), self.string(name))

    def plane_group_inflight(self, _country, name, task, x, y, altitude, plane_type, group_size=1):
        pg = self.plane_group(name)
        pg.task = task
        for i in range(1, group_size + 1):
            p = self.plane(name + " Pilot #{nr}".format(nr=i), plane_type)
            p.x = x
            p.y = y
            p.alt = altitude
            callsign = _country.callsign.get(plane_type.role)[0]
            if callsign:
                p.callsign_name = callsign
            pg.add_unit(p)

        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = mp.type
        mp.x = pg.units[0].x
        mp.y = pg.units[0].y
        mp.alt = p.alt

        pg.add_point(mp)

        _country.add_plane_group(pg)
        return pg

    def plane_group_from_runway(self, _country, name, task, plane_type: PlaneType, airport: Airport, group_size=1):
        pg = self.plane_group(name)
        pg.task = task

        for i in range(1, group_size + 1):
            p = self.plane(name + " Pilot #{nr}".format(nr=i), plane_type)
            p.x = airport.x
            p.y = airport.y
            callsign = _country.callsign.get(plane_type.role)[0]
            if callsign:
                p.callsign_name = callsign
            pg.add_unit(p)

        mp = MovingPoint()
        mp.type = "TakeOff"
        mp.action = "From Runway"
        mp.x = pg.units[0].x
        mp.y = pg.units[0].y
        mp.airdrome_id = airport.id
        mp.alt = p.alt

        pg.add_point(mp)

        _country.add_plane_group(pg)
        return pg

    def plane_group_from_parking(self,
                                 _country: Country,
                                 name,
                                 task,
                                 plane_type: PlaneType,
                                 airport: Airport,
                                 coldstart=True,
                                 parking_slots: ParkingSlot=None,
                                 group_size=1) -> PlaneGroup:
        """
        Add a new PlaneGroup at parking position on the given airport.
        :param _country: Country object the plane group belongs to
        :param name: Name of the plane group
        :param task: Task of the plane group
        :param plane_type: PlaneType object representing the plane
        :param airport: Airport object on which to spawn the plane
        :param coldstart: Coldstart yes or no
        :param parking_slots: List of parking slots to use for planes
        :param group_size: Group size 1-4
        :return: the new PlaneGroup
        """
        pg = self.plane_group(name)
        pg.task = task

        callsign = _country.callsign.get(plane_type.role)[0]

        for i in range(1, group_size + 1):
            p = self.plane(name + " Pilot #{nr}".format(nr=i), plane_type)
            parking_slot = parking_slots.pop(i) if parking_slots else airport.free_parking_slot(plane_type.large_parking_slot)
            p.x = parking_slot.x
            p.y = parking_slot.y
            p.set_parking(parking_slot)
            if callsign:
                p.callsign_name = callsign
            pg.add_unit(p)

        mp = MovingPoint()
        mp.type = "TakeOffParking" if coldstart else "TakeOffParkingHot"
        mp.action = "From Parking Area" if coldstart else "From Parking Area Hot"
        mp.x = pg.units[0].x
        mp.y = pg.units[0].y
        mp.airdrome_id = airport.id
        mp.alt = p.alt

        pg.add_point(mp)

        _country.add_plane_group(pg)
        return pg

    def plane(self, name, _type: PlaneType):
        return Plane(self.next_unit_id(), self.string(name), _type)

    def save(self, filename):
        with zipfile.ZipFile(filename, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            # options
            zipf.writestr('options', str(self.options))

            # warehouses
            zipf.writestr('warehouses', str(self.warehouses))

            # translation files
            dicttext = lua.dumps(self.translation.dict('DEFAULT'), "dictionary", 1)
            zipf.writestr('l10n/DEFAULT/dictionary', dicttext)

            zipf.writestr('l10n/DEFAULT/mapResource', lua.dumps(self.mapresource, "mapResource", 1))

            zipf.writestr('mission', str(self))
        return True

    def __str__(self):
        m = {}
        m["trig"] = self.trig
        m["result"] = self.result
        m["groundControl"] = self.groundControl
        m["usedModules"] = self.usedModules
        m["resourceCounter"] = self.resourceCounter
        m["triggers"] = self.triggers
        m["weather"] = self.weather.dict()
        m["theatre"] = self.terrain.name
        m["needModules"] = self.needModules
        m["map"] = self.map
        m["descriptionText"] = self.description_text.id
        m["pictureFileNameR"] = self.pictureFileNameR
        m["pictureFileNameB"] = self.pictureFileNameB
        m["descriptionBlueTask"] = self.description_bluetask.id
        m["descriptionRedTask"] = self.description_redtask.id
        m["trigrules"] = {}
        m["coalition"] = {}
        for col in self.coalition.keys():
            m["coalition"][col] = self.coalition[col].dict()
        col_blue = {self.coalition["blue"].country(x).id for x in self.coalition["blue"].countries.keys()}
        col_red = {self.coalition["red"].country(x).id for x in self.coalition["red"].countries.keys()}
        col_neutral = list(Mission.COUNTRY_IDS - col_blue - col_red)
        col_blue = list(col_blue)
        col_red = list(col_red)
        m["coalitions"] = {
            "neutral": {x + 1: col_neutral[x] for x in range(0, len(col_neutral))},
            "blue": {x + 1: col_blue[x] for x in range(0, len(col_blue))},
            "red": {x + 1: col_red[x] for x in range(0, len(col_red))}
        }
        m["sortie"] = self.sortie.id
        m["version"] = self.version
        m["goals"] = self.goals
        m["currentKey"] = self.currentKey
        m["start_time"] = self.start_time
        m["forcedOptions"] = self.forcedOptions
        m["failures"] = self.failures

        return lua.dumps(m, "mission", 1)

    def __repr__(self):
        rep = {"base": self.values, "options": self.options, "translation": self.translation}
        return repr(rep)
