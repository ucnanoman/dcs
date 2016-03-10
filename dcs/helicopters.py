# This file is generated from pydcs_export.lua

from .weapons_data import Weapons
from . import task
from .unittype import FlyingType


class HelicopterType(FlyingType):
    helicopter = True


class Ka_50(HelicopterType):
    id = "Ka-50"
    flyable = True
    height = 5.6
    width = 14.4
    length = 15.84
    fuel_max = 1450
    max_speed = 300
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 0
    flare_charge_size = 1
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                7: 40,
                1: 21.5,
                2: 25.7,
                4: 28,
                8: 50,
                9: 55.5,
                5: 30,
                10: 59.9,
                3: 27,
                6: 32
            },
        },
        2: {
            "channels": {
                15: 0.995,
                13: 0.583,
                7: 0.443,
                1: 0.625,
                2: 0.303,
                4: 0.591,
                8: 0.215,
                16: 1.21,
                9: 0.525,
                5: 0.408,
                10: 1.065,
                14: 0.283,
                3: 0.289,
                6: 0.803,
                12: 0.35,
                11: 0.718
            },
        },
    }

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        APU_6___6_9A4172_Vikhr = (1, Weapons.APU_6___6_9A4172_Vikhr)
        Kh_25ML = (1, Weapons.Kh_25ML)
        B_8V20A___20_S_8KOM = (1, Weapons.B_8V20A___20_S_8KOM)
        B_13L___5_S_13_OF = (1, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (1, Weapons.UPK_23_250)
        KMGU_2___96_AO_2_5RT = (1, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (1, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (1, Weapons.FAB_250)
        FAB_500_M62 = (1, Weapons.FAB_500_M62)
        Fuel_tank_Ka_50 = (1, Weapons.Fuel_tank_Ka_50)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (2, Weapons.UPK_23_250)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        Fuel_tank_Ka_50 = (2, Weapons.Fuel_tank_Ka_50)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (3, Weapons.UPK_23_250)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        Fuel_tank_Ka_50 = (3, Weapons.Fuel_tank_Ka_50)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        APU_6___6_9A4172_Vikhr = (4, Weapons.APU_6___6_9A4172_Vikhr)
        Kh_25ML = (4, Weapons.Kh_25ML)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (4, Weapons.UPK_23_250)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        Fuel_tank_Ka_50 = (4, Weapons.Fuel_tank_Ka_50)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Ka_52(HelicopterType):
    id = "Ka-52"
    height = 5.6
    width = 14.4
    length = 15.84
    fuel_max = 1500
    max_speed = 300
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (1, Weapons.B_8V20A___20_S_8KOM)
        R_73 = (1, Weapons.R_73)
        APU_6___6_9A4172_Vikhr = (1, Weapons.APU_6___6_9A4172_Vikhr)
        B_13L___5_S_13_OF = (1, Weapons.B_13L___5_S_13_OF)
        KMGU_2___96_AO_2_5RT = (1, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (1, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (1, Weapons.FAB_250)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)
        Kh_25ML = (2, Weapons.Kh_25ML)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)
        Kh_25ML = (3, Weapons.Kh_25ML)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)
        APU_6___6_9A4172_Vikhr = (4, Weapons.APU_6___6_9A4172_Vikhr)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (4, Weapons.FAB_250)
        R_73 = (4, Weapons.R_73)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.PinpointStrike, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Mi_24V(HelicopterType):
    id = "Mi-24V"
    height = 4.354
    width = 17.3
    length = 20.953
    fuel_max = 1704
    max_speed = 320
    chaff = 0
    flare = 192
    charge_total = 192
    chaff_charge_size = 0
    flare_charge_size = 1

    class Pylon1:
        _9M114_Shturm_V___2 = (1, Weapons._9M114_Shturm_V___2)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        _9M114_Shturm_V___2 = (2, Weapons._9M114_Shturm_V___2)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (2, Weapons.UPK_23_250)
        Fuel_tank_Ka_50 = (2, Weapons.Fuel_tank_Ka_50)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)
        GUV_VOG = (2, Weapons.GUV_VOG)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (3, Weapons.UPK_23_250)
        Fuel_tank_Ka_50 = (3, Weapons.Fuel_tank_Ka_50)
        GUV_YakB_GSHP = (3, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (3, Weapons.GUV_VOG)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        UB_32A___32_S_5KO = (4, Weapons.UB_32A___32_S_5KO)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        B_8M1___20_S_8TsM = (4, Weapons.B_8M1___20_S_8TsM)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (4, Weapons.UPK_23_250)
        Fuel_tank_Ka_50 = (4, Weapons.Fuel_tank_Ka_50)
        GUV_YakB_GSHP = (4, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (4, Weapons.GUV_VOG)

    class Pylon5:
        B_8V20A_CM = (5, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (5, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (5, Weapons.B_8V20A_OM)
        UB_32A___32_S_5KO = (5, Weapons.UB_32A___32_S_5KO)
        _9M114_Shturm_V___2 = (5, Weapons._9M114_Shturm_V___2)
        B_8M1___20_S_8TsM = (5, Weapons.B_8M1___20_S_8TsM)
        B_13L___5_S_13_OF = (5, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (5, Weapons.UPK_23_250)
        Fuel_tank_Ka_50 = (5, Weapons.Fuel_tank_Ka_50)
        B_8V20A___20_S_8KOM = (5, Weapons.B_8V20A___20_S_8KOM)
        GUV_VOG = (5, Weapons.GUV_VOG)

    class Pylon6:
        _9M114_Shturm_V___2 = (6, Weapons._9M114_Shturm_V___2)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.Transport, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Mi_8MT(HelicopterType):
    id = "Mi-8MT"
    flyable = True
    large_parking_slot = True
    height = 4.908
    width = 21.33
    length = 25.942
    fuel_max = 1929
    max_speed = 250
    chaff = 0
    flare = 192
    charge_total = 192
    chaff_charge_size = 0
    flare_charge_size = 1

    panel_radio = {
        1: {
            "channels": {
                1: 127.5,
                2: 135,
                4: 127,
                8: 128,
                16: 132,
                17: 138,
                9: 126,
                18: 122,
                5: 125,
                10: 133,
                20: 137,
                11: 130,
                3: 136,
                6: 121,
                12: 129,
                13: 123,
                7: 141,
                14: 131,
                19: 124,
                15: 134
            },
        },
        2: {
            "channels": {
                7: 40,
                1: 21.5,
                2: 25.7,
                4: 28,
                8: 50,
                9: 55.5,
                5: 30,
                10: 59.9,
                3: 27,
                6: 32
            },
        },
    }

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A___20_S_8KOM = (1, Weapons.B_8V20A___20_S_8KOM)
        FAB_100 = (1, Weapons.FAB_100)
        SAB_100 = (1, Weapons.SAB_100)
        FAB_250 = (1, Weapons.FAB_250)
        GUV_VOG = (1, Weapons.GUV_VOG)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        UPK_23_250 = (2, Weapons.UPK_23_250)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        GUV_YakB_GSHP = (2, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (2, Weapons.GUV_VOG)
        FAB_100 = (2, Weapons.FAB_100)
        SAB_100 = (2, Weapons.SAB_100)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_100 = (4, Weapons.FAB_100)
        SAB_100 = (4, Weapons.SAB_100)

    class Pylon5:
        B_8V20A_CM = (5, Weapons.B_8V20A_CM)
        B_8V20A_OM = (5, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (5, Weapons.B_8V20A_OFP2)
        UPK_23_250 = (5, Weapons.UPK_23_250)
        B_8V20A___20_S_8KOM = (5, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (5, Weapons.FAB_250)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        GUV_YakB_GSHP = (5, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (5, Weapons.GUV_VOG)
        FAB_100 = (5, Weapons.FAB_100)
        SAB_100 = (5, Weapons.SAB_100)

    class Pylon6:
        B_8V20A_CM = (6, Weapons.B_8V20A_CM)
        B_8V20A_OM = (6, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (6, Weapons.B_8V20A_OFP2)
        B_8V20A___20_S_8KOM = (6, Weapons.B_8V20A___20_S_8KOM)
        FAB_100 = (6, Weapons.FAB_100)
        SAB_100 = (6, Weapons.SAB_100)
        FAB_250 = (6, Weapons.FAB_250)
        GUV_VOG = (6, Weapons.GUV_VOG)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.Transport, task.AFAC, task.AntishipStrike]
    task_default = task.Transport


class Mi_26(HelicopterType):
    id = "Mi-26"
    group_size_max = 1
    large_parking_slot = True
    height = 12.9
    width = 32
    length = 40.854
    fuel_max = 9600
    max_speed = 300
    chaff = 0
    flare = 192
    charge_total = 192
    chaff_charge_size = 0
    flare_charge_size = 1

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class Ka_27(HelicopterType):
    id = "Ka-27"
    height = 5.2
    width = 15.9
    length = 15.92
    fuel_max = 2616
    max_speed = 290

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class UH_60A(HelicopterType):
    id = "UH-60A"
    height = 4.893
    width = 16.4
    length = 18.654
    fuel_max = 1100
    max_speed = 300
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class CH_53E(HelicopterType):
    id = "CH-53E"
    large_parking_slot = True
    height = 7.83
    width = 24.08
    length = 30.18
    fuel_max = 1908
    max_speed = 310
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class CH_47D(HelicopterType):
    id = "CH-47D"
    large_parking_slot = True
    height = 5.998
    width = 18.3
    length = 28.3
    fuel_max = 3600
    max_speed = 300
    chaff = 120
    flare = 120
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class SH_3W(HelicopterType):
    id = "SH-3W"
    large_parking_slot = True
    height = 6.807
    width = 18.91
    length = 30.207
    fuel_max = 2132
    max_speed = 270
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class AH_64A(HelicopterType):
    id = "AH-64A"
    height = 4.15
    width = 14.63
    length = 17.87
    fuel_max = 1157
    max_speed = 300
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        AGM_114K___4 = (1, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon2:
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (2, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        AGM_114K___4 = (2, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon3:
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (3, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        AGM_114K___4 = (3, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon4:
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        AGM_114K___4 = (4, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class AH_64D(HelicopterType):
    id = "AH-64D"
    height = 4.15
    width = 14.63
    length = 17.87
    fuel_max = 1157
    max_speed = 280
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        AGM_114K___4 = (1, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon2:
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (2, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        AGM_114K___4 = (2, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon3:
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (3, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        AGM_114K___4 = (3, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon4:
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        AGM_114K___4 = (4, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class AH_1W(HelicopterType):
    id = "AH-1W"
    height = 3.9
    width = 14.64
    length = 17.27
    fuel_max = 1250.0
    max_speed = 290
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        AGM_114K___4 = (1, Weapons.AGM_114K___4)
        BGM_71D_Tow___4 = (1, Weapons.BGM_71D_Tow___4)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        M260_HYDRA = (1, Weapons.M260_HYDRA)

    class Pylon2:
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        M260_HYDRA = (2, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (2, Weapons.M260_HYDRA_WP)
        LAU_61___19_2_75__rockets_MK156_WP = (2, Weapons.LAU_61___19_2_75__rockets_MK156_WP)

    class Pylon3:
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        M260_HYDRA = (3, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (3, Weapons.M260_HYDRA_WP)
        LAU_61___19_2_75__rockets_MK156_WP = (3, Weapons.LAU_61___19_2_75__rockets_MK156_WP)

    class Pylon4:
        AGM_114K___4 = (4, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        M260_HYDRA = (4, Weapons.M260_HYDRA)
        BGM_71D_Tow___4 = (4, Weapons.BGM_71D_Tow___4)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class SH_60B(HelicopterType):
    id = "SH-60B"
    height = 4.893
    width = 16.4
    length = 18.654
    fuel_max = 1100
    max_speed = 240
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        AGM_119B_Penguin = (1, Weapons.AGM_119B_Penguin)

    pylons = {1}

    tasks = [task.AntishipStrike, task.Transport]
    task_default = task.Transport


class UH_1H(HelicopterType):
    id = "UH-1H"
    flyable = True
    height = 4.41
    width = 14.7
    length = 17.62
    fuel_max = 631
    max_speed = 200
    chaff = 0
    flare = 60
    charge_total = 60
    chaff_charge_size = 0
    flare_charge_size = 1
    radio_frequency = 251

    panel_radio = {
        1: {
            "channels": {
                1: 251,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    class Pylon1:
        M134_L = (1, Weapons.M134_L)

    class Pylon2:
        XM158_MK1 = (2, Weapons.XM158_MK1)
        XM158_MK5 = (2, Weapons.XM158_MK5)
        XM158_M151 = (2, Weapons.XM158_M151)
        XM158_M156 = (2, Weapons.XM158_M156)
        XM158_M274 = (2, Weapons.XM158_M274)
        XM158_M257 = (2, Weapons.XM158_M257)
        M261_MK151 = (2, Weapons.M261_MK151)
        M261_MK156 = (2, Weapons.M261_MK156)

    class Pylon3:
        M134_SIDE_L = (3, Weapons.M134_SIDE_L)
        M60_SIDE_L = (3, Weapons.M60_SIDE_L)

    class Pylon4:
        M134_SIDE_R = (4, Weapons.M134_SIDE_R)
        M60_SIDE_R = (4, Weapons.M60_SIDE_R)

    class Pylon5:
        XM158_MK1 = (5, Weapons.XM158_MK1)
        XM158_MK5 = (5, Weapons.XM158_MK5)
        XM158_M151 = (5, Weapons.XM158_M151)
        XM158_M156 = (5, Weapons.XM158_M156)
        XM158_M274 = (5, Weapons.XM158_M274)
        XM158_M257 = (5, Weapons.XM158_M257)
        M261_MK151 = (5, Weapons.M261_MK151)
        M261_MK156 = (5, Weapons.M261_MK156)

    class Pylon6:
        M134_R = (6, Weapons.M134_R)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.Transport]
    task_default = task.Transport


class Mi_28N(HelicopterType):
    id = "Mi-28N"
    height = 5.087
    width = 17.2
    length = 17.87
    fuel_max = 1500
    max_speed = 305
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 0
    flare_charge_size = 1

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        _9M114_Shturm_V_x_8 = (1, Weapons._9M114_Shturm_V_x_8)
        B_8V20A___20_S_8KOM = (1, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (1, Weapons.FAB_250)
        KMGU_2___96_AO_2_5RT = (1, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (1, Weapons.B_13L___5_S_13_OF)
        Fuel_tank_Ka_50 = (1, Weapons.Fuel_tank_Ka_50)
        B_8M1___20_S_8TsM = (1, Weapons.B_8M1___20_S_8TsM)
        FAB_500_M62 = (1, Weapons.FAB_500_M62)
        UPK_23_250 = (1, Weapons.UPK_23_250)
        KMGU_2___96_PTAB_2_5KO = (1, Weapons.KMGU_2___96_PTAB_2_5KO)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        FAB_250 = (2, Weapons.FAB_250)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        Fuel_tank_Ka_50 = (2, Weapons.Fuel_tank_Ka_50)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        UPK_23_250 = (2, Weapons.UPK_23_250)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        FAB_250 = (3, Weapons.FAB_250)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        Fuel_tank_Ka_50 = (3, Weapons.Fuel_tank_Ka_50)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        UPK_23_250 = (3, Weapons.UPK_23_250)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        FAB_250 = (4, Weapons.FAB_250)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        Fuel_tank_Ka_50 = (4, Weapons.Fuel_tank_Ka_50)
        B_8M1___20_S_8TsM = (4, Weapons.B_8M1___20_S_8TsM)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        UPK_23_250 = (4, Weapons.UPK_23_250)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        _9M114_Shturm_V_x_8 = (4, Weapons._9M114_Shturm_V_x_8)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class OH_58D(HelicopterType):
    id = "OH-58D"
    height = 2.29
    width = 10.53
    length = 10.48
    fuel_max = 1100
    max_speed = 220
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        M260_HYDRA = (1, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (1, Weapons.M260_HYDRA_WP)
        AGM114x2_OH_58 = (1, Weapons.AGM114x2_OH_58)
        oh_58_brauning = (1, Weapons.oh_58_brauning)

    class Pylon2:
        M260_HYDRA_WP = (2, Weapons.M260_HYDRA_WP)
        M260_HYDRA = (2, Weapons.M260_HYDRA)
        AGM114x2_OH_58 = (2, Weapons.AGM114x2_OH_58)

    pylons = {1, 2}

    tasks = [task.AFAC, task.Transport, task.GroundAttack, task.Escort, task.AntishipStrike]
    task_default = task.AFAC


helicopter_map = {
    "Ka-50": Ka_50,
    "Ka-52": Ka_52,
    "Mi-24V": Mi_24V,
    "Mi-8MT": Mi_8MT,
    "Mi-26": Mi_26,
    "Ka-27": Ka_27,
    "UH-60A": UH_60A,
    "CH-53E": CH_53E,
    "CH-47D": CH_47D,
    "SH-3W": SH_3W,
    "AH-64A": AH_64A,
    "AH-64D": AH_64D,
    "AH-1W": AH_1W,
    "SH-60B": SH_60B,
    "UH-1H": UH_1H,
    "Mi-28N": Mi_28N,
    "OH-58D": OH_58D,
}
