# terrain module


class ParkingSlot:
    def __init__(self, _id, x, y, large=False, slot_name=None, heli=False):
        self.id = _id
        self.x = x
        self.y = y
        self.helicopter = heli
        self.large = large
        self.unit_id = None  # type: int
        self.slot_name = slot_name


class Runway:
    def __init__(self, heading, ils=None, leftright=0):
        """

        :param heading: Compass direction of runway
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
        self.runways = []  # type: list[Runway]
        self.parking_slots = {}  # type: dict[str:ParkingSlot]
        self.runway_free = True

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

    def free_parking_slot(self, large: bool, helicopter: bool):
        slots_sorted = sorted(self.parking_slots)
        free_large_slots = {x for x in slots_sorted
                            if self.parking_slots[x].unit_id is None and
                            self.parking_slots[x].large}

        if large:
            if free_large_slots:
                return self.parking_slots[list(free_large_slots)[0]]
            else:
                return None

        free_heli_slots = {x for x in slots_sorted
                           if self.parking_slots[x].unit_id is None and
                           self.parking_slots[x].helicopter}
        if helicopter:
            if free_heli_slots:
                return self.parking_slots[list(free_heli_slots)[0]]
            else:
                return None

        free_slots = [x for x in slots_sorted if self.parking_slots[x].unit_id is None] + list(free_large_slots)

        if free_slots:
            return self.parking_slots[free_slots[0]]
        return None

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
            "weapons": self.weapons,
            "suppliers": self.suppliers
        }
        return d


class Terrain:
    def __init__(self, name: str):
        self.name = name
        self.center = {"lat": 0, "long": 0}  # WGS84 decimal
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}
        self.airports = {}  # type dict[str,Airport]

    def airport_by_id(self, id: int) -> Airport:
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

        sochi = Airport(18, "Sochi", 127.0, -164474.73482633, 462236.21834688, None)
        sochi.runways.append(Runway(240))
        sochi.runways.append(Runway(60))
        sochi.parking_slots[6] = ParkingSlot(6, -164477.484375, 461754.53125, True, "20")
        sochi.parking_slots[22] = ParkingSlot(22, -164505.65625, 461701.5, True, "19")
        sochi.parking_slots[26] = ParkingSlot(26, -164970.5625, 460858.0625, False, "03")
        sochi.parking_slots[27] = ParkingSlot(27, -164989.203125, 460822.71875, False, "01")
        sochi.parking_slots[28] = ParkingSlot(28, -164979.890625, 460840.40625, False, "02")
        sochi.parking_slots[29] = ParkingSlot(29, -164420.703125, 461860.6875, True, "22")
        sochi.parking_slots[31] = ParkingSlot(31, -164392.53125, 461913.59375, True, "23")
        sochi.parking_slots[33] = ParkingSlot(33, -164336.171875, 462019.59375, True, "25")
        sochi.parking_slots[35] = ParkingSlot(35, -164364.359375, 461966.59375, True, "24")
        sochi.parking_slots[37] = ParkingSlot(37, -164449.3125, 461807.4375, True, "21")
        sochi.parking_slots[38] = ParkingSlot(38, -164931.828125, 460930.46875, False, "07")
        sochi.parking_slots[39] = ParkingSlot(39, -164829.203125, 461125.09375, False, "18")
        sochi.parking_slots[40] = ParkingSlot(40, -164875.828125, 461036.65625, False, "13")
        sochi.parking_slots[42] = ParkingSlot(42, -164959.78125, 460877.4375, False, "04")
        sochi.parking_slots[43] = ParkingSlot(43, -164950.453125, 460895.15625, False, "05")
        sochi.parking_slots[44] = ParkingSlot(44, -164941.125, 460912.75, False, "06")
        sochi.parking_slots[45] = ParkingSlot(45, -164922.46875, 460948.15625, False, "08")
        sochi.parking_slots[46] = ParkingSlot(46, -164913.171875, 460965.875, False, "09")
        sochi.parking_slots[47] = ParkingSlot(47, -164903.828125, 460983.59375, False, "10")
        sochi.parking_slots[48] = ParkingSlot(48, -164838.53125, 461107.40625, False, "17")
        sochi.parking_slots[49] = ParkingSlot(49, -164866.515625, 461054.34375, False, "14")
        sochi.parking_slots[50] = ParkingSlot(50, -164857.1875, 461072.03125, False, "15")
        sochi.parking_slots[51] = ParkingSlot(51, -164847.84375, 461089.75, False, "16")
        sochi.parking_slots[52] = ParkingSlot(52, -164885.171875, 461018.96875, False, "12")
        sochi.parking_slots[53] = ParkingSlot(53, -164894.5, 461001.28125, False, "11")
        sochi.parking_slots[59] = ParkingSlot(59, -164288.921875, 462107.65625, True, "26")
        sochi.parking_slots[60] = ParkingSlot(60, -164260.75, 462160.65625, True, "27")
        sochi.parking_slots[61] = ParkingSlot(61, -164232.578125, 462213.59375, True, "28")
        sochi.parking_slots[62] = ParkingSlot(62, -164147.625, 462372.71875, True, "31")
        sochi.parking_slots[63] = ParkingSlot(63, -164119.4375, 462425.75, True, "32")
        sochi.parking_slots[64] = ParkingSlot(64, -164091.28125, 462478.6875, True, "33")
        sochi.parking_slots[65] = ParkingSlot(65, -164175.796875, 462319.75, True, "30")
        sochi.parking_slots[66] = ParkingSlot(66, -164203.96875, 462266.84375, True, "29")
        sochi.parking_slots[78] = ParkingSlot(78, -164775.546875, 463128.5625, False, "66")
        sochi.parking_slots[80] = ParkingSlot(80, -164838.75, 463060.25, False, "68")
        sochi.parking_slots[81] = ParkingSlot(81, -164766.0625, 463016.3125, False, "67")
        sochi.parking_slots[83] = ParkingSlot(83, -164674.28125, 463183.09375, False, "63")
        sochi.parking_slots[85] = ParkingSlot(85, -164737.484375, 463114.78125, False, "65")
        sochi.parking_slots[86] = ParkingSlot(86, -164664.796875, 463070.84375, False, "64")
        sochi.parking_slots[88] = ParkingSlot(88, -164573.921875, 463238, False, "60")
        sochi.parking_slots[90] = ParkingSlot(90, -164637.125, 463169.6875, False, "62")
        sochi.parking_slots[91] = ParkingSlot(91, -164564.4375, 463125.75, False, "61")
        sochi.parking_slots[93] = ParkingSlot(93, -164473.5625, 463292.375, False, "57")
        sochi.parking_slots[95] = ParkingSlot(95, -164536.765625, 463224.0625, False, "59")
        sochi.parking_slots[96] = ParkingSlot(96, -164464.078125, 463180.125, False, "58")
        sochi.parking_slots[98] = ParkingSlot(98, -164370.953125, 463346.75, False, "54")
        sochi.parking_slots[100] = ParkingSlot(100, -164434.15625, 463278.4375, False, "56")
        sochi.parking_slots[101] = ParkingSlot(101, -164361.46875, 463234.5, False, "55")
        sochi.parking_slots[104] = ParkingSlot(104, -164333.625, 463333.6875, False, "53")
        sochi.parking_slots[105] = ParkingSlot(105, -164260.9375, 463289.75, False, "52")
        sochi.parking_slots[106] = ParkingSlot(106, -164270.421875, 463402, False, "51")
        sochi.parking_slots[109] = ParkingSlot(109, -164233.5, 463387.84375, False, "50")
        sochi.parking_slots[110] = ParkingSlot(110, -164160.8125, 463343.90625, False, "49")
        sochi.parking_slots[111] = ParkingSlot(111, -164170.296875, 463456.15625, False, "48")
        sochi.parking_slots[114] = ParkingSlot(114, -164132.734375, 463442.59375, False, "47")
        sochi.parking_slots[115] = ParkingSlot(115, -164060.046875, 463398.65625, False, "46")
        sochi.parking_slots[116] = ParkingSlot(116, -164069.53125, 463510.90625, False, "45")
        sochi.parking_slots[119] = ParkingSlot(119, -164032.046875, 463497.90625, False, "44")
        sochi.parking_slots[120] = ParkingSlot(120, -163968.84375, 463566.21875, False, "42")
        sochi.parking_slots[121] = ParkingSlot(121, -163959.359375, 463453.96875, False, "43")
        sochi.parking_slots[128] = ParkingSlot(128, -164034.625, 462584.46875, True, "35")
        sochi.parking_slots[129] = ParkingSlot(129, -164006.4375, 462637.5, True, "36")
        sochi.parking_slots[130] = ParkingSlot(130, -164062.796875, 462531.5, True, "34")
        sochi.parking_slots[134] = ParkingSlot(134, -163949.84375, 462743.25, True, "38")
        sochi.parking_slots[135] = ParkingSlot(135, -163921.65625, 462796.28125, True, "39")
        sochi.parking_slots[136] = ParkingSlot(136, -163978.015625, 462690.28125, True, "37")
        sochi.parking_slots[137] = ParkingSlot(137, -163893.3125, 462849.15625, True, "40")
        sochi.parking_slots[138] = ParkingSlot(138, -163865.125, 462902.1875, True, "41")
        self.airports[sochi.name] = sochi

        krasnodar_pashkovsky = Airport(19, "Krasnodar-Pashkovsky", 128.0, 0, 0, None)
        self.airports[krasnodar_pashkovsky.name] = krasnodar_pashkovsky

        sukhumi = Airport(20, "Sukhumi", 129.0, -219863.984375, 563508.6875, None)
        sukhumi.runways.append(Runway(300))
        sukhumi.runways.append(Runway(120))
        sukhumi.parking_slots[9] = ParkingSlot(9, -219863.984375, 563508.6875, True, "23")
        sukhumi.parking_slots[10] = ParkingSlot(10, -219887.796875, 563586.0625, True, "22")
        sukhumi.parking_slots[12] = ParkingSlot(12, -219911.09375, 563654.5625, True, "21")
        sukhumi.parking_slots[22] = ParkingSlot(22, -219760.4375, 563975.125, False, "05")
        sukhumi.parking_slots[26] = ParkingSlot(26, -219710.328125, 564235, False, "12")
        sukhumi.parking_slots[27] = ParkingSlot(27, -219830.765625, 564130.75, False, "15")
        sukhumi.parking_slots[29] = ParkingSlot(29, -219791.421875, 563737, True, "02")
        sukhumi.parking_slots[30] = ParkingSlot(30, -219773.0625, 563880.4375, True, "03")
        sukhumi.parking_slots[31] = ParkingSlot(31, -219733.421875, 563743.375, True, "01")
        sukhumi.parking_slots[42] = ParkingSlot(42, -219714.203125, 564198, False, "11")
        sukhumi.parking_slots[45] = ParkingSlot(45, -219701.984375, 564314.5625, False, "14")
        sukhumi.parking_slots[46] = ParkingSlot(46, -219706.140625, 564274.8125, False, "13")
        sukhumi.parking_slots[47] = ParkingSlot(47, -219809.890625, 564329.5, False, "20")
        sukhumi.parking_slots[48] = ParkingSlot(48, -219814.046875, 564289.875, False, "19")
        sukhumi.parking_slots[49] = ParkingSlot(49, -219818.21875, 564250.0625, False, "18")
        sukhumi.parking_slots[50] = ParkingSlot(50, -219822.40625, 564210.3125, False, "17")
        sukhumi.parking_slots[51] = ParkingSlot(51, -219826.59375, 564170.5, False, "16")
        sukhumi.parking_slots[52] = ParkingSlot(52, -219740.046875, 564173.4375, False, "10")
        sukhumi.parking_slots[53] = ParkingSlot(53, -219743.703125, 564134.25, False, "09")
        sukhumi.parking_slots[54] = ParkingSlot(54, -219747.890625, 564094.5, False, "08")
        sukhumi.parking_slots[55] = ParkingSlot(55, -219752.0625, 564054.6875, False, "07")
        sukhumi.parking_slots[56] = ParkingSlot(56, -219756.25, 564014.9375, False, "06")
        sukhumi.parking_slots[57] = ParkingSlot(57, -219760.46875, 563934.625, True, "04")

        self.airports[sukhumi.name] = sukhumi

        gudauta = Airport(21, "Gudauta", 130.0, 0, 0, None)
        self.airports[gudauta.name] = gudauta

        batumi = Airport(22, "Batumi", 131.0, -355692.3067714, 617269.96285781, "16X")
        batumi.runways.append(Runway(300))
        batumi.runways.append(Runway(120, 110.3))
        batumi.parking_slots[3] = ParkingSlot(3, -355972.03125, 618122.6875, False, "01")
        batumi.parking_slots[5] = ParkingSlot(5, -355984.8125, 618141.25, False, "02")
        batumi.parking_slots[7] = ParkingSlot(7, -356010.375, 618177.5625, False, "04")
        batumi.parking_slots[9] = ParkingSlot(9, -355997.40625, 618159.25, False, "03")
        batumi.parking_slots[15] = ParkingSlot(15, -356091.65625, 618219.125, True, "06")
        batumi.parking_slots[16] = ParkingSlot(16, -356059.21875, 618240.25, False, "05")
        batumi.parking_slots[18] = ParkingSlot(18, -356100.46875, 618303.125, False, "07")
        batumi.parking_slots[21] = ParkingSlot(21, -356140.09375, 618271.0625, True, "08")
        batumi.parking_slots[23] = ParkingSlot(23, -356180.90625, 618327, True, "10")
        batumi.parking_slots[24] = ParkingSlot(24, -356151.25, 618352.625, False, "09")
        self.airports[batumi.name] = batumi

        senaki = Airport(23, "Senaki", 132.0, -281619.03125, 646385.625, "31X")
        senaki.runways.append(Runway(90, 108.9))
        self.airports[senaki.name] = senaki

        kobuleti = Airport(24, "Kobuleti", 133.0, -317948.32727306, 635639.37385346, "67X")
        kobuleti.runways.append(Runway(70, 111.50))
        kobuleti.runways.append(Runway(250))
        kobuleti.parking_slots[22] = ParkingSlot(22, -317899.40625, 636670.4375, large=True, slot_name="28", heli=False)
        kobuleti.parking_slots[23] = ParkingSlot(23, -317680.78125, 636917.5625, large=True, slot_name="30", heli=False)
        kobuleti.parking_slots[24] = ParkingSlot(24, -317870.0625, 636859.8125, large=True, slot_name="29", heli=False)
        kobuleti.parking_slots[25] = ParkingSlot(25, -317874.9375, 635000.375, large=True, slot_name="42", heli=False)
        kobuleti.parking_slots[26] = ParkingSlot(26, -317740.6875, 635084.25, large=True, slot_name="41", heli=False)
        kobuleti.parking_slots[28] = ParkingSlot(28, -318024.84375, 636164.5625, large=False, slot_name="24", heli=False)
        kobuleti.parking_slots[30] = ParkingSlot(30, -318097.4375, 636237.875, large=False, slot_name="22", heli=False)
        kobuleti.parking_slots[31] = ParkingSlot(31, -318026.75, 636258.8125, large=False, slot_name="23", heli=False)
        kobuleti.parking_slots[33] = ParkingSlot(33, -317938.25, 636402.5, large=False, slot_name="27", heli=False)
        kobuleti.parking_slots[35] = ParkingSlot(35, -318010.84375, 636475.875, large=False, slot_name="25", heli=False)
        kobuleti.parking_slots[36] = ParkingSlot(36, -317940.15625, 636496.8125, large=False, slot_name="26", heli=False)
        kobuleti.parking_slots[37] = ParkingSlot(37, -317787.46875, 635295.8125, large=False, slot_name="40", heli=False)
        kobuleti.parking_slots[38] = ParkingSlot(38, -317697.21875, 635543.6875, large=False, slot_name="37", heli=False)
        kobuleti.parking_slots[39] = ParkingSlot(39, -317584.375, 635853.8125, large=False, slot_name="31", heli=False)
        kobuleti.parking_slots[40] = ParkingSlot(40, -317621.96875, 635750.4375, large=False, slot_name="33", heli=False)
        kobuleti.parking_slots[41] = ParkingSlot(41, -317471.53125, 635753.3125, large=False, slot_name="32", heli=False)
        kobuleti.parking_slots[42] = ParkingSlot(42, -317509.15625, 635649.9375, large=False, slot_name="34", heli=False)
        kobuleti.parking_slots[43] = ParkingSlot(43, -317546.78125, 635546.5625, large=False, slot_name="36", heli=False)
        kobuleti.parking_slots[44] = ParkingSlot(44, -317641.71875, 635285.6875, large=False, slot_name="39", heli=False)
        kobuleti.parking_slots[45] = ParkingSlot(45, -317584.40625, 635443.1875, large=False, slot_name="38", heli=False)
        kobuleti.parking_slots[47] = ParkingSlot(47, -318319.71875, 635219.75, large=False, slot_name="02", heli=True)
        kobuleti.parking_slots[48] = ParkingSlot(48, -318326.46875, 635190.4375, large=False, slot_name="01", heli=True)
        kobuleti.parking_slots[53] = ParkingSlot(53, -318272.5, 635424.3125, large=False, slot_name="09", heli=True)
        kobuleti.parking_slots[54] = ParkingSlot(54, -318279.21875, 635395.0625, large=False, slot_name="08", heli=True)
        kobuleti.parking_slots[57] = ParkingSlot(57, -318286, 635365.8125, large=False, slot_name="07", heli=True)
        kobuleti.parking_slots[58] = ParkingSlot(58, -318312.96875, 635248.9375, large=False, slot_name="03", heli=True)
        kobuleti.parking_slots[60] = ParkingSlot(60, -318292.71875, 635336.625, large=False, slot_name="06", heli=True)
        kobuleti.parking_slots[62] = ParkingSlot(62, -318299.46875, 635307.4375, large=False, slot_name="05", heli=True)
        kobuleti.parking_slots[63] = ParkingSlot(63, -318306.21875, 635278.125, large=False, slot_name="04", heli=True)
        kobuleti.parking_slots[66] = ParkingSlot(66, -318189.96875, 635662.6875, large=False, slot_name="16", heli=True)
        kobuleti.parking_slots[68] = ParkingSlot(68, -318200.21875, 635634.5, large=False, slot_name="15", heli=True)
        kobuleti.parking_slots[70] = ParkingSlot(70, -318210.5, 635606.3125, large=False, slot_name="14", heli=True)
        kobuleti.parking_slots[72] = ParkingSlot(72, -318220.75, 635578.125, large=False, slot_name="13", heli=True)
        kobuleti.parking_slots[74] = ParkingSlot(74, -318231, 635549.9375, large=False, slot_name="12", heli=True)
        kobuleti.parking_slots[75] = ParkingSlot(75, -318241.28125, 635521.75, large=False, slot_name="11", heli=True)
        kobuleti.parking_slots[76] = ParkingSlot(76, -318251.53125, 635493.5625, large=False, slot_name="10", heli=True)
        kobuleti.parking_slots[78] = ParkingSlot(78, -318102, 635959.75, large=True, slot_name="21", heli=False)
        kobuleti.parking_slots[80] = ParkingSlot(80, -318122.53125, 635903.375, large=True, slot_name="20", heli=False)
        kobuleti.parking_slots[82] = ParkingSlot(82, -318143.03125, 635847, large=True, slot_name="19", heli=False)
        kobuleti.parking_slots[84] = ParkingSlot(84, -318163.5625, 635790.625, large=True, slot_name="18", heli=False)
        kobuleti.parking_slots[85] = ParkingSlot(85, -317659.59375, 635647.0625, large=False, slot_name="35", heli=False)
        kobuleti.parking_slots[86] = ParkingSlot(86, -318184.09375, 635734.25, large=True, slot_name="17", heli=False)
        self.airports[kobuleti.name] = kobuleti

        kutaisi = Airport(25, "Kutaisi", 134.0, 0, 0, None)
        kutaisi.runways.append(Runway(70, 109.40))
        self.airports[kutaisi.name] = kutaisi

        mineralnye = Airport(26, "Mineralnye", 135.0, 0, 0, None)
        self.airports[mineralnye.name] = mineralnye

        nalchik = Airport(27, "Nalchik", 136.0, -124921.90954665, 760428.0733062, None)
        nalchik.runways.append(Runway(60))
        nalchik.runways.append(Runway(240))
        nalchik.parking_slots[18] = ParkingSlot(18, -125277.8359375, 760545.625, large=False, slot_name="02", heli=True)
        nalchik.parking_slots[21] = ParkingSlot(21, -125119.265625, 760800.75, large=True, slot_name="01", heli=False)
        nalchik.parking_slots[23] = ParkingSlot(23, -125153.2734375, 760751.3125, large=True, slot_name="03", heli=False)
        nalchik.parking_slots[24] = ParkingSlot(24, -125187.2265625, 760701.875, large=True, slot_name="04", heli=False)
        nalchik.parking_slots[25] = ParkingSlot(25, -125221.234375, 760652.375, large=True, slot_name="05", heli=False)
        nalchik.parking_slots[27] = ParkingSlot(27, -125294.8359375, 760520.875, large=False, slot_name="06", heli=True)
        nalchik.parking_slots[29] = ParkingSlot(29, -125311.7890625, 760496.1875, large=False, slot_name="07", heli=True)
        nalchik.parking_slots[31] = ParkingSlot(31, -125328.7890625, 760471.4375, large=False, slot_name="08", heli=True)
        nalchik.parking_slots[33] = ParkingSlot(33, -125345.796875, 760446.75, large=False, slot_name="09", heli=True)
        nalchik.parking_slots[34] = ParkingSlot(34, -125362.796875, 760422, large=False, slot_name="10", heli=True)
        nalchik.parking_slots[35] = ParkingSlot(35, -125379.75, 760397.3125, large=False, slot_name="11", heli=True)
        nalchik.parking_slots[37] = ParkingSlot(37, -125396.75, 760372.5625, large=False, slot_name="12", heli=True)
        nalchik.parking_slots[38] = ParkingSlot(38, -125413.7578125, 760347.8125, large=False, slot_name="13", heli=True)
        nalchik.parking_slots[39] = ParkingSlot(39, -125430.7578125, 760323.125, large=False, slot_name="14", heli=True)
        nalchik.parking_slots[41] = ParkingSlot(41, -125255.1875, 760602.9375, large=True, slot_name="15", heli=False)
        self.airports[nalchik.name] = nalchik

        mozdok = Airport(28, "Mozdok", 137.0, -83454.571428571, 834453.14285714, None)
        mozdok.runways.append(Runway(80, None))
        mozdok.runways.append(Runway(260, None))
        mozdok.parking_slots[6] = ParkingSlot(6, -83756.9765625, 835044.375, False, "23", heli=True)
        mozdok.parking_slots[8] = ParkingSlot(8, -83709.4765625, 835329.4375, False, "24", heli=True)
        mozdok.parking_slots[12] = ParkingSlot(12, -85089.6484375, 831900.625, False, "37", heli=True)
        mozdok.parking_slots[15] = ParkingSlot(15, -85244.9765625, 831859.3125, False, "38", heli=True)
        mozdok.parking_slots[17] = ParkingSlot(17, -85211.515625, 831977.5, False, "36", heli=True)
        mozdok.parking_slots[18] = ParkingSlot(18, -85076.625, 832018.875, False, "35", heli=True)
        mozdok.parking_slots[20] = ParkingSlot(20, -85228.046875, 832295.875, False, "33", heli=True)
        mozdok.parking_slots[21] = ParkingSlot(21, -85267.84375, 832172.375, False, "34", heli=True)
        mozdok.parking_slots[23] = ParkingSlot(23, -85130.890625, 832222.5, False, "32", heli=True)
        mozdok.parking_slots[25] = ParkingSlot(25, -83971.671875, 832792.3125, False, "31", heli=True)
        mozdok.parking_slots[27] = ParkingSlot(27, -83950.7578125, 833011.4375, False, "30", heli=True)
        mozdok.parking_slots[29] = ParkingSlot(29, -83939.3828125, 833133.4375, False, "29", heli=True)
        mozdok.parking_slots[30] = ParkingSlot(30, -83928.53125, 833278.125, False, "28", heli=True)
        mozdok.parking_slots[32] = ParkingSlot(32, -83958.5078125, 833466.25, False, "27", heli=True)
        mozdok.parking_slots[34] = ParkingSlot(34, -84066, 833605.25, False, "26", heli=True)
        mozdok.parking_slots[37] = ParkingSlot(37, -83759.5078125, 835548.25, False, "25", heli=True)
        mozdok.parking_slots[68] = ParkingSlot(68, -84032.2421875, 834076.9375, True, "01", heli=True)
        mozdok.parking_slots[69] = ParkingSlot(69, -84018.8125, 834181.0625, True, "04", heli=True)
        mozdok.parking_slots[70] = ParkingSlot(70, -83991.9609375, 834389.3125, False, "05", heli=True)
        mozdok.parking_slots[71] = ParkingSlot(71, -83985.4296875, 834443.375, False, "06", heli=True)
        mozdok.parking_slots[72] = ParkingSlot(72, -83978.53125, 834493.5, False, "07", heli=True)
        mozdok.parking_slots[73] = ParkingSlot(73, -83972.1171875, 834548.625, False, "08", heli=True)
        mozdok.parking_slots[74] = ParkingSlot(74, -83965.109375, 834597.625, False, "09", heli=True)
        mozdok.parking_slots[75] = ParkingSlot(75, -83958.8046875, 834653.875, False, "10", heli=True)
        mozdok.parking_slots[76] = ParkingSlot(76, -83951.6796875, 834701.75, False, "11", heli=True)
        mozdok.parking_slots[77] = ParkingSlot(77, -83945.4921875, 834754.125, False, "12", heli=True)
        mozdok.parking_slots[78] = ParkingSlot(78, -83938.25, 834805.875, False, "13", heli=True)
        mozdok.parking_slots[79] = ParkingSlot(79, -83933.109375, 834858.5, False, "14", heli=True)
        mozdok.parking_slots[80] = ParkingSlot(80, -83924.8203125, 834910, False, "15", heli=True)
        mozdok.parking_slots[81] = ParkingSlot(81, -83918.8671875, 834961.875, False, "16", heli=True)
        mozdok.parking_slots[82] = ParkingSlot(82, -83911.390625, 835014.1875, False, "17", heli=True)
        mozdok.parking_slots[83] = ParkingSlot(83, -83897.96875, 835118.3125, False, "18", heli=True)
        mozdok.parking_slots[84] = ParkingSlot(84, -83891.9375, 835169, False, "19", heli=True)
        mozdok.parking_slots[85] = ParkingSlot(85, -83884.5390625, 835222.4375, False, "20", heli=True)
        mozdok.parking_slots[86] = ParkingSlot(86, -83878.3125, 835277, False, "21", heli=True)
        mozdok.parking_slots[87] = ParkingSlot(87, -85118.03125, 831784.9375, False, "39", heli=True)
        mozdok.parking_slots[88] = ParkingSlot(88, -83872.03125, 835325.9375, False, "22", heli=True)
        mozdok.parking_slots[90] = ParkingSlot(90, -84058.984375, 833868.6875, True, "03", heli=True)
        mozdok.parking_slots[91] = ParkingSlot(91, -84045.5546875, 833972.875, True, "02", heli=True)
        self.airports[mozdok.name] = mozdok

        lochini = Airport(29, "Lochini", 138.0, 0, 0, None)
        lochini.runways.append(Runway(130, 110.30, 2))
        lochini.runways.append(Runway(300, 108.90, 1))
        self.airports[lochini.name] = lochini

        soganlug = Airport(30, "Soganlug", 139.0, -317838.57142857, 895424.57142858, None)
        soganlug.runways.append(Runway(130))
        soganlug.runways.append(Runway(310))
        soganlug.parking_slots[2] = ParkingSlot(2, -317118.53125, 894178.25, large=True, slot_name="05", heli=False)
        soganlug.parking_slots[8] = ParkingSlot(8, -317991.84375, 895367.25, large=True, slot_name="04", heli=False)
        soganlug.parking_slots[10] = ParkingSlot(10, -318016.28125, 895389.9375, large=False, slot_name="03", heli=True)
        soganlug.parking_slots[12] = ParkingSlot(12, -318051.78125, 895428.6875, large=True, slot_name="02", heli=False)
        soganlug.parking_slots[14] = ParkingSlot(14, -318528.5625, 895798.75, large=False, slot_name="01", heli=True)
        self.airports[soganlug.name] = soganlug

        vaziani = Airport(31, "Vaziani", 140.0, 0, 0, None)
        vaziani.runways.append(Runway(130, 108.75))
        vaziani.runways.append(Runway(310, 108.75))
        self.airports[vaziani.name] = vaziani

        beslan = Airport(32, "Beslan", 141.0, -148810.84954665, 843756.7533062, None)
        beslan.runways.append(Runway(90, 110.5))
        beslan.runways.append(Runway(270))
        beslan.parking_slots[2] = ParkingSlot(2, -148868.4375, 843496.4375, False, "02", heli=True)
        beslan.parking_slots[8] = ParkingSlot(8, -148838.5, 843498.3125, False, "01", heli=True)
        beslan.parking_slots[9] = ParkingSlot(9, -148845.28125, 843609.375, False, "04", heli=True)
        beslan.parking_slots[16] = ParkingSlot(16, -148815.34375, 843611.1875, False, "03", heli=True)
        beslan.parking_slots[20] = ParkingSlot(20, -148875.234375, 843607.5, False, "05", heli=True)
        beslan.parking_slots[42] = ParkingSlot(42, -148853.515625, 843744, False, "06", heli=True)
        beslan.parking_slots[55] = ParkingSlot(55, -148875.8125, 844108.375, True, "15", heli=True)
        beslan.parking_slots[56] = ParkingSlot(56, -148873.375, 844068.5, False, "14", heli=True)
        beslan.parking_slots[57] = ParkingSlot(57, -148870.921875, 844028.5625, True, "13", heli=True)
        beslan.parking_slots[58] = ParkingSlot(58, -148868.484375, 843988.625, False, "12", heli=True)
        beslan.parking_slots[59] = ParkingSlot(59, -148866.046875, 843948.6875, True, "11", heli=True)
        beslan.parking_slots[60] = ParkingSlot(60, -148863.59375, 843908.75, False, "10", heli=True)
        beslan.parking_slots[61] = ParkingSlot(61, -148860.84375, 843863.75, True, "09", heli=True)
        beslan.parking_slots[62] = ParkingSlot(62, -148858.421875, 843824.125, False, "08", heli=True)
        beslan.parking_slots[63] = ParkingSlot(63, -148856.03125, 843784.9375, True, "07", heli=True)
        self.airports[beslan.name] = beslan

    def airport_soganlug(self):
        return self.airports["Soganlug"]

    def airport_senaki(self):
        return self.airports["Senaki"]

    def airport_sochi(self):
        return self.airports["Sochi"]

    def airport_batumi(self):
        return self.airports["Batumi"]

    def airport_nalchik(self):
        return self.airports["Nalchik"]

    def airport_beslan(self):
        return self.airports["Beslan"]


class Nevada(Terrain):
    def __init__(self):
        super(Nevada, self).__init__("Nevada")
        # nttr center MGRS
        # 11SPE9400410022
        self.center = {"lat": 39.81806, "long": -114.73333}
        self.bullseye_blue = {"x": -409931.344, "y": -14024.097}
        self.bullseye_red = {"x": -288293.969, "y": -88022.641}
