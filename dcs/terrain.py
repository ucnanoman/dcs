# terrain module
from typing import List, Dict
from . import mapping


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
        self.runways = []  # type: List[Runway]
        self.parking_slots = {}  # type: Dict[int,ParkingSlot]
        self.unit_zones = []  # type: List[mapping.Rectangle]
        self.runway_free = True
        self.civilian = True

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

    def free_parking_slots(self, large: bool, helicopter: bool):
        slots_sorted = sorted(self.parking_slots, reverse=True)
        free_large_slots = {x for x in slots_sorted
                            if self.parking_slots[x].unit_id is None and
                            self.parking_slots[x].large}

        if large:
            if free_large_slots:
                return [self.parking_slots[x] for x in free_large_slots]
            else:
                return []

        free_heli_slots = {x for x in slots_sorted
                           if self.parking_slots[x].unit_id is None and
                           self.parking_slots[x].helicopter}
        if helicopter:
            free_slots = list(free_heli_slots) + list(free_large_slots)
            if free_slots:
                return [self.parking_slots[x] for x in free_slots]
            else:
                return []

        free_slots = [x for x in slots_sorted if self.parking_slots[x].unit_id is None] + list(free_large_slots)

        return [self.parking_slots[x] for x in free_slots]

    def free_parking_slot(self, large: bool, helicopter: bool):
        slots = self.free_parking_slots(large, helicopter)
        if slots:
            return slots[0]
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
    Center = {"lat": 45.12945, "long": 34.26527}
    Top = 337143
    Left = -557857
    Bottom = -584643
    Right = 1121943

    def __init__(self):
        super(Caucasus, self).__init__("Caucasus")
        # caucasus center MGRS
        # 36TWQ9949898109
        self.bullseye_blue = {"x": -291014, "y": 617414}
        self.bullseye_red = {"x": 11557, "y": 371700}

        anapa = Airport(12, "Anapa", 121.0, -5406.2803440839, 243127.2973737, None)
        anapa.runways.append(Runway(40))
        anapa.runways.append(Runway(220))
        anapa.parking_slots[1] = ParkingSlot(1, -5210.8227539063, 244593.3125, large=False, slot_name="91", heli=False)
        anapa.parking_slots[5] = ParkingSlot(5, -5132.0927734375, 244642.953125, large=False, slot_name="92", heli=False)
        anapa.parking_slots[7] = ParkingSlot(7, -5041.333984375, 244797.3125, large=False, slot_name="82", heli=False)
        anapa.parking_slots[9] = ParkingSlot(9, -5120.0620117188, 244747.6875, large=False, slot_name="83", heli=False)
        anapa.parking_slots[11] = ParkingSlot(11, -4928.2514648438, 244830.65625, large=False, slot_name="80", heli=False)
        anapa.parking_slots[12] = ParkingSlot(12, -4803.1616210938, 244945.359375, large=False, slot_name="77", heli=False)
        anapa.parking_slots[13] = ParkingSlot(13, -4849.3823242188, 244864.5625, large=False, slot_name="78", heli=False)
        anapa.parking_slots[15] = ParkingSlot(15, -4748.1674804688, 244814.921875, large=False, slot_name="75", heli=False)
        anapa.parking_slots[17] = ParkingSlot(17, -4788.91796875, 244331.359375, large=False, slot_name="73", heli=False)
        anapa.parking_slots[19] = ParkingSlot(19, -4934.5922851563, 244157.984375, large=False, slot_name="66", heli=False)
        anapa.parking_slots[21] = ParkingSlot(21, -4970.013671875, 244304.828125, large=False, slot_name="70", heli=False)
        anapa.parking_slots[41] = ParkingSlot(41, -4888.375, 244238.765625, large=False, slot_name="67", heli=False)
        anapa.parking_slots[44] = ParkingSlot(44, -4835.1455078125, 244250.59375, large=False, slot_name="72", heli=False)
        anapa.parking_slots[129] = ParkingSlot(129, -5913.833984375, 241692.09375, large=False, slot_name="56", heli=False)
        anapa.parking_slots[132] = ParkingSlot(132, -5783.2290039063, 241654.5625, large=False, slot_name="50", heli=False)
        anapa.parking_slots[135] = ParkingSlot(135, -5750.9443359375, 241965.640625, large=False, slot_name="53", heli=False)
        anapa.parking_slots[138] = ParkingSlot(138, -5827.509765625, 242001.28125, large=False, slot_name="62", heli=False)
        anapa.parking_slots[143] = ParkingSlot(143, -5450.2270507813, 241772.78125, large=False, slot_name="47", heli=False)
        anapa.parking_slots[146] = ParkingSlot(146, -5482.51953125, 241461.65625, large=False, slot_name="44", heli=False)
        anapa.parking_slots[149] = ParkingSlot(149, -5319.6337890625, 241735.21875, large=False, slot_name="41", heli=False)
        anapa.parking_slots[150] = ParkingSlot(150, -5693.875, 242025.953125, large=False, slot_name="59", heli=False)
        anapa.parking_slots[151] = ParkingSlot(151, -5431.3403320313, 241689.96875, large=False, slot_name="48", heli=False)
        anapa.parking_slots[152] = ParkingSlot(152, -5408.34765625, 241546.4375, large=False, slot_name="46", heli=False)
        anapa.parking_slots[153] = ParkingSlot(153, -5524.3833007813, 241687.984375, large=False, slot_name="49", heli=False)
        anapa.parking_slots[162] = ParkingSlot(162, -5709.0590820313, 241739.3125, large=False, slot_name="52", heli=False)
        anapa.parking_slots[164] = ParkingSlot(164, -4923.7856445313, 244385.59375, large=False, slot_name="69", heli=False)
        anapa.parking_slots[167] = ParkingSlot(167, -5004.4897460938, 244412.03125, large=False, slot_name="68", heli=False)
        anapa.parking_slots[168] = ParkingSlot(168, -4853.888671875, 244131.53125, large=False, slot_name="65", heli=False)
        anapa.parking_slots[169] = ParkingSlot(169, -4754.4418945313, 244224.140625, large=False, slot_name="71", heli=False)
        anapa.parking_slots[170] = ParkingSlot(170, -4713.6962890625, 244707.6875, large=False, slot_name="74", heli=False)
        anapa.parking_slots[171] = ParkingSlot(171, -4883.8500976563, 244971.8125, large=False, slot_name="76", heli=False)
        anapa.parking_slots[172] = ParkingSlot(172, -5008.9404296875, 244857.09375, large=False, slot_name="79", heli=False)
        anapa.parking_slots[173] = ParkingSlot(173, -5151.9809570313, 244532.0625, large=False, slot_name="90", heli=False)
        anapa.parking_slots[174] = ParkingSlot(174, -5326.1245117188, 244537.140625, large=False, slot_name="87", heli=False)
        anapa.parking_slots[175] = ParkingSlot(175, -5100.162109375, 244858.546875, large=False, slot_name="81", heli=False)
        anapa.parking_slots[176] = ParkingSlot(176, -5239.669921875, 244840.875, large=False, slot_name="84", heli=False)
        anapa.parking_slots[183] = ParkingSlot(183, -5207.0048828125, 244762.484375, large=False, slot_name="85", heli=False)
        anapa.parking_slots[184] = ParkingSlot(184, -5297.986328125, 244744.515625, large=False, slot_name="86", heli=False)
        anapa.parking_slots[185] = ParkingSlot(185, -5297.392578125, 242734.078125, large=False, slot_name="20", heli=True)
        anapa.parking_slots[186] = ParkingSlot(186, -5327.2578125, 242707.5, large=False, slot_name="18", heli=True)
        anapa.parking_slots[187] = ParkingSlot(187, -5342.1748046875, 242694.171875, large=False, slot_name="17", heli=True)
        anapa.parking_slots[188] = ParkingSlot(188, -5252.5966796875, 242773.984375, large=False, slot_name="23", heli=False)
        anapa.parking_slots[189] = ParkingSlot(189, -5267.5219726563, 242760.703125, large=False, slot_name="22", heli=False)
        anapa.parking_slots[190] = ParkingSlot(190, -5282.4541015625, 242747.375, large=False, slot_name="21", heli=False)
        anapa.parking_slots[191] = ParkingSlot(191, -5312.3198242188, 242720.765625, large=False, slot_name="19", heli=True)
        anapa.parking_slots[192] = ParkingSlot(192, -5237.6557617188, 242787.296875, large=False, slot_name="24", heli=False)
        anapa.parking_slots[193] = ParkingSlot(193, -5357.1171875, 242680.859375, large=False, slot_name="16", heli=True)
        anapa.parking_slots[194] = ParkingSlot(194, -5372.0551757813, 242667.578125, large=False, slot_name="15", heli=True)
        anapa.parking_slots[195] = ParkingSlot(195, -5386.9770507813, 242654.25, large=False, slot_name="14", heli=True)
        anapa.parking_slots[196] = ParkingSlot(196, -5401.9111328125, 242640.96875, large=False, slot_name="13", heli=True)
        anapa.parking_slots[197] = ParkingSlot(197, -5416.8559570313, 242627.65625, large=False, slot_name="12", heli=True)
        anapa.parking_slots[198] = ParkingSlot(198, -4894.9404296875, 243043, large=True, slot_name="27", heli=False)
        anapa.parking_slots[199] = ParkingSlot(199, -4939.7358398438, 243003.09375, large=True, slot_name="26", heli=False)
        anapa.parking_slots[200] = ParkingSlot(200, -4984.5400390625, 242963.1875, large=True, slot_name="25", heli=False)
        anapa.parking_slots[201] = ParkingSlot(201, -5359.1123046875, 244615.390625, large=False, slot_name="88", heli=False)
        anapa.parking_slots[202] = ParkingSlot(202, -5267.8071289063, 244633.515625, large=False, slot_name="89", heli=False)
        anapa.parking_slots[203] = ParkingSlot(203, -4669.0244140625, 243243.609375, large=True, slot_name="32", heli=False)
        anapa.parking_slots[204] = ParkingSlot(204, -4713.8266601563, 243203.6875, large=True, slot_name="31", heli=False)
        anapa.parking_slots[205] = ParkingSlot(205, -4758.6293945313, 243163.75, large=True, slot_name="30", heli=False)
        anapa.parking_slots[206] = ParkingSlot(206, -4803.4248046875, 243123.859375, large=True, slot_name="29", heli=False)
        anapa.parking_slots[207] = ParkingSlot(207, -4848.224609375, 243083.953125, large=True, slot_name="28", heli=False)
        anapa.parking_slots[208] = ParkingSlot(208, -4811.4125976563, 244637.4375, large=True, slot_name="40", heli=False)
        anapa.parking_slots[209] = ParkingSlot(209, -4772.6127929688, 244591.703125, large=True, slot_name="39", heli=False)
        anapa.parking_slots[210] = ParkingSlot(210, -4733.7978515625, 244545.921875, large=True, slot_name="38", heli=False)
        anapa.parking_slots[211] = ParkingSlot(211, -4617.3813476563, 244408.671875, large=True, slot_name="35", heli=False)
        anapa.parking_slots[212] = ParkingSlot(212, -4694.9990234375, 244500.171875, large=True, slot_name="37", heli=False)
        anapa.parking_slots[213] = ParkingSlot(213, -4656.1831054688, 244454.40625, large=True, slot_name="36", heli=False)
        anapa.parking_slots[214] = ParkingSlot(214, -4578.5727539063, 244362.890625, large=True, slot_name="34", heli=False)
        anapa.parking_slots[215] = ParkingSlot(215, -4539.7690429688, 244317.125, large=True, slot_name="33", heli=False)
        anapa.parking_slots[216] = ParkingSlot(216, -5798.951171875, 242110.25, large=False, slot_name="63", heli=False)
        anapa.parking_slots[217] = ParkingSlot(217, -5732.0517578125, 241882.84375, large=False, slot_name="55", heli=False)
        anapa.parking_slots[218] = ParkingSlot(218, -5839.6616210938, 241776.875, large=False, slot_name="58", heli=False)
        anapa.parking_slots[219] = ParkingSlot(219, -5932.72265625, 241774.890625, large=False, slot_name="57", heli=False)
        anapa.parking_slots[220] = ParkingSlot(220, -5825.1123046875, 241880.859375, large=False, slot_name="54", heli=False)
        anapa.parking_slots[221] = ParkingSlot(221, -5881.3588867188, 242066.9375, large=False, slot_name="64", heli=False)
        anapa.parking_slots[222] = ParkingSlot(222, -5802.1215820313, 241737.328125, large=False, slot_name="51", heli=False)
        anapa.parking_slots[223] = ParkingSlot(223, -5665.3227539063, 242134.90625, large=False, slot_name="60", heli=False)
        anapa.parking_slots[224] = ParkingSlot(224, -5747.7255859375, 242091.609375, large=False, slot_name="61", heli=False)
        anapa.parking_slots[225] = ParkingSlot(225, -5501.3950195313, 241544.453125, large=False, slot_name="45", heli=False)
        anapa.parking_slots[226] = ParkingSlot(226, -5393.787109375, 241650.421875, large=False, slot_name="43", heli=False)
        anapa.parking_slots[227] = ParkingSlot(227, -5300.724609375, 241652.40625, large=False, slot_name="42", heli=False)
        anapa.parking_slots[228] = ParkingSlot(228, -5431.810546875, 242614.359375, large=False, slot_name="11", heli=True)
        anapa.parking_slots[229] = ParkingSlot(229, -5446.7602539063, 242601.078125, large=False, slot_name="10", heli=True)
        anapa.parking_slots[230] = ParkingSlot(230, -5461.9755859375, 242587.5625, large=False, slot_name="09", heli=True)
        anapa.parking_slots[231] = ParkingSlot(231, -5476.9311523438, 242574.265625, large=False, slot_name="08", heli=True)
        anapa.parking_slots[232] = ParkingSlot(232, -5491.8818359375, 242560.984375, large=False, slot_name="07", heli=True)
        anapa.parking_slots[233] = ParkingSlot(233, -5506.8481445313, 242547.703125, large=False, slot_name="06", heli=True)
        anapa.parking_slots[234] = ParkingSlot(234, -5521.7978515625, 242534.421875, large=False, slot_name="05", heli=True)
        anapa.parking_slots[235] = ParkingSlot(235, -5536.7490234375, 242521.140625, large=False, slot_name="04", heli=True)
        anapa.parking_slots[236] = ParkingSlot(236, -5551.69921875, 242507.859375, large=False, slot_name="03", heli=True)
        anapa.parking_slots[237] = ParkingSlot(237, -5566.6494140625, 242494.578125, large=False, slot_name="02", heli=True)
        anapa.parking_slots[238] = ParkingSlot(238, -5581.6000976563, 242481.296875, large=False, slot_name="01", heli=True)
        anapa.unit_zones.append(mapping.Rectangle(-7402.857142854, 242768.57142857, -5802.857142854, 244368.57142857))
        anapa.unit_zones.append(mapping.Rectangle(-5417.1428571397, 239325.71428572, -4217.1428571397, 240525.71428572))
        anapa.unit_zones.append(mapping.Rectangle(-7159.9999999969, 239132.85714286, -5759.9999999969, 240532.85714286))
        anapa.unit_zones.append(mapping.Rectangle(-6767.1428571397, 245318.57142857, -3967.1428571397, 248118.57142857))
        self.airports[anapa.name] = anapa

        krasnodar_center = Airport(13, "Krasnodar-Center", 122.0, 11692.789495652, 367948.47230953, None)
        krasnodar_center.runways.append(Runway(80))
        krasnodar_center.runways.append(Runway(260))
        self.airports[krasnodar_center.name] = krasnodar_center

        novorossiysk = Airport(14, "Novorossiysk", 123.0, -40915.496728899, 279256.64920952, None)
        novorossiysk.runways.append(Runway(220))
        novorossiysk.runways.append(Runway(40))
        novorossiysk.parking_slots[2] = ParkingSlot(2, -41061.63671875, 278799.125, large=True, slot_name="08", heli=False)
        novorossiysk.parking_slots[4] = ParkingSlot(4, -41110.4453125, 278764.21875, large=True, slot_name="07", heli=False)
        novorossiysk.parking_slots[6] = ParkingSlot(6, -41159.2578125, 278729.28125, large=True, slot_name="06", heli=False)
        novorossiysk.parking_slots[8] = ParkingSlot(8, -41208.05859375, 278694.40625, large=True, slot_name="05", heli=False)
        novorossiysk.parking_slots[10] = ParkingSlot(10, -41256.859375, 278659.53125, large=True, slot_name="04", heli=False)
        novorossiysk.parking_slots[12] = ParkingSlot(12, -41307.6875, 278623.8125, large=True, slot_name="03", heli=False)
        novorossiysk.parking_slots[14] = ParkingSlot(14, -41356.48828125, 278588.875, large=True, slot_name="02", heli=False)
        novorossiysk.parking_slots[16] = ParkingSlot(16, -41405.296875, 278553.96875, large=True, slot_name="01", heli=False)
        novorossiysk.parking_slots[25] = ParkingSlot(25, -40107.84765625, 279575.78125, large=False, slot_name="09", heli=True)
        novorossiysk.parking_slots[26] = ParkingSlot(26, -40107.2109375, 279595.78125, large=False, slot_name="10", heli=True)
        novorossiysk.parking_slots[27] = ParkingSlot(27, -40106.53515625, 279615.75, large=False, slot_name="11", heli=True)
        novorossiysk.parking_slots[28] = ParkingSlot(28, -40105.86328125, 279635.71875, large=False, slot_name="12", heli=True)
        novorossiysk.parking_slots[29] = ParkingSlot(29, -40105.21484375, 279655.71875, large=False, slot_name="13", heli=True)
        novorossiysk.parking_slots[30] = ParkingSlot(30, -40104.5625, 279675.71875, large=False, slot_name="14", heli=True)
        novorossiysk.parking_slots[31] = ParkingSlot(31, -40103.875, 279695.6875, large=False, slot_name="15", heli=True)
        novorossiysk.parking_slots[32] = ParkingSlot(32, -40103.21875, 279715.6875, large=False, slot_name="16", heli=True)
        novorossiysk.parking_slots[37] = ParkingSlot(37, -40484.4296875, 279207.28125, large=False, slot_name="33", heli=False)
        novorossiysk.parking_slots[39] = ParkingSlot(39, -40330.08984375, 279041.5625, large=False, slot_name="37", heli=False)
        novorossiysk.parking_slots[40] = ParkingSlot(40, -40480.1875, 279024.3125, large=False, slot_name="31", heli=False)
        novorossiysk.parking_slots[44] = ParkingSlot(44, -40404.67578125, 279097.28125, large=False, slot_name="36", heli=False)
        novorossiysk.parking_slots[46] = ParkingSlot(46, -40409.90625, 279151.5625, large=False, slot_name="34", heli=False)
        novorossiysk.parking_slots[47] = ParkingSlot(47, -40294.01171875, 279118.4375, large=False, slot_name="38", heli=False)
        novorossiysk.parking_slots[48] = ParkingSlot(48, -40373.796875, 279228.4375, large=False, slot_name="35", heli=False)
        novorossiysk.parking_slots[52] = ParkingSlot(52, -40559.94140625, 279134.28125, large=False, slot_name="32", heli=False)
        novorossiysk.parking_slots[53] = ParkingSlot(53, -40670.59765625, 279113.15625, large=False, slot_name="28", heli=False)
        novorossiysk.parking_slots[55] = ParkingSlot(55, -40590.78515625, 279003.125, large=False, slot_name="29", heli=False)
        novorossiysk.parking_slots[56] = ParkingSlot(56, -40554.7109375, 279080.03125, large=False, slot_name="30", heli=False)
        novorossiysk.parking_slots[60] = ParkingSlot(60, -40769.64453125, 279003.03125, large=False, slot_name="22", heli=False)
        novorossiysk.parking_slots[62] = ParkingSlot(62, -40615.3046875, 278837.3125, large=False, slot_name="26", heli=False)
        novorossiysk.parking_slots[63] = ParkingSlot(63, -40765.40234375, 278820.0625, large=False, slot_name="21", heli=False)
        novorossiysk.parking_slots[67] = ParkingSlot(67, -40689.890625, 278893.03125, large=False, slot_name="25", heli=False)
        novorossiysk.parking_slots[69] = ParkingSlot(69, -40695.12109375, 278947.3125, large=False, slot_name="23", heli=False)
        novorossiysk.parking_slots[70] = ParkingSlot(70, -40579.2265625, 278914.1875, large=False, slot_name="27", heli=False)
        novorossiysk.parking_slots[71] = ParkingSlot(71, -40659.01171875, 279024.1875, large=False, slot_name="24", heli=False)
        novorossiysk.parking_slots[75] = ParkingSlot(75, -40845.15625, 278930.03125, large=False, slot_name="18", heli=False)
        novorossiysk.parking_slots[76] = ParkingSlot(76, -40955.8125, 278908.90625, large=False, slot_name="17", heli=False)
        novorossiysk.parking_slots[78] = ParkingSlot(78, -40876, 278798.875, large=False, slot_name="20", heli=False)
        novorossiysk.parking_slots[79] = ParkingSlot(79, -40839.92578125, 278875.78125, large=False, slot_name="19", heli=False)
        novorossiysk.unit_zones.append(mapping.Rectangle(-40122.285714285, 277836.85714285, -39022.285714285, 278936.85714285))
        novorossiysk.unit_zones.append(mapping.Rectangle(-40790.857142857, 279953.99999999, -40290.857142857, 280453.99999999))
        novorossiysk.unit_zones.append(mapping.Rectangle(-41155.142857142, 276589.71428571, -40255.142857142, 277489.71428571))
        self.airports[novorossiysk.name] = novorossiysk

        krymsk = Airport(15, "Krymsk", 124.0, -6583.663574989, 294383.98405512, None)
        krymsk.runways.append(Runway(30))
        krymsk.runways.append(Runway(210))
        self.airports[krymsk.name] = krymsk

        maykop = Airport(16, "Maykop", 125.0, -26441.347360305, 458040.61422532, None)
        maykop.runways.append(Runway(220))
        maykop.runways.append(Runway(40))
        maykop.parking_slots[16] = ParkingSlot(16, -27414.4921875, 457887.875, large=False, slot_name="16", heli=True)
        maykop.parking_slots[17] = ParkingSlot(17, -27425.181640625, 457871, large=False, slot_name="15", heli=True)
        maykop.parking_slots[18] = ParkingSlot(18, -27435.921875, 457854.09375, large=False, slot_name="14", heli=True)
        maykop.parking_slots[19] = ParkingSlot(19, -27446.619140625, 457837.25, large=False, slot_name="13", heli=True)
        maykop.parking_slots[26] = ParkingSlot(26, -27500.54296875, 457808.5, large=False, slot_name="11", heli=True)
        maykop.parking_slots[27] = ParkingSlot(27, -27579.2734375, 457794.34375, large=False, slot_name="07", heli=True)
        maykop.parking_slots[28] = ParkingSlot(28, -27480.849609375, 457812.0625, large=False, slot_name="12", heli=True)
        maykop.parking_slots[34] = ParkingSlot(34, -27946.376953125, 457556, large=True, slot_name="03", heli=False)
        maykop.parking_slots[35] = ParkingSlot(35, -27991.70703125, 457444.875, large=True, slot_name="01", heli=False)
        maykop.parking_slots[36] = ParkingSlot(36, -27520.232421875, 457804.96875, large=False, slot_name="10", heli=True)
        maykop.parking_slots[37] = ParkingSlot(37, -27969.04296875, 457500.4375, large=True, slot_name="02", heli=False)
        maykop.parking_slots[38] = ParkingSlot(38, -27923.71484375, 457611.53125, large=True, slot_name="04", heli=False)
        maykop.parking_slots[52] = ParkingSlot(52, -26534.21875, 458463.9375, large=False, slot_name="33", heli=True)
        maykop.parking_slots[53] = ParkingSlot(53, -26425.2890625, 458514.25, large=False, slot_name="39", heli=True)
        maykop.parking_slots[54] = ParkingSlot(54, -26443.4296875, 458505.875, large=False, slot_name="38", heli=True)
        maykop.parking_slots[55] = ParkingSlot(55, -26461.591796875, 458497.46875, large=False, slot_name="37", heli=True)
        maykop.parking_slots[56] = ParkingSlot(56, -26479.755859375, 458489.09375, large=False, slot_name="36", heli=True)
        maykop.parking_slots[57] = ParkingSlot(57, -26497.89453125, 458480.71875, large=False, slot_name="35", heli=True)
        maykop.parking_slots[58] = ParkingSlot(58, -26516.0546875, 458472.3125, large=False, slot_name="34", heli=True)
        maykop.parking_slots[59] = ParkingSlot(59, -26407.126953125, 458522.65625, large=False, slot_name="40", heli=True)
        maykop.parking_slots[60] = ParkingSlot(60, -26552.357421875, 458455.5625, large=False, slot_name="32", heli=True)
        maykop.parking_slots[61] = ParkingSlot(61, -26570.521484375, 458447.15625, large=False, slot_name="31", heli=True)
        maykop.parking_slots[62] = ParkingSlot(62, -26588.6875, 458438.75, large=False, slot_name="30", heli=True)
        maykop.parking_slots[63] = ParkingSlot(63, -26606.8203125, 458430.375, large=False, slot_name="29", heli=True)
        maykop.parking_slots[64] = ParkingSlot(64, -26624.990234375, 458421.96875, large=False, slot_name="28", heli=True)
        maykop.parking_slots[65] = ParkingSlot(65, -26643.146484375, 458413.59375, large=False, slot_name="27", heli=True)
        maykop.parking_slots[66] = ParkingSlot(66, -26661.28515625, 458405.21875, large=False, slot_name="26", heli=True)
        maykop.parking_slots[78] = ParkingSlot(78, -26404.630859375, 458758.59375, large=False, slot_name="46", heli=True)
        maykop.parking_slots[79] = ParkingSlot(79, -26361.634765625, 458870.625, large=False, slot_name="52", heli=True)
        maykop.parking_slots[80] = ParkingSlot(80, -26368.80078125, 458851.9375, large=False, slot_name="51", heli=True)
        maykop.parking_slots[81] = ParkingSlot(81, -26375.96875, 458833.25, large=False, slot_name="50", heli=True)
        maykop.parking_slots[82] = ParkingSlot(82, -26383.13671875, 458814.625, large=False, slot_name="49", heli=True)
        maykop.parking_slots[83] = ParkingSlot(83, -26390.3046875, 458795.9375, large=False, slot_name="48", heli=True)
        maykop.parking_slots[84] = ParkingSlot(84, -26397.470703125, 458777.28125, large=False, slot_name="47", heli=True)
        maykop.parking_slots[85] = ParkingSlot(85, -26433.294921875, 458683.90625, large=False, slot_name="42", heli=True)
        maykop.parking_slots[86] = ParkingSlot(86, -26440.4609375, 458665.25, large=False, slot_name="41", heli=True)
        maykop.parking_slots[87] = ParkingSlot(87, -27539.900390625, 457801.40625, large=False, slot_name="09", heli=True)
        maykop.parking_slots[88] = ParkingSlot(88, -27901.052734375, 457667.09375, large=True, slot_name="05", heli=False)
        maykop.parking_slots[89] = ParkingSlot(89, -27559.578125, 457797.90625, large=False, slot_name="08", heli=True)
        maykop.parking_slots[90] = ParkingSlot(90, -26426.15625, 458702.4375, large=False, slot_name="43", heli=True)
        maykop.parking_slots[92] = ParkingSlot(92, -26418.98828125, 458721.125, large=False, slot_name="44", heli=True)
        maykop.parking_slots[93] = ParkingSlot(93, -26411.8203125, 458739.75, large=False, slot_name="45", heli=True)
        maykop.parking_slots[94] = ParkingSlot(94, -27549.08984375, 457621.1875, large=True, slot_name="06", heli=False)
        maykop.parking_slots[96] = ParkingSlot(96, -27380.05078125, 458053.75, large=True, slot_name="17", heli=False)
        maykop.parking_slots[97] = ParkingSlot(97, -27105.31640625, 458037.6875, large=True, slot_name="20", heli=False)
        maykop.parking_slots[98] = ParkingSlot(98, -27307.609375, 458166.40625, large=True, slot_name="19", heli=False)
        maykop.parking_slots[99] = ParkingSlot(99, -27192.81640625, 458303.0625, large=True, slot_name="21", heli=False)
        maykop.parking_slots[100] = ParkingSlot(100, -26940.52734375, 458193.53125, large=True, slot_name="22", heli=False)
        maykop.parking_slots[101] = ParkingSlot(101, -26974.025390625, 458469.5625, large=True, slot_name="23", heli=False)
        maykop.parking_slots[102] = ParkingSlot(102, -26827.0078125, 458538.0625, large=True, slot_name="24", heli=False)
        maykop.parking_slots[103] = ParkingSlot(103, -26726.876953125, 458320.21875, large=True, slot_name="25", heli=False)
        maykop.parking_slots[105] = ParkingSlot(105, -26154.03125, 458811.5, large=True, slot_name="54", heli=False)
        maykop.parking_slots[106] = ParkingSlot(106, -26267.814453125, 459022.59375, large=True, slot_name="53", heli=False)
        maykop.parking_slots[107] = ParkingSlot(107, -26168.03125, 459077.71875, large=True, slot_name="55", heli=False)
        maykop.parking_slots[108] = ParkingSlot(108, -25954.34375, 458886.34375, large=True, slot_name="57", heli=False)
        maykop.parking_slots[110] = ParkingSlot(110, -25984.953125, 459124.1875, large=True, slot_name="56", heli=False)
        maykop.parking_slots[112] = ParkingSlot(112, -27178.244140625, 457924.375, large=True, slot_name="18", heli=False)
        maykop.unit_zones.append(mapping.Rectangle(-26574.285714285, 455938.57142857, -24574.285714285, 457938.57142857))
        maykop.unit_zones.append(mapping.Rectangle(-29088.571428571, 459010, -26888.571428571, 461210))
        maykop.unit_zones.append(mapping.Rectangle(-26717.142857142, 459945.71428572, -24917.142857142, 461745.71428572))
        maykop.unit_zones.append(mapping.Rectangle(-30738.57142857, 457451.42857144, -29138.57142857, 459051.42857144))
        self.airports[maykop.name] = maykop

        gelendzhik = Airport(17, "Gelendzhik", 126.0, -50392.648146355, 298387.43849386, None)
        gelendzhik.runways.append(Runway(220))
        gelendzhik.runways.append(Runway(40))
        gelendzhik.parking_slots[0] = ParkingSlot(0, -50007.546875, 298460.71875, large=True, slot_name="13", heli=False)
        gelendzhik.parking_slots[2] = ParkingSlot(2, -50053.63671875, 298422.3125, large=True, slot_name="12", heli=False)
        gelendzhik.parking_slots[4] = ParkingSlot(4, -50099.7421875, 298383.875, large=True, slot_name="11", heli=False)
        gelendzhik.parking_slots[6] = ParkingSlot(6, -50435.8515625, 298121.28125, large=False, slot_name="10", heli=True)
        gelendzhik.parking_slots[8] = ParkingSlot(8, -50451.4609375, 298108.21875, large=False, slot_name="09", heli=True)
        gelendzhik.parking_slots[10] = ParkingSlot(10, -50466.8046875, 298095.375, large=False, slot_name="08", heli=True)
        gelendzhik.parking_slots[12] = ParkingSlot(12, -50482.14453125, 298082.5625, large=False, slot_name="07", heli=True)
        gelendzhik.parking_slots[14] = ParkingSlot(14, -50497.5, 298069.71875, large=False, slot_name="06", heli=True)
        gelendzhik.parking_slots[16] = ParkingSlot(16, -50512.8359375, 298056.875, large=False, slot_name="05", heli=True)
        gelendzhik.parking_slots[18] = ParkingSlot(18, -50528.171875, 298044.0625, large=False, slot_name="04", heli=True)
        gelendzhik.parking_slots[20] = ParkingSlot(20, -50543.51171875, 298031.21875, large=False, slot_name="03", heli=True)
        gelendzhik.parking_slots[22] = ParkingSlot(22, -50558.84765625, 298018.375, large=False, slot_name="02", heli=True)
        gelendzhik.parking_slots[24] = ParkingSlot(24, -50574.1875, 298005.5625, large=False, slot_name="01", heli=True)
        gelendzhik.unit_zones.append(mapping.Rectangle(-50972.857142857, 296894.28571429, -50072.857142857, 297794.28571429))
        gelendzhik.unit_zones.append(mapping.Rectangle(-50135.714285714, 296528.57142857, -49435.714285714, 297228.57142857))
        gelendzhik.unit_zones.append(mapping.Rectangle(-51170, 298271.42857143, -50470, 298971.42857143))
        gelendzhik.unit_zones.append(mapping.Rectangle(-49265.714285714, 297704.28571428, -48665.714285714, 298304.28571428))
        self.airports[gelendzhik.name] = gelendzhik

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

        krasnodar_pashkovsky = Airport(19, "Krasnodar-Pashkovsky", 128.0, 7674.038444859, 385029.5736699, None)
        krasnodar_pashkovsky.runways.append(Runway(40))
        krasnodar_pashkovsky.runways.append(Runway(220))
        krasnodar_pashkovsky.parking_slots[2] = ParkingSlot(2, 8005.3208007813, 387845.03125, large=True, slot_name="09", heli=False)
        krasnodar_pashkovsky.parking_slots[4] = ParkingSlot(4, 8127.8627929688, 387976.8125, large=True, slot_name="12", heli=False)
        krasnodar_pashkovsky.parking_slots[6] = ParkingSlot(6, 8087.0170898438, 387932.84375, large=True, slot_name="11", heli=False)
        krasnodar_pashkovsky.parking_slots[8] = ParkingSlot(8, 8046.1616210938, 387888.8125, large=True, slot_name="10", heli=False)
        krasnodar_pashkovsky.parking_slots[10] = ParkingSlot(10, 7923.1420898438, 387756.90625, large=True, slot_name="07", heli=False)
        krasnodar_pashkovsky.parking_slots[24] = ParkingSlot(24, 8168.7744140625, 388020.78125, large=True, slot_name="13", heli=False)
        krasnodar_pashkovsky.parking_slots[27] = ParkingSlot(27, 6926.1547851563, 386704.40625, large=False, slot_name="02", heli=True)
        krasnodar_pashkovsky.parking_slots[29] = ParkingSlot(29, 6966.53125, 386748.78125, large=False, slot_name="03", heli=True)
        krasnodar_pashkovsky.parking_slots[31] = ParkingSlot(31, 7047.3159179688, 386837.5625, large=False, slot_name="05", heli=True)
        krasnodar_pashkovsky.parking_slots[33] = ParkingSlot(33, 7006.9116210938, 386793.125, large=False, slot_name="04", heli=True)
        krasnodar_pashkovsky.parking_slots[35] = ParkingSlot(35, 6885.4204101563, 386660.3125, large=False, slot_name="01", heli=True)
        krasnodar_pashkovsky.parking_slots[46] = ParkingSlot(46, 7087.6899414063, 386881.90625, large=False, slot_name="06", heli=True)
        krasnodar_pashkovsky.parking_slots[50] = ParkingSlot(50, 8734.8017578125, 388642.53125, large=False, slot_name="16", heli=True)
        krasnodar_pashkovsky.parking_slots[52] = ParkingSlot(52, 8775.5771484375, 388686.59375, large=False, slot_name="17", heli=True)
        krasnodar_pashkovsky.parking_slots[54] = ParkingSlot(54, 8816.3603515625, 388730.59375, large=False, slot_name="18", heli=True)
        krasnodar_pashkovsky.parking_slots[56] = ParkingSlot(56, 8857.1376953125, 388774.625, large=False, slot_name="19", heli=True)
        krasnodar_pashkovsky.parking_slots[58] = ParkingSlot(58, 8694.072265625, 388598.53125, large=False, slot_name="15", heli=True)
        krasnodar_pashkovsky.parking_slots[71] = ParkingSlot(71, 8652.9404296875, 388554.84375, large=False, slot_name="14", heli=True)
        krasnodar_pashkovsky.unit_zones.append(mapping.Rectangle(6705.7142857243, 388292.85714286, 8105.7142857243, 389692.85714286))
        krasnodar_pashkovsky.unit_zones.append(mapping.Rectangle(6184.2857142957, 384857.14285715, 7184.2857142957, 385857.14285715))
        krasnodar_pashkovsky.unit_zones.append(mapping.Rectangle(7948.571428581399, 386628.57142858, 8848.5714285814, 387528.57142858))
        krasnodar_pashkovsky.unit_zones.append(mapping.Rectangle(8570.0000000098, 383164.28571429, 9570.0000000098, 384164.28571429))
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

        gudauta = Airport(21, "Gudauta", 130.0, -196974.19851241, 516290.23098695, None)
        gudauta.runways.append(Runway(150))
        gudauta.runways.append(Runway(330))
        self.airports[gudauta.name] = gudauta

        batumi = Airport(22, "Batumi", 131.0, -355692.3067714, 617269.96285781, "16X")
        batumi.runways.append(Runway(300))
        batumi.runways.append(Runway(120, 110.3))
        batumi.parking_slots[3] = ParkingSlot(3, -355972.03125, 618122.6875, large=False, slot_name="01", heli=True)
        batumi.parking_slots[5] = ParkingSlot(5, -355984.8125, 618141.25, large=False, slot_name="02", heli=True)
        batumi.parking_slots[7] = ParkingSlot(7, -356010.375, 618177.5625, large=False, slot_name="04", heli=True)
        batumi.parking_slots[9] = ParkingSlot(9, -355997.40625, 618159.25, large=False, slot_name="03", heli=True)
        batumi.parking_slots[15] = ParkingSlot(15, -356091.65625, 618219.125, large=True, slot_name="06", heli=False)
        batumi.parking_slots[16] = ParkingSlot(16, -356059.21875, 618240.25, large=False, slot_name="05", heli=True)
        batumi.parking_slots[18] = ParkingSlot(18, -356100.46875, 618303.125, large=False, slot_name="07", heli=True)
        batumi.parking_slots[21] = ParkingSlot(21, -356140.09375, 618271.0625, large=True, slot_name="08", heli=False)
        batumi.parking_slots[23] = ParkingSlot(23, -356180.90625, 618327, large=True, slot_name="10", heli=False)
        batumi.parking_slots[24] = ParkingSlot(24, -356151.25, 618352.625, large=False, slot_name="09", heli=True)
        batumi.unit_zones.append(mapping.Rectangle(-356960, 616688.00000003, -356160, 617488.00000003))
        batumi.unit_zones.append(mapping.Rectangle(-358551.42857143, 614990.85714289, -357551.42857143, 615990.85714289))
        batumi.unit_zones.append(mapping.Rectangle(-356474.28571429, 615740.85714289, -355574.28571429, 616640.85714289))
        self.airports[batumi.name] = batumi

        senaki = Airport(23, "Senaki", 132.0, -281619.03125, 646385.625, "31X")
        senaki.runways.append(Runway(90, 108.9))
        senaki.runways.append(Runway(270))
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

        kutaisi = Airport(25, "Kutaisi", 134.0, -284889.06283057, 683853.75717885, None)
        kutaisi.runways.append(Runway(70, 109.40))
        kutaisi.runways.append(Runway(250))
        kutaisi.parking_slots[1] = ParkingSlot(1, -284388.03125, 683374.5, large=False, slot_name="01", heli=True)
        kutaisi.parking_slots[4] = ParkingSlot(4, -284599, 682349.875, large=True, slot_name="16", heli=False)
        kutaisi.parking_slots[6] = ParkingSlot(6, -286161.75, 683077.3125, large=True, slot_name="17", heli=False)
        kutaisi.parking_slots[8] = ParkingSlot(8, -285940.21875, 683041, large=True, slot_name="18", heli=False)
        kutaisi.parking_slots[10] = ParkingSlot(10, -286057.875, 682825.1875, large=True, slot_name="19", heli=False)
        kutaisi.parking_slots[12] = ParkingSlot(12, -285906.40625, 682736.6875, large=True, slot_name="20", heli=False)
        kutaisi.parking_slots[14] = ParkingSlot(14, -285759.90625, 682944.1875, large=True, slot_name="21", heli=False)
        kutaisi.parking_slots[16] = ParkingSlot(16, -284219.84375, 685068.0625, large=True, slot_name="55", heli=False)
        kutaisi.parking_slots[18] = ParkingSlot(18, -283953.65625, 685187.75, large=True, slot_name="58", heli=False)
        kutaisi.parking_slots[20] = ParkingSlot(20, -283989.9375, 684966.1875, large=True, slot_name="56", heli=False)
        kutaisi.parking_slots[22] = ParkingSlot(22, -284123.03125, 685177.5625, large=True, slot_name="57", heli=False)
        kutaisi.parking_slots[23] = ParkingSlot(23, -284379.75, 683403.3125, large=False, slot_name="02", heli=True)
        kutaisi.parking_slots[25] = ParkingSlot(25, -284371.5, 683432.1875, large=False, slot_name="03", heli=True)
        kutaisi.parking_slots[27] = ParkingSlot(27, -284363.21875, 683461, large=False, slot_name="04", heli=True)
        kutaisi.parking_slots[29] = ParkingSlot(29, -284354.96875, 683489.875, large=False, slot_name="05", heli=True)
        kutaisi.parking_slots[31] = ParkingSlot(31, -284346.6875, 683518.6875, large=False, slot_name="06", heli=True)
        kutaisi.parking_slots[33] = ParkingSlot(33, -284338.4375, 683547.5, large=False, slot_name="07", heli=True)
        kutaisi.parking_slots[35] = ParkingSlot(35, -284330.15625, 683576.375, large=False, slot_name="08", heli=True)
        kutaisi.parking_slots[37] = ParkingSlot(37, -284321.875, 683605.1875, large=False, slot_name="09", heli=True)
        kutaisi.parking_slots[39] = ParkingSlot(39, -284313.59375, 683634.0625, large=False, slot_name="10", heli=True)
        kutaisi.parking_slots[41] = ParkingSlot(41, -284305.34375, 683662.875, large=False, slot_name="11", heli=True)
        kutaisi.parking_slots[43] = ParkingSlot(43, -284297.0625, 683691.6875, large=False, slot_name="12", heli=True)
        kutaisi.parking_slots[44] = ParkingSlot(44, -284473.4375, 683648.5625, large=False, slot_name="36", heli=False)
        kutaisi.parking_slots[45] = ParkingSlot(45, -284506.53125, 683533.25, large=False, slot_name="35", heli=False)
        kutaisi.parking_slots[46] = ParkingSlot(46, -284539.59375, 683417.875, large=False, slot_name="34", heli=False)
        kutaisi.parking_slots[47] = ParkingSlot(47, -284559.3125, 682395, large=True, slot_name="15", heli=False)
        kutaisi.parking_slots[49] = ParkingSlot(49, -284519.65625, 682440, large=True, slot_name="14", heli=False)
        kutaisi.parking_slots[51] = ParkingSlot(51, -284480, 682485, large=True, slot_name="13", heli=False)
        kutaisi.parking_slots[52] = ParkingSlot(52, -284703.15625, 682692.6875, large=False, slot_name="22", heli=False)
        kutaisi.parking_slots[54] = ParkingSlot(54, -284670.0625, 682808, large=False, slot_name="24", heli=False)
        kutaisi.parking_slots[56] = ParkingSlot(56, -284637, 682923.375, large=False, slot_name="26", heli=False)
        kutaisi.parking_slots[58] = ParkingSlot(58, -284838.28125, 682980.8125, large=False, slot_name="27", heli=False)
        kutaisi.parking_slots[59] = ParkingSlot(59, -284871.375, 682865.5, large=False, slot_name="25", heli=False)
        kutaisi.parking_slots[60] = ParkingSlot(60, -284904.4375, 682750.125, large=False, slot_name="23", heli=False)
        kutaisi.parking_slots[61] = ParkingSlot(61, -284435.9375, 683201.3125, large=False, slot_name="32", heli=False)
        kutaisi.parking_slots[63] = ParkingSlot(63, -284594.96875, 683021.5625, large=False, slot_name="28", heli=False)
        kutaisi.parking_slots[65] = ParkingSlot(65, -284515.4375, 683111.4375, large=False, slot_name="30", heli=False)
        kutaisi.parking_slots[67] = ParkingSlot(67, -284672.34375, 683250, large=False, slot_name="31", heli=False)
        kutaisi.parking_slots[68] = ParkingSlot(68, -284592.84375, 683339.875, large=False, slot_name="33", heli=False)
        kutaisi.parking_slots[69] = ParkingSlot(69, -284751.875, 683160.125, large=False, slot_name="29", heli=False)
        kutaisi.parking_slots[70] = ParkingSlot(70, -284164.1875, 683969, large=False, slot_name="41", heli=False)
        kutaisi.parking_slots[72] = ParkingSlot(72, -284230.34375, 683738.3125, large=False, slot_name="37", heli=False)
        kutaisi.parking_slots[74] = ParkingSlot(74, -284197.25, 683853.625, large=False, slot_name="39", heli=False)
        kutaisi.parking_slots[76] = ParkingSlot(76, -284398.5625, 683911.125, large=False, slot_name="40", heli=False)
        kutaisi.parking_slots[77] = ParkingSlot(77, -284365.46875, 684026.4375, large=False, slot_name="42", heli=False)
        kutaisi.parking_slots[78] = ParkingSlot(78, -284431.625, 683795.75, large=False, slot_name="38", heli=False)
        kutaisi.parking_slots[79] = ParkingSlot(79, -284120.59375, 684724.3125, large=False, slot_name="53", heli=False)
        kutaisi.parking_slots[81] = ParkingSlot(81, -284186.75, 684493.625, large=False, slot_name="49", heli=False)
        kutaisi.parking_slots[83] = ParkingSlot(83, -284153.65625, 684608.9375, large=False, slot_name="51", heli=False)
        kutaisi.parking_slots[85] = ParkingSlot(85, -284354.96875, 684666.4375, large=False, slot_name="52", heli=False)
        kutaisi.parking_slots[86] = ParkingSlot(86, -284321.875, 684781.75, large=False, slot_name="54", heli=False)
        kutaisi.parking_slots[87] = ParkingSlot(87, -284388.03125, 684551.0625, large=False, slot_name="50", heli=False)
        kutaisi.parking_slots[88] = ParkingSlot(88, -284196.4375, 684391, large=False, slot_name="47", heli=False)
        kutaisi.parking_slots[90] = ParkingSlot(90, -284156.8125, 684154.3125, large=False, slot_name="43", heli=False)
        kutaisi.parking_slots[92] = ParkingSlot(92, -284176.625, 684272.6875, large=False, slot_name="45", heli=False)
        kutaisi.parking_slots[94] = ParkingSlot(94, -284383.0625, 684237.875, large=False, slot_name="46", heli=False)
        kutaisi.parking_slots[95] = ParkingSlot(95, -284402.90625, 684356.25, large=False, slot_name="48", heli=False)
        kutaisi.parking_slots[96] = ParkingSlot(96, -284363.28125, 684119.5625, large=False, slot_name="44", heli=False)
        kutaisi.unit_zones.append(mapping.Rectangle(-286691.42857142, 683870.00000001, -285691.42857142, 684870.00000001))
        kutaisi.unit_zones.append(mapping.Rectangle(-286131.42857142, 685257.14285716, -285131.42857142, 686257.14285716))
        kutaisi.unit_zones.append(mapping.Rectangle(-283762.85714285, 682065.71428573, -283062.85714285, 682765.71428573))
        kutaisi.unit_zones.append(mapping.Rectangle(-283752.85714285, 685130.00000001, -283252.85714285, 685630.00000001))
        self.airports[kutaisi.name] = kutaisi

        mineralnye = Airport(26, "Mineralnye", 135.0, -51251.551717591, 705718.47981263, None)
        mineralnye.runways.append(Runway(290))
        mineralnye.runways.append(Runway(110))
        mineralnye.parking_slots[3] = ParkingSlot(3, -51745.29296875, 705864.25, large=False, slot_name="13", heli=True)
        mineralnye.parking_slots[6] = ParkingSlot(6, -51900.9296875, 706188.875, large=True, slot_name="19", heli=False)
        mineralnye.parking_slots[8] = ParkingSlot(8, -51875.19921875, 706134.625, large=True, slot_name="18", heli=False)
        mineralnye.parking_slots[10] = ParkingSlot(10, -51849.44921875, 706080.4375, large=True, slot_name="17", heli=False)
        mineralnye.parking_slots[12] = ParkingSlot(12, -51823.73828125, 706026.25, large=True, slot_name="16", heli=False)
        mineralnye.parking_slots[14] = ParkingSlot(14, -51797.9921875, 705972, large=True, slot_name="15", heli=False)
        mineralnye.parking_slots[16] = ParkingSlot(16, -51772.23828125, 705917.875, large=True, slot_name="14", heli=False)
        mineralnye.parking_slots[18] = ParkingSlot(18, -51732.44921875, 705837.1875, large=False, slot_name="12", heli=True)
        mineralnye.parking_slots[20] = ParkingSlot(20, -51719.55078125, 705810.0625, large=False, slot_name="11", heli=True)
        mineralnye.parking_slots[22] = ParkingSlot(22, -51706.6640625, 705783, large=False, slot_name="10", heli=True)
        mineralnye.parking_slots[24] = ParkingSlot(24, -51693.83203125, 705755.875, large=False, slot_name="09", heli=True)
        mineralnye.parking_slots[26] = ParkingSlot(26, -51680.92578125, 705728.75, large=False, slot_name="08", heli=True)
        mineralnye.parking_slots[28] = ParkingSlot(28, -51668.078125, 705701.6875, large=False, slot_name="07", heli=True)
        mineralnye.parking_slots[30] = ParkingSlot(30, -51655.234375, 705674.625, large=False, slot_name="06", heli=True)
        mineralnye.parking_slots[32] = ParkingSlot(32, -51642.3515625, 705647.4375, large=False, slot_name="05", heli=True)
        mineralnye.parking_slots[34] = ParkingSlot(34, -51629.46484375, 705620.375, large=False, slot_name="04", heli=True)
        mineralnye.parking_slots[36] = ParkingSlot(36, -51616.6328125, 705593.3125, large=False, slot_name="03", heli=True)
        mineralnye.parking_slots[38] = ParkingSlot(38, -51603.75, 705566.1875, large=False, slot_name="02", heli=True)
        mineralnye.parking_slots[39] = ParkingSlot(39, -51590.890625, 705539.125, large=False, slot_name="01", heli=True)
        mineralnye.parking_slots[41] = ParkingSlot(41, -52055.375, 706514.0625, large=True, slot_name="25", heli=False)
        mineralnye.parking_slots[43] = ParkingSlot(43, -52029.640625, 706459.8125, large=True, slot_name="24", heli=False)
        mineralnye.parking_slots[45] = ParkingSlot(45, -52003.89453125, 706405.6875, large=True, slot_name="23", heli=False)
        mineralnye.parking_slots[47] = ParkingSlot(47, -51978.17578125, 706351.4375, large=True, slot_name="22", heli=False)
        mineralnye.parking_slots[49] = ParkingSlot(49, -51952.421875, 706297.1875, large=True, slot_name="21", heli=False)
        mineralnye.parking_slots[51] = ParkingSlot(51, -51926.6796875, 706243, large=True, slot_name="20", heli=False)
        mineralnye.parking_slots[53] = ParkingSlot(53, -52132.625, 706676.75, large=True, slot_name="28", heli=False)
        mineralnye.parking_slots[55] = ParkingSlot(55, -52106.890625, 706622.4375, large=True, slot_name="27", heli=False)
        mineralnye.parking_slots[57] = ParkingSlot(57, -52081.140625, 706568.375, large=True, slot_name="26", heli=False)
        mineralnye.unit_zones.append(mapping.Rectangle(-51275.714285712, 706205.71428572, -50675.714285712, 706805.71428572))
        mineralnye.unit_zones.append(mapping.Rectangle(-53002.857142855, 704720, -52302.857142855, 705420))
        mineralnye.unit_zones.append(mapping.Rectangle(-52594.285714284, 701500, -51194.285714284, 702900))
        mineralnye.unit_zones.append(mapping.Rectangle(-48849.999999998, 706642.85714286, -48049.999999998, 707442.85714286))
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
        mozdok.civilian = False
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

        lochini = Airport(29, "Lochini", 138.0, -315478.57142857, 896538.85714286, None)
        lochini.runways.append(Runway(300, 108.90, 1))
        lochini.runways.append(Runway(130, 110.30, 2))
        lochini.parking_slots[1] = ParkingSlot(1, -315166.40625, 897212.5, large=False, slot_name="36", heli=True)
        lochini.parking_slots[3] = ParkingSlot(3, -315195.96875, 897192.25, large=False, slot_name="37", heli=True)
        lochini.parking_slots[5] = ParkingSlot(5, -315225.53125, 897172, large=False, slot_name="39", heli=True)
        lochini.parking_slots[7] = ParkingSlot(7, -315255.09375, 897151.75, large=False, slot_name="38", heli=True)
        lochini.parking_slots[9] = ParkingSlot(9, -315109.90625, 897130, large=True, slot_name="31", heli=False)
        lochini.parking_slots[11] = ParkingSlot(11, -315139.46875, 897109.75, large=False, slot_name="32", heli=True)
        lochini.parking_slots[13] = ParkingSlot(13, -315169.03125, 897089.5, large=True, slot_name="34", heli=False)
        lochini.parking_slots[15] = ParkingSlot(15, -315198.59375, 897069.25, large=False, slot_name="33", heli=True)
        lochini.parking_slots[17] = ParkingSlot(17, -315228.15625, 897049, large=False, slot_name="35", heli=True)
        lochini.parking_slots[19] = ParkingSlot(19, -315053.375, 897047.5, large=True, slot_name="26", heli=False)
        lochini.parking_slots[21] = ParkingSlot(21, -315082.9375, 897027.25, large=False, slot_name="27", heli=True)
        lochini.parking_slots[23] = ParkingSlot(23, -315112.5, 897007, large=True, slot_name="29", heli=False)
        lochini.parking_slots[25] = ParkingSlot(25, -315142.0625, 896986.75, large=False, slot_name="28", heli=True)
        lochini.parking_slots[27] = ParkingSlot(27, -315171.625, 896966.5, large=False, slot_name="30", heli=True)
        lochini.parking_slots[29] = ParkingSlot(29, -314996.875, 896964.9375, large=True, slot_name="21", heli=False)
        lochini.parking_slots[31] = ParkingSlot(31, -315026.4375, 896944.6875, large=False, slot_name="22", heli=True)
        lochini.parking_slots[33] = ParkingSlot(33, -315056, 896924.4375, large=True, slot_name="24", heli=False)
        lochini.parking_slots[35] = ParkingSlot(35, -315085.5625, 896904.1875, large=False, slot_name="23", heli=True)
        lochini.parking_slots[37] = ParkingSlot(37, -315115.125, 896883.9375, large=False, slot_name="25", heli=True)
        lochini.parking_slots[39] = ParkingSlot(39, -314940.375, 896882.4375, large=True, slot_name="16", heli=False)
        lochini.parking_slots[41] = ParkingSlot(41, -314969.9375, 896862.1875, large=False, slot_name="17", heli=True)
        lochini.parking_slots[43] = ParkingSlot(43, -314999.5, 896841.9375, large=True, slot_name="19", heli=False)
        lochini.parking_slots[45] = ParkingSlot(45, -315029.0625, 896821.6875, large=False, slot_name="18", heli=True)
        lochini.parking_slots[47] = ParkingSlot(47, -315058.625, 896801.4375, large=False, slot_name="20", heli=True)
        lochini.parking_slots[49] = ParkingSlot(49, -314883.84375, 896799.9375, large=True, slot_name="11", heli=False)
        lochini.parking_slots[51] = ParkingSlot(51, -314913.40625, 896779.6875, large=False, slot_name="12", heli=True)
        lochini.parking_slots[53] = ParkingSlot(53, -314942.96875, 896759.4375, large=True, slot_name="14", heli=False)
        lochini.parking_slots[55] = ParkingSlot(55, -314972.53125, 896739.1875, large=False, slot_name="13", heli=True)
        lochini.parking_slots[57] = ParkingSlot(57, -315002.09375, 896718.9375, large=False, slot_name="15", heli=True)
        lochini.parking_slots[59] = ParkingSlot(59, -314827.34375, 896717.4375, large=True, slot_name="06", heli=False)
        lochini.parking_slots[61] = ParkingSlot(61, -314856.90625, 896697.1875, large=False, slot_name="07", heli=True)
        lochini.parking_slots[63] = ParkingSlot(63, -314886.46875, 896676.9375, large=True, slot_name="09", heli=False)
        lochini.parking_slots[65] = ParkingSlot(65, -314916.03125, 896656.6875, large=False, slot_name="08", heli=True)
        lochini.parking_slots[67] = ParkingSlot(67, -314945.59375, 896636.4375, large=False, slot_name="10", heli=True)
        lochini.parking_slots[69] = ParkingSlot(69, -314770.84375, 896635, large=True, slot_name="05", heli=False)
        lochini.parking_slots[71] = ParkingSlot(71, -314800.40625, 896614.75, large=False, slot_name="04", heli=True)
        lochini.parking_slots[73] = ParkingSlot(73, -314829.96875, 896594.5, large=True, slot_name="03", heli=False)
        lochini.parking_slots[75] = ParkingSlot(75, -314859.53125, 896574.25, large=False, slot_name="02", heli=True)
        lochini.parking_slots[78] = ParkingSlot(78, -314983.3125, 896467.0625, large=False, slot_name="44", heli=True)
        lochini.parking_slots[80] = ParkingSlot(80, -314990.90625, 896555, large=False, slot_name="42", heli=True)
        lochini.parking_slots[82] = ParkingSlot(82, -315016.125, 896539.75, large=False, slot_name="43", heli=True)
        lochini.parking_slots[88] = ParkingSlot(88, -314889.09375, 896554, large=False, slot_name="01", heli=True)
        lochini.parking_slots[108] = ParkingSlot(108, -314940.34375, 896389.9375, large=True, slot_name="46", heli=False)
        lochini.parking_slots[109] = ParkingSlot(109, -314901.03125, 896415.6875, large=False, slot_name="47", heli=True)
        lochini.parking_slots[112] = ParkingSlot(112, -315042, 896525.5, large=False, slot_name="48", heli=True)
        lochini.parking_slots[113] = ParkingSlot(113, -314713.125, 896543.9375, large=True, slot_name="51", heli=False)
        lochini.parking_slots[114] = ParkingSlot(114, -314742.71875, 896523.75, large=False, slot_name="50", heli=True)
        lochini.parking_slots[115] = ParkingSlot(115, -314772.28125, 896503.5, large=True, slot_name="49", heli=False)
        lochini.parking_slots[120] = ParkingSlot(120, -314420.96875, 895574.75, large=False, slot_name="66", heli=True)
        lochini.parking_slots[122] = ParkingSlot(122, -314394.9375, 895595.125, large=False, slot_name="65", heli=True)
        lochini.parking_slots[124] = ParkingSlot(124, -314371.6875, 895613.8125, large=False, slot_name="64", heli=True)
        lochini.parking_slots[126] = ParkingSlot(126, -314345.0625, 895634.5, large=False, slot_name="63", heli=True)
        lochini.parking_slots[128] = ParkingSlot(128, -314249.375, 895478.125, large=False, slot_name="69", heli=True)
        lochini.parking_slots[130] = ParkingSlot(130, -314326.15625, 895514.375, large=False, slot_name="68", heli=True)
        lochini.parking_slots[131] = ParkingSlot(131, -314370.125, 895537.3125, large=False, slot_name="67", heli=True)
        lochini.parking_slots[133] = ParkingSlot(133, -314324.09375, 895745.875, large=False, slot_name="70", heli=True)
        lochini.parking_slots[135] = ParkingSlot(135, -314385.09375, 895827.25, large=False, slot_name="56", heli=True)
        lochini.parking_slots[136] = ParkingSlot(136, -314301.25, 895767.9375, large=False, slot_name="71", heli=True)
        lochini.parking_slots[138] = ParkingSlot(138, -314266.40625, 895797.8125, large=False, slot_name="72", heli=True)
        lochini.parking_slots[140] = ParkingSlot(140, -314342.28125, 895862.125, large=False, slot_name="55", heli=True)
        lochini.parking_slots[142] = ParkingSlot(142, -314310.25, 895892.6875, large=False, slot_name="54", heli=True)
        lochini.parking_slots[144] = ParkingSlot(144, -314273.65625, 895919.9375, large=False, slot_name="53", heli=True)
        lochini.parking_slots[146] = ParkingSlot(146, -314242.53125, 895946.5, large=False, slot_name="73", heli=True)
        lochini.parking_slots[147] = ParkingSlot(147, -314256.84375, 896017.9375, large=False, slot_name="52", heli=True)
        lochini.parking_slots[149] = ParkingSlot(149, -314336.625, 895987.625, large=False, slot_name="74", heli=True)
        lochini.parking_slots[150] = ParkingSlot(150, -314373.125, 895962.5625, large=False, slot_name="78", heli=True)
        lochini.parking_slots[152] = ParkingSlot(152, -314404.75, 895930.1875, large=False, slot_name="77", heli=True)
        lochini.parking_slots[154] = ParkingSlot(154, -314422.5, 895756.75, large=False, slot_name="57", heli=True)
        lochini.parking_slots[156] = ParkingSlot(156, -314482.53125, 895824.4375, large=False, slot_name="58", heli=True)
        lochini.parking_slots[159] = ParkingSlot(159, -314958.96875, 896482.875, large=True, slot_name="45", heli=False)
        lochini.unit_zones.append(mapping.Rectangle(-316225.71428571, 894574.28571429, -315025.71428571, 895774.28571429))
        lochini.unit_zones.append(mapping.Rectangle(-317425.71428571, 896138.57142857, -316225.71428571, 897338.57142857))
        lochini.unit_zones.append(mapping.Rectangle(-315982.85714286, 897795.71428571, -314582.85714286, 899195.71428571))
        self.airports[lochini.name] = lochini

        soganlug = Airport(30, "Soganlug", 139.0, -317838.57142857, 895424.57142858, None)
        soganlug.runways.append(Runway(130))
        soganlug.runways.append(Runway(310))
        soganlug.parking_slots[2] = ParkingSlot(2, -317118.53125, 894178.25, large=True, slot_name="05", heli=False)
        soganlug.parking_slots[8] = ParkingSlot(8, -317991.84375, 895367.25, large=True, slot_name="04", heli=False)
        soganlug.parking_slots[10] = ParkingSlot(10, -318016.28125, 895389.9375, large=False, slot_name="03", heli=True)
        soganlug.parking_slots[12] = ParkingSlot(12, -318051.78125, 895428.6875, large=True, slot_name="02", heli=False)
        soganlug.parking_slots[14] = ParkingSlot(14, -318528.5625, 895798.75, large=False, slot_name="01", heli=True)
        soganlug.unit_zones.append(mapping.Rectangle(-318931.42857142, 894650.00000001, -318431.42857142, 895150.00000001))
        soganlug.unit_zones.append(mapping.Rectangle(-319549.99999999, 894894.28571429, -318949.99999999, 895494.28571429))
        soganlug.unit_zones.append(mapping.Rectangle(-319215.7142857, 897200.00000001, -318215.7142857, 898200.00000001))
        self.airports[soganlug.name] = soganlug

        vaziani = Airport(31, "Vaziani", 140.0, -319069.063, 903150.625, None)
        vaziani.civilian = False
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

    def airport_soganlug(self) -> Airport:
        return self.airports["Soganlug"]

    def airport_senaki(self) -> Airport:
        return self.airports["Senaki"]

    def airport_sochi(self) -> Airport:
        return self.airports["Sochi"]

    def airport_batumi(self) -> Airport:
        return self.airports["Batumi"]

    def airport_nalchik(self) -> Airport:
        return self.airports["Nalchik"]

    def airport_beslan(self) -> Airport:
        return self.airports["Beslan"]

    def airport_mozdok(self) -> Airport:
        return self.airports["Mozdok"]

    def airport_anapa(self) -> Airport:
        return self.airports["Anapa"]

    def airport_krasnodarcenter(self) -> Airport:
        return self.airports["Krasnodar-Center"]

    def airport_krasnodarpashkovsky(self) -> Airport:
        return self.airports["Krasnodar-Pashkovsky"]

    def airport_novorossiysk(self) -> Airport:
        return self.airports["Novorossiysk"]

    def airport_krymsk(self) -> Airport:
        return self.airports["Krymsk"]

    def airport_maykop(self) -> Airport:
        return self.airports["Maykop"]

    def airport_gelendzhik(self) -> Airport:
        return self.airports["Gelendzhik"]

    def airport_mineralnye(self) -> Airport:
        return self.airports["Mineralnye"]

    def airport_gudauta(self) -> Airport:
        return self.airports["Gudauta"]

    def airport_vaziani(self) -> Airport:
        return self.airports["Vaziani"]

    def airport_lochini(self) -> Airport:
        return self.airports["Lochini"]

    def airport_kobuleti(self) -> Airport:
        return self.airports["Kobuleti"]

    def airport_kutaisi(self) -> Airport:
        return self.airports["Kutaisi"]

    def default_red_airports(self) -> List[Airport]:
        return [
            self.airport_anapa(),
            self.airport_krymsk(),
            self.airport_novorossiysk(),
            self.airport_krasnodarcenter(),
            self.airport_krasnodarpashkovsky(),
            self.airport_maykop(),
            self.airport_gelendzhik(),
            self.airport_mineralnye(),
            self.airport_mozdok(),
            self.airport_beslan(),
            self.airport_nalchik(),
            self.airport_sochi()
        ]

    def default_blue_airports(self) -> List[Airport]:
        return [
            self.airport_batumi(),
            self.airport_vaziani(),
            self.airport_soganlug(),
            self.airport_kobuleti(),
            self.airport_senaki(),
            self.airport_lochini(),
            self.airport_kutaisi()
        ]


class Nevada(Terrain):
    def __init__(self):
        super(Nevada, self).__init__("Nevada")
        # nttr center MGRS
        # 11SPE9400410022
        self.center = {"lat": 39.81806, "long": -114.73333}
        self.bullseye_blue = {"x": -409931.344, "y": -14024.097}
        self.bullseye_red = {"x": -288293.969, "y": -88022.641}
