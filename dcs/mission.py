import zipfile
import lua


class Options():
    difficulty = {}
    playerName = ""
    graphics = {}
    plugins = {}
    views = {}
    sound = {}
    miscellaneous = {}


class Weather():
    pass


class Coalition():
    blue = {}
    red = {}
    neutral = {}


class Mission():
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

    def __init__(self, filename):
        self.loadFile(filename)

    def loadFile(self, filename):
        mission_dict = {}
        options_dict = {}
        warehouse_dict = {}
        with zipfile.ZipFile(filename, 'r') as miz:
            with miz.open('mission') as mfile:
                mission_data = mfile.read()

                mission_data = mission_data.decode()
                mission_dict = lua.loads(mission_data)
                print(mission_dict)

            with miz.open('options') as optfile:
                opt_data = optfile.read()

                opt_data = opt_data.decode()
                options_dict = lua.loads(opt_data)
                print(options_dict)

            with miz.open('warehouses') as warefile:
                ware_data = warefile.read()

                ware_data = ware_data.decode()
                warehouse_dict = lua.loads(ware_data)
                print(warehouse_dict)

        return True
