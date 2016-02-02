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
        kobuleti.parking_positions[22] = {"x": -317899.40625, "y": 636670.4375}
        kobuleti.parking_positions[23] = {"x": -317680.78125, "y": 636917.5625}
        kobuleti.parking_positions[24] = {"x": -317870.0625, "y": 636859.8125}
        kobuleti.parking_positions[25] = {"x": -317874.9375, "y": 635000.375}
        kobuleti.parking_positions[26] = {"x": -317740.6875, "y": 635084.25}
        kobuleti.parking_positions[28] = {"x": -318024.84375, "y": 636164.5625}
        kobuleti.parking_positions[30] = {"x": -318097.4375, "y": 636237.875}
        kobuleti.parking_positions[31] = {"x": -318026.75, "y": 636258.8125}
        kobuleti.parking_positions[33] = {"x": -317938.25, "y": 636402.5}
        kobuleti.parking_positions[35] = {"x": -318010.84375, "y": 636475.875}
        kobuleti.parking_positions[36] = {"x": -317940.15625, "y": 636496.8125}
        kobuleti.parking_positions[37] = {"x": -317787.46875, "y": 635295.8125}
        kobuleti.parking_positions[38] = {"x": -317697.21875, "y": 635543.6875}
        kobuleti.parking_positions[39] = {"x": -317584.375, "y": 635853.8125}
        kobuleti.parking_positions[40] = {"x": -317621.96875, "y": 635750.4375}
        kobuleti.parking_positions[41] = {"x": -317471.53125, "y": 635753.3125}
        kobuleti.parking_positions[42] = {"x": -317509.15625, "y": 635649.9375}
        kobuleti.parking_positions[43] = {"x": -317546.78125, "y": 635546.5625}
        kobuleti.parking_positions[44] = {"x": -317641.71875, "y": 635285.6875}
        kobuleti.parking_positions[45] = {"x": -317584.40625, "y": 635443.1875}
        kobuleti.parking_positions[47] = {"x": -318319.71875, "y": 635219.75}
        kobuleti.parking_positions[48] = {"x": -318326.46875, "y": 635190.4375}
        kobuleti.parking_positions[53] = {"x": -318272.5, "y": 635424.3125}
        kobuleti.parking_positions[54] = {"x": -318279.21875, "y": 635395.0625}
        kobuleti.parking_positions[57] = {"x": -318286, "y": 635365.8125}
        kobuleti.parking_positions[58] = {"x": -318312.96875, "y": 635248.9375}
        kobuleti.parking_positions[60] = {"x": -318292.71875, "y": 635336.625}
        kobuleti.parking_positions[62] = {"x": -318299.46875, "y": 635307.4375}
        kobuleti.parking_positions[63] = {"x": -318306.21875, "y": 635278.125}
        kobuleti.parking_positions[66] = {"x": -318189.96875, "y": 635662.6875}
        kobuleti.parking_positions[68] = {"x": -318200.21875, "y": 635634.5}
        kobuleti.parking_positions[70] = {"x": -318210.5, "y": 635606.3125}
        kobuleti.parking_positions[72] = {"x": -318220.75, "y": 635578.125}
        kobuleti.parking_positions[74] = {"x": -318231, "y": 635549.9375}
        kobuleti.parking_positions[75] = {"x": -318241.28125, "y": 635521.75}
        kobuleti.parking_positions[76] = {"x": -318251.53125, "y": 635493.5625}
        kobuleti.parking_positions[78] = {"x": -318102, "y": 635959.75}
        kobuleti.parking_positions[80] = {"x": -318122.53125, "y": 635903.375}
        kobuleti.parking_positions[82] = {"x": -318143.03125, "y": 635847}
        kobuleti.parking_positions[84] = {"x": -318163.5625, "y": 635790.625}
        kobuleti.parking_positions[85] = {"x": -317659.59375, "y": 635647.0625}
        kobuleti.parking_positions[86] = {"x": -318184.09375, "y": 635734.25}
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


class Airport:
    def __init__(self, _id: int, name: str, frequency: float, pos: dict, tacan: str =None, ils=None):
        self.id = _id
        self.name = name
        self.tacan = tacan
        self.ils = ils
        self.frequency = frequency
        self.position = pos
        self.parking_positions = {}  # type: dict[str:dict]
