# terrain module


class Terrain:
    def __init__(self, name: str):
        self.name = name
        self.center = {"lat": 0, "long": 0}  # WGS84 decimal
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}
        self.airports = {}  # type dict[str,Airport]

    def airport_by_id(self, id: int):
        for x in self.airports:
            if self.airports[x].id == id:
                return self.airports[x]
        return None


class Caucasus(Terrain):
    def __init__(self):
        super(Caucasus, self).__init__("Caucasus")
        # caucasus center MGRS
        # 36TWQ9949898109
        self.center = {"lat": 45.12945, "long": 34.26527}
        self.bullseye_blue = {"x": -291014, "y": 617414}
        self.bullseye_red = {"x": 11557, "y": 371700}

        anapa = Airport(12, "Anapa", 121.0, 0, 0, None)
        self.airports[anapa.name] = anapa

        krasnodar_center = Airport(13, "Krasnodar-Center", 122.0, 0, 0, None)
        self.airports[krasnodar_center.name] = krasnodar_center

        novorossiysk = Airport(14, "Novorossiysk", 123.0, 0, 0, None)
        self.airports[novorossiysk.name] = novorossiysk

        krymsk = Airport(15, "Krymsk", 124.0, 0, 0, None)
        self.airports[krymsk.name] = krymsk

        maykop = Airport(16, "Maykop", 125.0, 0, 0, None)
        self.airports[maykop.name] = maykop

        gelendzihik = Airport(17, "Gelendzihik", 126.0, 0, 0, None)
        self.airports[gelendzihik.name] = gelendzihik

        sochi = Airport(18, "Sochi", 127.0, 0, 0, None)
        self.airports[sochi.name] = sochi

        krasnodar_pashkovsky = Airport(19, "Krasnodar-Pashkovsky", 128.0, 0, 0, None)
        self.airports[krasnodar_pashkovsky.name] = krasnodar_pashkovsky

        sukhumi = Airport(20, "Sukhumi", 129.0, 0, 0, None)
        self.airports[sukhumi.name] = sukhumi

        gudauta = Airport(21, "Gudauta", 130.0, 0, 0, None)
        self.airports[gudauta.name] = gudauta

        batumi = Airport(22, "Batumi", 131.0, -293933, 540000, "16X")
        batumi.runways.append(Runway(120, 110.3))
        self.airports[batumi.name] = batumi

        senaki = Airport(23, "Senaki", 132.0, -281619.03125, 646385.625, "31X")
        senaki.runways.append(Runway(90, 108.9))
        self.airports[senaki.name] = senaki

        kobuleti = Airport(24, "Kobuleti", 133.0, -317948.32727306, 635639.37385346, "67X")
        kobuleti.runways.append(Runway(70, 111.50))
        kobuleti.runways.append(Runway(290))
        kobuleti.parking_slots[22] = ParkingSlot(22, -317899.40625, 636670.4375, True)
        kobuleti.parking_slots[23] = ParkingSlot(23, -317680.78125, 636917.5625, True)
        kobuleti.parking_slots[24] = ParkingSlot(24, -317870.0625, 636859.8125, True)
        kobuleti.parking_slots[25] = ParkingSlot(25, -317874.9375, 635000.375, True)
        kobuleti.parking_slots[26] = ParkingSlot(26, -317740.6875, 635084.25, True)
        kobuleti.parking_slots[28] = ParkingSlot(28, -318024.84375, 636164.5625, False)
        kobuleti.parking_slots[30] = ParkingSlot(30, -318097.4375, 636237.875, False)
        kobuleti.parking_slots[31] = ParkingSlot(31, -318026.75, 636258.8125, False)
        kobuleti.parking_slots[33] = ParkingSlot(33, -317938.25, 636402.5, False)
        kobuleti.parking_slots[35] = ParkingSlot(35, -318010.84375, 636475.875, False)
        kobuleti.parking_slots[36] = ParkingSlot(36, -317940.15625, 636496.8125, False)
        kobuleti.parking_slots[37] = ParkingSlot(37, -317787.46875, 635295.8125, False)
        kobuleti.parking_slots[38] = ParkingSlot(38, -317697.21875, 635543.6875, False)
        kobuleti.parking_slots[39] = ParkingSlot(39, -317584.375, 635853.8125, False)
        kobuleti.parking_slots[40] = ParkingSlot(40, -317621.96875, 635750.4375, False)
        kobuleti.parking_slots[41] = ParkingSlot(41, -317471.53125, 635753.3125, False)
        kobuleti.parking_slots[42] = ParkingSlot(42, -317509.15625, 635649.9375, False)
        kobuleti.parking_slots[43] = ParkingSlot(43, -317546.78125, 635546.5625, False)
        kobuleti.parking_slots[44] = ParkingSlot(44, -317641.71875, 635285.6875, False)
        kobuleti.parking_slots[45] = ParkingSlot(45, -317584.40625, 635443.1875, False)
        kobuleti.parking_slots[47] = ParkingSlot(47, -318319.71875, 635219.75, False)
        kobuleti.parking_slots[48] = ParkingSlot(48, -318326.46875, 635190.4375, False)
        kobuleti.parking_slots[53] = ParkingSlot(53, -318272.5, 635424.3125, False)
        kobuleti.parking_slots[54] = ParkingSlot(54, -318279.21875, 635395.0625, False)
        kobuleti.parking_slots[57] = ParkingSlot(57, -318286, 635365.8125, False)
        kobuleti.parking_slots[58] = ParkingSlot(58, -318312.96875, 635248.9375, False)
        kobuleti.parking_slots[60] = ParkingSlot(60, -318292.71875, 635336.625, False)
        kobuleti.parking_slots[62] = ParkingSlot(62, -318299.46875, 635307.4375, False)
        kobuleti.parking_slots[63] = ParkingSlot(63, -318306.21875, 635278.125, False)
        kobuleti.parking_slots[66] = ParkingSlot(66, -318189.96875, 635662.6875, False)
        kobuleti.parking_slots[68] = ParkingSlot(68, -318200.21875, 635634.5, False)
        kobuleti.parking_slots[70] = ParkingSlot(70, -318210.5, 635606.3125, False)
        kobuleti.parking_slots[72] = ParkingSlot(72, -318220.75, 635578.125, False)
        kobuleti.parking_slots[74] = ParkingSlot(74, -318231, 635549.9375, False)
        kobuleti.parking_slots[75] = ParkingSlot(75, -318241.28125, 635521.75, False)
        kobuleti.parking_slots[76] = ParkingSlot(76, -318251.53125, 635493.5625, False)
        kobuleti.parking_slots[78] = ParkingSlot(78, -318102, 635959.75, True)
        kobuleti.parking_slots[80] = ParkingSlot(80, -318122.53125, 635903.375, True)
        kobuleti.parking_slots[82] = ParkingSlot(82, -318143.03125, 635847, True)
        kobuleti.parking_slots[84] = ParkingSlot(84, -318163.5625, 635790.625, True)
        kobuleti.parking_slots[85] = ParkingSlot(85, -317659.59375, 635647.0625, False)
        kobuleti.parking_slots[86] = ParkingSlot(86, -318184.09375, 635734.25, True)
        self.airports[kobuleti.name] = kobuleti

        kutaisi = Airport(25, "Kutaisi", 134.0, 0, 0, None)
        kutaisi.runways.append(Runway(70, 109.40))
        self.airports[kutaisi.name] = kutaisi

        mineralnye = Airport(26, "Mineralnye", 135.0, 0, 0, None)
        self.airports[mineralnye.name] = mineralnye

        nalchik = Airport(27, "Nalchik", 136.0, 0, 0, None)
        self.airports[nalchik.name] = nalchik

        mozdok = Airport(28, "Mozdok", 137.0, 0, 0, None)
        self.airports[mozdok.name] = mozdok

        lochini = Airport(29, "Lochini", 138.0, 0, 0, None)
        lochini.runways.append(Runway(130, 110.30, 2))
        lochini.runways.append(Runway(300, 108.90, 1))
        self.airports[lochini.name] = lochini

        soganlug = Airport(30, "Soganlug", 139.0, 0, 0, None)
        self.airports[soganlug.name] = soganlug

        vaziani = Airport(31, "Vaziani", 140.0, 0, 0, None)
        vaziani.runways.append(Runway(130, 108.75))
        vaziani.runways.append(Runway(310, 108.75))
        self.airports[vaziani.name] = vaziani

        beslan = Airport(32, "Beslan", 141.0, 0, 0, None)
        self.airports[beslan.name] = beslan


class Nevada(Terrain):
    def __init__(self):
        super(Nevada, self).__init__("Nevada")
        # nttr center MGRS
        # 11SPE9400410022
        self.center = {"lat": 39.81806, "long": -114.73333}
        self.bullseye_blue = {"x": -409931.344, "y": -14024.097}
        self.bullseye_red = {"x": -288293.969, "y": -88022.641}


class ParkingSlot:
    def __init__(self, _id, x, y, large=False):
        self.id = _id
        self.x = x
        self.y = y
        self.large = large
        self.unit_id = None  # type: int


class Runway:
    def __init__(self, heading, ils=None, leftright=0):
        """

        :param heading:
        :param ils:
        :param leftright: 0 only 1 runway
                          1 left runway
                          2 right runway
        :return: None
        """
        self.heading = heading
        self.ils = ils
        self.leftright = leftright


class Airport:
    def __init__(self, _id: int, name: str, frequency: float, x, y, tacan: str=None):
        self.id = _id
        self.name = name
        self.tacan = tacan
        self.frequency = frequency
        self.x = x
        self.y = y
        self.runways = []
        self.parking_slots = {}  # type: dict[str:ParkingSlot]

        # warehouse values
        self.coalition = "NEUTRAL"
        self.size = 100
        self.speed = 16.666666
        self.periodicity = 30
        self.unlimited_munitions = True
        self.unlimited_aircrafts = True
        self.unlimited_fuel = True
        self.operating_level_air = 10
        self.operating_level_fuel = 10
        self.operating_level_equipment = 10
        self.aircrafts = {}
        self.weapons = {}
        self.suppliers = {}
        self.gasoline_init = 100
        self.methanol_mixture_init = 100
        self.diesel_init = 100
        self.jet_init = 100

    def load_from_dict(self, d):
        self.coalition = d["coalition"]
        self.speed = d["speed"]
        self.size = d["size"]
        self.periodicity = d["periodicity"]
        self.unlimited_munitions = d["unlimitedMunitions"]
        self.unlimited_fuel = d["unlimitedFuel"]
        self.unlimited_aircrafts = d["unlimitedAircrafts"]
        self.operating_level_air = d["OperatingLevel_Air"]
        self.operating_level_equipment = d["OperatingLevel_Eqp"]
        self.operating_level_fuel = d["OperatingLevel_Fuel"]
        self.gasoline_init = d.get("gasoline", {}).get("InitFuel", 100)
        self.diesel_init = d.get("diesel", {}).get("InitFuel", 100)
        self.jet_init = d.get("jet_fuel", {}).get("InitFuel", 100)
        self.methanol_mixture_init = d.get("methanol_mixture", {}).get("InitFuel", 100)
        self.aircrafts = d["aircrafts"]
        self.weapons = d["weapons"]

    def set_blue(self):
        self.coalition = "BLUE"

    def set_red(self):
        self.coalition = "RED"

    def set_neutral(self):
        self.coalition = "NEUTRAL"

    def free_parking_slot(self, large: bool):
        free_slots = [x for x in sorted(self.parking_slots)
                      if self.parking_slots[x].unit_id is None and
                      self.parking_slots[x].large == large]
        return self.parking_slots[free_slots[0]]

    def dict(self):
        d = {
            "coalition": self.coalition,
            "speed": self.speed,
            "size": self.size,
            "periodicity": self.periodicity,
            "unlimitedMunitions": self.unlimited_munitions,
            "unlimitedFuel": self.unlimited_fuel,
            "unlimitedAircrafts": self.unlimited_aircrafts,
            "OperatingLevel_Air": self.operating_level_air,
            "OperatingLevel_Eqp": self.operating_level_equipment,
            "OperatingLevel_Fuel": self.operating_level_fuel,
            "gasoline": {"InitFuel": self.gasoline_init},
            "diesel": {"InitFuel": self.diesel_init},
            "jet_fuel": {"InitFuel": self.jet_init},
            "methanol_mixture": {"InitFuel": self.methanol_mixture_init},
            "aircrafts": self.aircrafts,
            "weapons": self.weapons
        }
        return d
