from .group import VehicleGroup, PlaneGroup, StaticGroup


class Country:
    def __init__(self, _id, name):
        self.id = _id
        self.name = name
        self.vehicle_group = []  # type: list[VehicleGroup]
        self.plane_group = []  # type: list[PlaneGroup]
        self.static_group = []  # type: list[StaticGroup]

    def name(self):
        return self.name

    def add_vehicle_group(self, vgroup):
        self.vehicle_group.append(vgroup)

    def add_plane_group(self, pgroup):
        self.plane_group.append(pgroup)

    def add_static_group(self, sgroup):
        self.static_group.append(sgroup)

    def dict(self):
        d = {}
        d["name"] = self.name
        d["id"] = self.id

        if self.vehicle_group:
            d["vehicle"] = {"group": {}}
            i = 1
            for vgroup in self.vehicle_group:
                d["vehicle"]["group"][i] = vgroup.dict()
                i += 1
        if self.plane_group:
            d["plane"] = {"group": {}}
            i = 1
            for plane_group in self.plane_group:
                d["plane"]["group"][i] = plane_group.dict()
                i += 1

        if self.static_group:
            d["static"] = {"group": {}}
            i = 1
            for static_group in self.static_group:
                d["static"]["group"][i] = static_group.dict()
                i += 1
        return d

    def __str__(self):
        return str(self.id) + "," + self.name + "," + str(self.vehicle_group)


class Russia(Country):
    Vehicle_BTR80 = "BTR-80"
    Vehicle_1L13EWR = "1L13 EWR"
    Vehicle_55G6EWR = "55G6 EWR"
    Vehicle_S300PS40B6Mtr = "S-300PS 40B6M tr"
    Vehicle_S300PS40B6MDsr = "S-300PS 40B6MD sr"
    Vehicle_S300PS64H6Esr = "S-300PS 64H6E sr"
    Vehicle_S300PS5P85Cln = "S-300PS 5P85C ln"
    Vehicle_S300PS5P85Dln = "S-300PS 5P85D ln"
    Vehicle_SA11BukSR9S18M1 = "SA-11 Buk SR 9S18M1"
    Vehicle_SA11BukCC9S470M1 = "SA-11 Buk CC 9S470M1"
    Vehicle_SA11BukLN9A310M1 = "SA-11 Buk LN 9A310M1"
    Vehicle_Kub1S91str = "Kub 1S91 str"
    Vehicle_Kub2P25ln = "Kub 2P25 ln"
    Vehicle_Osa9A33ln = "Osa 9A33 ln"
    Vehicle_Strela19P31 = "Strela-1 9P31"
    Vehicle_Strela10M3 = "Strela-10M3"
    Vehicle_DogEarradar = "Dog Ear radar"
    Vehicle_Tor9A331 = "Tor 9A331"
    Vehicle_2S6Tunguska = "2S6 Tunguska"
    Vehicle_ZSU234Shilka = "ZSU-23-4 Shilka"
    Vehicle_SAUMsta = "SAU Msta"
    Vehicle_SAUAkatsia = "SAU Akatsia"
    Vehicle_SAU2C9 = "SAU 2-C9"
    Vehicle_ATMZ5 = "ATMZ-5"
    Vehicle_ATZ10 = "ATZ-10"
    Vehicle_BMD1 = "BMD-1"
    Vehicle_BMP1 = "BMP-1"
    Vehicle_BMP2 = "BMP-2"
    Vehicle_BRDM2 = "BRDM-2"
    Vehicle_GradURAL = "Grad-URAL"
    Vehicle_Uragan_BM27 = "Uragan_BM-27"
    Vehicle_Smerch = "Smerch"
    Vehicle_T80UD = "T-80UD"
    Vehicle_UAZ469 = "UAZ-469"
    Vehicle_Ural375 = "Ural-375"
    Vehicle_Ural375PBU = "Ural-375 PBU"
    Vehicle_IKARUSBus = "IKARUS Bus"
    Vehicle_VAZCar = "VAZ Car"
    Vehicle_Trolleybus = "Trolley bus"
    Vehicle_KAMAZTruck = "KAMAZ Truck"
    Vehicle_LAZBus = "LAZ Bus"
    Vehicle_SAUGvozdika = "SAU Gvozdika"
    Vehicle_BMP3 = "BMP-3"
    Vehicle_BTR_D = "BTR_D"
    Vehicle_S300PS54K6cp = "S-300PS 54K6 cp"
    Vehicle_GAZ3307 = "GAZ-3307"
    Vehicle_GAZ66 = "GAZ-66"
    Vehicle_GAZ3308 = "GAZ-3308"
    Vehicle_MAZ6303 = "MAZ-6303"
    Vehicle_ZIL4331 = "ZIL-4331"
    Vehicle_SKP11 = "SKP-11"
    Vehicle_Ural4320T = "Ural-4320T"
    Vehicle_Ural432031 = "Ural-4320-31"
    Vehicle_UralATsP6 = "Ural ATsP-6"
    Vehicle_ZiL131APA80 = "ZiL-131 APA-80"
    Vehicle_ZIL131KUNG = "ZIL-131 KUNG"
    Vehicle_Ural4320APA5D = "Ural-4320 APA-5D"
    Vehicle_ZU23Emplacement = "ZU-23 Emplacement"
    Vehicle_ZU23EmplacementClosed = "ZU-23 Emplacement Closed"
    Vehicle_Ural375ZU23 = "Ural-375 ZU-23"
    Vehicle_MTLB = "MTLB"
    Vehicle_T72B = "T-72B"
    Vehicle_SA18IglaSmanpad = "SA-18 Igla-S manpad"
    Vehicle_SA18IglaScomm = "SA-18 Igla-S comm"
    Vehicle_T55 = "T-55"
    Vehicle_ParatrooperRPG16 = "Paratrooper RPG-16"
    Vehicle_ParatrooperAKS74 = "Paratrooper AKS-74"
    Vehicle_Boman = "Boman"
    Vehicle_2B11mortar = "2B11 mortar"
    Vehicle_5p73s125ln = "5p73 s-125 ln"
    Vehicle_snrs125tr = "snr s-125 tr"
    Vehicle_p19s125sr = "p-19 s-125 sr"
    Vehicle_InfantryAK = "Infantry AK"
    Vehicle_T90 = "T-90"
    Vehicle_Tigr_233036 = "Tigr_233036"

    def __init__(self):
        super(Russia, self).__init__(0, "Russia")


class Ukraine(Country):
    def __init__(self):
        super(Ukraine, self).__init__(1, "Ukraine")


class USA(Country):
    def __init__(self):
        super(USA, self).__init__(2, "USA")


class Turkey(Country):
    def __init__(self):
        super(Turkey, self).__init__(3, "Turkey")


class UK(Country):
    def __init__(self):
        super(UK, self).__init__(4, "UK")


class France(Country):
    def __init__(self):
        super(France, self).__init__(5, "France")


class Germany(Country):
    def __init__(self):
        super(Germany, self).__init__(6, "Germany")


class USAFAggressors(Country):
    def __init__(self):
        super(USAFAggressors, self).__init__(7, "USAF Aggressors")


class Canada(Country):
    def __init__(self):
        super(Canada, self).__init__(8, "Canada")


class Spain(Country):
    def __init__(self):
        super(Spain, self).__init__(9, "Spain")


class Netherlands(Country):
    def __init__(self):
        super(Netherlands, self).__init__(10, "Netherlands")


class Belgium(Country):
    def __init__(self):
        super(Belgium, self).__init__(11, "Belgium")


class Norway(Country):
    def __init__(self):
        super(Norway, self).__init__(12, "Norway")


class Denmark(Country):
    def __init__(self):
        super(Denmark, self).__init__(13, "Denmark")


class Israel(Country):
    def __init__(self):
        super(Israel, self).__init__(15, "Israel")


class Georgia(Country):
    def __init__(self):
        super(Georgia, self).__init__(16, "Georgia")


class Insurgents(Country):
    def __init__(self):
        super(Insurgents, self).__init__(17, "Insurgents")


class Abkhazia(Country):
    def __init__(self):
        super(Abkhazia, self).__init__(18, "Abkhazia")


class SouthOssetia(Country):
    def __init__(self):
        super(SouthOssetia, self).__init__(19, "South Ossetia")


class Italy(Country):
    def __init__(self):
        super(Italy, self).__init__(20, "Italy")


class Australia(Country):
    def __init__(self):
        super(Australia, self).__init__(21, "Australia")


class Switzerland(Country):
    def __init__(self):
        super(Switzerland, self).__init__(22, "Switzerland")


class Austria(Country):
    def __init__(self):
        super(Austria, self).__init__(23, "Austria")


class Belarus(Country):
    def __init__(self):
        super(Belarus, self).__init__(24, "Belarus")


class Bulgaria(Country):
    def __init__(self):
        super(Bulgaria, self).__init__(25, "Bulgaria")


class CzechRepublic(Country):
    def __init__(self):
        super(CzechRepublic, self).__init__(26, "Czech Republic")


class China(Country):
    def __init__(self):
        super(China, self).__init__(27, "China")


class Croatia(Country):
    def __init__(self):
        super(Croatia, self).__init__(28, "Croatia")


class Egypt(Country):
    def __init__(self):
        super(Egypt, self).__init__(29, "Egypt")


class Finland(Country):
    def __init__(self):
        super(Finland, self).__init__(30, "Finland")


class Greece(Country):
    def __init__(self):
        super(Greece, self).__init__(31, "Greece")


class Hungary(Country):
    def __init__(self):
        super(Hungary, self).__init__(32, "Hungary")


class India(Country):
    def __init__(self):
        super(India, self).__init__(33, "India")


class Iran(Country):
    def __init__(self):
        super(Iran, self).__init__(34, "Iran")


class Iraq(Country):
    def __init__(self):
        super(Iraq, self).__init__(35, "Iraq")


class Japan(Country):
    def __init__(self):
        super(Japan, self).__init__(36, "Japan")


class Kazakhstan(Country):
    def __init__(self):
        super(Kazakhstan, self).__init__(37, "Kazakhstan")


class NorthKorea(Country):
    def __init__(self):
        super(NorthKorea, self).__init__(38, "North Korea")


class Pakistan(Country):
    def __init__(self):
        super(Pakistan, self).__init__(39, "Pakistan")


class Poland(Country):
    def __init__(self):
        super(Poland, self).__init__(40, "Poland")


class Romania(Country):
    def __init__(self):
        super(Romania, self).__init__(41, "Romania")


class SaudiArabia(Country):
    def __init__(self):
        super(SaudiArabia, self).__init__(42, "Saudi Arabia")


class Serbia(Country):
    def __init__(self):
        super(Serbia, self).__init__(43, "Serbia")


class Slovakia(Country):
    def __init__(self):
        super(Slovakia, self).__init__(44, "Slovakia")


class SouthKorea(Country):
    def __init__(self):
        super(SouthKorea, self).__init__(45, "South Korea")


class Sweden(Country):
    def __init__(self):
        super(Sweden, self).__init__(46, "Sweden")


class Syria(Country):
    def __init__(self):
        super(Syria, self).__init__(47, "Syria")
