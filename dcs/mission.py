import zipfile


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

    def loadFile(filename):
        with zipfile.ZipFile(filename, 'r') as miz:
            print(miz.namelist)

        return True
