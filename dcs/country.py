from .group import VehicleGroup, PlaneGroup, StaticGroup


class Country:
    callsign = {}

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

    def find_vehicle_group(self, name: str):
        for vgroup in self.vehicle_group:
            if name in vgroup.name.str():
                return vgroup

    def find_plane_group(self, name: str):
        for group in self.plane_group:
            if name in group.name.str():
                return group

    def find_static_group(self, name: str):
        for group in self.static_group_group:
            if name in group.name.str():
                return group

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
    id = 0

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
        super(Russia, self).__init__(Russia.id, "Russia")


class Ukraine(Country):
    id = 1

    def __init__(self):
        super(Ukraine, self).__init__(Ukraine.id, "Ukraine")


class USA(Country):
    id = 2

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    callsign = {"air": [CallsignAir.Enfield,
                        CallsignAir.Springfield,
                        CallsignAir.Uzi,
                        CallsignAir.Colt,
                        CallsignAir.Dodge,
                        CallsignAir.Ford,
                        CallsignAir.Chevy,
                        CallsignAir.Pontiac]
                }

    def __init__(self):
        super(USA, self).__init__(USA.id, "USA")
        self.callsign = USA.callsign


class Turkey(Country):
    id = 3

    def __init__(self):
        super(Turkey, self).__init__(Turkey.id, "Turkey")


class UK(Country):
    id = 4

    def __init__(self):
        super(UK, self).__init__(UK.id, "UK")


class France(Country):
    id = 5

    def __init__(self):
        super(France, self).__init__(France.id, "France")


class Germany(Country):
    id = 6

    def __init__(self):
        super(Germany, self).__init__(Germany.id, "Germany")


class USAFAggressors(Country):
    id = 7

    def __init__(self):
        super(USAFAggressors, self).__init__(USAFAggressors.id, "USAF Aggressors")


class Canada(Country):
    id = 8

    def __init__(self):
        super(Canada, self).__init__(Canada.id, "Canada")


class Spain(Country):
    id = 9

    def __init__(self):
        super(Spain, self).__init__(Spain.id, "Spain")


class Netherlands(Country):
    id = 10

    def __init__(self):
        super(Netherlands, self).__init__(Netherlands.id, "Netherlands")


class Belgium(Country):
    id = 11

    def __init__(self):
        super(Belgium, self).__init__(Belgium.id, "Belgium")


class Norway(Country):
    id = 12

    def __init__(self):
        super(Norway, self).__init__(Norway.id, "Norway")


class Denmark(Country):
    id = 13

    def __init__(self):
        super(Denmark, self).__init__(Denmark.id, "Denmark")


class Israel(Country):
    id = 15

    def __init__(self):
        super(Israel, self).__init__(Israel.id, "Israel")


class Georgia(Country):
    id = 16

    def __init__(self):
        super(Georgia, self).__init__(Georgia.id, "Georgia")


class Insurgents(Country):
    id = 17

    def __init__(self):
        super(Insurgents, self).__init__(Insurgents.id, "Insurgents")


class Abkhazia(Country):
    id = 18

    def __init__(self):
        super(Abkhazia, self).__init__(Abkhazia.id, "Abkhazia")


class SouthOssetia(Country):
    id = 19

    def __init__(self):
        super(SouthOssetia, self).__init__(SouthOssetia.id, "South Ossetia")


class Italy(Country):
    id = 20

    def __init__(self):
        super(Italy, self).__init__(Italy.id, "Italy")


class Australia(Country):
    id = 21

    def __init__(self):
        super(Australia, self).__init__(Australia.id, "Australia")


class Switzerland(Country):
    id = 22

    def __init__(self):
        super(Switzerland, self).__init__(Switzerland.id, "Switzerland")


class Austria(Country):
    id = 23

    def __init__(self):
        super(Austria, self).__init__(Austria.id, "Austria")


class Belarus(Country):
    id = 24

    def __init__(self):
        super(Belarus, self).__init__(Belarus.id, "Belarus")


class Bulgaria(Country):
    id = 25

    def __init__(self):
        super(Bulgaria, self).__init__(Bulgaria.id, "Bulgaria")


class CzechRepublic(Country):
    id = 26

    def __init__(self):
        super(CzechRepublic, self).__init__(CzechRepublic.id, "Czech Republic")


class China(Country):
    id = 27

    def __init__(self):
        super(China, self).__init__(China.id, "China")


class Croatia(Country):
    id = 28

    def __init__(self):
        super(Croatia, self).__init__(Croatia.id, "Croatia")


class Egypt(Country):
    id = 29

    def __init__(self):
        super(Egypt, self).__init__(Egypt.id, "Egypt")


class Finland(Country):
    id = 30

    def __init__(self):
        super(Finland, self).__init__(Finland.id, "Finland")


class Greece(Country):
    id = 31

    def __init__(self):
        super(Greece, self).__init__(Greece.id, "Greece")


class Hungary(Country):
    id = 32

    def __init__(self):
        super(Hungary, self).__init__(Hungary.id, "Hungary")


class India(Country):
    id = 33

    def __init__(self):
        super(India, self).__init__(India.id, "India")


class Iran(Country):
    id = 34

    def __init__(self):
        super(Iran, self).__init__(Iran.id, "Iran")


class Iraq(Country):
    id = 35

    def __init__(self):
        super(Iraq, self).__init__(Iraq.id, "Iraq")


class Japan(Country):
    id = 36

    def __init__(self):
        super(Japan, self).__init__(Japan.id, "Japan")


class Kazakhstan(Country):
    id = 37

    def __init__(self):
        super(Kazakhstan, self).__init__(Kazakhstan.id, "Kazakhstan")


class NorthKorea(Country):
    id = 38

    def __init__(self):
        super(NorthKorea, self).__init__(NorthKorea.id, "North Korea")


class Pakistan(Country):
    id = 39

    def __init__(self):
        super(Pakistan, self).__init__(Pakistan.id, "Pakistan")


class Poland(Country):
    id = 40

    def __init__(self):
        super(Poland, self).__init__(Poland.id, "Poland")


class Romania(Country):
    id = 41

    def __init__(self):
        super(Romania, self).__init__(Romania.id, "Romania")


class SaudiArabia(Country):
    id = 42

    def __init__(self):
        super(SaudiArabia, self).__init__(SaudiArabia.id, "Saudi Arabia")


class Serbia(Country):
    id = 43

    def __init__(self):
        super(Serbia, self).__init__(Serbia.id, "Serbia")


class Slovakia(Country):
    id = 44

    def __init__(self):
        super(Slovakia, self).__init__(Slovakia.id, "Slovakia")


class SouthKorea(Country):
    id = 45

    def __init__(self):
        super(SouthKorea, self).__init__(SouthKorea.id, "South Korea")


class Sweden(Country):
    id = 46

    def __init__(self):
        super(Sweden, self).__init__(Sweden.id, "Sweden")


class Syria(Country):
    id = 47

    def __init__(self):
        super(Syria, self).__init__(Syria.id, "Syria")

country_dict = {
    Russia.id: Russia(),
    Ukraine.id: Ukraine(),
    USA.id: USA(),
    Turkey.id: Turkey(),
    UK.id: UK(),
    France.id: France(),
    Germany.id: Germany(),
    USAFAggressors.id: USAFAggressors(),
    Canada.id: Canada(),
    Spain.id: Spain(),
    Netherlands.id: Netherlands(),
    Belgium.id: Belgium(),
    Norway.id: Norway(),
    Denmark.id: Denmark(),
    Israel.id: Israel(),
    Georgia.id: Georgia(),
    Insurgents.id: Insurgents(),
    Abkhazia.id: Abkhazia(),
    SouthOssetia.id: SouthOssetia(),
    Italy.id: Italy(),
    Australia.id: Australia(),
    Switzerland.id: Switzerland(),
    Austria.id: Austria(),
    Belarus.id: Belarus(),
    Bulgaria.id: Bulgaria(),
    CzechRepublic.id: CzechRepublic(),
    China.id: China(),
    Croatia.id: Croatia(),
    Egypt.id: Egypt(),
    Finland.id: Finland(),
    Greece.id: Greece(),
    Hungary.id: Hungary(),
    India.id: India(),
    Iran.id: Iran(),
    Iraq.id: Iraq(),
    Japan.id: Japan(),
    Kazakhstan.id: Kazakhstan(),
    NorthKorea.id: NorthKorea(),
    Pakistan.id: Pakistan(),
    Poland.id: Poland(),
    Romania.id: Romania(),
    SaudiArabia.id: SaudiArabia(),
    Serbia.id: Serbia(),
    Slovakia.id: Slovakia(),
    SouthKorea.id: SouthKorea(),
    Sweden.id: Sweden(),
    Syria.id: Syria()
}


def get_by_id(_id: int):
    return country_dict[_id]
