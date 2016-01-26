import zipfile
import lua


class Options:
    def __init__(self, opts={}):
        self.options = opts

    def __repr__(self):
        return repr(self.options)


class Weather:

    def dict(self):
        return {}

    def __str__(self):
        return lua.dumps({}, None, 1)


class Task:
    CAS = "CAS"
    CAP = "CAP"


class VehicleType:
    M818 = "M 818"


class PlaneType:
    A10C = "A-10C"


class Skill:
    AVERAGE = "Average"
    HIGH = "High"


class Unit:
    def __init__(self):
        self.type = ""
        self.x = 0
        self.y = 0
        self.heading = 0
        self.id = 0
        self.skill = Skill.AVERAGE
        self.player_can_drive = False
        self.transportable = {"randomTransportable": False}
        self.name = String()


class Plane(Unit):
    def __init__(self):
        self.livery_id = ""
        self.parking = None
        self.psi = ""
        self.callsign = {}
        self.onboard_num = "010"


class StaticType:
    AMMUNITION_DEPOT = ".Ammunition depot"


class Static(Unit):
    def __init__(self):
        self.category = "Warehouses"
        self.can_cargo = False


class Point:
    def __init__(self):
        self.alt = 0
        self.alt_type = "BARO"
        self.type = ""
        self.name = String()
        self.ETA = 0
        self.ETA_locked = True
        self.formation_template = ""
        self.speed_locked = True
        self.x = 0
        self.y = 0
        self.speed = 0
        self.action = "Offroad"
        self.task = []
        self.properties = None


class Group:
    def __init__(self):
        self.task = ""
        self.tasks = []
        self.uncontrolled = False
        self.id = 0
        self.hidden = False
        self.units = []
        self.x = 0
        self.y = 0
        self.start_time = 0
        self.spans = []
        self.points = []
        self.name = String()
        self.frequency = None


class Country:
    def __init__(self, _id, name, vehicle_group=[], plane_group=[], static_group=[]):
        self.id = _id
        self.name = name

    def name(self):
        return self.name

    def dict(self):
        d = {}
        d["name"] = self.name
        d["id"] = self.id
        return d


class Coalition:
    def __init__(self, name, bullseye=None):
        self.name = name
        self.countries = []
        self.bullseye = bullseye
        self.nav_points = []

    def set_bullseye(self, bulls):
        self.bullseye = bulls

    def add_country(self, country):
        self.countries.append(country)

    def remove_country(self, name):
        return self.countries.pop(name)

    def dict(self):
        d = {}
        d["name"] = self.name
        if self.bullseye:
            d["bullseye"] = self.bullseye
        d["country"] = {}
        i = 1
        for country in self.countries:
            d["country"][i] = country.dict()
            i += 1
        d["nav_points"] = {}
        return d


class String:
    def __init__(self, _id='', translation=None, lang='DEFAULT'):
        self.translation = translation
        self.lang = lang
        self._id = _id

    def set(self, text):
        self.translation.set_string(self._id, text, self.lang)
        return str(self)

    def id(self):
        return self._id

    def __str__(self):
        return self.translation.strings[self.lang][self._id]

    def __repr__(self):
        return self._id + ":" + str(self)


class Translation:
    def __init__(self):
        self.strings = {}
        self.maxDictId = 0

    def set_string(self, _id, string, lang='DEFAULT'):
        if lang not in self.strings:
            self.strings[lang] = {}
        self.strings[lang][_id] = string
        return _id

    def get_string(self, _id, lang='DEFAULT'):
        return String(_id, self, lang)

    def set_max_dict_id(self, dict_id):
        self.maxDictId = dict_id

    def max_dict_id(self):
        return self.maxDictId

    def __str__(self):
        return str(self.strings)

    def __repr__(self):
        return repr(self.strings)


class Mission:
    trig = {}
    triggers = {}
    result = {}
    groundControl = {}
    usedModules = {}
    resourceCounter = {}
    weather = Weather()
    needModules = {}
    COUNTRY_IDS = [x for x in range(0, 47)]

    options = Options()
    forcedOptions = {}
    failures = {}

    def __init__(self):
        self.translation = Translation()

        self.description_text = String()
        self.description_bluetask = String()
        self.description_redtask = String()
        self.sortie = String()
        self.pictureFileNameR = ""
        self.pictureFileNameB = ""
        self.version = 9
        self.currentKey = 0
        self.start_time = 43200
        self.theatre = "Caucasus"
        self.goals = {}
        self.coalition = {}

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

        self.translation.set_max_dict_id(imp_mission["maxDictId"])

        # print(self.translation)

        # import options
        self.options = Options(options_dict["options"])

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

        # import coalition
        def imp_coalition(coalition, key):
            if key not in coalition:
                return None
            imp_col = coalition[key]
            col = Coalition(key, imp_col["bullseye"])
            for country_idx in imp_col["country"]:
                imp_country = imp_col["country"][country_idx]
                if "vehicle" in imp_country:
                    for vgroup in imp_country["vehicle"]["group"]:
                        print(vgroup)
                col.add_country(Country(imp_country["id"], imp_country["name"]))
            return col
        # blue
        self.coalition["blue"] = imp_coalition(imp_mission["coalition"], "blue")
        self.coalition["red"] = imp_coalition(imp_mission["coalition"], "red")
        neutral_col = imp_coalition(imp_mission["coalition"], "neutral")
        if neutral_col:
            self.coalition["neutral"] = imp_coalition(imp_mission["coalition"], "neutral")

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

    def string(self, s):
        return "not implemented"

    def save(self, filename):
        return False

    def __str__(self):
        m = {}
        m["trig"] = self.trig
        m["result"] = self.result
        m["groundControl"] = self.groundControl
        m["usedModules"] = self.usedModules
        m["resourceCounter"] = self.resourceCounter
        m["triggers"] = self.triggers
        m["weather"] = self.weather.dict()
        m["theatre"] = self.theatre
        m["needModules"] = self.needModules
        m["map"] = {}
        m["descriptionText"] = self.description_text.id()
        m["pictureFileNameR"] = self.pictureFileNameR
        m["pictureFileNameB"] = self.pictureFileNameB
        m["descriptionBlueTask"] = self.description_bluetask.id()
        m["descriptionRedTask"] = self.description_redtask.id()
        m["trigrules"] = {}
        m["coalition"] = {}
        for col in self.coalition.keys():
            m["coalition"][col] = self.coalition[col].dict()
        m["coalitions"] = {}  # generate from coalition
        m["sortie"] = self.sortie.id()
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
