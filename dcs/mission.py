import zipfile
import lua


class Options:
    difficulty = {}
    playerName = ""
    graphics = {}
    plugins = {}
    views = {}
    sound = {}
    miscellaneous = {}


class Weather:
    pass


class Coalition:
    blue = {}
    red = {}
    neutral = {}


class String:

    def __init__(self, s, lang='DEFAULT'):
        self.string = {}
        self.string[lang] = s

    def get(self, lang='DEFAULT'):
        return self.string[lang]

    def __str__(self):
        return self.get()


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
    coalition = Coalition()  # unit descriptions
    version = 9
    goals = {}
    currentKey = 0
    start_time = 43200

    descriptionText = ""
    descriptionBlueTask = ""
    descriptionRedTask = ""
    pictureFileNameR = ""
    pictureFileNameB = ""

    options = Options()
    forcedOptions = {}
    failures = {}

    def __init__(self):
        pass

    def loadFile(self, filename):
        mission_dict = {}
        options_dict = {}
        warehouse_dict = {}
        dictionary_dict = {}

        def loaddict(fname, miz):
            with miz.open('mission') as mfile:
                data = mfile.read()
                data = data.decode()
                return lua.loads(data)

        with zipfile.ZipFile(filename, 'r') as miz:
            mission_dict = loaddict('mission', miz)
            options_dict = loaddict('options', miz)
            warehouse_dict = loaddict('warehouses', miz)
            dictionary_dict = loaddict('DEFAULT/dictionary', miz)

        print(mission_dict["mission"]["descriptionText"])

        return True
