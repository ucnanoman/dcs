import zipfile
import lua


class Options:

    def __init__(self, opts={}):
        self.options = opts

    def __repr__(self):
        return repr(self.options)


class Weather:
    pass


class Task:
    CAS = "CAS"
    CAP = "CAP"


class UnitType:
    M818 = "M 818"

class Unit:

    def __init__(self):
        self.type = ""
        self.x = 0
        self.y = 0
        self.heading = 0
        self.id = 0
        self.skill = "Average"
        self.player_can_drive = False
        self.transportable = {"randomTransportable": False}


class Point:

    def __init__(self):
        self.alt = 0
        self.alt_type = "BARO"
        self.type = ""
        self.ETA = 0
        self.speed_locked = True
        self.x = 0
        self.y = 0
        self.speed = 0
        self.action = "Offroad"
        self.task = []


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

class Country:

    def __init__(self, _id, name, vehicle=[], plane=[], static=[]):
        self.id = _id
        self.name = name

    def name(self):
        return self.name


class Coalition:

    def __init__(self, name):
        self.name = name
        self.countries = {}
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


class String:

    def __init__(self, _id, translation, lang='DEFAULT'):
        self.translation = translation
        self.lang = lang
        self._id = _id

    def set(self, text):
        self.translation.set_string(self._id, text, self.lang)
        return str(self)

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
    trig = []
    triggers = {}
    result = []
    maxDictId = 0
    groundControl = {}
    usedModules = {}
    weather = Weather()
    theatre = "Caucasus"
    needModules = {}
    coalitions = {}
    coalition = Coalition("Blue")  # unit descriptions
    version = 9
    goals = {}
    currentKey = 0
    start_time = 43200

    descriptionBlueTask = ""
    descriptionRedTask = ""
    pictureFileNameR = ""
    pictureFileNameB = ""

    options = Options()
    forcedOptions = {}
    failures = {}

    def __init__(self):
        self.translation = Translation()

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

        print(self.translation)

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

    def __repr__(self):
        rep = {"base": self.values, "options": self.options, "translation": self.translation}
        return repr(rep)