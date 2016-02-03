# terrain module


class Terrain:
    def __init__(self, name: str):
        self.name = name
        self.center = {"lat": 0, "long": 0}  # WGS84 decimal
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}
        self.airports = {} # type dict[str,Airport]


class Caucasus(Terrain):
    def __init__(self):
        super(Caucasus, self).__init__("Caucasus")
        # caucasus center MGRS
        # 36TWQ9949898109
        self.center = {"lat": 45.12945, "long": 34.26527}
        self.bullseye_blue = {"x": -291014, "y": 617414}
        self.bullseye_red = {"x": 371700, "y": 11557}

        kobuleti = Airport(13, "Kobuleti", 133.0, {"x": -317874.9375, "y": 635000.375}, "67X", 111.5)
        kobuleti.parking_slots[22] = ParkingSlot(22, -317899.40625, 636670.4375, False)
        kobuleti.parking_slots[23] = ParkingSlot(23, -317680.78125, 636917.5625, False)
        kobuleti.parking_slots[24] = ParkingSlot(24, -317870.0625, 636859.8125, False)
        kobuleti.parking_slots[25] = ParkingSlot(25, -317874.9375, 635000.375, False)
        kobuleti.parking_slots[26] = ParkingSlot(26, -317740.6875, 635084.25, False)
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
        kobuleti.parking_slots[78] = ParkingSlot(78, -318102, 635959.75, False)
        kobuleti.parking_slots[80] = ParkingSlot(80, -318122.53125, 635903.375, False)
        kobuleti.parking_slots[82] = ParkingSlot(82, -318143.03125, 635847, False)
        kobuleti.parking_slots[84] = ParkingSlot(84, -318163.5625, 635790.625, False)
        kobuleti.parking_slots[85] = ParkingSlot(85, -317659.59375, 635647.0625, False)
        kobuleti.parking_slots[86] = ParkingSlot(86, -318184.09375, 635734.25, False)
        self.airports[kobuleti.name] = kobuleti

        self.airports["Batumi"] = Airport(11, "Batumi", 131.0, {"x": -293933, "y": 540000}, "16X", 110.3)


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


class Airport:
    def __init__(self, _id: int, name: str, frequency: float, pos: dict, tacan: str =None, ils=None):
        self.id = _id
        self.name = name
        self.coalition = "NEUTRAL"
        self.tacan = tacan
        self.ils = ils
        self.frequency = frequency
        self.position = pos
        self.parking_slots = {}  # type: dict[str:ParkingSlot]

    def free_parking_slot(self, plane_type):
        free_slots = [x for x in sorted(self.parking_slots) if self.parking_slots[x].unit_id is None]
        return self.parking_slots[free_slots[0]]
