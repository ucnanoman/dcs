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
    def __init__(self, _id, name, vehicle=[], plane=[], static=[]):
        self.id = _id
        self.name = name

    def name(self):
        return self.name


class Coalition:
    def __init__(self, name):
        self.name = name
        self.countries = []
        self.bulls_x = 0
        self.bulls_y = 0
        self.nav_points = []

    def set_bullseye(self, x, y):
        self.bulls_x = x
        self.bulls_y = y

    def add_country(self, country):
        self.countries[country.name()] = country

    def remove_country(self, name):
        return self.countries.pop(name)

    def dict(self):
        d = {}
        d["name"] = self.name
        if self.bulls_y and self.bulls_x:
            d["bullseye"] = {"x": self.bulls_x, "y": self.bulls_y}
        d["country"] = {}
        i = 0
        for country in self.countries:
            d["country"][i] = country.dict()
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

    def set_string(self, _id, string, lang='DEFAULT'):
        if lang not in self.strings:
            self.strings[lang] = {}
        self.strings[lang][_id] = string
        return _id

    def get_string(self, _id, lang='DEFAULT'):
        return String(_id, self, lang)

    def __str__(self):
        return str(self.strings)

    def __repr__(self):
        return repr(self.strings)


class Mission:
    trig = {}
    triggers = {}
    result = {}
    maxDictId = 0
    groundControl = {}
    usedModules = {}
    resourceCounter = {}
    weather = Weather()
    theatre = "Caucasus"
    needModules = {}
    coalition = Coalition("Blue")  # unit descriptions
    version = 9
    goals = {}
    currentKey = 0
    start_time = 43200

    options = Options()
    forcedOptions = {}
    failures = {}

    def __init__(self):
        self.translation = Translation()

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

        # print(self.translation)

        # import options
        self.options = Options(options_dict["options"])

        # import base values
        self.values = {}
        self.values["descriptionText"] = self.translation.get_string(imp_mission["descriptionText"])
        self.values["descriptionBlueTask"] = self.translation.get_string(imp_mission["descriptionBlueTask"])
        self.values["descriptionRedTask"] = self.translation.get_string(imp_mission["descriptionRedTask"])
        self.values["sortie"] = self.translation.get_string(imp_mission["sortie"])
        self.values["pictureFileNameR"] = imp_mission["pictureFileNameR"]
        self.values["pictureFileNameB"] = imp_mission["pictureFileNameB"]
        self.values["version"] = imp_mission["version"]
        self.values["currentKey"] = imp_mission["currentKey"]
        self.values["start_time"] = imp_mission["start_time"]
        self.values["maxDictId"] = imp_mission["maxDictId"]
        self.usedModules = imp_mission["usedModules"]
        print(self.usedModules)

        return True

    def description_text(self):
        return str(self.values["descriptionText"])

    def set_description_text(self, text):
        self.values["descriptionText"].set(text)

    def description_bluetask_text(self):
        return str(self.values["descriptionBlueTask"])

    def set_description_bluetask_text(self, text):
        self.values["descriptionBlueTask"].set(text)

    def description_redtask_text(self):
        return str(self.values["descriptionRedTask"])

    def set_description_redtask_text(self, text):
        self.values["descriptionRedTask"].set(text)

    def string(self, s):
        return "not implemented"

    def save(self, filename):
        return False

    def __str__(self):
        m = {}
        m["trig"] = self.trig
        m["result"] = self.result
        m["grounControl"] = self.groundControl
        m["usedModules"] = self.usedModules
        m["resourceCounter"] = self.resourceCounter
        m["triggers"] = self.triggers
        m["weather"] = self.weather.dict()
        m["theatre"] = self.theatre
        m["needModules"] = self.needModules
        m["map"] = {}
        m["descriptionText"] = self.values["descriptionText"].id()
        m["pictureFileNameR"] = self.values["pictureFileNameR"]
        m["pictureFileNameB"] = self.values["pictureFileNameB"]
        m["descriptionBlueTask"] = self.values["descriptionBlueTask"].id()
        m["descriptionRedTask"] = self.values["descriptionRedTask"].id()
        m["trigrules"] = {}
        m["coalition"] = self.coalition.dict()
        m["coalitions"] = {}  # generate from coalition
        m["sortie"] = self.values["sortie"].id()
        m["version"] = self.values["version"]
        m["goals"] = self.goals
        m["currentKey"] = self.currentKey
        m["start_time"] = self.start_time
        m["forcedOptions"] = self.forcedOptions
        m["failures"] = self.failures

        return lua.dumps(m, "mission", 1)

    def __repr__(self):
        rep = {"base": self.values, "options": self.options, "translation": self.translation}
        return repr(rep)
