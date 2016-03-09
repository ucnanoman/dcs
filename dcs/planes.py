# This file is generated from pydcs_export.lua

from .weapons_data import Weapons
from . import task
from .flyingtype import FlyingType


class PlaneType(FlyingType):
    pass


class Tornado_GR4(PlaneType):
    id = "Tornado GR4"
    height = 5.7
    width = 13.91
    length = 16.7
    fuel_max = 4663
    max_speed = 2340
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        BOZ_107 = (1, Weapons.BOZ_107)
        Sky_Shadow_ECM_Pod = (1, Weapons.Sky_Shadow_ECM_Pod)

    class Pylon2:
        TORNADO_Fuel_tank = (2, Weapons.TORNADO_Fuel_tank)

    class Pylon3:
        AIM_9M = (3, Weapons.AIM_9M)
        ALARM = (3, Weapons.ALARM)
        AN_ASQ_T50_TCTS_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon4:
        GBU_16 = (4, Weapons.GBU_16)
        ALARM = (4, Weapons.ALARM)
        Sea_Eagle = (4, Weapons.Sea_Eagle)
        GBU_27 = (4, Weapons.GBU_27)

    class Pylon5:
        GBU_12 = (5, Weapons.GBU_12)
        AN_AAQ_28_LITENING = (5, Weapons.AN_AAQ_28_LITENING)

    class Pylon6:
        GBU_12 = (6, Weapons.GBU_12)

    class Pylon7:
        GBU_12 = (7, Weapons.GBU_12)

    class Pylon8:
        GBU_12 = (8, Weapons.GBU_12)

    class Pylon9:
        GBU_16 = (9, Weapons.GBU_16)
        ALARM = (9, Weapons.ALARM)
        Sea_Eagle = (9, Weapons.Sea_Eagle)
        GBU_27 = (9, Weapons.GBU_27)

    class Pylon10:
        AIM_9M = (10, Weapons.AIM_9M)
        ALARM = (10, Weapons.ALARM)
        AN_ASQ_T50_TCTS_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon11:
        TORNADO_Fuel_tank = (11, Weapons.TORNADO_Fuel_tank)

    class Pylon12:
        BOZ_107 = (12, Weapons.BOZ_107)
        Sky_Shadow_ECM_Pod = (12, Weapons.Sky_Shadow_ECM_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.PinpointStrike, task.GroundAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.GroundAttack


class Tornado_IDS(PlaneType):
    id = "Tornado IDS"
    height = 5.7
    width = 13.91
    length = 16.7
    fuel_max = 4663
    max_speed = 2340
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        BOZ_107 = (1, Weapons.BOZ_107)
        Sky_Shadow_ECM_Pod = (1, Weapons.Sky_Shadow_ECM_Pod)

    class Pylon2:
        AGM_88C_ = (2, Weapons.AGM_88C_)
        Kormoran = (2, Weapons.Kormoran)
        TORNADO_Fuel_tank = (2, Weapons.TORNADO_Fuel_tank)

    class Pylon3:
        AIM_9M = (3, Weapons.AIM_9M)
        AN_ASQ_T50_TCTS_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon4:
        GBU_16 = (4, Weapons.GBU_16)
        AGM_88C_ = (4, Weapons.AGM_88C_)
        Kormoran = (4, Weapons.Kormoran)

    class Pylon5:
        Mk_82 = (5, Weapons.Mk_82)

    class Pylon6:
        Mk_82 = (6, Weapons.Mk_82)

    class Pylon7:
        Mk_82 = (7, Weapons.Mk_82)

    class Pylon8:
        Mk_82 = (8, Weapons.Mk_82)

    class Pylon9:
        GBU_16 = (9, Weapons.GBU_16)
        AGM_88C_ = (9, Weapons.AGM_88C_)
        Kormoran = (9, Weapons.Kormoran)

    class Pylon10:
        AIM_9M = (10, Weapons.AIM_9M)
        AN_ASQ_T50_TCTS_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon11:
        AGM_88C_ = (11, Weapons.AGM_88C_)
        Kormoran = (11, Weapons.Kormoran)
        TORNADO_Fuel_tank = (11, Weapons.TORNADO_Fuel_tank)

    class Pylon12:
        BOZ_107 = (12, Weapons.BOZ_107)
        Sky_Shadow_ECM_Pod = (12, Weapons.Sky_Shadow_ECM_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.PinpointStrike, task.GroundAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.GroundAttack


class F_A_18A(PlaneType):
    id = "F/A-18A"
    height = 4.66
    width = 11.43
    length = 17.07
    fuel_max = 6531
    max_speed = 1920
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_9M = (1, Weapons.AIM_9M)
        AIM_9P = (1, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        AIM_7M = (2, Weapons.AIM_7M)
        AIM_9M = (2, Weapons.AIM_9M)
        AIM_9P = (2, Weapons.AIM_9P)
        LAU_10___4_ZUNI_MK_71 = (2, Weapons.LAU_10___4_ZUNI_MK_71)
        AGM_84A = (2, Weapons.AGM_84A)
        AGM_88C_ = (2, Weapons.AGM_88C_)
        LAU_117_AGM_65D = (2, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65K = (2, Weapons.LAU_117_AGM_65K)
        LAU_117_AGM_65E = (2, Weapons.LAU_117_AGM_65E)
        GBU_10 = (2, Weapons.GBU_10)
        GBU_12 = (2, Weapons.GBU_12)
        GBU_16 = (2, Weapons.GBU_16)
        MER_2_MK_82 = (2, Weapons.MER_2_MK_82)
        Mk_84 = (2, Weapons.Mk_84)
        _2_Mk_20_Rockeye = (2, Weapons._2_Mk_20_Rockeye)

    class Pylon3:
        AIM_7M = (3, Weapons.AIM_7M)
        AGM_84A = (3, Weapons.AGM_84A)
        AGM_88C_ = (3, Weapons.AGM_88C_)
        MER_2_MK_82 = (3, Weapons.MER_2_MK_82)
        Fuel_tank_330_gal = (3, Weapons.Fuel_tank_330_gal)

    class Pylon4:
        AIM_7M = (4, Weapons.AIM_7M)
        AN_AAS_38_FLIR = (4, Weapons.AN_AAS_38_FLIR)

    class Pylon5:
        Fuel_tank_330_gal = (5, Weapons.Fuel_tank_330_gal)

    class Pylon6:
        AIM_7M = (6, Weapons.AIM_7M)
        AN_ASQ_173_LST_SCAM = (6, Weapons.AN_ASQ_173_LST_SCAM)

    class Pylon7:
        AIM_7M = (7, Weapons.AIM_7M)
        AGM_84A = (7, Weapons.AGM_84A)
        AGM_88C_ = (7, Weapons.AGM_88C_)
        MER_2_MK_82 = (7, Weapons.MER_2_MK_82)
        Fuel_tank_330_gal = (7, Weapons.Fuel_tank_330_gal)

    class Pylon8:
        AIM_7M = (8, Weapons.AIM_7M)
        AIM_9M = (8, Weapons.AIM_9M)
        AIM_9P = (8, Weapons.AIM_9P)
        LAU_10___4_ZUNI_MK_71 = (8, Weapons.LAU_10___4_ZUNI_MK_71)
        AGM_84A = (8, Weapons.AGM_84A)
        AGM_88C_ = (8, Weapons.AGM_88C_)
        LAU_117_AGM_65D = (8, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65K = (8, Weapons.LAU_117_AGM_65K)
        LAU_117_AGM_65E = (8, Weapons.LAU_117_AGM_65E)
        GBU_10 = (8, Weapons.GBU_10)
        GBU_12 = (8, Weapons.GBU_12)
        GBU_16 = (8, Weapons.GBU_16)
        MER_2_MK_82 = (8, Weapons.MER_2_MK_82)
        Mk_84 = (8, Weapons.Mk_84)
        _2_Mk_20_Rockeye = (8, Weapons._2_Mk_20_Rockeye)

    class Pylon9:
        AIM_9M = (9, Weapons.AIM_9M)
        AIM_9P = (9, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.CAP


class F_A_18C(PlaneType):
    id = "F/A-18C"
    height = 4.66
    width = 11.43
    length = 17.07
    fuel_max = 6531
    max_speed = 1920
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"

    class Pylon1:
        AIM_120B = (1, Weapons.AIM_120B)
        AIM_120C = (1, Weapons.AIM_120C)
        AIM_9M = (1, Weapons.AIM_9M)
        AIM_9P = (1, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        AIM_120B = (2, Weapons.AIM_120B)
        AIM_120C = (2, Weapons.AIM_120C)
        AIM_7M = (2, Weapons.AIM_7M)
        LAU_10___4_ZUNI_MK_71 = (2, Weapons.LAU_10___4_ZUNI_MK_71)
        AGM_84A = (2, Weapons.AGM_84A)
        AGM_84E = (2, Weapons.AGM_84E)
        AGM_88C_ = (2, Weapons.AGM_88C_)
        LAU_117_AGM_65E = (2, Weapons.LAU_117_AGM_65E)
        AGM_154C = (2, Weapons.AGM_154C)
        AGM_62 = (2, Weapons.AGM_62)
        GBU_10 = (2, Weapons.GBU_10)
        GBU_12 = (2, Weapons.GBU_12)
        GBU_16 = (2, Weapons.GBU_16)
        MER_2_MK_82 = (2, Weapons.MER_2_MK_82)
        Mk_84 = (2, Weapons.Mk_84)
        _2_Mk_20_Rockeye = (2, Weapons._2_Mk_20_Rockeye)
        Mk_82 = (2, Weapons.Mk_82)
        _3_Mk_82 = (2, Weapons._3_Mk_82)
        Mk_82AIR = (2, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (2, Weapons._3_Mk_82AIR)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (2, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (2, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (2, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        GBU_31_V_3_B = (2, Weapons.GBU_31_V_3_B)
        GBU_31 = (2, Weapons.GBU_31)
        GBU_38 = (2, Weapons.GBU_38)
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)

    class Pylon3:
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_120C = (3, Weapons.AIM_120C)
        AIM_7M = (3, Weapons.AIM_7M)
        AGM_84A = (3, Weapons.AGM_84A)
        AGM_84E = (3, Weapons.AGM_84E)
        AGM_88C_ = (3, Weapons.AGM_88C_)
        MER_2_MK_82 = (3, Weapons.MER_2_MK_82)
        Fuel_tank_330_gal_ = (3, Weapons.Fuel_tank_330_gal_)
        GBU_31_V_3_B = (3, Weapons.GBU_31_V_3_B)
        GBU_31 = (3, Weapons.GBU_31)
        GBU_38 = (3, Weapons.GBU_38)
        GBU_10 = (3, Weapons.GBU_10)
        GBU_12 = (3, Weapons.GBU_12)
        GBU_16 = (3, Weapons.GBU_16)
        Mk_84 = (3, Weapons.Mk_84)
        _2_Mk_20_Rockeye = (3, Weapons._2_Mk_20_Rockeye)
        Mk_82 = (3, Weapons.Mk_82)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        Mk_82AIR = (3, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (3, Weapons._3_Mk_82AIR)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (3, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)

    class Pylon4:
        AIM_120B = (4, Weapons.AIM_120B)
        AIM_120C = (4, Weapons.AIM_120C)
        AIM_7M = (4, Weapons.AIM_7M)
        AN_AAS_38_FLIR = (4, Weapons.AN_AAS_38_FLIR)

    class Pylon5:
        Fuel_tank_330_gal_ = (5, Weapons.Fuel_tank_330_gal_)
        AN_AAQ_28_LITENING = (5, Weapons.AN_AAQ_28_LITENING)

    class Pylon6:
        AIM_120B = (6, Weapons.AIM_120B)
        AIM_120C = (6, Weapons.AIM_120C)
        AIM_7M = (6, Weapons.AIM_7M)
        AN_ASQ_173_LST_SCAM = (6, Weapons.AN_ASQ_173_LST_SCAM)

    class Pylon7:
        AIM_120B = (7, Weapons.AIM_120B)
        AIM_120C = (7, Weapons.AIM_120C)
        AIM_7M = (7, Weapons.AIM_7M)
        AGM_84A = (7, Weapons.AGM_84A)
        AGM_84E = (7, Weapons.AGM_84E)
        AGM_88C_ = (7, Weapons.AGM_88C_)
        MER_2_MK_82 = (7, Weapons.MER_2_MK_82)
        Fuel_tank_330_gal_ = (7, Weapons.Fuel_tank_330_gal_)
        GBU_31_V_3_B = (7, Weapons.GBU_31_V_3_B)
        GBU_31 = (7, Weapons.GBU_31)
        GBU_38 = (7, Weapons.GBU_38)
        GBU_10 = (7, Weapons.GBU_10)
        GBU_12 = (7, Weapons.GBU_12)
        GBU_16 = (7, Weapons.GBU_16)
        Mk_84 = (7, Weapons.Mk_84)
        _2_Mk_20_Rockeye = (7, Weapons._2_Mk_20_Rockeye)
        Mk_82 = (7, Weapons.Mk_82)
        _3_Mk_82 = (7, Weapons._3_Mk_82)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (7, Weapons._3_Mk_82AIR)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (7, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (7, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (7, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (7, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (7, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (7, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (7, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (7, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)

    class Pylon8:
        AIM_120B = (8, Weapons.AIM_120B)
        AIM_120C = (8, Weapons.AIM_120C)
        AIM_7M = (8, Weapons.AIM_7M)
        LAU_10___4_ZUNI_MK_71 = (8, Weapons.LAU_10___4_ZUNI_MK_71)
        AGM_84A = (8, Weapons.AGM_84A)
        AGM_84E = (8, Weapons.AGM_84E)
        AGM_88C_ = (8, Weapons.AGM_88C_)
        LAU_117_AGM_65E = (8, Weapons.LAU_117_AGM_65E)
        AGM_154C = (8, Weapons.AGM_154C)
        AGM_62 = (8, Weapons.AGM_62)
        GBU_10 = (8, Weapons.GBU_10)
        GBU_12 = (8, Weapons.GBU_12)
        GBU_16 = (8, Weapons.GBU_16)
        MER_2_MK_82 = (8, Weapons.MER_2_MK_82)
        Mk_84 = (8, Weapons.Mk_84)
        _2_Mk_20_Rockeye = (8, Weapons._2_Mk_20_Rockeye)
        GBU_31_V_3_B = (8, Weapons.GBU_31_V_3_B)
        GBU_31 = (8, Weapons.GBU_31)
        GBU_38 = (8, Weapons.GBU_38)
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        Mk_82 = (8, Weapons.Mk_82)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        Mk_82AIR = (8, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (8, Weapons._3_Mk_82AIR)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (8, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (8, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (8, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (8, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (8, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)

    class Pylon9:
        AIM_120B = (9, Weapons.AIM_120B)
        AIM_120C = (9, Weapons.AIM_120C)
        AIM_9M = (9, Weapons.AIM_9M)
        AIM_9P = (9, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.CAP


class MiG_29S(PlaneType):
    id = "MiG-29S"
    flyable = True
    height = 4.73
    width = 11.36
    length = 20.32
    fuel_max = 3500
    max_speed = 2450
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"
    radio_frequency = 124

    class Pylon1:
        R_60M = (1, Weapons.R_60M)
        R_73 = (1, Weapons.R_73)
        R_77 = (1, Weapons.R_77)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_60M = (2, Weapons.R_60M)
        R_73 = (2, Weapons.R_73)
        R_77 = (2, Weapons.R_77)
        B_8M1___20_S_8KOM = (2, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (2, Weapons.S_24B_)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)

    class Pylon3:
        R_60M = (3, Weapons.R_60M)
        R_73 = (3, Weapons.R_73)
        R_77 = (3, Weapons.R_77)
        R_27R = (3, Weapons.R_27R)
        R_27ER = (3, Weapons.R_27ER)
        R_27T = (3, Weapons.R_27T)
        R_27ET = (3, Weapons.R_27ET)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (3, Weapons.S_24B_)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        Fuel_tank_1150L_MiG_29 = (3, Weapons.Fuel_tank_1150L_MiG_29)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)

    class Pylon4:
        Fuel_tank_1500L = (4, Weapons.Fuel_tank_1500L)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)

    class Pylon5:
        R_60M = (5, Weapons.R_60M)
        R_73 = (5, Weapons.R_73)
        R_77 = (5, Weapons.R_77)
        R_27R = (5, Weapons.R_27R)
        R_27ER = (5, Weapons.R_27ER)
        R_27T = (5, Weapons.R_27T)
        R_27ET = (5, Weapons.R_27ET)
        B_8M1___20_S_8KOM = (5, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (5, Weapons.S_24B_)
        BetAB_500 = (5, Weapons.BetAB_500)
        BetAB_500ShP = (5, Weapons.BetAB_500ShP)
        FAB_250 = (5, Weapons.FAB_250)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (5, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (5, Weapons.KMGU_2___96_PTAB_2_5KO)
        Fuel_tank_1150L_MiG_29 = (5, Weapons.Fuel_tank_1150L_MiG_29)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (5, Weapons.B_8M1___20_S_8TsM)

    class Pylon6:
        R_60M = (6, Weapons.R_60M)
        R_73 = (6, Weapons.R_73)
        R_77 = (6, Weapons.R_77)
        B_8M1___20_S_8KOM = (6, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (6, Weapons.S_24B_)
        BetAB_500 = (6, Weapons.BetAB_500)
        BetAB_500ShP = (6, Weapons.BetAB_500ShP)
        FAB_250 = (6, Weapons.FAB_250)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (6, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (6, Weapons.KMGU_2___96_PTAB_2_5KO)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (6, Weapons.B_8M1___20_S_8TsM)

    class Pylon7:
        R_60M = (7, Weapons.R_60M)
        R_73 = (7, Weapons.R_73)
        R_77 = (7, Weapons.R_77)
        Smoke_Generator___red = (7, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (7, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (7, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (7, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (7, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (7, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.GroundAttack, task.CAS, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class MiG_29A(PlaneType):
    id = "MiG-29A"
    flyable = True
    height = 4.73
    width = 11.36
    length = 20.32
    fuel_max = 3380
    max_speed = 2450
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"
    radio_frequency = 124

    class Pylon1:
        R_60M = (1, Weapons.R_60M)
        R_73 = (1, Weapons.R_73)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73 = (2, Weapons.R_73)
        R_60M = (2, Weapons.R_60M)
        B_8M1___20_S_8KOM = (2, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (2, Weapons.S_24B_)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)

    class Pylon3:
        R_27R = (3, Weapons.R_27R)
        R_27T = (3, Weapons.R_27T)
        R_27ER = (3, Weapons.R_27ER)
        R_27ET = (3, Weapons.R_27ET)
        R_73 = (3, Weapons.R_73)
        R_60M = (3, Weapons.R_60M)
        Fuel_tank_1150L_MiG_29 = (3, Weapons.Fuel_tank_1150L_MiG_29)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (3, Weapons.S_24B_)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)

    class Pylon4:
        Fuel_tank_1500L = (4, Weapons.Fuel_tank_1500L)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)

    class Pylon5:
        R_27R = (5, Weapons.R_27R)
        R_27T = (5, Weapons.R_27T)
        R_27ER = (5, Weapons.R_27ER)
        R_27ET = (5, Weapons.R_27ET)
        R_73 = (5, Weapons.R_73)
        R_60M = (5, Weapons.R_60M)
        Fuel_tank_1150L_MiG_29 = (5, Weapons.Fuel_tank_1150L_MiG_29)
        B_8M1___20_S_8KOM = (5, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (5, Weapons.S_24B_)
        BetAB_500 = (5, Weapons.BetAB_500)
        BetAB_500ShP = (5, Weapons.BetAB_500ShP)
        FAB_250 = (5, Weapons.FAB_250)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (5, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (5, Weapons.KMGU_2___96_PTAB_2_5KO)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (5, Weapons.B_8M1___20_S_8TsM)

    class Pylon6:
        R_73 = (6, Weapons.R_73)
        R_60M = (6, Weapons.R_60M)
        B_8M1___20_S_8KOM = (6, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (6, Weapons.S_24B_)
        BetAB_500 = (6, Weapons.BetAB_500)
        BetAB_500ShP = (6, Weapons.BetAB_500ShP)
        FAB_250 = (6, Weapons.FAB_250)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (6, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (6, Weapons.KMGU_2___96_PTAB_2_5KO)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (6, Weapons.B_8M1___20_S_8TsM)

    class Pylon7:
        R_60M = (7, Weapons.R_60M)
        R_73 = (7, Weapons.R_73)
        Smoke_Generator___red = (7, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (7, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (7, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (7, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (7, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (7, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.GroundAttack, task.CAS, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class F_14A(PlaneType):
    id = "F-14A"
    large_parking_slot = True
    height = 4.88
    width = 19.54
    length = 19.1
    fuel_max = 7348
    max_speed = 2490
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_9M = (1, Weapons.AIM_9M)
        AIM_9P = (1, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        AIM_54C = (2, Weapons.AIM_54C)
        AIM_7M = (2, Weapons.AIM_7M)

    class Pylon3:
        Fuel_tank_367_gal = (3, Weapons.Fuel_tank_367_gal)

    class Pylon4:
        AIM_54C = (4, Weapons.AIM_54C)

    class Pylon5:
        AIM_54C = (5, Weapons.AIM_54C)

    class Pylon6:
        AIM_7M = (6, Weapons.AIM_7M)

    class Pylon7:
        AIM_7M = (7, Weapons.AIM_7M)

    class Pylon8:
        AIM_54C = (8, Weapons.AIM_54C)

    class Pylon9:
        AIM_54C = (9, Weapons.AIM_54C)

    class Pylon10:
        Fuel_tank_367_gal = (10, Weapons.Fuel_tank_367_gal)

    class Pylon11:
        AIM_54C = (11, Weapons.AIM_54C)
        AIM_7M = (11, Weapons.AIM_7M)

    class Pylon12:
        AIM_9M = (12, Weapons.AIM_9M)
        AIM_9P = (12, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (12, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance]
    task_default = task.Intercept


class Tu_22M3(PlaneType):
    id = "Tu-22M3"
    group_size_max = 1
    large_parking_slot = True
    height = 11.05
    width = 34.28
    length = 46.12
    fuel_max = 50000
    max_speed = 2300
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        Kh_22N = (1, Weapons.Kh_22N)
        MER_9_FAB_250 = (1, Weapons.MER_9_FAB_250)

    class Pylon2:
        MER_9_FAB_250 = (2, Weapons.MER_9_FAB_250)

    class Pylon3:
        Kh_22N = (3, Weapons.Kh_22N)
        FAB_500_33 = (3, Weapons.FAB_500_33)
        FAB_250_33 = (3, Weapons.FAB_250_33)

    class Pylon4:
        MER_9_FAB_250 = (4, Weapons.MER_9_FAB_250)

    class Pylon5:
        Kh_22N = (5, Weapons.Kh_22N)
        MER_9_FAB_250 = (5, Weapons.MER_9_FAB_250)

    pylons = {1, 2, 3, 4, 5}

    tasks = [task.AntishipStrike, task.GroundAttack, task.RunwayAttack]
    task_default = task.AntishipStrike


class F_4E(PlaneType):
    id = "F-4E"
    height = 5
    width = 11.68
    length = 19.2
    fuel_max = 4864
    max_speed = 2370
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        GBU_10 = (1, Weapons.GBU_10)
        GBU_12 = (1, Weapons.GBU_12)
        _3_Mk_20_Rockeye = (1, Weapons._3_Mk_20_Rockeye)
        MER_6_Mk_82 = (1, Weapons.MER_6_Mk_82)
        Mk_84 = (1, Weapons.Mk_84)
        LAU_10___4_ZUNI_MK_71 = (1, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61_3___57_2_75__rockets_MK151__HE_ = (1, Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_)
        LAU_61___19_2_75__rockets_MK156_WP = (1, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        F_4_Fuel_tank_W = (1, Weapons.F_4_Fuel_tank_W)
        AGM_45B_ = (1, Weapons.AGM_45B_)

    class Pylon2:
        LAU_7___2_AIM_9M = (2, Weapons.LAU_7___2_AIM_9M)
        LAU_7___2_AIM_9P = (2, Weapons.LAU_7___2_AIM_9P)
        GBU_10 = (2, Weapons.GBU_10)
        GBU_12 = (2, Weapons.GBU_12)
        _3_Mk_20_Rockeye = (2, Weapons._3_Mk_20_Rockeye)
        _3_Mk_82 = (2, Weapons._3_Mk_82)
        Mk_84 = (2, Weapons.Mk_84)
        LAU_88_AGM_65K_2 = (2, Weapons.LAU_88_AGM_65K_2)
        LAU_88_AGM_65D_2 = (2, Weapons.LAU_88_AGM_65D_2)
        AGM_45B_ = (2, Weapons.AGM_45B_)
        LAU_10___4_ZUNI_MK_71 = (2, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61_3___57_2_75__rockets_MK151__HE_ = (2, Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_)
        LAU_7___AN_ASQ_T50 = (2, Weapons.LAU_7___AN_ASQ_T50)

    class Pylon3:
        AIM_7M = (3, Weapons.AIM_7M)
        ALQ_131 = (3, Weapons.ALQ_131)

    class Pylon4:
        AIM_7M = (4, Weapons.AIM_7M)

    class Pylon5:
        F_4_Fuel_tank_C = (5, Weapons.F_4_Fuel_tank_C)

    class Pylon6:
        AIM_7M = (6, Weapons.AIM_7M)

    class Pylon7:
        AIM_7M = (7, Weapons.AIM_7M)

    class Pylon8:
        LAU_7___2_AIM_9M = (8, Weapons.LAU_7___2_AIM_9M)
        LAU_7___2_AIM_9P = (8, Weapons.LAU_7___2_AIM_9P)
        GBU_10 = (8, Weapons.GBU_10)
        GBU_12 = (8, Weapons.GBU_12)
        _3_Mk_20_Rockeye = (8, Weapons._3_Mk_20_Rockeye)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        Mk_84 = (8, Weapons.Mk_84)
        LAU_88_AGM_65K_2_ = (8, Weapons.LAU_88_AGM_65K_2_)
        LAU_88_AGM_65D_2_ = (8, Weapons.LAU_88_AGM_65D_2_)
        AGM_45B_ = (8, Weapons.AGM_45B_)
        LAU_10___4_ZUNI_MK_71 = (8, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61_3___57_2_75__rockets_MK151__HE_ = (8, Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_)

    class Pylon9:
        GBU_10 = (9, Weapons.GBU_10)
        GBU_12 = (9, Weapons.GBU_12)
        _3_Mk_20_Rockeye = (9, Weapons._3_Mk_20_Rockeye)
        MER_6_Mk_82 = (9, Weapons.MER_6_Mk_82)
        Mk_84 = (9, Weapons.Mk_84)
        LAU_10___4_ZUNI_MK_71 = (9, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (9, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61_3___57_2_75__rockets_MK151__HE_ = (9, Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_)
        LAU_61___19_2_75__rockets_MK156_WP = (9, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        F_4_Fuel_tank_W = (9, Weapons.F_4_Fuel_tank_W)
        AGM_45B_ = (9, Weapons.AGM_45B_)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.GroundAttack, task.CAS, task.PinpointStrike, task.SEAD, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class B_52H(PlaneType):
    id = "B-52H"
    group_size_max = 1
    large_parking_slot = True
    height = 12.4
    width = 56.4
    length = 49.05
    fuel_max = 141135
    max_speed = 1000
    chaff = 1125
    flare = 192
    charge_total = 1317
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True

    class Pylon1:
        MER_12_Mk_82 = (1, Weapons.MER_12_Mk_82)
        HSAB_9_Mk_20_Rockeye = (1, Weapons.HSAB_9_Mk_20_Rockeye)
        HSAB_9_Mk_84 = (1, Weapons.HSAB_9_Mk_84)
        MER_6_AGM_86C = (1, Weapons.MER_6_AGM_86C)

    class Pylon2:
        _27_Mk_82 = (2, Weapons._27_Mk_82)
        AGM_86C_8 = (2, Weapons.AGM_86C_8)
        AGM_84A_8 = (2, Weapons.AGM_84A_8)

    class Pylon3:
        MER_12_Mk_82 = (3, Weapons.MER_12_Mk_82)
        HSAB_9_Mk_20_Rockeye = (3, Weapons.HSAB_9_Mk_20_Rockeye)
        HSAB_9_Mk_84 = (3, Weapons.HSAB_9_Mk_84)
        MER_6_AGM_86C = (3, Weapons.MER_6_AGM_86C)
#ERRR {HSAB*9 GBU-31}

    pylons = {1, 2, 3}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.AntishipStrike, task.CAS]
    task_default = task.GroundAttack


class MiG_27K(PlaneType):
    id = "MiG-27K"
    height = 5.64
    width = 14
    length = 16.7
    fuel_max = 4500
    max_speed = 1810
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon2:
        Kh_25ML_ = (2, Weapons.Kh_25ML_)
        Kh_25MPU_ = (2, Weapons.Kh_25MPU_)
        Kh_25MR = (2, Weapons.Kh_25MR)
        Kh_29L_ = (2, Weapons.Kh_29L_)
        Kh_29T_ = (2, Weapons.Kh_29T_)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (2, Weapons.B_8M1___20_S_8KOM)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)
        KAB_500L = (2, Weapons.KAB_500L)
        KAB_500kr = (2, Weapons.KAB_500kr)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        MER_6_2_FAB_250 = (2, Weapons.MER_6_2_FAB_250)
        R_60M = (2, Weapons.R_60M)

    class Pylon3:
        R_60M = (3, Weapons.R_60M)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)

    class Pylon4:
        FAB_250 = (4, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)

    class Pylon5:
        Fuel_tank_800L = (5, Weapons.Fuel_tank_800L)

    class Pylon6:
        FAB_250 = (6, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)

    class Pylon7:
        R_60M = (7, Weapons.R_60M)
        UB_32A___32_S_5KO = (7, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (7, Weapons.B_8M1___20_S_8KOM)

    class Pylon8:
        Kh_25ML_ = (8, Weapons.Kh_25ML_)
        Kh_25MPU_ = (8, Weapons.Kh_25MPU_)
        Kh_25MR = (8, Weapons.Kh_25MR)
        Kh_29L_ = (8, Weapons.Kh_29L_)
        Kh_29T_ = (8, Weapons.Kh_29T_)
        UB_32A___32_S_5KO = (8, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (8, Weapons.B_8M1___20_S_8KOM)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        BetAB_500 = (8, Weapons.BetAB_500)
        BetAB_500ShP = (8, Weapons.BetAB_500ShP)
        KAB_500L = (8, Weapons.KAB_500L)
        KAB_500kr = (8, Weapons.KAB_500kr)
        KMGU_2___96_AO_2_5RT = (8, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (8, Weapons.KMGU_2___96_PTAB_2_5KO)
        MER_6_2_FAB_250 = (8, Weapons.MER_6_2_FAB_250)
        R_60M = (8, Weapons.R_60M)

    pylons = {2, 3, 4, 5, 6, 7, 8}

    tasks = [task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AntishipStrike]
    task_default = task.GroundAttack


class F_111F(PlaneType):
    id = "F-111F"
    large_parking_slot = True
    height = 5.22
    width = 19.2
    length = 22.4
    fuel_max = 15500
    max_speed = 2221.2
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        MER_6_Mk_82 = (1, Weapons.MER_6_Mk_82)
        MER_6_Mk_20_Rockeye = (1, Weapons.MER_6_Mk_20_Rockeye)
        MER_6_BLU_107 = (1, Weapons.MER_6_BLU_107)
        Mk_84 = (1, Weapons.Mk_84)
        GBU_28 = (1, Weapons.GBU_28)
        GBU_15 = (1, Weapons.GBU_15)
        GBU_10 = (1, Weapons.GBU_10)
        GBU_12 = (1, Weapons.GBU_12)
        GBU_24 = (1, Weapons.GBU_24)
        AIM_9M = (1, Weapons.AIM_9M)

    class Pylon2:
        MER_6_Mk_82 = (2, Weapons.MER_6_Mk_82)
        MER_6_Mk_20_Rockeye = (2, Weapons.MER_6_Mk_20_Rockeye)
        MER_6_BLU_107 = (2, Weapons.MER_6_BLU_107)
        Mk_84 = (2, Weapons.Mk_84)
        GBU_10 = (2, Weapons.GBU_10)
        GBU_12 = (2, Weapons.GBU_12)
        GBU_24 = (2, Weapons.GBU_24)
        AIM_9M = (2, Weapons.AIM_9M)

    class Pylon3:
        Pavetack_F_111 = (3, Weapons.Pavetack_F_111)

    class Pylon4:
        _6_Mk_82 = (4, Weapons._6_Mk_82)
        Mk_20_Rockeye__6 = (4, Weapons.Mk_20_Rockeye__6)
        Mk_84 = (4, Weapons.Mk_84)
        GBU_28 = (4, Weapons.GBU_28)
        GBU_15 = (4, Weapons.GBU_15)
        GBU_10 = (4, Weapons.GBU_10)
        GBU_12 = (4, Weapons.GBU_12)
        GBU_24 = (4, Weapons.GBU_24)

    class Pylon5:
        MER_6_Mk_82 = (5, Weapons.MER_6_Mk_82)
        MER_6_Mk_20_Rockeye = (5, Weapons.MER_6_Mk_20_Rockeye)
        MER_6_BLU_107 = (5, Weapons.MER_6_BLU_107)
        Mk_84 = (5, Weapons.Mk_84)
        GBU_10 = (5, Weapons.GBU_10)
        GBU_12 = (5, Weapons.GBU_12)
        GBU_24 = (5, Weapons.GBU_24)
        AIM_9M = (5, Weapons.AIM_9M)

    class Pylon6:
        MER_6_Mk_82 = (6, Weapons.MER_6_Mk_82)
        MER_6_Mk_20_Rockeye = (6, Weapons.MER_6_Mk_20_Rockeye)
        MER_6_BLU_107 = (6, Weapons.MER_6_BLU_107)
        Mk_84 = (6, Weapons.Mk_84)
        GBU_28 = (6, Weapons.GBU_28)
        GBU_15 = (6, Weapons.GBU_15)
        GBU_10 = (6, Weapons.GBU_10)
        GBU_12 = (6, Weapons.GBU_12)
        GBU_24 = (6, Weapons.GBU_24)
        AIM_9M = (6, Weapons.AIM_9M)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.AFAC]
    task_default = task.GroundAttack


class A_10A(PlaneType):
    id = "A-10A"
    flyable = True
    height = 4.47
    width = 17.53
    length = 16.26
    fuel_max = 5029
    max_speed = 840
    chaff = 240
    flare = 120
    charge_total = 480
    chaff_charge_size = 1
    flare_charge_size = 2
    radio_frequency = 124

    callnames = {
        "USA": [
            "Hawg",
            "Boar",
            "Pig",
            "Tusk",
        ]
    }

    class Pylon1:
        LAU_105___2_AIM_9M = (1, Weapons.LAU_105___2_AIM_9M)
        LAU_105_1_AIM_9M_L = (1, Weapons.LAU_105_1_AIM_9M_L)
        LAU_105_1_CATM_9M_L = (1, Weapons.LAU_105_1_CATM_9M_L)
        LAU_105___2_AIM_9P = (1, Weapons.LAU_105___2_AIM_9P)
        ALQ_131 = (1, Weapons.ALQ_131)
        ALQ_184 = (1, Weapons.ALQ_184)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        Mk_82AIR = (1, Weapons.Mk_82AIR)
        CBU_87 = (1, Weapons.CBU_87)
        BDU_50LD = (1, Weapons.BDU_50LD)
        BDU_50HD = (1, Weapons.BDU_50HD)
        CBU_97 = (1, Weapons.CBU_97)
        Mk_82 = (1, Weapons.Mk_82)
        LAU_105_AIS_ASQ_T50_L = (1, Weapons.LAU_105_AIS_ASQ_T50_L)

    class Pylon2:
        Mk_82 = (2, Weapons.Mk_82)
        SUU_25___8_LUU_2 = (2, Weapons.SUU_25___8_LUU_2)
        Mk_82AIR = (2, Weapons.Mk_82AIR)
        CBU_87 = (2, Weapons.CBU_87)
        BDU_50LD = (2, Weapons.BDU_50LD)
        BDU_50HD = (2, Weapons.BDU_50HD)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (2, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (2, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (2, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (2, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (2, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (2, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (2, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (2, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (2, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (2, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
        CBU_97 = (2, Weapons.CBU_97)

    class Pylon3:
        LAU_117_AGM_65K = (3, Weapons.LAU_117_AGM_65K)
        LAU_117_AGM_65D = (3, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65D_2 = (3, Weapons.LAU_88_AGM_65D_2)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65D_3 = (3, Weapons.LAU_88_AGM_65D_3)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_CATM_65K = (3, Weapons.LAU_117_CATM_65K)
        LAU_117_TGM_65D = (3, Weapons.LAU_117_TGM_65D)
        LAU_117_TGM_65G = (3, Weapons.LAU_117_TGM_65G)
        LAU_117_TGM_65H = (3, Weapons.LAU_117_TGM_65H)
        Mk_84 = (3, Weapons.Mk_84)
        Mk_82 = (3, Weapons.Mk_82)
        Mk_82AIR = (3, Weapons.Mk_82AIR)
        CBU_87 = (3, Weapons.CBU_87)
        BDU_50LD = (3, Weapons.BDU_50LD)
        BDU_50HD = (3, Weapons.BDU_50HD)
        BRU_42_3_BDU_33 = (3, Weapons.BRU_42_3_BDU_33)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        _3_Mk_82AIR = (3, Weapons._3_Mk_82AIR)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (3, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (3, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (3, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (3, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (3, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (3, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
        CBU_97 = (3, Weapons.CBU_97)

    class Pylon4:
        Mk_82 = (4, Weapons.Mk_82)
        Mk_84 = (4, Weapons.Mk_84)
        Mk_82AIR = (4, Weapons.Mk_82AIR)
        CBU_87 = (4, Weapons.CBU_87)
        BDU_50LD = (4, Weapons.BDU_50LD)
        BDU_50HD = (4, Weapons.BDU_50HD)
        BRU_42_3_BDU_33 = (4, Weapons.BRU_42_3_BDU_33)
        _3_Mk_82 = (4, Weapons._3_Mk_82)
        _3_Mk_82AIR = (4, Weapons._3_Mk_82AIR)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (4, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (4, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (4, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (4, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (4, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (4, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (4, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (4, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (4, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (4, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (4, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (4, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (4, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (4, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (4, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (4, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
        Fuel_Tank_FT600 = (4, Weapons.Fuel_Tank_FT600)
        CBU_97 = (4, Weapons.CBU_97)

    class Pylon5:
        Mk_82 = (5, Weapons.Mk_82)
        Mk_84 = (5, Weapons.Mk_84)
        Mk_82AIR = (5, Weapons.Mk_82AIR)
        CBU_87 = (5, Weapons.CBU_87)
        BDU_50LD = (5, Weapons.BDU_50LD)
        BDU_50HD = (5, Weapons.BDU_50HD)
        BRU_42_3_BDU_33 = (5, Weapons.BRU_42_3_BDU_33)
        CBU_97 = (5, Weapons.CBU_97)

    class Pylon6:
        Mk_82 = (6, Weapons.Mk_82)
        Mk_84 = (6, Weapons.Mk_84)
        Mk_82AIR = (6, Weapons.Mk_82AIR)
        CBU_87 = (6, Weapons.CBU_87)
        BDU_50LD = (6, Weapons.BDU_50LD)
        BDU_50HD = (6, Weapons.BDU_50HD)
        BRU_42_3_BDU_33 = (6, Weapons.BRU_42_3_BDU_33)
        Fuel_Tank_FT600 = (6, Weapons.Fuel_Tank_FT600)
        CBU_97 = (6, Weapons.CBU_97)

    class Pylon7:
        Mk_82 = (7, Weapons.Mk_82)
        Mk_84 = (7, Weapons.Mk_84)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        CBU_87 = (7, Weapons.CBU_87)
        BDU_50LD = (7, Weapons.BDU_50LD)
        BDU_50HD = (7, Weapons.BDU_50HD)
        BRU_42_3_BDU_33 = (7, Weapons.BRU_42_3_BDU_33)
        CBU_97 = (7, Weapons.CBU_97)

    class Pylon8:
        Mk_82 = (8, Weapons.Mk_82)
        Mk_84 = (8, Weapons.Mk_84)
        Mk_82AIR = (8, Weapons.Mk_82AIR)
        CBU_87 = (8, Weapons.CBU_87)
        BDU_50LD = (8, Weapons.BDU_50LD)
        BDU_50HD = (8, Weapons.BDU_50HD)
        BRU_42_3_BDU_33 = (8, Weapons.BRU_42_3_BDU_33)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        _3_Mk_82AIR = (8, Weapons._3_Mk_82AIR)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (8, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (8, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (8, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (8, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (8, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (8, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (8, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (8, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (8, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (8, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (8, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (8, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (8, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
        Fuel_Tank_FT600 = (8, Weapons.Fuel_Tank_FT600)
        CBU_97 = (8, Weapons.CBU_97)

    class Pylon9:
        LAU_117_AGM_65K = (9, Weapons.LAU_117_AGM_65K)
        LAU_117_AGM_65D = (9, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65G = (9, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65H = (9, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65D_2_ = (9, Weapons.LAU_88_AGM_65D_2_)
        LAU_88_AGM_65H_2_R = (9, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65D_3 = (9, Weapons.LAU_88_AGM_65D_3)
        LAU_88_AGM_65H_3 = (9, Weapons.LAU_88_AGM_65H_3)
        LAU_117_CATM_65K = (9, Weapons.LAU_117_CATM_65K)
        LAU_117_TGM_65D = (9, Weapons.LAU_117_TGM_65D)
        LAU_117_TGM_65G = (9, Weapons.LAU_117_TGM_65G)
        LAU_117_TGM_65H = (9, Weapons.LAU_117_TGM_65H)
        Mk_84 = (9, Weapons.Mk_84)
        Mk_82 = (9, Weapons.Mk_82)
        Mk_82AIR = (9, Weapons.Mk_82AIR)
        CBU_87 = (9, Weapons.CBU_87)
        BDU_50LD = (9, Weapons.BDU_50LD)
        BDU_50HD = (9, Weapons.BDU_50HD)
        BRU_42_3_BDU_33 = (9, Weapons.BRU_42_3_BDU_33)
        _3_Mk_82 = (9, Weapons._3_Mk_82)
        _3_Mk_82AIR = (9, Weapons._3_Mk_82AIR)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (9, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (9, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (9, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (9, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (9, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (9, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (9, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (9, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (9, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (9, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (9, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (9, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (9, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (9, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (9, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (9, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
        CBU_97 = (9, Weapons.CBU_97)

    class Pylon10:
        Mk_82 = (10, Weapons.Mk_82)
        SUU_25___8_LUU_2 = (10, Weapons.SUU_25___8_LUU_2)
        Mk_82AIR = (10, Weapons.Mk_82AIR)
        CBU_87 = (10, Weapons.CBU_87)
        BDU_50LD = (10, Weapons.BDU_50LD)
        BDU_50HD = (10, Weapons.BDU_50HD)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (10, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (10, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (10, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (10, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (10, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (10, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (10, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (10, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (10, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (10, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (10, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (10, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (10, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (10, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (10, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (10, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
        CBU_97 = (10, Weapons.CBU_97)

    class Pylon11:
        LAU_105___2_AIM_9M = (11, Weapons.LAU_105___2_AIM_9M)
        LAU_105_1_AIM_9M_R = (11, Weapons.LAU_105_1_AIM_9M_R)
        LAU_105_1_CATM_9M_R = (11, Weapons.LAU_105_1_CATM_9M_R)
        LAU_105___2_AIM_9P = (11, Weapons.LAU_105___2_AIM_9P)
        ALQ_131 = (11, Weapons.ALQ_131)
        ALQ_184 = (11, Weapons.ALQ_184)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        Mk_82AIR = (11, Weapons.Mk_82AIR)
        CBU_87 = (11, Weapons.CBU_87)
        BDU_50LD = (11, Weapons.BDU_50LD)
        BDU_50HD = (11, Weapons.BDU_50HD)
        CBU_97 = (11, Weapons.CBU_97)
        Mk_82 = (11, Weapons.Mk_82)
        LAU_105_AIS_ASQ_T50_R = (11, Weapons.LAU_105_AIS_ASQ_T50_R)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAS


class Su_27(PlaneType):
    id = "Su-27"
    flyable = True
    height = 5.932
    width = 14.7
    length = 21.935
    fuel_max = 9400
    max_speed = 2500
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"
    radio_frequency = 127.5

    class Pylon1:
        R_73 = (1, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73 = (2, Weapons.R_73)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)

    class Pylon3:
        R_73 = (3, Weapons.R_73)
        R_27R = (3, Weapons.R_27R)
        R_27T = (3, Weapons.R_27T)
        R_27ER = (3, Weapons.R_27ER)
        R_27ET = (3, Weapons.R_27ET)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        SAB_100 = (3, Weapons.SAB_100)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        S_25_OFM = (3, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        MER_6_FAB_100 = (3, Weapons.MER_6_FAB_100)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)

    class Pylon4:
        R_27R = (4, Weapons.R_27R)
        R_27ER = (4, Weapons.R_27ER)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        BetAB_500 = (4, Weapons.BetAB_500)
        BetAB_500ShP = (4, Weapons.BetAB_500ShP)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        SAB_100 = (4, Weapons.SAB_100)
        MER_6_FAB_100 = (4, Weapons.MER_6_FAB_100)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)

    class Pylon5:
        R_27R = (5, Weapons.R_27R)
        R_27ER = (5, Weapons.R_27ER)
        FAB_250 = (5, Weapons.FAB_250)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        BetAB_500 = (5, Weapons.BetAB_500)
        BetAB_500ShP = (5, Weapons.BetAB_500ShP)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        SAB_100 = (5, Weapons.SAB_100)
        MER_6_FAB_100 = (5, Weapons.MER_6_FAB_100)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)

    class Pylon6:
        R_27R = (6, Weapons.R_27R)
        R_27ER = (6, Weapons.R_27ER)
        FAB_250 = (6, Weapons.FAB_250)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        BetAB_500 = (6, Weapons.BetAB_500)
        BetAB_500ShP = (6, Weapons.BetAB_500ShP)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (6, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (6, Weapons.KMGU_2___96_PTAB_2_5KO)
        SAB_100 = (6, Weapons.SAB_100)
        MER_6_FAB_100 = (6, Weapons.MER_6_FAB_100)

    class Pylon7:
        R_27R = (7, Weapons.R_27R)
        R_27ER = (7, Weapons.R_27ER)
        FAB_250 = (7, Weapons.FAB_250)
        FAB_500_M62 = (7, Weapons.FAB_500_M62)
        BetAB_500 = (7, Weapons.BetAB_500)
        BetAB_500ShP = (7, Weapons.BetAB_500ShP)
        RBK_250_PTAB_2_5M = (7, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (7, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (7, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (7, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (7, Weapons.KMGU_2___96_PTAB_2_5KO)
        SAB_100 = (7, Weapons.SAB_100)
        MER_6_FAB_100 = (7, Weapons.MER_6_FAB_100)
        Smoke_Generator___red = (7, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (7, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (7, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (7, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (7, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (7, Weapons.Smoke_Generator___orange)

    class Pylon8:
        R_73 = (8, Weapons.R_73)
        R_27R = (8, Weapons.R_27R)
        R_27T = (8, Weapons.R_27T)
        R_27ER = (8, Weapons.R_27ER)
        R_27ET = (8, Weapons.R_27ET)
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_250 = (8, Weapons.FAB_250)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        BetAB_500 = (8, Weapons.BetAB_500)
        BetAB_500ShP = (8, Weapons.BetAB_500ShP)
        RBK_250_PTAB_2_5M = (8, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (8, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (8, Weapons.KMGU_2___96_PTAB_2_5KO)
        SAB_100 = (8, Weapons.SAB_100)
        B_8M1___20_S_8KOM = (8, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (8, Weapons.B_13L___5_S_13_OF)
        S_25_OFM = (8, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (8, Weapons.B_8M1___20_S_8TsM)
        MER_6_FAB_100 = (8, Weapons.MER_6_FAB_100)
        Smoke_Generator___red = (8, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (8, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (8, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (8, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (8, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (8, Weapons.Smoke_Generator___orange)

    class Pylon9:
        R_73 = (9, Weapons.R_73)
        Smoke_Generator___red = (9, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (9, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (9, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (9, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (9, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (9, Weapons.Smoke_Generator___orange)

    class Pylon10:
        R_73 = (10, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__right_ = (10, Weapons.L005_Sorbtsiya_ECM_pod__right_)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Intercept, task.Escort, task.FighterSweep, task.AFAC, task.GroundAttack, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class MiG_29G(PlaneType):
    id = "MiG-29G"
    height = 4.73
    width = 11.36
    length = 20.32
    fuel_max = 3380
    max_speed = 2450
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"
    radio_frequency = 124

    class Pylon1:
        R_60M = (1, Weapons.R_60M)
        R_73 = (1, Weapons.R_73)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73 = (2, Weapons.R_73)
        R_60M = (2, Weapons.R_60M)
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)

    class Pylon3:
        R_27R = (3, Weapons.R_27R)
        R_73 = (3, Weapons.R_73)
        R_60M = (3, Weapons.R_60M)
        Fuel_tank_1150L_MiG_29 = (3, Weapons.Fuel_tank_1150L_MiG_29)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)

    class Pylon4:
        Fuel_tank_1500L = (4, Weapons.Fuel_tank_1500L)

    class Pylon5:
        R_27R = (5, Weapons.R_27R)
        R_73 = (5, Weapons.R_73)
        R_60M = (5, Weapons.R_60M)
        Fuel_tank_1150L_MiG_29 = (5, Weapons.Fuel_tank_1150L_MiG_29)
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (5, Weapons.B_8M1___20_S_8TsM)

    class Pylon6:
        R_73 = (6, Weapons.R_73)
        R_60M = (6, Weapons.R_60M)
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (6, Weapons.B_8M1___20_S_8TsM)

    class Pylon7:
        R_60M = (7, Weapons.R_60M)
        R_73 = (7, Weapons.R_73)
        Smoke_Generator___red = (7, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (7, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (7, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (7, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (7, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (7, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC]
    task_default = task.CAP


class MiG_23MLD(PlaneType):
    id = "MiG-23MLD"
    height = 5.772
    width = 14
    length = 15.7
    fuel_max = 3800
    max_speed = 2500
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon2:
        R_24R = (2, Weapons.R_24R)
        R_24T = (2, Weapons.R_24T)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (2, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (2, Weapons.S_24B_)
        FAB_100 = (2, Weapons.FAB_100)
        SAB_100 = (2, Weapons.SAB_100)
        FAB_250 = (2, Weapons.FAB_250)
        MBD_2_67U___4_FAB_100 = (2, Weapons.MBD_2_67U___4_FAB_100)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)

    class Pylon3:
        R_60M_2 = (3, Weapons.R_60M_2)
        R_60M = (3, Weapons.R_60M)
        S_24B_ = (3, Weapons.S_24B_)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)
        FAB_250 = (3, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)

    class Pylon4:
        Fuel_tank_800L = (4, Weapons.Fuel_tank_800L)

    class Pylon5:
        R_60M_2_ = (5, Weapons.R_60M_2_)
        R_60M = (5, Weapons.R_60M)
        S_24B_ = (5, Weapons.S_24B_)
        B_8M1___20_S_8KOM = (5, Weapons.B_8M1___20_S_8KOM)
        UB_32A___32_S_5KO = (5, Weapons.UB_32A___32_S_5KO)
        FAB_100 = (5, Weapons.FAB_100)
        SAB_100 = (5, Weapons.SAB_100)
        FAB_250 = (5, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)

    class Pylon6:
        R_24R = (6, Weapons.R_24R)
        R_24T = (6, Weapons.R_24T)
        UB_32A___32_S_5KO = (6, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (6, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (6, Weapons.S_24B_)
        FAB_100 = (6, Weapons.FAB_100)
        SAB_100 = (6, Weapons.SAB_100)
        FAB_250 = (6, Weapons.FAB_250)
        MBD_2_67U___4_FAB_100 = (6, Weapons.MBD_2_67U___4_FAB_100)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)

    pylons = {2, 3, 4, 5, 6}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.GroundAttack, task.CAS]
    task_default = task.CAP


class Su_25(PlaneType):
    id = "Su-25"
    flyable = True
    height = 4.8
    width = 14.35
    length = 15.36
    fuel_max = 2835
    max_speed = 980
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    class Pylon1:
        R_60M = (1, Weapons.R_60M)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (2, Weapons.FAB_100)
        SAB_100 = (2, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (2, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (2, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (2, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (2, Weapons.S_24B_)
        S_25_OFM = (2, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)
        S_25L = (2, Weapons.S_25L)

    class Pylon3:
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (3, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (3, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25ML_ = (3, Weapons.Kh_25ML_)
        S_25L = (3, Weapons.S_25L)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (3, Weapons.S_24B_)
        S_25_OFM = (3, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (3, Weapons.Fuel_tank_800L_Wing)

    class Pylon4:
        B_8M1___20_S_8OFP2 = (4, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (4, Weapons.FAB_100)
        SAB_100 = (4, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (4, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (4, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (4, Weapons.BetAB_500)
        BetAB_500ShP = (4, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25ML_ = (4, Weapons.Kh_25ML_)
        S_25L = (4, Weapons.S_25L)
        UB_32A___32_S_5KO = (4, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (4, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (4, Weapons.S_24B_)
        S_25_OFM = (4, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (4, Weapons.B_8M1___20_S_8TsM)
        SPPU_22_1_Gun_pod = (4, Weapons.SPPU_22_1_Gun_pod)

    class Pylon5:
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (5, Weapons.FAB_100)
        SAB_100 = (5, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (5, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (5, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (5, Weapons.BetAB_500)
        BetAB_500ShP = (5, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (5, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (5, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_29L_ = (5, Weapons.Kh_29L_)
        S_25L = (5, Weapons.S_25L)
        UB_32A___32_S_5KO = (5, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (5, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (5, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (5, Weapons.S_24B_)
        S_25_OFM = (5, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (5, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (5, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1_Gun_pod = (5, Weapons.SPPU_22_1_Gun_pod)

    class Pylon6:
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (6, Weapons.FAB_100)
        SAB_100 = (6, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (6, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (6, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (6, Weapons.BetAB_500)
        BetAB_500ShP = (6, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (6, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (6, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_29L_ = (6, Weapons.Kh_29L_)
        S_25L = (6, Weapons.S_25L)
        UB_32A___32_S_5KO = (6, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (6, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (6, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (6, Weapons.S_24B_)
        S_25_OFM = (6, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (6, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (6, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1_Gun_pod = (6, Weapons.SPPU_22_1_Gun_pod)

    class Pylon7:
        B_8M1___20_S_8OFP2 = (7, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (7, Weapons.FAB_100)
        SAB_100 = (7, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (7, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (7, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (7, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (7, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (7, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (7, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (7, Weapons.BetAB_500)
        BetAB_500ShP = (7, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (7, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (7, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25ML_ = (7, Weapons.Kh_25ML_)
        S_25L = (7, Weapons.S_25L)
        UB_32A___32_S_5KO = (7, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (7, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (7, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (7, Weapons.S_24B_)
        S_25_OFM = (7, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (7, Weapons.B_8M1___20_S_8TsM)
        SPPU_22_1_Gun_pod = (7, Weapons.SPPU_22_1_Gun_pod)

    class Pylon8:
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (8, Weapons.FAB_100)
        SAB_100 = (8, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (8, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (8, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (8, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (8, Weapons.BetAB_500)
        BetAB_500ShP = (8, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (8, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (8, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25ML_ = (8, Weapons.Kh_25ML_)
        S_25L = (8, Weapons.S_25L)
        UB_32A___32_S_5KO = (8, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (8, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (8, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (8, Weapons.S_24B_)
        S_25_OFM = (8, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (8, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (8, Weapons.Fuel_tank_800L_Wing)
        SPS_141 = (8, Weapons.SPS_141)

    class Pylon9:
        B_8M1___20_S_8OFP2 = (9, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (9, Weapons.FAB_100)
        SAB_100 = (9, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (9, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (9, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (9, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (9, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (9, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (9, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (9, Weapons.BetAB_500)
        BetAB_500ShP = (9, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (9, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (9, Weapons.KMGU_2___96_PTAB_2_5KO)
        UB_32A___32_S_5KO = (9, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (9, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (9, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (9, Weapons.S_24B_)
        S_25_OFM = (9, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (9, Weapons.B_8M1___20_S_8TsM)
        S_25L = (9, Weapons.S_25L)

    class Pylon10:
        R_60M = (10, Weapons.R_60M)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Su_25TM(PlaneType):
    id = "Su-25TM"
    height = 5.2
    width = 14.36
    length = 15.35
    fuel_max = 3790
    max_speed = 950
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_60M = (1, Weapons.R_60M)
        MPS_410 = (1, Weapons.MPS_410)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (2, Weapons.FAB_100)
        SAB_100 = (2, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (2, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (2, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (2, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (2, Weapons.S_24B_)
        S_25_OFM = (2, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)
        S_25L = (2, Weapons.S_25L)
        R_73_ = (2, Weapons.R_73_)
        R_77_ = (2, Weapons.R_77_)

    class Pylon3:
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (3, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (3, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25MPU_ = (3, Weapons.Kh_25MPU_)
        Kh_25ML_ = (3, Weapons.Kh_25ML_)
        S_25L = (3, Weapons.S_25L)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (3, Weapons.S_24B_)
        S_25_OFM = (3, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (3, Weapons.Fuel_tank_800L_Wing)

    class Pylon4:
        B_8M1___20_S_8OFP2 = (4, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (4, Weapons.FAB_100)
        SAB_100 = (4, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (4, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (4, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (4, Weapons.BetAB_500)
        BetAB_500ShP = (4, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25MPU_ = (4, Weapons.Kh_25MPU_)
        Kh_25ML_ = (4, Weapons.Kh_25ML_)
        APU_8___8_9A4172_Vikhr = (4, Weapons.APU_8___8_9A4172_Vikhr)
        S_25L = (4, Weapons.S_25L)
        UB_32A___32_S_5KO = (4, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (4, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (4, Weapons.S_24B_)
        S_25_OFM = (4, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (4, Weapons.B_8M1___20_S_8TsM)
        SPPU_22_1_Gun_pod = (4, Weapons.SPPU_22_1_Gun_pod)

    class Pylon5:
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (5, Weapons.FAB_100)
        SAB_100 = (5, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (5, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (5, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        KAB_500kr = (5, Weapons.KAB_500kr)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (5, Weapons.BetAB_500)
        BetAB_500ShP = (5, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (5, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (5, Weapons.KMGU_2___96_PTAB_2_5KO)
        S_25L = (5, Weapons.S_25L)
        Kh_29L_ = (5, Weapons.Kh_29L_)
        Kh_29T_ = (5, Weapons.Kh_29T_)
        Kh_58U_ = (5, Weapons.Kh_58U_)
        Kh_31A_ = (5, Weapons.Kh_31A_)
        Kh_31P_ = (5, Weapons.Kh_31P_)
        Kh_35_ = (5, Weapons.Kh_35_)
        UB_32A___32_S_5KO = (5, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (5, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (5, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (5, Weapons.S_24B_)
        S_25_OFM = (5, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (5, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (5, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1_Gun_pod = (5, Weapons.SPPU_22_1_Gun_pod)

    class Pylon6:
        Mercury_LLTV_Pod = (6, Weapons.Mercury_LLTV_Pod)
        Kopyo_radar_pod = (6, Weapons.Kopyo_radar_pod)
        L_081_Fantasmagoria_ELINT_pod = (6, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon7:
        B_8M1___20_S_8OFP2 = (7, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (7, Weapons.FAB_100)
        SAB_100 = (7, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (7, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (7, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (7, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (7, Weapons.FAB_500_M62)
        KAB_500kr = (7, Weapons.KAB_500kr)
        RBK_500_PTAB_10_5 = (7, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (7, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (7, Weapons.BetAB_500)
        BetAB_500ShP = (7, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (7, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (7, Weapons.KMGU_2___96_PTAB_2_5KO)
        S_25L = (7, Weapons.S_25L)
        Kh_29L_ = (7, Weapons.Kh_29L_)
        Kh_29T_ = (7, Weapons.Kh_29T_)
        Kh_58U_ = (7, Weapons.Kh_58U_)
        Kh_31A_ = (7, Weapons.Kh_31A_)
        Kh_31P_ = (7, Weapons.Kh_31P_)
        Kh_35_ = (7, Weapons.Kh_35_)
        UB_32A___32_S_5KO = (7, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (7, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (7, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (7, Weapons.S_24B_)
        S_25_OFM = (7, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (7, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (7, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1_Gun_pod = (7, Weapons.SPPU_22_1_Gun_pod)

    class Pylon8:
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (8, Weapons.FAB_100)
        SAB_100 = (8, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (8, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (8, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (8, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (8, Weapons.BetAB_500)
        BetAB_500ShP = (8, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (8, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (8, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25MPU_ = (8, Weapons.Kh_25MPU_)
        Kh_25ML_ = (8, Weapons.Kh_25ML_)
        APU_8___8_9A4172_Vikhr = (8, Weapons.APU_8___8_9A4172_Vikhr)
        S_25L = (8, Weapons.S_25L)
        UB_32A___32_S_5KO = (8, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (8, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (8, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (8, Weapons.S_24B_)
        S_25_OFM = (8, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (8, Weapons.B_8M1___20_S_8TsM)
        SPPU_22_1_Gun_pod = (8, Weapons.SPPU_22_1_Gun_pod)

    class Pylon9:
        B_8M1___20_S_8OFP2 = (9, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (9, Weapons.FAB_100)
        SAB_100 = (9, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (9, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (9, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (9, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (9, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (9, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (9, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (9, Weapons.BetAB_500)
        BetAB_500ShP = (9, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (9, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (9, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25MPU_ = (9, Weapons.Kh_25MPU_)
        Kh_25ML_ = (9, Weapons.Kh_25ML_)
        S_25L = (9, Weapons.S_25L)
        UB_32A___32_S_5KO = (9, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (9, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (9, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (9, Weapons.S_24B_)
        S_25_OFM = (9, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (9, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (9, Weapons.Fuel_tank_800L_Wing)

    class Pylon10:
        B_8M1___20_S_8OFP2 = (10, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (10, Weapons.FAB_100)
        SAB_100 = (10, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (10, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (10, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (10, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (10, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (10, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (10, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (10, Weapons.BetAB_500)
        BetAB_500ShP = (10, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (10, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (10, Weapons.KMGU_2___96_PTAB_2_5KO)
        UB_32A___32_S_5KO = (10, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (10, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (10, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (10, Weapons.S_24B_)
        S_25_OFM = (10, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (10, Weapons.B_8M1___20_S_8TsM)
        S_25L = (10, Weapons.S_25L)
        R_73_ = (10, Weapons.R_73_)
        R_77_ = (10, Weapons.R_77_)

    class Pylon11:
        R_60M = (11, Weapons.R_60M)
        MPS_410_ = (11, Weapons.MPS_410_)
        Smoke_Generator___red = (11, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (11, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (11, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (11, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (11, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (11, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.SEAD, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Su_25T(PlaneType):
    id = "Su-25T"
    flyable = True
    height = 5.2
    width = 14.36
    length = 15.35
    fuel_max = 3790
    max_speed = 950
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    class Pylon1:
        R_60M = (1, Weapons.R_60M)
        MPS_410 = (1, Weapons.MPS_410)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (2, Weapons.FAB_100)
        SAB_100 = (2, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (2, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (2, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (2, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (2, Weapons.S_24B_)
        S_25_OFM = (2, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)
        S_25L = (2, Weapons.S_25L)
        R_73_ = (2, Weapons.R_73_)

    class Pylon3:
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (3, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (3, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25MPU_ = (3, Weapons.Kh_25MPU_)
        Kh_25ML_ = (3, Weapons.Kh_25ML_)
        S_25L = (3, Weapons.S_25L)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (3, Weapons.S_24B_)
        S_25_OFM = (3, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (3, Weapons.Fuel_tank_800L_Wing)

    class Pylon4:
        B_8M1___20_S_8OFP2 = (4, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (4, Weapons.FAB_100)
        SAB_100 = (4, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (4, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (4, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (4, Weapons.BetAB_500)
        BetAB_500ShP = (4, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25MPU_ = (4, Weapons.Kh_25MPU_)
        Kh_25ML_ = (4, Weapons.Kh_25ML_)
        APU_8___8_9A4172_Vikhr = (4, Weapons.APU_8___8_9A4172_Vikhr)
        S_25L = (4, Weapons.S_25L)
        UB_32A___32_S_5KO = (4, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (4, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (4, Weapons.S_24B_)
        S_25_OFM = (4, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (4, Weapons.B_8M1___20_S_8TsM)
        SPPU_22_1_Gun_pod = (4, Weapons.SPPU_22_1_Gun_pod)

    class Pylon5:
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (5, Weapons.FAB_100)
        SAB_100 = (5, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (5, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (5, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        KAB_500kr = (5, Weapons.KAB_500kr)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (5, Weapons.BetAB_500)
        BetAB_500ShP = (5, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (5, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (5, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_29L_ = (5, Weapons.Kh_29L_)
        Kh_29T_ = (5, Weapons.Kh_29T_)
        Kh_58U_ = (5, Weapons.Kh_58U_)
        S_25L = (5, Weapons.S_25L)
        UB_32A___32_S_5KO = (5, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (5, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (5, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (5, Weapons.S_24B_)
        S_25_OFM = (5, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (5, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (5, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1_Gun_pod = (5, Weapons.SPPU_22_1_Gun_pod)

    class Pylon6:
        Mercury_LLTV_Pod = (6, Weapons.Mercury_LLTV_Pod)
        L_081_Fantasmagoria_ELINT_pod = (6, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon7:
        B_8M1___20_S_8OFP2 = (7, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (7, Weapons.FAB_100)
        SAB_100 = (7, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (7, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (7, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (7, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (7, Weapons.FAB_500_M62)
        KAB_500kr = (7, Weapons.KAB_500kr)
        RBK_500_PTAB_10_5 = (7, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (7, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (7, Weapons.BetAB_500)
        BetAB_500ShP = (7, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (7, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (7, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_29L_ = (7, Weapons.Kh_29L_)
        Kh_29T_ = (7, Weapons.Kh_29T_)
        Kh_58U_ = (7, Weapons.Kh_58U_)
        S_25L = (7, Weapons.S_25L)
        UB_32A___32_S_5KO = (7, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (7, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (7, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (7, Weapons.S_24B_)
        S_25_OFM = (7, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (7, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (7, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1_Gun_pod = (7, Weapons.SPPU_22_1_Gun_pod)

    class Pylon8:
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (8, Weapons.FAB_100)
        SAB_100 = (8, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (8, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (8, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (8, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (8, Weapons.BetAB_500)
        BetAB_500ShP = (8, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (8, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (8, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25MPU_ = (8, Weapons.Kh_25MPU_)
        Kh_25ML_ = (8, Weapons.Kh_25ML_)
        APU_8___8_9A4172_Vikhr = (8, Weapons.APU_8___8_9A4172_Vikhr)
        S_25L = (8, Weapons.S_25L)
        UB_32A___32_S_5KO = (8, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (8, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (8, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (8, Weapons.S_24B_)
        S_25_OFM = (8, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (8, Weapons.B_8M1___20_S_8TsM)
        SPPU_22_1_Gun_pod = (8, Weapons.SPPU_22_1_Gun_pod)

    class Pylon9:
        B_8M1___20_S_8OFP2 = (9, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (9, Weapons.FAB_100)
        SAB_100 = (9, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (9, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (9, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (9, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (9, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (9, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (9, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (9, Weapons.BetAB_500)
        BetAB_500ShP = (9, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (9, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (9, Weapons.KMGU_2___96_PTAB_2_5KO)
        Kh_25MPU_ = (9, Weapons.Kh_25MPU_)
        Kh_25ML_ = (9, Weapons.Kh_25ML_)
        S_25L = (9, Weapons.S_25L)
        UB_32A___32_S_5KO = (9, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (9, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (9, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (9, Weapons.S_24B_)
        S_25_OFM = (9, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (9, Weapons.B_8M1___20_S_8TsM)
        Fuel_tank_800L_Wing = (9, Weapons.Fuel_tank_800L_Wing)

    class Pylon10:
        B_8M1___20_S_8OFP2 = (10, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (10, Weapons.FAB_100)
        SAB_100 = (10, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100_ = (10, Weapons.MBD_2_67U___4_FAB_100_)
        FAB_250 = (10, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (10, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (10, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (10, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (10, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (10, Weapons.BetAB_500)
        BetAB_500ShP = (10, Weapons.BetAB_500ShP)
        KMGU_2___96_AO_2_5RT = (10, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (10, Weapons.KMGU_2___96_PTAB_2_5KO)
        UB_32A___32_S_5KO = (10, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (10, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (10, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (10, Weapons.S_24B_)
        S_25_OFM = (10, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (10, Weapons.B_8M1___20_S_8TsM)
        S_25L = (10, Weapons.S_25L)
        R_73_ = (10, Weapons.R_73_)

    class Pylon11:
        R_60M = (11, Weapons.R_60M)
        MPS_410_ = (11, Weapons.MPS_410_)
        Smoke_Generator___red = (11, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (11, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (11, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (11, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (11, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (11, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.SEAD, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Su_33(PlaneType):
    id = "Su-33"
    flyable = True
    height = 5.72
    width = 14.7
    length = 21.18
    fuel_max = 9400
    max_speed = 2300
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"
    radio_frequency = 124

    class Pylon1:
        R_73 = (1, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73 = (2, Weapons.R_73)
        FAB_250 = (2, Weapons.FAB_250)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)

    class Pylon3:
        R_73 = (3, Weapons.R_73)
        R_27R = (3, Weapons.R_27R)
        R_27T = (3, Weapons.R_27T)
        R_27ET = (3, Weapons.R_27ET)
        R_27ER = (3, Weapons.R_27ER)
        FAB_250 = (3, Weapons.FAB_250)
        BetAB_500 = (3, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        S_25_OFM = (3, Weapons.S_25_OFM)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)

    class Pylon4:
        R_27R = (4, Weapons.R_27R)
        R_27ER = (4, Weapons.R_27ER)
        FAB_250 = (4, Weapons.FAB_250)
        BetAB_500 = (4, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        B_8M1___20_S_8KOM = (4, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        S_25_OFM = (4, Weapons.S_25_OFM)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (4, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (4, Weapons.B_8M1___20_S_8TsM)

    class Pylon5:
        R_27R = (5, Weapons.R_27R)
        R_27ER = (5, Weapons.R_27ER)
        FAB_250 = (5, Weapons.FAB_250)
        BetAB_500 = (5, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (5, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (5, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)

    class Pylon6:
        R_27R = (6, Weapons.R_27R)
        R_27ER = (6, Weapons.R_27ER)
        FAB_250 = (6, Weapons.FAB_250)
        BetAB_500 = (6, Weapons.BetAB_500)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)

    class Pylon7:
        R_27R = (7, Weapons.R_27R)
        R_27ER = (7, Weapons.R_27ER)
        FAB_250 = (7, Weapons.FAB_250)
        BetAB_500 = (7, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (7, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (7, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (7, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (7, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (7, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (7, Weapons.FAB_500_M62)

    class Pylon8:
        R_27R = (8, Weapons.R_27R)
        R_27ER = (8, Weapons.R_27ER)
        FAB_250 = (8, Weapons.FAB_250)
        BetAB_500 = (8, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (8, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (8, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (8, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        Smoke_Generator___red = (8, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (8, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (8, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (8, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (8, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (8, Weapons.Smoke_Generator___orange)

    class Pylon9:
        R_27R = (9, Weapons.R_27R)
        R_27ER = (9, Weapons.R_27ER)
        FAB_250 = (9, Weapons.FAB_250)
        BetAB_500 = (9, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (9, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (9, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (9, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (9, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (9, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (9, Weapons.FAB_500_M62)
        B_8M1___20_S_8KOM = (9, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (9, Weapons.B_13L___5_S_13_OF)
        S_25_OFM = (9, Weapons.S_25_OFM)
        Smoke_Generator___red = (9, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (9, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (9, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (9, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (9, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (9, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (9, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (9, Weapons.B_8M1___20_S_8TsM)

    class Pylon10:
        R_73 = (10, Weapons.R_73)
        R_27R = (10, Weapons.R_27R)
        R_27T = (10, Weapons.R_27T)
        R_27ET = (10, Weapons.R_27ET)
        R_27ER = (10, Weapons.R_27ER)
        FAB_250 = (10, Weapons.FAB_250)
        BetAB_500 = (10, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (10, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (10, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (10, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (10, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (10, Weapons.RBK_500U_PTAB_1M)
        FAB_500_M62 = (10, Weapons.FAB_500_M62)
        B_8M1___20_S_8KOM = (10, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (10, Weapons.B_13L___5_S_13_OF)
        S_25_OFM = (10, Weapons.S_25_OFM)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (10, Weapons.B_8M1___20_S_8OFP2)
        B_8M1___20_S_8TsM = (10, Weapons.B_8M1___20_S_8TsM)

    class Pylon11:
        R_73 = (11, Weapons.R_73)
        FAB_250 = (11, Weapons.FAB_250)
        Smoke_Generator___red = (11, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (11, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (11, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (11, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (11, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (11, Weapons.Smoke_Generator___orange)

    class Pylon12:
        R_73 = (12, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__right_ = (12, Weapons.L005_Sorbtsiya_ECM_pod__right_)
        Smoke_Generator___red = (12, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (12, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (12, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (12, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (12, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (12, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.CAS, task.GroundAttack, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class MiG_25PD(PlaneType):
    id = "MiG-25PD"
    height = 6.1
    width = 14
    length = 23.82
    fuel_max = 15245
    max_speed = 3000
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_40R = (1, Weapons.R_40R)
        R_40T = (1, Weapons.R_40T)
        R_60M = (1, Weapons.R_60M)

    class Pylon2:
        R_40R = (2, Weapons.R_40R)
        R_40T = (2, Weapons.R_40T)

    class Pylon3:
        R_40R = (3, Weapons.R_40R)
        R_40T = (3, Weapons.R_40T)

    class Pylon4:
        R_40R = (4, Weapons.R_40R)
        R_40T = (4, Weapons.R_40T)
        R_60M = (4, Weapons.R_60M)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.Intercept


class MiG_25RBT(PlaneType):
    id = "MiG-25RBT"
    height = 6.1
    width = 14
    length = 23.82
    fuel_max = 15245
    max_speed = 3000

    class Pylon1:
        R_60M = (1, Weapons.R_60M)
        FAB_100 = (1, Weapons.FAB_100)
        SAB_100 = (1, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100 = (1, Weapons.MBD_2_67U___4_FAB_100)
        FAB_250 = (1, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (1, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (1, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (1, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (1, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (1, Weapons.BetAB_500)
        BetAB_500ShP = (1, Weapons.BetAB_500ShP)

    class Pylon2:
        FAB_100 = (2, Weapons.FAB_100)
        SAB_100 = (2, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100 = (2, Weapons.MBD_2_67U___4_FAB_100)
        FAB_250 = (2, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)

    class Pylon3:
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100 = (3, Weapons.MBD_2_67U___4_FAB_100)
        FAB_250 = (3, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)

    class Pylon4:
        R_60M = (4, Weapons.R_60M)
        FAB_100 = (4, Weapons.FAB_100)
        SAB_100 = (4, Weapons.SAB_100)
        MBD_2_67U___4_FAB_100 = (4, Weapons.MBD_2_67U___4_FAB_100)
        FAB_250 = (4, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (4, Weapons.BetAB_500)
        BetAB_500ShP = (4, Weapons.BetAB_500ShP)

    pylons = {1, 2, 3, 4}

    tasks = [task.Reconnaissance, task.AFAC, task.GroundAttack]
    task_default = task.Reconnaissance


class Su_30(PlaneType):
    id = "Su-30"
    height = 6.36
    width = 14.7
    length = 21.9
    fuel_max = 9400
    max_speed = 2200
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_73 = (1, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73 = (2, Weapons.R_73)
        R_77 = (2, Weapons.R_77)

    class Pylon3:
        R_27R = (3, Weapons.R_27R)
        R_27ER = (3, Weapons.R_27ER)
        R_27T = (3, Weapons.R_27T)
        R_27ET = (3, Weapons.R_27ET)
        R_77 = (3, Weapons.R_77)
        R_73 = (3, Weapons.R_73)
        Kh_31P = (3, Weapons.Kh_31P)
        Kh_31A = (3, Weapons.Kh_31A)
        Kh_29L = (3, Weapons.Kh_29L)
        Kh_29T = (3, Weapons.Kh_29T)
        Kh_59M = (3, Weapons.Kh_59M)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        S_25_OFM = (3, Weapons.S_25_OFM)
        BetAB_500 = (3, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (3, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        KAB_500L = (3, Weapons.KAB_500L)
        KAB_500kr = (3, Weapons.KAB_500kr)
        FAB_1500_M54 = (3, Weapons.FAB_1500_M54)
        KAB_1500L = (3, Weapons.KAB_1500L)
        MER_6_FAB_250 = (3, Weapons.MER_6_FAB_250)

    class Pylon4:
        R_27R = (4, Weapons.R_27R)
        R_27ER = (4, Weapons.R_27ER)
        R_27ET = (4, Weapons.R_27ET)
        R_77 = (4, Weapons.R_77)
        Kh_31P = (4, Weapons.Kh_31P)
        Kh_31A = (4, Weapons.Kh_31A)
        Kh_29L = (4, Weapons.Kh_29L)
        Kh_29T = (4, Weapons.Kh_29T)
        BetAB_500 = (4, Weapons.BetAB_500)
        FAB_250 = (4, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        KAB_500L = (4, Weapons.KAB_500L)
        KAB_500kr = (4, Weapons.KAB_500kr)
        MER_6_FAB_250 = (4, Weapons.MER_6_FAB_250)

    class Pylon5:
        R_27R = (5, Weapons.R_27R)
        R_27ER = (5, Weapons.R_27ER)
        R_77 = (5, Weapons.R_77)
        Kh_35 = (5, Weapons.Kh_35)
        BetAB_500 = (5, Weapons.BetAB_500)
        FAB_250 = (5, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        KAB_500L = (5, Weapons.KAB_500L)
        KAB_500kr = (5, Weapons.KAB_500kr)
        KAB_1500L = (5, Weapons.KAB_1500L)
        MER_6_FAB_250 = (5, Weapons.MER_6_FAB_250)

    class Pylon6:
        R_27R = (6, Weapons.R_27R)
        R_27ER = (6, Weapons.R_27ER)
        R_77 = (6, Weapons.R_77)
        Kh_35 = (6, Weapons.Kh_35)
        BetAB_500 = (6, Weapons.BetAB_500)
        FAB_250 = (6, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        KAB_500L = (6, Weapons.KAB_500L)
        KAB_500kr = (6, Weapons.KAB_500kr)
        MER_6_FAB_250 = (6, Weapons.MER_6_FAB_250)

    class Pylon7:
        R_27R = (7, Weapons.R_27R)
        R_27ER = (7, Weapons.R_27ER)
        R_27ET = (7, Weapons.R_27ET)
        R_77 = (7, Weapons.R_77)
        Kh_31P = (7, Weapons.Kh_31P)
        Kh_31A = (7, Weapons.Kh_31A)
        Kh_29L = (7, Weapons.Kh_29L)
        Kh_29T = (7, Weapons.Kh_29T)
        BetAB_500 = (7, Weapons.BetAB_500)
        FAB_250 = (7, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (7, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (7, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (7, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (7, Weapons.RBK_500U_PTAB_1M)
        KAB_500L = (7, Weapons.KAB_500L)
        KAB_500kr = (7, Weapons.KAB_500kr)
        MER_6_FAB_250 = (7, Weapons.MER_6_FAB_250)

    class Pylon8:
        R_27R = (8, Weapons.R_27R)
        R_27ER = (8, Weapons.R_27ER)
        R_27T = (8, Weapons.R_27T)
        R_27ET = (8, Weapons.R_27ET)
        R_77 = (8, Weapons.R_77)
        R_73 = (8, Weapons.R_73)
        Kh_31P = (8, Weapons.Kh_31P)
        Kh_31A = (8, Weapons.Kh_31A)
        Kh_29L = (8, Weapons.Kh_29L)
        Kh_29T = (8, Weapons.Kh_29T)
        Kh_59M = (8, Weapons.Kh_59M)
        B_8M1___20_S_8KOM = (8, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (8, Weapons.B_13L___5_S_13_OF)
        S_25_OFM = (8, Weapons.S_25_OFM)
        BetAB_500 = (8, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (8, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (8, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (8, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (8, Weapons.RBK_250_PTAB_2_5M)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        KAB_500L = (8, Weapons.KAB_500L)
        KAB_500kr = (8, Weapons.KAB_500kr)
        FAB_1500_M54 = (8, Weapons.FAB_1500_M54)
        KAB_1500L = (8, Weapons.KAB_1500L)
        MER_6_FAB_250 = (8, Weapons.MER_6_FAB_250)

    class Pylon9:
        R_73 = (9, Weapons.R_73)
        R_77 = (9, Weapons.R_77)

    class Pylon10:
        R_73 = (10, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__right_ = (10, Weapons.L005_Sorbtsiya_ECM_pod__right_)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.SEAD, task.AntishipStrike, task.CAS, task.PinpointStrike, task.GroundAttack, task.RunwayAttack]
    task_default = task.CAP


class Su_34(PlaneType):
    id = "Su-34"
    height = 6
    width = 14.7
    length = 23.3
    fuel_max = 9800
    max_speed = 1900
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_73 = (1, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)

    class Pylon2:
        R_73 = (2, Weapons.R_73)
        R_77 = (2, Weapons.R_77)
        FAB_250 = (2, Weapons.FAB_250)

    class Pylon3:
        R_73 = (3, Weapons.R_73)
        R_77 = (3, Weapons.R_77)
        Kh_25MPU = (3, Weapons.Kh_25MPU)
        Kh_25ML = (3, Weapons.Kh_25ML)
        Kh_25MR = (3, Weapons.Kh_25MR)
        Kh_29T = (3, Weapons.Kh_29T)
        Kh_31A = (3, Weapons.Kh_31A)
        Kh_31P = (3, Weapons.Kh_31P)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        BetAB_500 = (3, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        KAB_500L = (3, Weapons.KAB_500L)
        KAB_500kr = (3, Weapons.KAB_500kr)
        KAB_1500L = (3, Weapons.KAB_1500L)
        MER_3_3_RBK_250_PTAB_1M = (3, Weapons.MER_3_3_RBK_250_PTAB_1M)
        MER_3_3_RBK_500_PTAB_2_5M = (3, Weapons.MER_3_3_RBK_500_PTAB_2_5M)
        MER_3_3_FAB_100 = (3, Weapons.MER_3_3_FAB_100)
        MER_3_3_FAB_250 = (3, Weapons.MER_3_3_FAB_250)
        MER_3_3_FAB_500 = (3, Weapons.MER_3_3_FAB_500)
        MER_3_3_BetAB_500 = (3, Weapons.MER_3_3_BetAB_500)
        SAB_100 = (3, Weapons.SAB_100)

    class Pylon4:
        R_77 = (4, Weapons.R_77)
        Kh_25MPU = (4, Weapons.Kh_25MPU)
        Kh_25ML = (4, Weapons.Kh_25ML)
        Kh_25MR = (4, Weapons.Kh_25MR)
        Kh_29T = (4, Weapons.Kh_29T)
        Kh_29L = (4, Weapons.Kh_29L)
        Kh_31A = (4, Weapons.Kh_31A)
        Kh_31P = (4, Weapons.Kh_31P)
        Kh_59M = (4, Weapons.Kh_59M)
        B_8M1___20_S_8KOM = (4, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        BetAB_500 = (4, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        KAB_500L = (4, Weapons.KAB_500L)
        KAB_500kr = (4, Weapons.KAB_500kr)
        FAB_1500_M54 = (4, Weapons.FAB_1500_M54)
        KAB_1500L = (4, Weapons.KAB_1500L)
        MER_3_3_RBK_250_PTAB_1M = (4, Weapons.MER_3_3_RBK_250_PTAB_1M)
        MER_3_3_RBK_500_PTAB_2_5M = (4, Weapons.MER_3_3_RBK_500_PTAB_2_5M)
        MER_3_3_FAB_100 = (4, Weapons.MER_3_3_FAB_100)
        MER_3_3_FAB_250 = (4, Weapons.MER_3_3_FAB_250)
        MER_3_3_FAB_500 = (4, Weapons.MER_3_3_FAB_500)
        MER_3_3_BetAB_500 = (4, Weapons.MER_3_3_BetAB_500)
        MER_6_FAB_100 = (4, Weapons.MER_6_FAB_100)
        SAB_100 = (4, Weapons.SAB_100)

    class Pylon5:
        R_77 = (5, Weapons.R_77)
        Kh_25MPU = (5, Weapons.Kh_25MPU)
        Kh_25ML = (5, Weapons.Kh_25ML)
        Kh_25MR = (5, Weapons.Kh_25MR)
        Kh_29T = (5, Weapons.Kh_29T)
        Kh_29L = (5, Weapons.Kh_29L)
        Kh_31A = (5, Weapons.Kh_31A)
        Kh_31P = (5, Weapons.Kh_31P)
        BetAB_500 = (5, Weapons.BetAB_500)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        FAB_250 = (5, Weapons.FAB_250)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        KAB_500L = (5, Weapons.KAB_500L)
        KAB_500kr = (5, Weapons.KAB_500kr)
        MER_3_3_RBK_250_PTAB_1M = (5, Weapons.MER_3_3_RBK_250_PTAB_1M)
        MER_3_3_FAB_100 = (5, Weapons.MER_3_3_FAB_100)
        MER_3_3_FAB_250 = (5, Weapons.MER_3_3_FAB_250)
        MER_6_FAB_100 = (5, Weapons.MER_6_FAB_100)
        SAB_100 = (5, Weapons.SAB_100)

    class Pylon6:
        R_77 = (6, Weapons.R_77)
        BetAB_500 = (6, Weapons.BetAB_500)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        FAB_250 = (6, Weapons.FAB_250)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        FAB_1500_M54 = (6, Weapons.FAB_1500_M54)
        KAB_500L = (6, Weapons.KAB_500L)
        KAB_500kr = (6, Weapons.KAB_500kr)
        KAB_1500L = (6, Weapons.KAB_1500L)
        MER_3_3_RBK_250_PTAB_1M = (6, Weapons.MER_3_3_RBK_250_PTAB_1M)
        MER_3_3_RBK_500_PTAB_2_5M = (6, Weapons.MER_3_3_RBK_500_PTAB_2_5M)
        MER_3_3_FAB_100 = (6, Weapons.MER_3_3_FAB_100)
        MER_3_3_FAB_250 = (6, Weapons.MER_3_3_FAB_250)
        MER_3_3_FAB_500 = (6, Weapons.MER_3_3_FAB_500)
        MER_3_3_BetAB_500 = (6, Weapons.MER_3_3_BetAB_500)
        SAB_100 = (6, Weapons.SAB_100)

    class Pylon7:
        R_77 = (7, Weapons.R_77)
        BetAB_500 = (7, Weapons.BetAB_500)
        RBK_250_PTAB_2_5M = (7, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (7, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (7, Weapons.RBK_500U_PTAB_1M)
        FAB_250 = (7, Weapons.FAB_250)
        FAB_500_M62 = (7, Weapons.FAB_500_M62)
        KAB_500L = (7, Weapons.KAB_500L)
        KAB_500kr = (7, Weapons.KAB_500kr)
        MER_3_3_RBK_250_PTAB_1M = (7, Weapons.MER_3_3_RBK_250_PTAB_1M)
        MER_3_3_RBK_500_PTAB_2_5M = (7, Weapons.MER_3_3_RBK_500_PTAB_2_5M)
        MER_3_3_FAB_100 = (7, Weapons.MER_3_3_FAB_100)
        MER_3_3_FAB_250 = (7, Weapons.MER_3_3_FAB_250)
        MER_3_3_FAB_500 = (7, Weapons.MER_3_3_FAB_500)
        MER_3_3_BetAB_500 = (7, Weapons.MER_3_3_BetAB_500)
        SAB_100 = (7, Weapons.SAB_100)

    class Pylon8:
        R_77 = (8, Weapons.R_77)
        Kh_25MPU = (8, Weapons.Kh_25MPU)
        Kh_25ML = (8, Weapons.Kh_25ML)
        Kh_25MR = (8, Weapons.Kh_25MR)
        Kh_29T = (8, Weapons.Kh_29T)
        Kh_29L = (8, Weapons.Kh_29L)
        Kh_31A = (8, Weapons.Kh_31A)
        Kh_31P = (8, Weapons.Kh_31P)
        BetAB_500 = (8, Weapons.BetAB_500)
        RBK_250_PTAB_2_5M = (8, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        FAB_250 = (8, Weapons.FAB_250)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        KAB_500L = (8, Weapons.KAB_500L)
        KAB_500kr = (8, Weapons.KAB_500kr)
        MER_3_3_RBK_250_PTAB_1M = (8, Weapons.MER_3_3_RBK_250_PTAB_1M)
        MER_3_3_FAB_100 = (8, Weapons.MER_3_3_FAB_100)
        MER_3_3_FAB_250 = (8, Weapons.MER_3_3_FAB_250)
        MER_6_FAB_100 = (8, Weapons.MER_6_FAB_100)
        SAB_100 = (8, Weapons.SAB_100)

    class Pylon9:
        R_77 = (9, Weapons.R_77)
        Kh_25MPU = (9, Weapons.Kh_25MPU)
        Kh_25ML = (9, Weapons.Kh_25ML)
        Kh_25MR = (9, Weapons.Kh_25MR)
        Kh_29T = (9, Weapons.Kh_29T)
        Kh_29L = (9, Weapons.Kh_29L)
        Kh_31A = (9, Weapons.Kh_31A)
        Kh_31P = (9, Weapons.Kh_31P)
        Kh_59M = (9, Weapons.Kh_59M)
        B_8M1___20_S_8KOM = (9, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (9, Weapons.B_13L___5_S_13_OF)
        BetAB_500 = (9, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (9, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (9, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (9, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (9, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (9, Weapons.RBK_500U_PTAB_1M)
        FAB_250 = (9, Weapons.FAB_250)
        FAB_500_M62 = (9, Weapons.FAB_500_M62)
        KAB_500L = (9, Weapons.KAB_500L)
        KAB_500kr = (9, Weapons.KAB_500kr)
        FAB_1500_M54 = (9, Weapons.FAB_1500_M54)
        KAB_1500L = (9, Weapons.KAB_1500L)
        MER_3_3_RBK_250_PTAB_1M = (9, Weapons.MER_3_3_RBK_250_PTAB_1M)
        MER_3_3_RBK_500_PTAB_2_5M = (9, Weapons.MER_3_3_RBK_500_PTAB_2_5M)
        MER_3_3_FAB_100 = (9, Weapons.MER_3_3_FAB_100)
        MER_3_3_FAB_250 = (9, Weapons.MER_3_3_FAB_250)
        MER_3_3_FAB_500 = (9, Weapons.MER_3_3_FAB_500)
        MER_3_3_BetAB_500 = (9, Weapons.MER_3_3_BetAB_500)
        MER_6_FAB_100 = (9, Weapons.MER_6_FAB_100)
        SAB_100 = (9, Weapons.SAB_100)

    class Pylon10:
        R_73 = (10, Weapons.R_73)
        R_77 = (10, Weapons.R_77)
        Kh_25MPU = (10, Weapons.Kh_25MPU)
        Kh_25ML = (10, Weapons.Kh_25ML)
        Kh_25MR = (10, Weapons.Kh_25MR)
        Kh_29T = (10, Weapons.Kh_29T)
        Kh_31A = (10, Weapons.Kh_31A)
        Kh_31P = (10, Weapons.Kh_31P)
        BetAB_500 = (10, Weapons.BetAB_500)
        KMGU_2___96_AO_2_5RT = (10, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (10, Weapons.KMGU_2___96_PTAB_2_5KO)
        RBK_250_PTAB_2_5M = (10, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (10, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (10, Weapons.RBK_500U_PTAB_1M)
        FAB_250 = (10, Weapons.FAB_250)
        FAB_500_M62 = (10, Weapons.FAB_500_M62)
        KAB_500L = (10, Weapons.KAB_500L)
        KAB_500kr = (10, Weapons.KAB_500kr)
        KAB_1500L = (10, Weapons.KAB_1500L)
        MER_3_3_RBK_250_PTAB_1M = (10, Weapons.MER_3_3_RBK_250_PTAB_1M)
        MER_3_3_RBK_500_PTAB_2_5M = (10, Weapons.MER_3_3_RBK_500_PTAB_2_5M)
        MER_3_3_FAB_100 = (10, Weapons.MER_3_3_FAB_100)
        MER_3_3_FAB_250 = (10, Weapons.MER_3_3_FAB_250)
        MER_3_3_FAB_500 = (10, Weapons.MER_3_3_FAB_500)
        MER_3_3_BetAB_500 = (10, Weapons.MER_3_3_BetAB_500)
        SAB_100 = (10, Weapons.SAB_100)
        B_8M1___20_S_8KOM = (10, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (10, Weapons.B_13L___5_S_13_OF)

    class Pylon11:
        R_73 = (11, Weapons.R_73)
        R_77 = (11, Weapons.R_77)
        FAB_250 = (11, Weapons.FAB_250)

    class Pylon12:
        R_73 = (12, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__right_ = (12, Weapons.L005_Sorbtsiya_ECM_pod__right_)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.AFAC, task.SEAD, task.AntishipStrike, task.CAS, task.PinpointStrike, task.GroundAttack, task.RunwayAttack]
    task_default = task.GroundAttack


class Su_17M4(PlaneType):
    id = "Su-17M4"
    height = 5.129
    width = 13.68
    length = 19.26
    fuel_max = 3770
    max_speed = 1860
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        B_8M1___20_S_8OFP2 = (1, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (1, Weapons.FAB_100)
        SAB_100 = (1, Weapons.SAB_100)
        FAB_500_M62 = (1, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (1, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (1, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (1, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (1, Weapons.KMGU_2___96_PTAB_2_5KO)
        BetAB_500 = (1, Weapons.BetAB_500)
        BetAB_500ShP = (1, Weapons.BetAB_500ShP)
        MER_4_FAB_250 = (1, Weapons.MER_4_FAB_250)
        MER_6_FAB_100 = (1, Weapons.MER_6_FAB_100)
        MBD_2_67U___4_FAB_100 = (1, Weapons.MBD_2_67U___4_FAB_100)
        MER_4_RBK_250_PTAB_1M = (1, Weapons.MER_4_RBK_250_PTAB_1M)
        MER_6_FAB_100 = (1, Weapons.MER_6_FAB_100)
        MER_6_2_FAB_250 = (1, Weapons.MER_6_2_FAB_250)
        Kh_25ML = (1, Weapons.Kh_25ML)
        Kh_25MPU = (1, Weapons.Kh_25MPU)
        Kh_25MR = (1, Weapons.Kh_25MR)
        Fuel_tank_1150L = (1, Weapons.Fuel_tank_1150L)
        UB_32A___32_S_5KO = (1, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (1, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (1, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (1, Weapons.S_24B_)
        S_25_OFM = (1, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (1, Weapons.B_8M1___20_S_8TsM)

    class Pylon2:
        R_60M = (2, Weapons.R_60M)

    class Pylon3:
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)
        MER_4_FAB_250 = (3, Weapons.MER_4_FAB_250)
        MER_6_FAB_100 = (3, Weapons.MER_6_FAB_100)
        MBD_2_67U___4_FAB_100 = (3, Weapons.MBD_2_67U___4_FAB_100)
        MER_4_RBK_250_PTAB_1M = (3, Weapons.MER_4_RBK_250_PTAB_1M)
        MER_6_FAB_100 = (3, Weapons.MER_6_FAB_100)
        MER_6_2_FAB_250 = (3, Weapons.MER_6_2_FAB_250)
        MER_6_4_FAB_250 = (3, Weapons.MER_6_4_FAB_250)
        Kh_25ML = (3, Weapons.Kh_25ML)
        Kh_25MPU = (3, Weapons.Kh_25MPU)
        Kh_25MR = (3, Weapons.Kh_25MR)
        Kh_29L = (3, Weapons.Kh_29L)
        Kh_29T = (3, Weapons.Kh_29T)
        Kh_58U = (3, Weapons.Kh_58U)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (3, Weapons.S_24B_)
        S_25_OFM = (3, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        SPPU_22_1_Gun_pod = (3, Weapons.SPPU_22_1_Gun_pod)
        SPS_141 = (3, Weapons.SPS_141)

    class Pylon4:
        FAB_100 = (4, Weapons.FAB_100)
        SAB_100 = (4, Weapons.SAB_100)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (4, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        BetAB_500 = (4, Weapons.BetAB_500)
        BetAB_500ShP = (4, Weapons.BetAB_500ShP)
        MER_4_FAB_250 = (4, Weapons.MER_4_FAB_250)
        MBD_2_67U___4_FAB_100 = (4, Weapons.MBD_2_67U___4_FAB_100)
        MER_4_RBK_250_PTAB_1M = (4, Weapons.MER_4_RBK_250_PTAB_1M)
        MER_6_2_FAB_250 = (4, Weapons.MER_6_2_FAB_250)
        Fuel_tank_1150L = (4, Weapons.Fuel_tank_1150L)
        Fuel_tank_800L = (4, Weapons.Fuel_tank_800L)

    class Pylon5:
        FAB_100 = (5, Weapons.FAB_100)
        SAB_100 = (5, Weapons.SAB_100)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (5, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (5, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (5, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (5, Weapons.KMGU_2___96_PTAB_2_5KO)
        BetAB_500 = (5, Weapons.BetAB_500)
        BetAB_500ShP = (5, Weapons.BetAB_500ShP)
        MER_4_FAB_250 = (5, Weapons.MER_4_FAB_250)
        MBD_2_67U___4_FAB_100 = (5, Weapons.MBD_2_67U___4_FAB_100)
        MER_4_RBK_250_PTAB_1M = (5, Weapons.MER_4_RBK_250_PTAB_1M)
        MER_6_2_FAB_250 = (5, Weapons.MER_6_2_FAB_250)
        Fuel_tank_1150L = (5, Weapons.Fuel_tank_1150L)
        Fuel_tank_800L = (5, Weapons.Fuel_tank_800L)

    class Pylon6:
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (6, Weapons.FAB_100)
        SAB_100 = (6, Weapons.SAB_100)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (6, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (6, Weapons.KMGU_2___96_PTAB_2_5KO)
        BetAB_500 = (6, Weapons.BetAB_500)
        BetAB_500ShP = (6, Weapons.BetAB_500ShP)
        MER_4_FAB_250 = (6, Weapons.MER_4_FAB_250)
        MER_6_FAB_100 = (6, Weapons.MER_6_FAB_100)
        MBD_2_67U___4_FAB_100 = (6, Weapons.MBD_2_67U___4_FAB_100)
        MER_4_RBK_250_PTAB_1M = (6, Weapons.MER_4_RBK_250_PTAB_1M)
        MER_6_FAB_100 = (6, Weapons.MER_6_FAB_100)
        MER_6_4_FAB_250 = (6, Weapons.MER_6_4_FAB_250)
        Kh_25ML = (6, Weapons.Kh_25ML)
        Kh_25MPU = (6, Weapons.Kh_25MPU)
        Kh_25MR = (6, Weapons.Kh_25MR)
        Kh_29L = (6, Weapons.Kh_29L)
        Kh_29T = (6, Weapons.Kh_29T)
        Kh_58U = (6, Weapons.Kh_58U)
        UB_32A___32_S_5KO = (6, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (6, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (6, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (6, Weapons.S_24B_)
        S_25_OFM = (6, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (6, Weapons.B_8M1___20_S_8TsM)
        SPPU_22_1_Gun_pod = (6, Weapons.SPPU_22_1_Gun_pod)

    class Pylon7:
        R_60M = (7, Weapons.R_60M)

    class Pylon8:
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_100 = (8, Weapons.FAB_100)
        SAB_100 = (8, Weapons.SAB_100)
        FAB_500_M62 = (8, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (8, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (8, Weapons.RBK_500U_PTAB_1M)
        KMGU_2___96_AO_2_5RT = (8, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (8, Weapons.KMGU_2___96_PTAB_2_5KO)
        BetAB_500 = (8, Weapons.BetAB_500)
        BetAB_500ShP = (8, Weapons.BetAB_500ShP)
        MER_4_FAB_250 = (8, Weapons.MER_4_FAB_250)
        MER_6_2_FAB_250 = (8, Weapons.MER_6_2_FAB_250)
        MBD_2_67U___4_FAB_100 = (8, Weapons.MBD_2_67U___4_FAB_100)
        MER_6_FAB_100 = (8, Weapons.MER_6_FAB_100)
        MER_4_RBK_250_PTAB_1M = (8, Weapons.MER_4_RBK_250_PTAB_1M)
        MER_6_FAB_100 = (8, Weapons.MER_6_FAB_100)
        Kh_25ML = (8, Weapons.Kh_25ML)
        Kh_25MPU = (8, Weapons.Kh_25MPU)
        Kh_25MR = (8, Weapons.Kh_25MR)
        Fuel_tank_1150L = (8, Weapons.Fuel_tank_1150L)
        UB_32A___32_S_5KO = (8, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (8, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (8, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (8, Weapons.S_24B_)
        S_25_OFM = (8, Weapons.S_25_OFM)
        B_8M1___20_S_8TsM = (8, Weapons.B_8M1___20_S_8TsM)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.GroundAttack, task.CAS, task.PinpointStrike, task.SEAD, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.GroundAttack


class MiG_31(PlaneType):
    id = "MiG-31"
    height = 6.15
    width = 13.46
    length = 22.7
    fuel_max = 15500
    max_speed = 3000
    category = "Interceptor"

    class Pylon1:
        R_40R = (1, Weapons.R_40R)
        R_40T = (1, Weapons.R_40T)
        R_60M_2 = (1, Weapons.R_60M_2)

    class Pylon2:
        R_33 = (2, Weapons.R_33)

    class Pylon3:
        R_33 = (3, Weapons.R_33)

    class Pylon4:
        R_33 = (4, Weapons.R_33)

    class Pylon5:
        R_33 = (5, Weapons.R_33)

    class Pylon6:
        R_40R = (6, Weapons.R_40R)
        R_40T = (6, Weapons.R_40T)
        R_60M_2_ = (6, Weapons.R_60M_2_)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.Intercept


class Tu_95MS(PlaneType):
    id = "Tu-95MS"
    group_size_max = 1
    large_parking_slot = True
    height = 13.3
    width = 50.04
    length = 49.13
    fuel_max = 87000
    max_speed = 830
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        Kh_65_6 = (1, Weapons.Kh_65_6)

    pylons = {1}

    tasks = [task.PinpointStrike]
    task_default = task.PinpointStrike


class Su_24M(PlaneType):
    id = "Su-24M"
    height = 4.97
    width = 17.64
    length = 24.53
    fuel_max = 11700
    max_speed = 1700
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_60M_2 = (1, Weapons.R_60M_2)
        MER_6_FAB_100 = (1, Weapons.MER_6_FAB_100)
        RBK_250_PTAB_2_5M = (1, Weapons.RBK_250_PTAB_2_5M)
        SAB_100 = (1, Weapons.SAB_100)
        UB_32A___32_S_5KO = (1, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (1, Weapons.B_8M1___20_S_8KOM)
        FAB_250 = (1, Weapons.FAB_250)
        B_13L___5_S_13_OF = (1, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (1, Weapons.S_24B_)
        S_25_OFM = (1, Weapons.S_25_OFM)
        Kh_25ML = (1, Weapons.Kh_25ML)
        Kh_25MPU = (1, Weapons.Kh_25MPU)
        Kh_25MR = (1, Weapons.Kh_25MR)

    class Pylon2:
        MER_6_FAB_100 = (2, Weapons.MER_6_FAB_100)
        Kh_29L = (2, Weapons.Kh_29L)
        Kh_29T = (2, Weapons.Kh_29T)
        Kh_31A = (2, Weapons.Kh_31A)
        Kh_31P = (2, Weapons.Kh_31P)
        Kh_58U = (2, Weapons.Kh_58U)
        Kh_59M = (2, Weapons.Kh_59M)
        Kh_25ML = (2, Weapons.Kh_25ML)
        Kh_25MPU = (2, Weapons.Kh_25MPU)
        Kh_25MR = (2, Weapons.Kh_25MR)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (2, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)
        KAB_500L = (2, Weapons.KAB_500L)
        KAB_500kr = (2, Weapons.KAB_500kr)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        SAB_100 = (2, Weapons.SAB_100)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (2, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (2, Weapons.S_24B_)
        S_25_OFM = (2, Weapons.S_25_OFM)
        KAB_1500L = (2, Weapons.KAB_1500L)
        FAB_1500_M54 = (2, Weapons.FAB_1500_M54)
        Fuel_tank_3000L = (2, Weapons.Fuel_tank_3000L)

    class Pylon3:
        MER_6_FAB_100 = (3, Weapons.MER_6_FAB_100)
        RBK_250_PTAB_2_5M = (3, Weapons.RBK_250_PTAB_2_5M)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (3, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (3, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (3, Weapons.BetAB_500)
        BetAB_500ShP = (3, Weapons.BetAB_500ShP)
        KAB_500L = (3, Weapons.KAB_500L)
        KAB_500kr = (3, Weapons.KAB_500kr)
        SAB_100 = (3, Weapons.SAB_100)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (3, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (3, Weapons.S_24B_)

    class Pylon4:
        MER_6_FAB_100 = (4, Weapons.MER_6_FAB_100)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        FAB_250 = (4, Weapons.FAB_250)
        SAB_100 = (4, Weapons.SAB_100)
        KAB_1500L = (4, Weapons.KAB_1500L)
        FAB_1500_M54 = (4, Weapons.FAB_1500_M54)

    class Pylon5:
        Fuel_tank_2000L = (5, Weapons.Fuel_tank_2000L)
        L_081_Fantasmagoria_ELINT_pod = (5, Weapons.L_081_Fantasmagoria_ELINT_pod)
        FAB_250 = (5, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)

    class Pylon6:
        MER_6_FAB_100 = (6, Weapons.MER_6_FAB_100)
        RBK_250_PTAB_2_5M = (6, Weapons.RBK_250_PTAB_2_5M)
        FAB_250 = (6, Weapons.FAB_250)
        FAB_500_M62 = (6, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (6, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (6, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (6, Weapons.BetAB_500)
        BetAB_500ShP = (6, Weapons.BetAB_500ShP)
        KAB_500L = (6, Weapons.KAB_500L)
        KAB_500kr = (6, Weapons.KAB_500kr)
        SAB_100 = (6, Weapons.SAB_100)
        UB_32A___32_S_5KO = (6, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (6, Weapons.B_8M1___20_S_8KOM)
        S_24B_ = (6, Weapons.S_24B_)

    class Pylon7:
        MER_6_FAB_100 = (7, Weapons.MER_6_FAB_100)
        Kh_29L = (7, Weapons.Kh_29L)
        Kh_29T = (7, Weapons.Kh_29T)
        Kh_31A = (7, Weapons.Kh_31A)
        Kh_31P = (7, Weapons.Kh_31P)
        Kh_58U = (7, Weapons.Kh_58U)
        Kh_59M = (7, Weapons.Kh_59M)
        Kh_25ML = (7, Weapons.Kh_25ML)
        Kh_25MPU = (7, Weapons.Kh_25MPU)
        Kh_25MR = (7, Weapons.Kh_25MR)
        RBK_250_PTAB_2_5M = (7, Weapons.RBK_250_PTAB_2_5M)
        FAB_250 = (7, Weapons.FAB_250)
        FAB_500_M62 = (7, Weapons.FAB_500_M62)
        RBK_500_PTAB_10_5 = (7, Weapons.RBK_500_PTAB_10_5)
        RBK_500U_PTAB_1M = (7, Weapons.RBK_500U_PTAB_1M)
        BetAB_500 = (7, Weapons.BetAB_500)
        BetAB_500ShP = (7, Weapons.BetAB_500ShP)
        KAB_500L = (7, Weapons.KAB_500L)
        KAB_500kr = (7, Weapons.KAB_500kr)
        KMGU_2___96_AO_2_5RT = (7, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (7, Weapons.KMGU_2___96_PTAB_2_5KO)
        SAB_100 = (7, Weapons.SAB_100)
        UB_32A___32_S_5KO = (7, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (7, Weapons.B_8M1___20_S_8KOM)
        B_13L___5_S_13_OF = (7, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (7, Weapons.S_24B_)
        S_25_OFM = (7, Weapons.S_25_OFM)
        KAB_1500L = (7, Weapons.KAB_1500L)
        FAB_1500_M54 = (7, Weapons.FAB_1500_M54)
        Fuel_tank_3000L = (7, Weapons.Fuel_tank_3000L)

    class Pylon8:
        R_60M_2_ = (8, Weapons.R_60M_2_)
        MER_6_FAB_100 = (8, Weapons.MER_6_FAB_100)
        RBK_250_PTAB_2_5M = (8, Weapons.RBK_250_PTAB_2_5M)
        SAB_100 = (8, Weapons.SAB_100)
        UB_32A___32_S_5KO = (8, Weapons.UB_32A___32_S_5KO)
        B_8M1___20_S_8KOM = (8, Weapons.B_8M1___20_S_8KOM)
        FAB_250 = (8, Weapons.FAB_250)
        B_13L___5_S_13_OF = (8, Weapons.B_13L___5_S_13_OF)
        S_24B_ = (8, Weapons.S_24B_)
        S_25_OFM = (8, Weapons.S_25_OFM)
        Kh_25ML = (8, Weapons.Kh_25ML)
        Kh_25MPU = (8, Weapons.Kh_25MPU)
        Kh_25MR = (8, Weapons.Kh_25MR)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.GroundAttack, task.CAS, task.AntishipStrike, task.SEAD, task.PinpointStrike, task.AFAC, task.RunwayAttack]
    task_default = task.GroundAttack


class Su_24MR(PlaneType):
    id = "Su-24MR"
    height = 4.97
    width = 17.64
    length = 24.53
    fuel_max = 11700
    max_speed = 1700
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_60M_2 = (1, Weapons.R_60M_2)

    class Pylon2:
        Fuel_tank_3000L = (2, Weapons.Fuel_tank_3000L)

    class Pylon5:
        Fuel_tank_2000L = (5, Weapons.Fuel_tank_2000L)
        Tangazh_ELINT_pod = (5, Weapons.Tangazh_ELINT_pod)
        Shpil_2M_Laser_Intelligence_Pod = (5, Weapons.Shpil_2M_Laser_Intelligence_Pod)

    class Pylon7:
        Fuel_tank_3000L = (7, Weapons.Fuel_tank_3000L)

    class Pylon8:
        ETHER = (8, Weapons.ETHER)

    pylons = {1, 2, 5, 7, 8}

    tasks = [task.AFAC, task.Reconnaissance]
    task_default = task.Reconnaissance


class Tu_160(PlaneType):
    id = "Tu-160"
    group_size_max = 1
    large_parking_slot = True
    height = 13.25
    width = 55.7
    length = 54.1
    fuel_max = 157000
    max_speed = 2200
    chaff = 72
    flare = 72
    charge_total = 144
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        Kh_65_6 = (1, Weapons.Kh_65_6)

    class Pylon2:
        Kh_65_6 = (2, Weapons.Kh_65_6)

    pylons = {1, 2}

    tasks = [task.PinpointStrike]
    task_default = task.PinpointStrike


class F_117A(PlaneType):
    id = "F-117A"
    height = 3.78
    width = 13.2
    length = 20.08
    fuel_max = 3840
    max_speed = 1000

    class Pylon1:
        GBU_10 = (1, Weapons.GBU_10)
        GBU_12 = (1, Weapons.GBU_12)
        GBU_27 = (1, Weapons.GBU_27)

    class Pylon2:
        GBU_10 = (2, Weapons.GBU_10)
        GBU_12 = (2, Weapons.GBU_12)
        GBU_27 = (2, Weapons.GBU_27)

    pylons = {1, 2}

    tasks = [task.PinpointStrike]
    task_default = task.PinpointStrike


class B_1B(PlaneType):
    id = "B-1B"
    group_size_max = 1
    large_parking_slot = True
    height = 10.36
    width = 41.67
    length = 44.81
    fuel_max = 88450
    max_speed = 1530
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True

    class Pylon1:
        MK_82_28 = (1, Weapons.MK_82_28)
        CBU87_10 = (1, Weapons.CBU87_10)
        CBU97_10 = (1, Weapons.CBU97_10)
        B_1B_Mk_84_8 = (1, Weapons.B_1B_Mk_84_8)
        GBU_31_8 = (1, Weapons.GBU_31_8)
        GBU_31V3B_8 = (1, Weapons.GBU_31V3B_8)
        AGM_154C_4 = (1, Weapons.AGM_154C_4)
        GBU_38_16 = (1, Weapons.GBU_38_16)

    class Pylon2:
        MK_82_28 = (2, Weapons.MK_82_28)
        CBU87_10 = (2, Weapons.CBU87_10)
        CBU97_10 = (2, Weapons.CBU97_10)
        B_1B_Mk_84_8 = (2, Weapons.B_1B_Mk_84_8)
        GBU_31_8 = (2, Weapons.GBU_31_8)
        GBU_31V3B_8 = (2, Weapons.GBU_31V3B_8)
        AGM_154C_4 = (2, Weapons.AGM_154C_4)
        GBU_38_16 = (2, Weapons.GBU_38_16)

    class Pylon3:
        MK_82_28 = (3, Weapons.MK_82_28)
        CBU87_10 = (3, Weapons.CBU87_10)
        CBU97_10 = (3, Weapons.CBU97_10)
        B_1B_Mk_84_8 = (3, Weapons.B_1B_Mk_84_8)
        GBU_31_8 = (3, Weapons.GBU_31_8)
        GBU_31V3B_8 = (3, Weapons.GBU_31V3B_8)
        AGM_154C_4 = (3, Weapons.AGM_154C_4)
        GBU_38_16 = (3, Weapons.GBU_38_16)

    pylons = {1, 2, 3}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS]
    task_default = task.GroundAttack


class S_3B(PlaneType):
    id = "S-3B"
    group_size_max = 1
    large_parking_slot = True
    height = 6.93
    width = 20.93
    length = 16.26
    fuel_max = 5500
    max_speed = 840
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Tanker"

    class Pylon1:
        _3_Mk_82 = (1, Weapons._3_Mk_82)
        _3_Mk_20_Rockeye = (1, Weapons._3_Mk_20_Rockeye)
        Mk_82 = (1, Weapons.Mk_82)
        Mk_84 = (1, Weapons.Mk_84)
        Mk_20 = (1, Weapons.Mk_20)
        LAU_117_AGM_65D = (1, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65K = (1, Weapons.LAU_117_AGM_65K)
        AGM_84A = (1, Weapons.AGM_84A)
        AGM_84E = (1, Weapons.AGM_84E)
        LAU_10___4_ZUNI_MK_71 = (1, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61_3___57_2_75__rockets_MK151__HE_ = (1, Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_)
        Fuel_tank_S_3 = (1, Weapons.Fuel_tank_S_3)

    class Pylon2:
        Mk_82 = (2, Weapons.Mk_82)
        Mk_84 = (2, Weapons.Mk_84)
        Mk_20 = (2, Weapons.Mk_20)

    class Pylon3:
        Mk_82 = (3, Weapons.Mk_82)
        Mk_84 = (3, Weapons.Mk_84)
        Mk_20 = (3, Weapons.Mk_20)

    class Pylon4:
        Mk_82 = (4, Weapons.Mk_82)
        Mk_84 = (4, Weapons.Mk_84)
        Mk_20 = (4, Weapons.Mk_20)

    class Pylon5:
        Mk_82 = (5, Weapons.Mk_82)
        Mk_84 = (5, Weapons.Mk_84)
        Mk_20 = (5, Weapons.Mk_20)

    class Pylon6:
        _3_Mk_82 = (6, Weapons._3_Mk_82)
        _3_Mk_20_Rockeye = (6, Weapons._3_Mk_20_Rockeye)
        Mk_82 = (6, Weapons.Mk_82)
        Mk_84 = (6, Weapons.Mk_84)
        Mk_20 = (6, Weapons.Mk_20)
        LAU_117_AGM_65D = (6, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65K = (6, Weapons.LAU_117_AGM_65K)
        AGM_84A = (6, Weapons.AGM_84A)
        AGM_84E = (6, Weapons.AGM_84E)
        LAU_10___4_ZUNI_MK_71 = (6, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61_3___57_2_75__rockets_MK151__HE_ = (6, Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_)
        Fuel_tank_S_3 = (6, Weapons.Fuel_tank_S_3)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.GroundAttack, task.AntishipStrike, task.PinpointStrike]
    task_default = task.AntishipStrike


class S_3B_Tanker(PlaneType):
    id = "S-3B Tanker"
    group_size_max = 1
    large_parking_slot = True
    height = 6.93
    width = 20.93
    length = 16.26
    fuel_max = 5500
    max_speed = 840
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Tanker"

    pylons = {}

    tasks = [task.Refueling]
    task_default = task.Refueling


class Mirage_2000_5(PlaneType):
    id = "Mirage 2000-5"
    height = 5.2
    width = 9.13
    length = 14.36
    fuel_max = 3160
    max_speed = 2340
    chaff = 112
    flare = 16
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_550_Magic_2 = (1, Weapons.R_550_Magic_2)

    class Pylon2:
        Super_530D = (2, Weapons.Super_530D)
        MICA_RF = (2, Weapons.MICA_RF)
        MICA_IR = (2, Weapons.MICA_IR)
        M2000_Fuel_tank = (2, Weapons.M2000_Fuel_tank)

    class Pylon3:
        MICA_IR = (3, Weapons.MICA_IR)
        MICA_RF = (3, Weapons.MICA_RF)

    class Pylon4:
        MICA_IR = (4, Weapons.MICA_IR)
        MICA_RF = (4, Weapons.MICA_RF)

    class Pylon5:
        M2000_Fuel_tank = (5, Weapons.M2000_Fuel_tank)

    class Pylon6:
        MICA_IR = (6, Weapons.MICA_IR)
        MICA_RF = (6, Weapons.MICA_RF)

    class Pylon7:
        MICA_IR = (7, Weapons.MICA_IR)
        MICA_RF = (7, Weapons.MICA_RF)

    class Pylon8:
        Super_530D = (8, Weapons.Super_530D)
        MICA_RF = (8, Weapons.MICA_RF)
        MICA_IR = (8, Weapons.MICA_IR)
        M2000_Fuel_tank = (8, Weapons.M2000_Fuel_tank)

    class Pylon9:
        R_550_Magic_2 = (9, Weapons.R_550_Magic_2)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.Reconnaissance]
    task_default = task.CAP


class F_15C(PlaneType):
    id = "F-15C"
    flyable = True
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 6103
    max_speed = 2650
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"
    radio_frequency = 124

    class Pylon1:
        AIM_120B = (1, Weapons.AIM_120B)
        AIM_120C = (1, Weapons.AIM_120C)
        AIM_9M = (1, Weapons.AIM_9M)
        AIM_9P = (1, Weapons.AIM_9P)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        Fuel_tank_610_gal = (2, Weapons.Fuel_tank_610_gal)

    class Pylon3:
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_120C = (3, Weapons.AIM_120C)
        AIM_9M = (3, Weapons.AIM_9M)
        AIM_9P = (3, Weapons.AIM_9P)

    class Pylon4:
        AIM_120B = (4, Weapons.AIM_120B)
        AIM_120C = (4, Weapons.AIM_120C)
        AIM_7M = (4, Weapons.AIM_7M)

    class Pylon5:
        AIM_120B = (5, Weapons.AIM_120B)
        AIM_120C = (5, Weapons.AIM_120C)
        AIM_7M = (5, Weapons.AIM_7M)

    class Pylon6:
        Fuel_tank_610_gal = (6, Weapons.Fuel_tank_610_gal)

    class Pylon7:
        AIM_120B = (7, Weapons.AIM_120B)
        AIM_120C = (7, Weapons.AIM_120C)
        AIM_7M = (7, Weapons.AIM_7M)

    class Pylon8:
        AIM_120B = (8, Weapons.AIM_120B)
        AIM_120C = (8, Weapons.AIM_120C)
        AIM_7M = (8, Weapons.AIM_7M)

    class Pylon9:
        AIM_120B = (9, Weapons.AIM_120B)
        AIM_120C = (9, Weapons.AIM_120C)
        AIM_9M = (9, Weapons.AIM_9M)
        AIM_9P = (9, Weapons.AIM_9P)

    class Pylon10:
        Fuel_tank_610_gal = (10, Weapons.Fuel_tank_610_gal)

    class Pylon11:
        AIM_120B = (11, Weapons.AIM_120B)
        AIM_120C = (11, Weapons.AIM_120C)
        AIM_9M = (11, Weapons.AIM_9M)
        AIM_9P = (11, Weapons.AIM_9P)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.CAP


class F_15E(PlaneType):
    id = "F-15E"
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 10246
    max_speed = 2650
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"

    class Pylon1:
        AIM_120B = (1, Weapons.AIM_120B)
        AIM_120C = (1, Weapons.AIM_120C)
        AIM_9M = (1, Weapons.AIM_9M)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        Fuel_tank_610_gal = (2, Weapons.Fuel_tank_610_gal)
        Mk_82 = (2, Weapons.Mk_82)
        Mk_84 = (2, Weapons.Mk_84)
        Mk_82AIR = (2, Weapons.Mk_82AIR)
        GBU_10 = (2, Weapons.GBU_10)
        GBU_12 = (2, Weapons.GBU_12)
        GBU_27 = (2, Weapons.GBU_27)
        GBU_31 = (2, Weapons.GBU_31)
        GBU_38 = (2, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (2, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (2, Weapons.CBU_87)
        CBU_97 = (2, Weapons.CBU_97)
        CBU_103 = (2, Weapons.CBU_103)
        CBU_105 = (2, Weapons.CBU_105)
        LAU_117_AGM_65D = (2, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65E = (2, Weapons.LAU_117_AGM_65E)
        LAU_117_AGM_65H = (2, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65K = (2, Weapons.LAU_117_AGM_65K)
        AGM_154C = (2, Weapons.AGM_154C)
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)
        GBU_31_V_3_B = (2, Weapons.GBU_31_V_3_B)

    class Pylon3:
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_120C = (3, Weapons.AIM_120C)
        AIM_9M = (3, Weapons.AIM_9M)

    class Pylon4:
        Mk_82 = (4, Weapons.Mk_82)
        Mk_82AIR = (4, Weapons.Mk_82AIR)
        GBU_12 = (4, Weapons.GBU_12)
        GBU_38 = (4, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (4, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (4, Weapons.CBU_87)
        CBU_97 = (4, Weapons.CBU_97)
        CBU_103 = (4, Weapons.CBU_103)
        CBU_105 = (4, Weapons.CBU_105)

    class Pylon5:
        Mk_82 = (5, Weapons.Mk_82)
        Mk_82AIR = (5, Weapons.Mk_82AIR)
        GBU_12 = (5, Weapons.GBU_12)
        GBU_38 = (5, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (5, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (5, Weapons.CBU_87)
        CBU_97 = (5, Weapons.CBU_97)
        CBU_103 = (5, Weapons.CBU_103)
        CBU_105 = (5, Weapons.CBU_105)

    class Pylon6:
        Mk_82 = (6, Weapons.Mk_82)
        Mk_82AIR = (6, Weapons.Mk_82AIR)
        GBU_12 = (6, Weapons.GBU_12)
        GBU_38 = (6, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (6, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (6, Weapons.CBU_87)
        CBU_97 = (6, Weapons.CBU_97)
        CBU_103 = (6, Weapons.CBU_103)
        CBU_105 = (6, Weapons.CBU_105)

    class Pylon7:
        Mk_82 = (7, Weapons.Mk_82)
        Mk_84 = (7, Weapons.Mk_84)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        GBU_10 = (7, Weapons.GBU_10)
        GBU_12 = (7, Weapons.GBU_12)
        GBU_27 = (7, Weapons.GBU_27)
        GBU_31 = (7, Weapons.GBU_31)
        GBU_38 = (7, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (7, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (7, Weapons.CBU_87)
        CBU_97 = (7, Weapons.CBU_97)
        CBU_103 = (7, Weapons.CBU_103)
        CBU_105 = (7, Weapons.CBU_105)
        GBU_31_V_3_B = (7, Weapons.GBU_31_V_3_B)

    class Pylon8:
        Mk_82 = (8, Weapons.Mk_82)
        Mk_82AIR = (8, Weapons.Mk_82AIR)
        GBU_12 = (8, Weapons.GBU_12)
        GBU_38 = (8, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (8, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (8, Weapons.CBU_87)
        CBU_97 = (8, Weapons.CBU_97)
        CBU_103 = (8, Weapons.CBU_103)
        CBU_105 = (8, Weapons.CBU_105)

    class Pylon9:
        Mk_82 = (9, Weapons.Mk_82)
        Mk_84 = (9, Weapons.Mk_84)
        Mk_82AIR = (9, Weapons.Mk_82AIR)
        GBU_10 = (9, Weapons.GBU_10)
        GBU_12 = (9, Weapons.GBU_12)
        GBU_27 = (9, Weapons.GBU_27)
        GBU_31 = (9, Weapons.GBU_31)
        GBU_38 = (9, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (9, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (9, Weapons.CBU_87)
        CBU_97 = (9, Weapons.CBU_97)
        CBU_103 = (9, Weapons.CBU_103)
        CBU_105 = (9, Weapons.CBU_105)
        GBU_31_V_3_B = (9, Weapons.GBU_31_V_3_B)

    class Pylon10:
        Fuel_tank_610_gal = (10, Weapons.Fuel_tank_610_gal)
        Mk_82AIR = (10, Weapons.Mk_82AIR)
        GBU_10 = (10, Weapons.GBU_10)
        GBU_12 = (10, Weapons.GBU_12)
        GBU_27 = (10, Weapons.GBU_27)
        GBU_31 = (10, Weapons.GBU_31)
        GBU_31_V_3_B = (10, Weapons.GBU_31_V_3_B)
        GBU_38 = (10, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (10, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (10, Weapons.CBU_87)
        CBU_97 = (10, Weapons.CBU_97)
        CBU_103 = (10, Weapons.CBU_103)
        CBU_105 = (10, Weapons.CBU_105)
        Mk_84 = (10, Weapons.Mk_84)

    class Pylon11:
        Mk_82 = (11, Weapons.Mk_82)
        Mk_84 = (11, Weapons.Mk_84)
        Mk_82AIR = (11, Weapons.Mk_82AIR)
        GBU_10 = (11, Weapons.GBU_10)
        GBU_12 = (11, Weapons.GBU_12)
        GBU_27 = (11, Weapons.GBU_27)
        GBU_31 = (11, Weapons.GBU_31)
        GBU_38 = (11, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (11, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (11, Weapons.CBU_87)
        CBU_97 = (11, Weapons.CBU_97)
        CBU_103 = (11, Weapons.CBU_103)
        CBU_105 = (11, Weapons.CBU_105)
        GBU_31_V_3_B = (11, Weapons.GBU_31_V_3_B)

    class Pylon12:
        Mk_82 = (12, Weapons.Mk_82)
        Mk_82AIR = (12, Weapons.Mk_82AIR)
        GBU_12 = (12, Weapons.GBU_12)
        GBU_38 = (12, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (12, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (12, Weapons.CBU_87)
        CBU_97 = (12, Weapons.CBU_97)
        CBU_103 = (12, Weapons.CBU_103)
        CBU_105 = (12, Weapons.CBU_105)

    class Pylon13:
        Mk_82 = (13, Weapons.Mk_82)
        Mk_84 = (13, Weapons.Mk_84)
        Mk_82AIR = (13, Weapons.Mk_82AIR)
        GBU_10 = (13, Weapons.GBU_10)
        GBU_12 = (13, Weapons.GBU_12)
        GBU_27 = (13, Weapons.GBU_27)
        GBU_31 = (13, Weapons.GBU_31)
        GBU_38 = (13, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (13, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (13, Weapons.CBU_87)
        CBU_97 = (13, Weapons.CBU_97)
        CBU_103 = (13, Weapons.CBU_103)
        CBU_105 = (13, Weapons.CBU_105)
        GBU_31_V_3_B = (13, Weapons.GBU_31_V_3_B)

    class Pylon14:
        Mk_82 = (14, Weapons.Mk_82)
        Mk_82AIR = (14, Weapons.Mk_82AIR)
        GBU_12 = (14, Weapons.GBU_12)
        GBU_38 = (14, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (14, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (14, Weapons.CBU_87)
        CBU_97 = (14, Weapons.CBU_97)
        CBU_103 = (14, Weapons.CBU_103)
        CBU_105 = (14, Weapons.CBU_105)

    class Pylon15:
        Mk_82 = (15, Weapons.Mk_82)
        Mk_82AIR = (15, Weapons.Mk_82AIR)
        GBU_12 = (15, Weapons.GBU_12)
        GBU_38 = (15, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (15, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (15, Weapons.CBU_87)
        CBU_97 = (15, Weapons.CBU_97)
        CBU_103 = (15, Weapons.CBU_103)
        CBU_105 = (15, Weapons.CBU_105)

    class Pylon16:
        Mk_82 = (16, Weapons.Mk_82)
        Mk_82AIR = (16, Weapons.Mk_82AIR)
        GBU_12 = (16, Weapons.GBU_12)
        GBU_38 = (16, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (16, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (16, Weapons.CBU_87)
        CBU_97 = (16, Weapons.CBU_97)
        CBU_103 = (16, Weapons.CBU_103)
        CBU_105 = (16, Weapons.CBU_105)

    class Pylon17:
        AIM_120B = (17, Weapons.AIM_120B)
        AIM_120C = (17, Weapons.AIM_120C)
        AIM_9M = (17, Weapons.AIM_9M)

    class Pylon18:
        Fuel_tank_610_gal = (18, Weapons.Fuel_tank_610_gal)
        Mk_82 = (18, Weapons.Mk_82)
        Mk_84 = (18, Weapons.Mk_84)
        Mk_82AIR = (18, Weapons.Mk_82AIR)
        GBU_10 = (18, Weapons.GBU_10)
        GBU_12 = (18, Weapons.GBU_12)
        GBU_27 = (18, Weapons.GBU_27)
        GBU_31 = (18, Weapons.GBU_31)
        GBU_31_V_3_B = (18, Weapons.GBU_31_V_3_B)
        GBU_38 = (18, Weapons.GBU_38)
        SUU_25___8_LUU_2 = (18, Weapons.SUU_25___8_LUU_2)
        CBU_87 = (18, Weapons.CBU_87)
        CBU_97 = (18, Weapons.CBU_97)
        CBU_103 = (18, Weapons.CBU_103)
        CBU_105 = (18, Weapons.CBU_105)
        LAU_117_AGM_65D = (18, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65E = (18, Weapons.LAU_117_AGM_65E)
        LAU_117_AGM_65H = (18, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65K = (18, Weapons.LAU_117_AGM_65K)
        AGM_154C = (18, Weapons.AGM_154C)
        LAU_117_AGM_65G = (18, Weapons.LAU_117_AGM_65G)

    class Pylon19:
        AIM_120B = (19, Weapons.AIM_120B)
        AIM_120C = (19, Weapons.AIM_120C)
        AIM_9M = (19, Weapons.AIM_9M)
        AN_ASQ_T50_TCTS_Pod = (19, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.AFAC, task.Reconnaissance]
    task_default = task.GroundAttack


class MiG_29K(PlaneType):
    id = "MiG-29K"
    height = 5.175
    width = 11.99
    length = 20.37
    fuel_max = 4500
    max_speed = 2300
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    class Pylon3:
        R_73 = (3, Weapons.R_73)
        L005_Sorbtsiya_ECM_pod__left_ = (3, Weapons.L005_Sorbtsiya_ECM_pod__left_)

    pylons = {3}

    tasks = [task.SEAD, task.AntishipStrike, task.CAS, task.CAP, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept, task.AFAC, task.PinpointStrike, task.RunwayAttack]
    task_default = task.CAP


class Tu_142(PlaneType):
    id = "Tu-142"
    group_size_max = 1
    large_parking_slot = True
    height = 13.3
    width = 50.04
    length = 49.13
    fuel_max = 87000
    max_speed = 860
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        Kh_35_6 = (1, Weapons.Kh_35_6)

    pylons = {1}

    tasks = [task.AntishipStrike, task.Reconnaissance]
    task_default = task.AntishipStrike


class C_130(PlaneType):
    id = "C-130"
    group_size_max = 1
    large_parking_slot = True
    height = 11.66
    width = 40.4
    length = 29.79
    fuel_max = 20830
    max_speed = 610
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class An_26B(PlaneType):
    id = "An-26B"
    group_size_max = 1
    large_parking_slot = True
    height = 8.575
    width = 29.2
    length = 23.8
    fuel_max = 5500
    max_speed = 540
    chaff = 384
    flare = 384
    charge_total = 768
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class An_30M(PlaneType):
    id = "An-30M"
    group_size_max = 1
    large_parking_slot = True
    height = 8.575
    width = 29.2
    length = 23.8
    fuel_max = 8300
    max_speed = 540
    chaff = 192
    flare = 192
    charge_total = 384
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = [task.Transport, task.Reconnaissance]
    task_default = task.Transport


class C_17A(PlaneType):
    id = "C-17A"
    group_size_max = 1
    large_parking_slot = True
    height = 16.79
    width = 51.76
    length = 53.04
    fuel_max = 132405
    max_speed = 850
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class A_50(PlaneType):
    id = "A-50"
    group_size_max = 1
    large_parking_slot = True
    height = 14.76
    width = 50.5
    length = 46.59
    fuel_max = 70000
    max_speed = 850
    chaff = 192
    flare = 192
    charge_total = 384
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "AWACS"

    pylons = {}

    tasks = [task.AWACS]
    task_default = task.AWACS


class E_3A(PlaneType):
    id = "E-3A"
    group_size_max = 1
    large_parking_slot = True
    height = 12.93
    width = 44.4
    length = 46.61
    fuel_max = 65000
    max_speed = 860
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "AWACS"

    pylons = {}

    tasks = [task.AWACS]
    task_default = task.AWACS


class IL_78M(PlaneType):
    id = "IL-78M"
    group_size_max = 1
    large_parking_slot = True
    height = 14.76
    width = 50.5
    length = 46.59
    fuel_max = 90000
    max_speed = 850
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Tanker"

    pylons = {}

    tasks = [task.Refueling]
    task_default = task.Refueling


class E_2C(PlaneType):
    id = "E-2C"
    group_size_max = 1
    large_parking_slot = True
    height = 5.59
    width = 24.56
    length = 17.55
    fuel_max = 5624
    max_speed = 610
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "AWACS"

    pylons = {}

    tasks = [task.AWACS]
    task_default = task.AWACS


class IL_76MD(PlaneType):
    id = "IL-76MD"
    group_size_max = 1
    large_parking_slot = True
    height = 14.76
    width = 50.5
    length = 46.59
    fuel_max = 80000
    max_speed = 850
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class F_16C_bl_50(PlaneType):
    id = "F-16C bl.50"
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3104
    max_speed = 2150
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = (1, Weapons.AIM_120B)
        AIM_120C = (1, Weapons.AIM_120C)
        AIM_9M = (1, Weapons.AIM_9M)
        AIM_9P = (1, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        AIM_120B = (2, Weapons.AIM_120B)
        AIM_120C = (2, Weapons.AIM_120C)
        AIM_9M = (2, Weapons.AIM_9M)
        AIM_9P = (2, Weapons.AIM_9P)

    class Pylon3:
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_120C = (3, Weapons.AIM_120C)
        AIM_9M = (3, Weapons.AIM_9M)
        AIM_9P = (3, Weapons.AIM_9P)
        LAU_117_AGM_65K = (3, Weapons.LAU_117_AGM_65K)
        LAU_117_AGM_65D = (3, Weapons.LAU_117_AGM_65D)
        LAU_88_AGM_65K_3 = (3, Weapons.LAU_88_AGM_65K_3)
        LAU_88_AGM_65D_3 = (3, Weapons.LAU_88_AGM_65D_3)
        GBU_10 = (3, Weapons.GBU_10)
        GBU_12 = (3, Weapons.GBU_12)
        Mk_84 = (3, Weapons.Mk_84)
        Mk_82 = (3, Weapons.Mk_82)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_AGM_65D = (3, Weapons.LAU_117_AGM_65D)
        LAU_88_AGM_65D_2 = (3, Weapons.LAU_88_AGM_65D_2)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (3, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (3, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (3, Weapons._3_Mk_82AIR)
        GBU_38 = (3, Weapons.GBU_38)
        GBU_31 = (3, Weapons.GBU_31)
        GBU_31_V_3_B = (3, Weapons.GBU_31_V_3_B)
        CBU_87 = (3, Weapons.CBU_87)
        CBU_97 = (3, Weapons.CBU_97)
        CBU_103 = (3, Weapons.CBU_103)
        CBU_105 = (3, Weapons.CBU_105)
        _2xGBU_12 = (3, Weapons._2xGBU_12)
        GBU_27 = (3, Weapons.GBU_27)
        AGM_154C = (3, Weapons.AGM_154C)
        AGM_88C_ = (3, Weapons.AGM_88C_)

    class Pylon4:
        GBU_10 = (4, Weapons.GBU_10)
        GBU_12 = (4, Weapons.GBU_12)
        Mk_84 = (4, Weapons.Mk_84)
        Mk_82 = (4, Weapons.Mk_82)
        _3_Mk_82 = (4, Weapons._3_Mk_82)
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65D = (4, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (4, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (4, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (4, Weapons._3_Mk_82AIR)
        GBU_38 = (4, Weapons.GBU_38)
        GBU_31 = (4, Weapons.GBU_31)
        GBU_31_V_3_B = (4, Weapons.GBU_31_V_3_B)
        CBU_87 = (4, Weapons.CBU_87)
        CBU_97 = (4, Weapons.CBU_97)
        CBU_103 = (4, Weapons.CBU_103)
        CBU_105 = (4, Weapons.CBU_105)
        GBU_27 = (4, Weapons.GBU_27)

    class Pylon5:
        Lantirn_F_16 = (5, Weapons.Lantirn_F_16)
        AN_AAQ_28_LITENING = (5, Weapons.AN_AAQ_28_LITENING)

    class Pylon6:
        ALQ_131 = (6, Weapons.ALQ_131)
        Fuel_tank_300_gal = (6, Weapons.Fuel_tank_300_gal)

    class Pylon7:
        Fuel_tank_370_gal = (7, Weapons.Fuel_tank_370_gal)
        GBU_10 = (7, Weapons.GBU_10)
        GBU_12 = (7, Weapons.GBU_12)
        Mk_84 = (7, Weapons.Mk_84)
        Mk_82 = (7, Weapons.Mk_82)
        _3_Mk_82 = (7, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65D = (7, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65G = (7, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (7, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (7, Weapons._3_Mk_82AIR)
        GBU_38 = (7, Weapons.GBU_38)
        GBU_31 = (7, Weapons.GBU_31)
        GBU_31_V_3_B = (7, Weapons.GBU_31_V_3_B)
        CBU_87 = (7, Weapons.CBU_87)
        CBU_97 = (7, Weapons.CBU_97)
        CBU_103 = (7, Weapons.CBU_103)
        CBU_105 = (7, Weapons.CBU_105)
        GBU_27 = (7, Weapons.GBU_27)

    class Pylon8:
        AIM_120B = (8, Weapons.AIM_120B)
        AIM_120C = (8, Weapons.AIM_120C)
        AIM_9M = (8, Weapons.AIM_9M)
        AIM_9P = (8, Weapons.AIM_9P)
        LAU_117_AGM_65K = (8, Weapons.LAU_117_AGM_65K)
        LAU_88_AGM_65K_3 = (8, Weapons.LAU_88_AGM_65K_3)
        LAU_88_AGM_65D_3 = (8, Weapons.LAU_88_AGM_65D_3)
        GBU_10 = (8, Weapons.GBU_10)
        GBU_12 = (8, Weapons.GBU_12)
        Mk_84 = (8, Weapons.Mk_84)
        Mk_82 = (8, Weapons.Mk_82)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (8, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_AGM_65D = (8, Weapons.LAU_117_AGM_65D)
        LAU_88_AGM_65D_2 = (8, Weapons.LAU_88_AGM_65D_2)
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (8, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (8, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (8, Weapons._3_Mk_82AIR)
        GBU_38 = (8, Weapons.GBU_38)
        GBU_31 = (8, Weapons.GBU_31)
        GBU_31_V_3_B = (8, Weapons.GBU_31_V_3_B)
        CBU_87 = (8, Weapons.CBU_87)
        CBU_97 = (8, Weapons.CBU_97)
        CBU_103 = (8, Weapons.CBU_103)
        CBU_105 = (8, Weapons.CBU_105)
        _2xGBU_12_ = (8, Weapons._2xGBU_12_)
        GBU_27 = (8, Weapons.GBU_27)
        AGM_154C = (8, Weapons.AGM_154C)
        AGM_88C_ = (8, Weapons.AGM_88C_)

    class Pylon9:
        AIM_120B = (9, Weapons.AIM_120B)
        AIM_120C = (9, Weapons.AIM_120C)
        AIM_9M = (9, Weapons.AIM_9M)
        AIM_9P = (9, Weapons.AIM_9P)

    class Pylon10:
        AIM_120B = (10, Weapons.AIM_120B)
        AIM_120C = (10, Weapons.AIM_120C)
        AIM_9M = (10, Weapons.AIM_9M)
        AIM_9P = (10, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class F_16C_bl_52d(PlaneType):
    id = "F-16C bl.52d"
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3104
    max_speed = 2150
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"

    class Pylon1:
        AIM_120B = (1, Weapons.AIM_120B)
        AIM_120C = (1, Weapons.AIM_120C)
        AIM_9M = (1, Weapons.AIM_9M)
        AIM_9P = (1, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        AIM_120B = (2, Weapons.AIM_120B)
        AIM_120C = (2, Weapons.AIM_120C)
        AIM_9M = (2, Weapons.AIM_9M)
        AIM_9P = (2, Weapons.AIM_9P)

    class Pylon3:
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_120C = (3, Weapons.AIM_120C)
        AIM_9M = (3, Weapons.AIM_9M)
        AIM_9P = (3, Weapons.AIM_9P)
        LAU_88_AGM_65D_3 = (3, Weapons.LAU_88_AGM_65D_3)
        GBU_10 = (3, Weapons.GBU_10)
        GBU_12 = (3, Weapons.GBU_12)
        Mk_84 = (3, Weapons.Mk_84)
        Mk_82 = (3, Weapons.Mk_82)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_AGM_65D = (3, Weapons.LAU_117_AGM_65D)
        LAU_88_AGM_65D_2 = (3, Weapons.LAU_88_AGM_65D_2)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (3, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (3, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (3, Weapons._3_Mk_82AIR)
        GBU_38 = (3, Weapons.GBU_38)
        GBU_31 = (3, Weapons.GBU_31)
        GBU_31_V_3_B = (3, Weapons.GBU_31_V_3_B)
        CBU_87 = (3, Weapons.CBU_87)
        CBU_97 = (3, Weapons.CBU_97)
        CBU_103 = (3, Weapons.CBU_103)
        CBU_105 = (3, Weapons.CBU_105)
        _2xGBU_12 = (3, Weapons._2xGBU_12)
        GBU_27 = (3, Weapons.GBU_27)
        AGM_154C = (3, Weapons.AGM_154C)
        AGM_88C_ = (3, Weapons.AGM_88C_)

    class Pylon4:
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        AGM_154C = (4, Weapons.AGM_154C)
        GBU_10 = (4, Weapons.GBU_10)
        GBU_12 = (4, Weapons.GBU_12)
        Mk_84 = (4, Weapons.Mk_84)
        Mk_82 = (4, Weapons.Mk_82)
        _3_Mk_82 = (4, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65D = (4, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (4, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (4, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (4, Weapons._3_Mk_82AIR)
        GBU_38 = (4, Weapons.GBU_38)
        GBU_31 = (4, Weapons.GBU_31)
        GBU_31_V_3_B = (4, Weapons.GBU_31_V_3_B)
        CBU_87 = (4, Weapons.CBU_87)
        CBU_97 = (4, Weapons.CBU_97)
        CBU_103 = (4, Weapons.CBU_103)
        CBU_105 = (4, Weapons.CBU_105)
        GBU_27 = (4, Weapons.GBU_27)

    class Pylon5:
        Lantirn_F_16 = (5, Weapons.Lantirn_F_16)
        AN_AAQ_28_LITENING = (5, Weapons.AN_AAQ_28_LITENING)

    class Pylon6:
        ALQ_131 = (6, Weapons.ALQ_131)
        ALQ_184 = (6, Weapons.ALQ_184)
        Fuel_tank_300_gal = (6, Weapons.Fuel_tank_300_gal)

    class Pylon7:
        Fuel_tank_370_gal = (7, Weapons.Fuel_tank_370_gal)
        AGM_154C = (7, Weapons.AGM_154C)
        GBU_10 = (7, Weapons.GBU_10)
        GBU_12 = (7, Weapons.GBU_12)
        Mk_84 = (7, Weapons.Mk_84)
        Mk_82 = (7, Weapons.Mk_82)
        _3_Mk_82 = (7, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65D = (7, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65G = (7, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (7, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (7, Weapons._3_Mk_82AIR)
        GBU_38 = (7, Weapons.GBU_38)
        GBU_31 = (7, Weapons.GBU_31)
        GBU_31_V_3_B = (7, Weapons.GBU_31_V_3_B)
        CBU_87 = (7, Weapons.CBU_87)
        CBU_97 = (7, Weapons.CBU_97)
        CBU_103 = (7, Weapons.CBU_103)
        CBU_105 = (7, Weapons.CBU_105)
        GBU_27 = (7, Weapons.GBU_27)

    class Pylon8:
        AIM_120B = (8, Weapons.AIM_120B)
        AIM_120C = (8, Weapons.AIM_120C)
        AIM_9M = (8, Weapons.AIM_9M)
        AIM_9P = (8, Weapons.AIM_9P)
        LAU_88_AGM_65D_3 = (8, Weapons.LAU_88_AGM_65D_3)
        GBU_10 = (8, Weapons.GBU_10)
        GBU_12 = (8, Weapons.GBU_12)
        Mk_84 = (8, Weapons.Mk_84)
        Mk_82 = (8, Weapons.Mk_82)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_R = (8, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_AGM_65D = (8, Weapons.LAU_117_AGM_65D)
        LAU_88_AGM_65D_2_ = (8, Weapons.LAU_88_AGM_65D_2_)
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (8, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (8, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (8, Weapons._3_Mk_82AIR)
        GBU_38 = (8, Weapons.GBU_38)
        GBU_31 = (8, Weapons.GBU_31)
        GBU_31_V_3_B = (8, Weapons.GBU_31_V_3_B)
        CBU_87 = (8, Weapons.CBU_87)
        CBU_97 = (8, Weapons.CBU_97)
        CBU_103 = (8, Weapons.CBU_103)
        CBU_105 = (8, Weapons.CBU_105)
        _2xGBU_12_ = (8, Weapons._2xGBU_12_)
        GBU_27 = (8, Weapons.GBU_27)
        AGM_154C = (8, Weapons.AGM_154C)
        AGM_88C_ = (8, Weapons.AGM_88C_)

    class Pylon9:
        AIM_120B = (9, Weapons.AIM_120B)
        AIM_120C = (9, Weapons.AIM_120C)
        AIM_9M = (9, Weapons.AIM_9M)
        AIM_9P = (9, Weapons.AIM_9P)

    class Pylon10:
        AIM_120B = (10, Weapons.AIM_120B)
        AIM_120C = (10, Weapons.AIM_120C)
        AIM_9M = (10, Weapons.AIM_9M)
        AIM_9P = (10, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class F_16A(PlaneType):
    id = "F-16A"
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3104
    max_speed = 2150
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = (1, Weapons.AIM_120B)
        AIM_9M = (1, Weapons.AIM_9M)
        AIM_9P = (1, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        AIM_120B = (2, Weapons.AIM_120B)
        AIM_9M = (2, Weapons.AIM_9M)
        AIM_9P = (2, Weapons.AIM_9P)

    class Pylon3:
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_9M = (3, Weapons.AIM_9M)
        AIM_9P = (3, Weapons.AIM_9P)
        LAU_117_AGM_65D = (3, Weapons.LAU_117_AGM_65D)
        Mk_20 = (3, Weapons.Mk_20)
        _2_Mk_20_Rockeye = (3, Weapons._2_Mk_20_Rockeye)
        Mk_84 = (3, Weapons.Mk_84)
        Mk_82 = (3, Weapons.Mk_82)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65D_2 = (3, Weapons.LAU_88_AGM_65D_2)
        AIM_7M = (3, Weapons.AIM_7M)
        Mk_82AIR = (3, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (3, Weapons._3_Mk_82AIR)
        AGM_119B_Penguin = (3, Weapons.AGM_119B_Penguin)

    class Pylon4:
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        Mk_20 = (4, Weapons.Mk_20)
        _3_Mk_20_Rockeye = (4, Weapons._3_Mk_20_Rockeye)
        Mk_84 = (4, Weapons.Mk_84)
        Mk_82 = (4, Weapons.Mk_82)
        _3_Mk_82 = (4, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65D = (4, Weapons.LAU_117_AGM_65D)

    class Pylon6:
        ALQ_131 = (6, Weapons.ALQ_131)
        ALQ_184 = (6, Weapons.ALQ_184)
        Fuel_tank_300_gal = (6, Weapons.Fuel_tank_300_gal)

    class Pylon7:
        Fuel_tank_370_gal = (7, Weapons.Fuel_tank_370_gal)
        Mk_20 = (7, Weapons.Mk_20)
        _3_Mk_20_Rockeye = (7, Weapons._3_Mk_20_Rockeye)
        Mk_84 = (7, Weapons.Mk_84)
        Mk_82 = (7, Weapons.Mk_82)
        _3_Mk_82 = (7, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65D = (7, Weapons.LAU_117_AGM_65D)

    class Pylon8:
        AIM_120B = (8, Weapons.AIM_120B)
        AIM_9M = (8, Weapons.AIM_9M)
        AIM_9P = (8, Weapons.AIM_9P)
        LAU_117_AGM_65D = (8, Weapons.LAU_117_AGM_65D)
        Mk_20 = (8, Weapons.Mk_20)
        _2_Mk_20_Rockeye = (8, Weapons._2_Mk_20_Rockeye)
        Mk_84 = (8, Weapons.Mk_84)
        Mk_82 = (8, Weapons.Mk_82)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_R = (8, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65D_2_ = (8, Weapons.LAU_88_AGM_65D_2_)
        AIM_7M = (8, Weapons.AIM_7M)
        Mk_82AIR = (8, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (8, Weapons._3_Mk_82AIR)
        AGM_119B_Penguin = (8, Weapons.AGM_119B_Penguin)

    class Pylon9:
        AIM_120B = (9, Weapons.AIM_120B)
        AIM_9M = (9, Weapons.AIM_9M)
        AIM_9P = (9, Weapons.AIM_9P)

    class Pylon10:
        AIM_120B = (10, Weapons.AIM_120B)
        AIM_9M = (10, Weapons.AIM_9M)
        AIM_9P = (10, Weapons.AIM_9P)
        AN_ASQ_T50_TCTS_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class F_16A_MLU(PlaneType):
    id = "F-16A MLU"
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3104
    max_speed = 2150
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"

    class Pylon1:
        AIM_120B = (1, Weapons.AIM_120B)
        AIM_120C = (1, Weapons.AIM_120C)
        AIM_9M = (1, Weapons.AIM_9M)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        AIM_120B = (2, Weapons.AIM_120B)
        AIM_120C = (2, Weapons.AIM_120C)
        AIM_9M = (2, Weapons.AIM_9M)

    class Pylon3:
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_120C = (3, Weapons.AIM_120C)
        AIM_9M = (3, Weapons.AIM_9M)
        LAU_88_AGM_65D_3 = (3, Weapons.LAU_88_AGM_65D_3)
        GBU_10 = (3, Weapons.GBU_10)
        GBU_12 = (3, Weapons.GBU_12)
        Mk_84 = (3, Weapons.Mk_84)
        Mk_82 = (3, Weapons.Mk_82)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        AGM_119B_Penguin = (3, Weapons.AGM_119B_Penguin)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_AGM_65D = (3, Weapons.LAU_117_AGM_65D)
        LAU_88_AGM_65D_2 = (3, Weapons.LAU_88_AGM_65D_2)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (3, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (3, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (3, Weapons._3_Mk_82AIR)
        GBU_38 = (3, Weapons.GBU_38)
        GBU_31 = (3, Weapons.GBU_31)
        _2xGBU_12 = (3, Weapons._2xGBU_12)
        AGM_154C = (3, Weapons.AGM_154C)

    class Pylon4:
        GBU_10 = (4, Weapons.GBU_10)
        GBU_12 = (4, Weapons.GBU_12)
        Mk_84 = (4, Weapons.Mk_84)
        Mk_82 = (4, Weapons.Mk_82)
        _3_Mk_82 = (4, Weapons._3_Mk_82)
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        AGM_119B_Penguin = (4, Weapons.AGM_119B_Penguin)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65D = (4, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (4, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (4, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (4, Weapons._3_Mk_82AIR)
        GBU_38 = (4, Weapons.GBU_38)
        GBU_31 = (4, Weapons.GBU_31)

    class Pylon5:
        Lantirn_F_16 = (5, Weapons.Lantirn_F_16)
        AN_AAQ_28_LITENING = (5, Weapons.AN_AAQ_28_LITENING)

    class Pylon6:
        ALQ_131 = (6, Weapons.ALQ_131)
        Fuel_tank_300_gal = (6, Weapons.Fuel_tank_300_gal)

    class Pylon7:
        Fuel_tank_370_gal = (7, Weapons.Fuel_tank_370_gal)
        GBU_10 = (7, Weapons.GBU_10)
        GBU_12 = (7, Weapons.GBU_12)
        Mk_84 = (7, Weapons.Mk_84)
        Mk_82 = (7, Weapons.Mk_82)
        _3_Mk_82 = (7, Weapons._3_Mk_82)
        AGM_119B_Penguin = (7, Weapons.AGM_119B_Penguin)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65D = (7, Weapons.LAU_117_AGM_65D)
        LAU_117_AGM_65G = (7, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (7, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (7, Weapons._3_Mk_82AIR)
        GBU_38 = (7, Weapons.GBU_38)
        GBU_31 = (7, Weapons.GBU_31)

    class Pylon8:
        AIM_120B = (8, Weapons.AIM_120B)
        AIM_120C = (8, Weapons.AIM_120C)
        AIM_9M = (8, Weapons.AIM_9M)
        LAU_88_AGM_65D_3 = (8, Weapons.LAU_88_AGM_65D_3)
        GBU_10 = (8, Weapons.GBU_10)
        GBU_12 = (8, Weapons.GBU_12)
        Mk_84 = (8, Weapons.Mk_84)
        Mk_82 = (8, Weapons.Mk_82)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        AGM_119B_Penguin = (8, Weapons.AGM_119B_Penguin)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_R = (8, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_AGM_65D = (8, Weapons.LAU_117_AGM_65D)
        LAU_88_AGM_65D_2_ = (8, Weapons.LAU_88_AGM_65D_2_)
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65K = (8, Weapons.LAU_117_AGM_65K)
        Mk_82AIR = (8, Weapons.Mk_82AIR)
        _3_Mk_82AIR = (8, Weapons._3_Mk_82AIR)
        GBU_38 = (8, Weapons.GBU_38)
        GBU_31 = (8, Weapons.GBU_31)
        _2xGBU_12_ = (8, Weapons._2xGBU_12_)
        AGM_154C = (8, Weapons.AGM_154C)

    class Pylon9:
        AIM_120B = (9, Weapons.AIM_120B)
        AIM_120C = (9, Weapons.AIM_120C)
        AIM_9M = (9, Weapons.AIM_9M)

    class Pylon10:
        AIM_120B = (10, Weapons.AIM_120B)
        AIM_120C = (10, Weapons.AIM_120C)
        AIM_9M = (10, Weapons.AIM_9M)
        AN_ASQ_T50_TCTS_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class RQ_1A_Predator(PlaneType):
    id = "RQ-1A Predator"
    group_size_max = 1
    height = 2.21
    width = 14.8
    length = 8.13
    fuel_max = 200
    max_speed = 220
    eplrs = True
    radio_frequency = 127.5

    class Pylon1:
        AGM_114K = (1, Weapons.AGM_114K)

    class Pylon2:
        AGM_114K = (2, Weapons.AGM_114K)

    pylons = {1, 2}

    tasks = [task.GroundAttack, task.AFAC, task.Reconnaissance]
    task_default = task.Reconnaissance


class Yak_40(PlaneType):
    id = "Yak-40"
    group_size_max = 1
    large_parking_slot = True
    height = 6.5
    width = 25
    length = 20.36
    fuel_max = 3080
    max_speed = 570

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class A_10C(PlaneType):
    id = "A-10C"
    flyable = True
    height = 4.47
    width = 17.53
    length = 16.26
    fuel_max = 5029
    max_speed = 840
    chaff = 240
    flare = 120
    charge_total = 480
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True

    callnames = {
        "USA": [
            "Hawg",
            "Boar",
            "Pig",
            "Tusk",
        ]
    }

    class Pylon1:
        LAU_105___2_AIM_9M = (1, Weapons.LAU_105___2_AIM_9M)
        Mk_82 = (1, Weapons.Mk_82)
        LAU_105_1_AIM_9M_L = (1, Weapons.LAU_105_1_AIM_9M_L)
        LAU_105 = (1, Weapons.LAU_105)
        LAU_105_2_CATM_9M = (1, Weapons.LAU_105_2_CATM_9M)
        LAU_105_1_CATM_9M_L = (1, Weapons.LAU_105_1_CATM_9M_L)
        ALQ_131 = (1, Weapons.ALQ_131)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        GBU_12 = (1, Weapons.GBU_12)
        BDU_50LD = (1, Weapons.BDU_50LD)
        BDU_50LGB = (1, Weapons.BDU_50LGB)
        BDU_50HD = (1, Weapons.BDU_50HD)
        Mk_82AIR = (1, Weapons.Mk_82AIR)
        CBU_87 = (1, Weapons.CBU_87)
        ALQ_184 = (1, Weapons.ALQ_184)
        CBU_97 = (1, Weapons.CBU_97)
        LAU_105_AIS_ASQ_T50_L = (1, Weapons.LAU_105_AIS_ASQ_T50_L)

    class Pylon2:
        Mk_82 = (2, Weapons.Mk_82)
        AN_AAQ_28_LITENING = (2, Weapons.AN_AAQ_28_LITENING)
        GBU_12 = (2, Weapons.GBU_12)
        BDU_50LD = (2, Weapons.BDU_50LD)
        BDU_50HD = (2, Weapons.BDU_50HD)
        Mk_82AIR = (2, Weapons.Mk_82AIR)
        CBU_87 = (2, Weapons.CBU_87)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (2, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (2, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (2, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (2, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (2, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (2, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (2, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (2, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (2, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (2, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        CBU_97 = (2, Weapons.CBU_97)
        BDU_50LGB = (2, Weapons.BDU_50LGB)
        SUU_25___8_LUU_2 = (2, Weapons.SUU_25___8_LUU_2)

    class Pylon3:
        LAU_117_AGM_65K = (3, Weapons.LAU_117_AGM_65K)
        LAU_88_AGM_65D_ONE = (3, Weapons.LAU_88_AGM_65D_ONE)
        LAU_88_AGM_65D_2 = (3, Weapons.LAU_88_AGM_65D_2)
        LAU_88_AGM_65D_3 = (3, Weapons.LAU_88_AGM_65D_3)
        LAU_117_AGM_65D = (3, Weapons.LAU_117_AGM_65D)
        Mk_84 = (3, Weapons.Mk_84)
        Mk_82 = (3, Weapons.Mk_82)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        GBU_12 = (3, Weapons.GBU_12)
        BDU_50LD = (3, Weapons.BDU_50LD)
        BDU_50HD = (3, Weapons.BDU_50HD)
        Mk_82AIR = (3, Weapons.Mk_82AIR)
        CBU_87 = (3, Weapons.CBU_87)
        GBU_10 = (3, Weapons.GBU_10)
        GBU_31 = (3, Weapons.GBU_31)
        GBU_38 = (3, Weapons.GBU_38)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (3, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (3, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (3, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (3, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (3, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (3, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        LAU_68_3___7_2_75__rockets_MK1__Practice_ = (3, Weapons.LAU_68_3___7_2_75__rockets_MK1__Practice_)
        LAU_68_3___7_2_75__rockets_MK5__HE_ = (3, Weapons.LAU_68_3___7_2_75__rockets_MK5__HE_)
        LAU_68_3___7_2_75__rockets_MK61__Practice_ = (3, Weapons.LAU_68_3___7_2_75__rockets_MK61__Practice_)
        LAU_68_3___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_68_3___7_2_75__rockets_M151__HE_)
        LAU_68_3___7_2_75__rockets_M156__WP_ = (3, Weapons.LAU_68_3___7_2_75__rockets_M156__WP_)
        LAU_68_3___7_2_75__rockets_WTU1B__Practice_ = (3, Weapons.LAU_68_3___7_2_75__rockets_WTU1B__Practice_)
        LAU_68_3___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_68_3___7_2_75__rockets_M274__Practice_smoke_)
        LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (3, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (3, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (3, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (3, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (3, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (3, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (3, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (3, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (3, Weapons.MXU_648_TP)
        BRU_42_LS = (3, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (3, Weapons.BRU_42_3_BDU_33)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_88_AGM_65H = (3, Weapons.LAU_88_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_TGM_65D = (3, Weapons.LAU_117_TGM_65D)
        LAU_117_TGM_65G = (3, Weapons.LAU_117_TGM_65G)
        LAU_117_TGM_65H = (3, Weapons.LAU_117_TGM_65H)
        LAU_117_CATM_65K = (3, Weapons.LAU_117_CATM_65K)
        BRU_42_3_GBU_12 = (3, Weapons.BRU_42_3_GBU_12)
        CBU_97 = (3, Weapons.CBU_97)
        CBU_105 = (3, Weapons.CBU_105)
        CBU_103 = (3, Weapons.CBU_103)
        BDU_50LGB = (3, Weapons.BDU_50LGB)
        SUU_25___8_LUU_2 = (3, Weapons.SUU_25___8_LUU_2)
        _3_Mk_82AIR = (3, Weapons._3_Mk_82AIR)
        _3_SUU_25___8_LUU_2 = (3, Weapons._3_SUU_25___8_LUU_2)

    class Pylon4:
        Mk_82 = (4, Weapons.Mk_82)
        Mk_84 = (4, Weapons.Mk_84)
        Fuel_Tank_FT600 = (4, Weapons.Fuel_Tank_FT600)
        GBU_12 = (4, Weapons.GBU_12)
        BDU_50LD = (4, Weapons.BDU_50LD)
        BDU_50HD = (4, Weapons.BDU_50HD)
        Mk_82AIR = (4, Weapons.Mk_82AIR)
        GBU_10 = (4, Weapons.GBU_10)
        GBU_31 = (4, Weapons.GBU_31)
        GBU_38 = (4, Weapons.GBU_38)
        CBU_87 = (4, Weapons.CBU_87)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (4, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (4, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (4, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (4, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (4, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (4, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (4, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (4, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (4, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (4, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (4, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (4, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (4, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (4, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (4, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (4, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        LAU_68_3___7_2_75__rockets_MK1__Practice_ = (4, Weapons.LAU_68_3___7_2_75__rockets_MK1__Practice_)
        LAU_68_3___7_2_75__rockets_MK5__HE_ = (4, Weapons.LAU_68_3___7_2_75__rockets_MK5__HE_)
        LAU_68_3___7_2_75__rockets_MK61__Practice_ = (4, Weapons.LAU_68_3___7_2_75__rockets_MK61__Practice_)
        LAU_68_3___7_2_75__rockets_M151__HE_ = (4, Weapons.LAU_68_3___7_2_75__rockets_M151__HE_)
        LAU_68_3___7_2_75__rockets_M156__WP_ = (4, Weapons.LAU_68_3___7_2_75__rockets_M156__WP_)
        LAU_68_3___7_2_75__rockets_WTU1B__Practice_ = (4, Weapons.LAU_68_3___7_2_75__rockets_WTU1B__Practice_)
        LAU_68_3___7_2_75__rockets_M274__Practice_smoke_ = (4, Weapons.LAU_68_3___7_2_75__rockets_M274__Practice_smoke_)
        LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_ = (4, Weapons.LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (4, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (4, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (4, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (4, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (4, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (4, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (4, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (4, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (4, Weapons.MXU_648_TP)
        BRU_42_LS = (4, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (4, Weapons.BRU_42_3_BDU_33)
        BRU_42_3_GBU_12 = (4, Weapons.BRU_42_3_GBU_12)
        CBU_97 = (4, Weapons.CBU_97)
        CBU_105 = (4, Weapons.CBU_105)
        CBU_103 = (4, Weapons.CBU_103)
        BDU_50LGB = (4, Weapons.BDU_50LGB)
        _3_Mk_82AIR = (4, Weapons._3_Mk_82AIR)
        _3_Mk_82 = (4, Weapons._3_Mk_82)

    class Pylon5:
        Mk_82 = (5, Weapons.Mk_82)
        Mk_84 = (5, Weapons.Mk_84)
        GBU_12 = (5, Weapons.GBU_12)
        BDU_50LD = (5, Weapons.BDU_50LD)
        BDU_50HD = (5, Weapons.BDU_50HD)
        Mk_82AIR = (5, Weapons.Mk_82AIR)
        GBU_10 = (5, Weapons.GBU_10)
        GBU_31 = (5, Weapons.GBU_31)
        GBU_38 = (5, Weapons.GBU_38)
        CBU_87 = (5, Weapons.CBU_87)
        MXU_648_TP = (5, Weapons.MXU_648_TP)
        BRU_42_LS = (5, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (5, Weapons.BRU_42_3_BDU_33)
        CBU_97 = (5, Weapons.CBU_97)
        CBU_105 = (5, Weapons.CBU_105)
        CBU_103 = (5, Weapons.CBU_103)
        BDU_50LGB = (5, Weapons.BDU_50LGB)
        _3_Mk_82 = (5, Weapons._3_Mk_82)
        _3_Mk_82AIR = (5, Weapons._3_Mk_82AIR)

    class Pylon6:
        Mk_82 = (6, Weapons.Mk_82)
        Mk_84 = (6, Weapons.Mk_84)
        GBU_12 = (6, Weapons.GBU_12)
        BDU_50LD = (6, Weapons.BDU_50LD)
        BDU_50HD = (6, Weapons.BDU_50HD)
        Mk_82AIR = (6, Weapons.Mk_82AIR)
        GBU_10 = (6, Weapons.GBU_10)
        CBU_87 = (6, Weapons.CBU_87)
        MXU_648_TP = (6, Weapons.MXU_648_TP)
        BRU_42_LS = (6, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (6, Weapons.BRU_42_3_BDU_33)
        CBU_97 = (6, Weapons.CBU_97)
        BDU_50LGB = (6, Weapons.BDU_50LGB)
        Fuel_Tank_FT600 = (6, Weapons.Fuel_Tank_FT600)

    class Pylon7:
        Mk_82 = (7, Weapons.Mk_82)
        Mk_84 = (7, Weapons.Mk_84)
        GBU_12 = (7, Weapons.GBU_12)
        BDU_50LD = (7, Weapons.BDU_50LD)
        BDU_50HD = (7, Weapons.BDU_50HD)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        GBU_10 = (7, Weapons.GBU_10)
        GBU_31 = (7, Weapons.GBU_31)
        GBU_38 = (7, Weapons.GBU_38)
        CBU_87 = (7, Weapons.CBU_87)
        MXU_648_TP = (7, Weapons.MXU_648_TP)
        BRU_42_LS = (7, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (7, Weapons.BRU_42_3_BDU_33)
        CBU_97 = (7, Weapons.CBU_97)
        CBU_105 = (7, Weapons.CBU_105)
        CBU_103 = (7, Weapons.CBU_103)
        BDU_50LGB = (7, Weapons.BDU_50LGB)
        _3_Mk_82 = (7, Weapons._3_Mk_82)
        _3_Mk_82AIR = (7, Weapons._3_Mk_82AIR)

    class Pylon8:
        Mk_82 = (8, Weapons.Mk_82)
        Mk_84 = (8, Weapons.Mk_84)
        Fuel_Tank_FT600 = (8, Weapons.Fuel_Tank_FT600)
        GBU_12 = (8, Weapons.GBU_12)
        BDU_50LD = (8, Weapons.BDU_50LD)
        BDU_50HD = (8, Weapons.BDU_50HD)
        Mk_82AIR = (8, Weapons.Mk_82AIR)
        GBU_10 = (8, Weapons.GBU_10)
        GBU_31 = (8, Weapons.GBU_31)
        GBU_38 = (8, Weapons.GBU_38)
        CBU_87 = (8, Weapons.CBU_87)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (8, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (8, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (8, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (8, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (8, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (8, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (8, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (8, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (8, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (8, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (8, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (8, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (8, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (8, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        LAU_68_3___7_2_75__rockets_MK1__Practice_ = (8, Weapons.LAU_68_3___7_2_75__rockets_MK1__Practice_)
        LAU_68_3___7_2_75__rockets_MK5__HE_ = (8, Weapons.LAU_68_3___7_2_75__rockets_MK5__HE_)
        LAU_68_3___7_2_75__rockets_MK61__Practice_ = (8, Weapons.LAU_68_3___7_2_75__rockets_MK61__Practice_)
        LAU_68_3___7_2_75__rockets_M151__HE_ = (8, Weapons.LAU_68_3___7_2_75__rockets_M151__HE_)
        LAU_68_3___7_2_75__rockets_M156__WP_ = (8, Weapons.LAU_68_3___7_2_75__rockets_M156__WP_)
        LAU_68_3___7_2_75__rockets_WTU1B__Practice_ = (8, Weapons.LAU_68_3___7_2_75__rockets_WTU1B__Practice_)
        LAU_68_3___7_2_75__rockets_M274__Practice_smoke_ = (8, Weapons.LAU_68_3___7_2_75__rockets_M274__Practice_smoke_)
        LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_ = (8, Weapons.LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (8, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (8, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (8, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (8, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (8, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (8, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (8, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (8, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (8, Weapons.MXU_648_TP)
        BRU_42_LS = (8, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (8, Weapons.BRU_42_3_BDU_33)
        BRU_42_3_GBU_12 = (8, Weapons.BRU_42_3_GBU_12)
        CBU_97 = (8, Weapons.CBU_97)
        CBU_105 = (8, Weapons.CBU_105)
        CBU_103 = (8, Weapons.CBU_103)
        BDU_50LGB = (8, Weapons.BDU_50LGB)
        _3_Mk_82AIR = (8, Weapons._3_Mk_82AIR)
        _3_Mk_82 = (8, Weapons._3_Mk_82)

    class Pylon9:
        LAU_117_AGM_65K = (9, Weapons.LAU_117_AGM_65K)
        LAU_88_AGM_65D_ONE = (9, Weapons.LAU_88_AGM_65D_ONE)
        LAU_88_AGM_65D_2_ = (9, Weapons.LAU_88_AGM_65D_2_)
        LAU_88_AGM_65D_3 = (9, Weapons.LAU_88_AGM_65D_3)
        LAU_117_AGM_65D = (9, Weapons.LAU_117_AGM_65D)
        Mk_84 = (9, Weapons.Mk_84)
        Mk_82 = (9, Weapons.Mk_82)
        _3_Mk_82 = (9, Weapons._3_Mk_82)
        GBU_12 = (9, Weapons.GBU_12)
        BDU_50LD = (9, Weapons.BDU_50LD)
        BDU_50HD = (9, Weapons.BDU_50HD)
        Mk_82AIR = (9, Weapons.Mk_82AIR)
        GBU_10 = (9, Weapons.GBU_10)
        GBU_31 = (9, Weapons.GBU_31)
        GBU_38 = (9, Weapons.GBU_38)
        CBU_87 = (9, Weapons.CBU_87)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (9, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (9, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (9, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (9, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (9, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (9, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (9, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (9, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (9, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (9, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (9, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (9, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (9, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (9, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (9, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (9, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        LAU_68_3___7_2_75__rockets_MK1__Practice_ = (9, Weapons.LAU_68_3___7_2_75__rockets_MK1__Practice_)
        LAU_68_3___7_2_75__rockets_MK5__HE_ = (9, Weapons.LAU_68_3___7_2_75__rockets_MK5__HE_)
        LAU_68_3___7_2_75__rockets_MK61__Practice_ = (9, Weapons.LAU_68_3___7_2_75__rockets_MK61__Practice_)
        LAU_68_3___7_2_75__rockets_M151__HE_ = (9, Weapons.LAU_68_3___7_2_75__rockets_M151__HE_)
        LAU_68_3___7_2_75__rockets_M156__WP_ = (9, Weapons.LAU_68_3___7_2_75__rockets_M156__WP_)
        LAU_68_3___7_2_75__rockets_WTU1B__Practice_ = (9, Weapons.LAU_68_3___7_2_75__rockets_WTU1B__Practice_)
        LAU_68_3___7_2_75__rockets_M274__Practice_smoke_ = (9, Weapons.LAU_68_3___7_2_75__rockets_M274__Practice_smoke_)
        LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_ = (9, Weapons.LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (9, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (9, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (9, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (9, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (9, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (9, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (9, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (9, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (9, Weapons.MXU_648_TP)
        BRU_42_LS = (9, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (9, Weapons.BRU_42_3_BDU_33)
        LAU_117_AGM_65H = (9, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65G = (9, Weapons.LAU_117_AGM_65G)
        LAU_88_AGM_65H = (9, Weapons.LAU_88_AGM_65H)
        LAU_88_AGM_65H_2_R = (9, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65H_3 = (9, Weapons.LAU_88_AGM_65H_3)
        LAU_117_TGM_65D = (9, Weapons.LAU_117_TGM_65D)
        LAU_117_TGM_65G = (9, Weapons.LAU_117_TGM_65G)
        LAU_117_TGM_65H = (9, Weapons.LAU_117_TGM_65H)
        LAU_117_CATM_65K = (9, Weapons.LAU_117_CATM_65K)
        BRU_42_3_GBU_12 = (9, Weapons.BRU_42_3_GBU_12)
        CBU_97 = (9, Weapons.CBU_97)
        CBU_105 = (9, Weapons.CBU_105)
        CBU_103 = (9, Weapons.CBU_103)
        BDU_50LGB = (9, Weapons.BDU_50LGB)
        SUU_25___8_LUU_2 = (9, Weapons.SUU_25___8_LUU_2)
        _3_Mk_82AIR = (9, Weapons._3_Mk_82AIR)
        _3_SUU_25___8_LUU_2 = (9, Weapons._3_SUU_25___8_LUU_2)

    class Pylon10:
        Mk_82 = (10, Weapons.Mk_82)
        SUU_25___8_LUU_2 = (10, Weapons.SUU_25___8_LUU_2)
        AN_AAQ_28_LITENING = (10, Weapons.AN_AAQ_28_LITENING)
        GBU_12 = (10, Weapons.GBU_12)
        BDU_50LD = (10, Weapons.BDU_50LD)
        BDU_50HD = (10, Weapons.BDU_50HD)
        Mk_82AIR = (10, Weapons.Mk_82AIR)
        CBU_87 = (10, Weapons.CBU_87)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (10, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (10, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (10, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (10, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (10, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (10, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (10, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (10, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = (10, Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_)
        LAU_131___7_2_75__rockets_MK5__HE_ = (10, Weapons.LAU_131___7_2_75__rockets_MK5__HE_)
        LAU_131___7_2_75__rockets_MK61__Practice_ = (10, Weapons.LAU_131___7_2_75__rockets_MK61__Practice_)
        LAU_131___7_2_75__rockets_M151__HE_ = (10, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU_131___7_2_75__rockets_M156__WP_ = (10, Weapons.LAU_131___7_2_75__rockets_M156__WP_)
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = (10, Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_)
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = (10, Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = (10, Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        CBU_97 = (10, Weapons.CBU_97)
        BDU_50LGB = (10, Weapons.BDU_50LGB)

    class Pylon11:
        LAU_105___2_AIM_9M = (11, Weapons.LAU_105___2_AIM_9M)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        ALQ_131 = (11, Weapons.ALQ_131)
        GBU_12 = (11, Weapons.GBU_12)
        BDU_50LD = (11, Weapons.BDU_50LD)
        BDU_50HD = (11, Weapons.BDU_50HD)
        Mk_82AIR = (11, Weapons.Mk_82AIR)
        Mk_82 = (11, Weapons.Mk_82)
        CBU_87 = (11, Weapons.CBU_87)
        BDU_50LGB = (11, Weapons.BDU_50LGB)
        CBU_97 = (11, Weapons.CBU_97)
        LAU_105_1_AIM_9M_R = (11, Weapons.LAU_105_1_AIM_9M_R)
        LAU_105 = (11, Weapons.LAU_105)
        ALQ_184 = (11, Weapons.ALQ_184)
        LAU_105_2_CATM_9M = (11, Weapons.LAU_105_2_CATM_9M)
        LAU_105_1_CATM_9M_R = (11, Weapons.LAU_105_1_CATM_9M_R)
        LAU_105_AIS_ASQ_T50_R = (11, Weapons.LAU_105_AIS_ASQ_T50_R)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAS


class KC_135(PlaneType):
    id = "KC-135"
    group_size_max = 1
    large_parking_slot = True
    height = 12.93
    width = 40
    length = 46.61
    fuel_max = 90700
    max_speed = 980
    tacan = True
    category = "Tanker"

    pylons = {}

    tasks = [task.Refueling]
    task_default = task.Refueling


class P_51D(PlaneType):
    id = "P-51D"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 732
    max_speed = 750
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
    }

    class Pylon1:
        HVAR = (1, Weapons.HVAR)
        HVAR_Smoke_Generator = (1, Weapons.HVAR_Smoke_Generator)

    class Pylon2:
        HVAR = (2, Weapons.HVAR)

    class Pylon3:
        HVAR = (3, Weapons.HVAR)

    class Pylon4:
        AN_M64 = (4, Weapons.AN_M64)
        Drop_Tank_75Gal = (4, Weapons.Drop_Tank_75Gal)
        HVAR = (4, Weapons.HVAR)

    class Pylon5:
        HVAR = (5, Weapons.HVAR)

    class Pylon6:
        HVAR = (6, Weapons.HVAR)

    class Pylon7:
        AN_M64 = (7, Weapons.AN_M64)
        Drop_Tank_75Gal = (7, Weapons.Drop_Tank_75Gal)
        HVAR = (7, Weapons.HVAR)

    class Pylon8:
        HVAR = (8, Weapons.HVAR)

    class Pylon9:
        HVAR = (9, Weapons.HVAR)

    class Pylon10:
        HVAR = (10, Weapons.HVAR)
        HVAR_Smoke_Generator = (10, Weapons.HVAR_Smoke_Generator)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAS


class FW_190D9(PlaneType):
    id = "FW-190D9"
    flyable = True
    height = 4.77
    width = 10.5
    length = 12.13
    fuel_max = 388
    max_speed = 828
    category = "Air"
    radio_frequency = 38.4

    panel_radio = {
        1: {
            "channels": {
                1: 39,
                2: 40,
                4: 42,
                3: 41
            },
        },
    }

    class Pylon1:
        FW109_FUEL_TANK = (1, Weapons.FW109_FUEL_TANK)
        SC_501_SC500 = (1, Weapons.SC_501_SC500)
        ER_4_SC50 = (1, Weapons.ER_4_SC50)

    pylons = {1}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class Bf_109K_4(PlaneType):
    id = "Bf-109K-4"
    flyable = True
    height = 4.77
    width = 10.5
    length = 12.13
    fuel_max = 296
    max_speed = 828
    category = "Air"
    radio_frequency = 40

    panel_radio = {
        1: {
            "channels": {
                2: 40,
                3: 41,
                1: 39,
                4: 42,
                5: 38
            },
        },
    }

    class Pylon1:
        SC_501_SC500 = (1, Weapons.SC_501_SC500)
        SC_501_SC250 = (1, Weapons.SC_501_SC250)
        BF109K_4_FUEL_TANK = (1, Weapons.BF109K_4_FUEL_TANK)

    pylons = {1}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class C_101EB(PlaneType):
    id = "C-101EB"
    flyable = True
    height = 4.25
    width = 14
    length = 12.25
    fuel_max = 1885
    max_speed = 925.2
    category = "Air"
    radio_frequency = 127.5

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                15: 265
            },
        },
        2: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                15: 265
            },
        },
    }

    class Pylon1:
        Aviojet_Red_Smoke = (1, Weapons.Aviojet_Red_Smoke)

    class Pylon2:
        Aviojet_White_Smoke = (2, Weapons.Aviojet_White_Smoke)

    class Pylon3:
        Aviojet_Yellow_Smoke = (3, Weapons.Aviojet_Yellow_Smoke)

    pylons = {1, 2, 3}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.AFAC, task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.CAP


class C_101CC(PlaneType):
    id = "C-101CC"
    height = 4.25
    width = 14
    length = 12.25
    fuel_max = 1885
    max_speed = 925.2
    category = "Air"
    radio_frequency = 127.5

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                15: 265
            },
        },
    }

    class Pylon1:
        AIM_9M = (1, Weapons.AIM_9M)
        AIM_9P = (1, Weapons.AIM_9P)
        R_550_Magic_2 = (1, Weapons.R_550_Magic_2)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        BR_500 = (1, Weapons.BR_500)

    class Pylon2:
        Sea_Eagle = (2, Weapons.Sea_Eagle)
        Mk_84 = (2, Weapons.Mk_84)
        Mk_82 = (2, Weapons.Mk_82)
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_68___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (2, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (2, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (2, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        BL755 = (2, Weapons.BL755)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_100 = (2, Weapons.FAB_100)
        BR_250 = (2, Weapons.BR_250)
        BR_500 = (2, Weapons.BR_500)
        BIN_200 = (2, Weapons.BIN_200)

    class Pylon3:
        LAU_68___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (3, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        Mk_84 = (3, Weapons.Mk_84)
        Mk_82 = (3, Weapons.Mk_82)
        BL755 = (3, Weapons.BL755)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_100 = (3, Weapons.FAB_100)
        BR_250 = (3, Weapons.BR_250)
        BR_500 = (3, Weapons.BR_500)
        BIN_200 = (3, Weapons.BIN_200)
        BRU_42_3_BDU_33 = (3, Weapons.BRU_42_3_BDU_33)

    class Pylon4:
        DEFA_553_cal_30_mm = (4, Weapons.DEFA_553_cal_30_mm)
        AN_M3_cal_0_5_in = (4, Weapons.AN_M3_cal_0_5_in)

    class Pylon5:
        LAU_68___7_2_75__rockets_M151__HE_ = (5, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (5, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (5, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (5, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        Mk_84 = (5, Weapons.Mk_84)
        Mk_82 = (5, Weapons.Mk_82)
        BL755 = (5, Weapons.BL755)
        FAB_250 = (5, Weapons.FAB_250)
        FAB_100 = (5, Weapons.FAB_100)
        BR_250 = (5, Weapons.BR_250)
        BR_500 = (5, Weapons.BR_500)
        BIN_200 = (5, Weapons.BIN_200)
        BRU_42_3_BDU_33 = (5, Weapons.BRU_42_3_BDU_33)

    class Pylon6:
        Sea_Eagle = (6, Weapons.Sea_Eagle)
        Mk_84 = (6, Weapons.Mk_84)
        Mk_82 = (6, Weapons.Mk_82)
        LAU_61___19_2_75__rockets_MK151_HE = (6, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_68___7_2_75__rockets_M151__HE_ = (6, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (6, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (6, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (6, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        BL755 = (6, Weapons.BL755)
        FAB_250 = (6, Weapons.FAB_250)
        FAB_100 = (6, Weapons.FAB_100)
        BR_250 = (6, Weapons.BR_250)
        BR_500 = (6, Weapons.BR_500)
        BIN_200 = (6, Weapons.BIN_200)

    class Pylon7:
        AIM_9M = (7, Weapons.AIM_9M)
        AIM_9P = (7, Weapons.AIM_9P)
        R_550_Magic_2 = (7, Weapons.R_550_Magic_2)
        LAU_61___19_2_75__rockets_MK151_HE = (7, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        BR_500 = (7, Weapons.BR_500)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.AFAC, task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.CAP


class F_5E(PlaneType):
    id = "F-5E"
    height = 4.06
    width = 8.53
    length = 14.68
    fuel_max = 1996
    max_speed = 1742.4
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 0
    flare_charge_size = 0
    category = "Air"
    radio_frequency = 305

    class Pylon1:
        AIM_9P = (1, Weapons.AIM_9P)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        Mk_82 = (2, Weapons.Mk_82)
        Mk_82_SnakeEye = (2, Weapons.Mk_82_SnakeEye)
        M_117 = (2, Weapons.M_117)
        CBU_52B = (2, Weapons.CBU_52B)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (2, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (2, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (2, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (2, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        SUU_25___8_LUU_2 = (2, Weapons.SUU_25___8_LUU_2)
        GBU_12 = (2, Weapons.GBU_12)

    class Pylon3:
        Mk_82 = (3, Weapons.Mk_82)
        Mk_82_SnakeEye = (3, Weapons.Mk_82_SnakeEye)
        Mk_83 = (3, Weapons.Mk_83)
        M_117 = (3, Weapons.M_117)
        CBU_52B = (3, Weapons.CBU_52B)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (3, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (3, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        F_5_275Gal_Fuel_tank = (3, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (3, Weapons.F_5_150Gal_Fuel_tank)
        GBU_12 = (3, Weapons.GBU_12)
        MXU_648_TP = (3, Weapons.MXU_648_TP)

    class Pylon4:
        Mk_82 = (4, Weapons.Mk_82)
        Mk_82_SnakeEye = (4, Weapons.Mk_82_SnakeEye)
        Mk_83 = (4, Weapons.Mk_83)
        Mk_84 = (4, Weapons.Mk_84)
        M_117 = (4, Weapons.M_117)
        CBU_52B = (4, Weapons.CBU_52B)
        F_5_275Gal_Fuel_tank = (4, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (4, Weapons.F_5_150Gal_Fuel_tank)
        _5_Mk_82 = (4, Weapons._5_Mk_82)
        _5_Mk_82_SnakeEye = (4, Weapons._5_Mk_82_SnakeEye)
        MXU_648_TP = (4, Weapons.MXU_648_TP)

    class Pylon5:
        Mk_82 = (5, Weapons.Mk_82)
        Mk_82_SnakeEye = (5, Weapons.Mk_82_SnakeEye)
        Mk_83 = (5, Weapons.Mk_83)
        M_117 = (5, Weapons.M_117)
        CBU_52B = (5, Weapons.CBU_52B)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (5, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (5, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (5, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (5, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (5, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (5, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (5, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (5, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_61___19_2_75__rockets_MK151_HE = (5, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (5, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        F_5_275Gal_Fuel_tank = (5, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (5, Weapons.F_5_150Gal_Fuel_tank)
        GBU_12 = (5, Weapons.GBU_12)
        MXU_648_TP = (5, Weapons.MXU_648_TP)

    class Pylon6:
        Mk_82 = (6, Weapons.Mk_82)
        Mk_82_SnakeEye = (6, Weapons.Mk_82_SnakeEye)
        M_117 = (6, Weapons.M_117)
        CBU_52B = (6, Weapons.CBU_52B)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (6, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (6, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (6, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (6, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (6, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (6, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (6, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (6, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_61___19_2_75__rockets_MK151_HE = (6, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (6, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        SUU_25___8_LUU_2 = (6, Weapons.SUU_25___8_LUU_2)
        GBU_12 = (6, Weapons.GBU_12)

    class Pylon7:
        AIM_9P = (7, Weapons.AIM_9P)
        Smokewinder___red = (7, Weapons.Smokewinder___red)
        Smokewinder___green = (7, Weapons.Smokewinder___green)
        Smokewinder___blue = (7, Weapons.Smokewinder___blue)
        Smokewinder___white = (7, Weapons.Smokewinder___white)
        Smokewinder___yellow = (7, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (7, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod = (7, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAS, task.GroundAttack, task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.Reconnaissance]
    task_default = task.CAP


class F_5E_3(PlaneType):
    id = "F-5E-3"
    height = 4.06
    width = 8.53
    length = 14.68
    fuel_max = 2046
    max_speed = 1742.4
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Air"
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
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
        AIM_9P = (1, Weapons.AIM_9P)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod)

    class Pylon2:
        Mk_82 = (2, Weapons.Mk_82)
        Mk_82_SnakeEye = (2, Weapons.Mk_82_SnakeEye)
        M_117 = (2, Weapons.M_117)
        CBU_52B = (2, Weapons.CBU_52B)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (2, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (2, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (2, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (2, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (2, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        SUU_25___8_LUU_2 = (2, Weapons.SUU_25___8_LUU_2)
        GBU_12 = (2, Weapons.GBU_12)

    class Pylon3:
        Mk_82 = (3, Weapons.Mk_82)
        Mk_82_SnakeEye = (3, Weapons.Mk_82_SnakeEye)
        Mk_83 = (3, Weapons.Mk_83)
        M_117 = (3, Weapons.M_117)
        CBU_52B = (3, Weapons.CBU_52B)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (3, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (3, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (3, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (3, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (3, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (3, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        F_5_275Gal_Fuel_tank = (3, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (3, Weapons.F_5_150Gal_Fuel_tank)
        GBU_12 = (3, Weapons.GBU_12)
        MXU_648_TP = (3, Weapons.MXU_648_TP)

    class Pylon4:
        Mk_82 = (4, Weapons.Mk_82)
        Mk_82_SnakeEye = (4, Weapons.Mk_82_SnakeEye)
        Mk_83 = (4, Weapons.Mk_83)
        Mk_84 = (4, Weapons.Mk_84)
        M_117 = (4, Weapons.M_117)
        CBU_52B = (4, Weapons.CBU_52B)
        F_5_275Gal_Fuel_tank = (4, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (4, Weapons.F_5_150Gal_Fuel_tank)
        _5_Mk_82 = (4, Weapons._5_Mk_82)
        _5_Mk_82_SnakeEye = (4, Weapons._5_Mk_82_SnakeEye)
        MXU_648_TP = (4, Weapons.MXU_648_TP)

    class Pylon5:
        Mk_82 = (5, Weapons.Mk_82)
        Mk_82_SnakeEye = (5, Weapons.Mk_82_SnakeEye)
        Mk_83 = (5, Weapons.Mk_83)
        M_117 = (5, Weapons.M_117)
        CBU_52B = (5, Weapons.CBU_52B)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (5, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (5, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (5, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (5, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (5, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (5, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (5, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (5, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_61___19_2_75__rockets_MK151_HE = (5, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (5, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        F_5_275Gal_Fuel_tank = (5, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (5, Weapons.F_5_150Gal_Fuel_tank)
        GBU_12 = (5, Weapons.GBU_12)
        MXU_648_TP = (5, Weapons.MXU_648_TP)

    class Pylon6:
        Mk_82 = (6, Weapons.Mk_82)
        Mk_82_SnakeEye = (6, Weapons.Mk_82_SnakeEye)
        M_117 = (6, Weapons.M_117)
        CBU_52B = (6, Weapons.CBU_52B)
        LAU_68___7_2_75__rockets_MK1__Practice_ = (6, Weapons.LAU_68___7_2_75__rockets_MK1__Practice_)
        LAU_68___7_2_75__rockets_MK5__HE_ = (6, Weapons.LAU_68___7_2_75__rockets_MK5__HE_)
        LAU_68___7_2_75__rockets_MK61__Practice_ = (6, Weapons.LAU_68___7_2_75__rockets_MK61__Practice_)
        LAU_68___7_2_75__rockets_M151__HE_ = (6, Weapons.LAU_68___7_2_75__rockets_M151__HE_)
        LAU_68___7_2_75__rockets_M156_WP_ = (6, Weapons.LAU_68___7_2_75__rockets_M156_WP_)
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = (6, Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_)
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = (6, Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_)
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = (6, Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_)
        LAU_61___19_2_75__rockets_MK151_HE = (6, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (6, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        SUU_25___8_LUU_2 = (6, Weapons.SUU_25___8_LUU_2)
        GBU_12 = (6, Weapons.GBU_12)

    class Pylon7:
        AIM_9P = (7, Weapons.AIM_9P)
        Smokewinder___red = (7, Weapons.Smokewinder___red)
        Smokewinder___green = (7, Weapons.Smokewinder___green)
        Smokewinder___blue = (7, Weapons.Smokewinder___blue)
        Smokewinder___white = (7, Weapons.Smokewinder___white)
        Smokewinder___yellow = (7, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (7, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod = (7, Weapons.AN_ASQ_T50_TCTS_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAS, task.GroundAttack, task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.Reconnaissance]
    task_default = task.CAP


class F_86F_Sabre(PlaneType):
    id = "F-86F Sabre"
    flyable = True
    height = 4.496
    width = 11.9
    length = 11.43
    fuel_max = 1282
    max_speed = 964.8
    category = "Air"
    radio_frequency = 225

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                15: 265
            },
        },
    }

    class Pylon1:
        Fuel_Tank_200_gallons = (1, Weapons.Fuel_Tank_200_gallons)
        Fuel_Tank_120_gallons = (1, Weapons.Fuel_Tank_120_gallons)
        HVARx2 = (1, Weapons.HVARx2)
        HVAR_SMOKE_2 = (1, Weapons.HVAR_SMOKE_2)

    class Pylon2:
        HVARx2 = (2, Weapons.HVARx2)
        HVAR_SMOKE_2 = (2, Weapons.HVAR_SMOKE_2)

    class Pylon3:
        HVARx2 = (3, Weapons.HVARx2)
        HVAR_SMOKE_2 = (3, Weapons.HVAR_SMOKE_2)

    class Pylon4:
        Fuel_Tank_120_gallons = (4, Weapons.Fuel_Tank_120_gallons)
        AN_M64_ = (4, Weapons.AN_M64_)
        HVARx2 = (4, Weapons.HVARx2)
        HVAR_SMOKE_2 = (4, Weapons.HVAR_SMOKE_2)

    class Pylon5:
        GAR_8 = (5, Weapons.GAR_8)

    class Pylon6:
        GAR_8 = (6, Weapons.GAR_8)

    class Pylon7:
        Fuel_Tank_120_gallons = (7, Weapons.Fuel_Tank_120_gallons)
        AN_M64_ = (7, Weapons.AN_M64_)
        HVARx2 = (7, Weapons.HVARx2)
        HVAR_SMOKE_2 = (7, Weapons.HVAR_SMOKE_2)

    class Pylon8:
        HVARx2 = (8, Weapons.HVARx2)
        HVAR_SMOKE_2 = (8, Weapons.HVAR_SMOKE_2)

    class Pylon9:
        HVARx2 = (9, Weapons.HVARx2)
        HVAR_SMOKE_2 = (9, Weapons.HVAR_SMOKE_2)

    class Pylon10:
        Fuel_Tank_200_gallons = (10, Weapons.Fuel_Tank_200_gallons)
        Fuel_Tank_120_gallons = (10, Weapons.Fuel_Tank_120_gallons)
        HVARx2 = (10, Weapons.HVARx2)
        HVAR_SMOKE_2 = (10, Weapons.HVAR_SMOKE_2)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept, task.AntishipStrike]
    task_default = task.CAP


class Hawk(PlaneType):
    id = "Hawk"
    flyable = True
    height = 4.02
    width = 9.418
    length = 11.98
    fuel_max = 1272
    max_speed = 2880
    category = "Air"
    radio_frequency = 127.5

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                15: 265
            },
        },
    }

    class Pylon1:
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        CBU_87 = (1, Weapons.CBU_87)
        BRU_42_3_BDU_33 = (1, Weapons.BRU_42_3_BDU_33)
        _3_Mk_82 = (1, Weapons._3_Mk_82)

    class Pylon2:
        AIM_9M = (2, Weapons.AIM_9M)

    class Pylon3:
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        UPK_23_250 = (3, Weapons.UPK_23_250)

    class Pylon4:
        AIM_9M = (4, Weapons.AIM_9M)

    class Pylon5:
        LAU_61___19_2_75__rockets_MK151_HE = (5, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        CBU_87 = (5, Weapons.CBU_87)
        BRU_42_3_BDU_33 = (5, Weapons.BRU_42_3_BDU_33)
        _3_Mk_82 = (5, Weapons._3_Mk_82)

    pylons = {1, 2, 3, 4, 5}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept]
    task_default = task.CAP


class L_39C(PlaneType):
    id = "L-39C"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 980
    max_speed = 763.2
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 0
    flare_charge_size = 0
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
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
        FAB_100 = (1, Weapons.FAB_100)
        SAB_100 = (1, Weapons.SAB_100)
        UB_16___16_S_5KO = (1, Weapons.UB_16___16_S_5KO)
        P_50T = (1, Weapons.P_50T)
        Fuel_Tank_150_liters = (1, Weapons.Fuel_Tank_150_liters)
        R_3S = (1, Weapons.R_3S)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        Smoke_Generator___red_ = (2, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (2, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (2, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (2, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (2, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (2, Weapons.Smoke_Generator___orange_)

    class Pylon3:
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)
        UB_16___16_S_5KO = (3, Weapons.UB_16___16_S_5KO)
        P_50T = (3, Weapons.P_50T)
        Fuel_Tank_150_liters = (3, Weapons.Fuel_Tank_150_liters)
        R_3S = (3, Weapons.R_3S)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3}

    tasks = [task.GroundAttack, task.RunwayAttack, task.CAS, task.AFAC, task.CAP, task.AntishipStrike]
    task_default = task.CAS


class L_39ZA(PlaneType):
    id = "L-39ZA"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 980
    max_speed = 763.2
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 0
    flare_charge_size = 0
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
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
        FAB_100 = (1, Weapons.FAB_100)
        SAB_100 = (1, Weapons.SAB_100)
        FAB_250 = (1, Weapons.FAB_250)
        OFAB_100_Jupiter = (1, Weapons.OFAB_100_Jupiter)
        P_50T = (1, Weapons.P_50T)
        OFAB_100_Jupiter_x2 = (1, Weapons.OFAB_100_Jupiter_x2)
        UB_16___16_S_5KO = (1, Weapons.UB_16___16_S_5KO)
        PK_3 = (1, Weapons.PK_3)
        R_3S = (1, Weapons.R_3S)
        APU_60_1_R_60M = (1, Weapons.APU_60_1_R_60M)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        FAB_100 = (2, Weapons.FAB_100)
        SAB_100 = (2, Weapons.SAB_100)
        FAB_250 = (2, Weapons.FAB_250)
        OFAB_100_Jupiter = (2, Weapons.OFAB_100_Jupiter)
        P_50T = (2, Weapons.P_50T)
        OFAB_100_Jupiter_x2 = (2, Weapons.OFAB_100_Jupiter_x2)
        UB_16___16_S_5KO = (2, Weapons.UB_16___16_S_5KO)
        PK_3 = (2, Weapons.PK_3)
        Fuel_Tank_150_liters = (2, Weapons.Fuel_Tank_150_liters)
        Fuel_Tank_350_liters = (2, Weapons.Fuel_Tank_350_liters)

    class Pylon3:
        Smoke_Generator___red_ = (3, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (3, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (3, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (3, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (3, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (3, Weapons.Smoke_Generator___orange_)

    class Pylon4:
        FAB_100 = (4, Weapons.FAB_100)
        SAB_100 = (4, Weapons.SAB_100)
        FAB_250 = (4, Weapons.FAB_250)
        OFAB_100_Jupiter = (4, Weapons.OFAB_100_Jupiter)
        P_50T = (4, Weapons.P_50T)
        OFAB_100_Jupiter_x2 = (4, Weapons.OFAB_100_Jupiter_x2)
        UB_16___16_S_5KO = (4, Weapons.UB_16___16_S_5KO)
        PK_3 = (4, Weapons.PK_3)
        Fuel_Tank_150_liters = (4, Weapons.Fuel_Tank_150_liters)
        Fuel_Tank_350_liters = (4, Weapons.Fuel_Tank_350_liters)

    class Pylon5:
        FAB_100 = (5, Weapons.FAB_100)
        SAB_100 = (5, Weapons.SAB_100)
        FAB_250 = (5, Weapons.FAB_250)
        OFAB_100_Jupiter = (5, Weapons.OFAB_100_Jupiter)
        P_50T = (5, Weapons.P_50T)
        OFAB_100_Jupiter_x2 = (5, Weapons.OFAB_100_Jupiter_x2)
        UB_16___16_S_5KO = (5, Weapons.UB_16___16_S_5KO)
        PK_3 = (5, Weapons.PK_3)
        R_3S = (5, Weapons.R_3S)
        APU_60_1_R_60M = (5, Weapons.APU_60_1_R_60M)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)

    pylons = {1, 2, 3, 4, 5}

    tasks = [task.GroundAttack, task.RunwayAttack, task.CAS, task.AFAC, task.CAP, task.AntishipStrike]
    task_default = task.CAS


class M_2000C(PlaneType):
    id = "M-2000C"
    flyable = True
    height = 5.2
    width = 9.13
    length = 14.36
    fuel_max = 3165
    max_speed = 2520
    chaff = 112
    flare = 16
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Air"

    panel_radio = {
        1: {
            "channels": {
                1: 305,
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
        2: {
            "channels": {
                1: 129,
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
                12: 139,
                13: 140,
                7: 141,
                14: 131,
                19: 124,
                15: 134
            },
        },
    }

    class Pylon1:
        R_550_Magic_2 = (1, Weapons.R_550_Magic_2)
        Matra_Magic_II = (1, Weapons.Matra_Magic_II)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)

    class Pylon2:
        Super_530D = (2, Weapons.Super_530D)
        Matra_Super_530D = (2, Weapons.Matra_Super_530D)
        Matra_Type_155_Rocket_Pod = (2, Weapons.Matra_Type_155_Rocket_Pod)
        Mk_82 = (2, Weapons.Mk_82)
        Mk_82_SnakeEye = (2, Weapons.Mk_82_SnakeEye)
        Mk_20 = (2, Weapons.Mk_20)
        AUF2_MK_82_x_2 = (2, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (2, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_BLG_66_x_2 = (2, Weapons.AUF2_BLG_66_x_2)
        RPL_541_2000_liters_Fuel_Tank_ = (2, Weapons.RPL_541_2000_liters_Fuel_Tank_)

    class Pylon3:
        Mk_82 = (3, Weapons.Mk_82)
        Mk_82_SnakeEye = (3, Weapons.Mk_82_SnakeEye)
        Mk_20 = (3, Weapons.Mk_20)
        GBU_12 = (3, Weapons.GBU_12)

    class Pylon4:
        Mk_82 = (4, Weapons.Mk_82)
        Mk_82_SnakeEye = (4, Weapons.Mk_82_SnakeEye)
        Mk_20 = (4, Weapons.Mk_20)

    class Pylon5:
        Mk_20 = (5, Weapons.Mk_20)
        GBU_12 = (5, Weapons.GBU_12)
        GBU_16 = (5, Weapons.GBU_16)
        GBU_24 = (5, Weapons.GBU_24)
        AUF2_GBU_12_x_2 = (5, Weapons.AUF2_GBU_12_x_2)
        RPL_522_1300_liters_Fuel_Tank = (5, Weapons.RPL_522_1300_liters_Fuel_Tank)

    class Pylon6:
        Mk_82 = (6, Weapons.Mk_82)
        Mk_82_SnakeEye = (6, Weapons.Mk_82_SnakeEye)
        Mk_20 = (6, Weapons.Mk_20)

    class Pylon7:
        Mk_82 = (7, Weapons.Mk_82)
        Mk_82_SnakeEye = (7, Weapons.Mk_82_SnakeEye)
        Mk_20 = (7, Weapons.Mk_20)
        GBU_12 = (7, Weapons.GBU_12)

    class Pylon8:
        Super_530D = (8, Weapons.Super_530D)
        Matra_Super_530D = (8, Weapons.Matra_Super_530D)
        Matra_Type_155_Rocket_Pod = (8, Weapons.Matra_Type_155_Rocket_Pod)
        Mk_82 = (8, Weapons.Mk_82)
        Mk_82_SnakeEye = (8, Weapons.Mk_82_SnakeEye)
        Mk_20 = (8, Weapons.Mk_20)
        AUF2_MK_82_x_2 = (8, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (8, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_BLG_66_x_2 = (8, Weapons.AUF2_BLG_66_x_2)
        RPL_541_2000_liters_Fuel_Tank__ = (8, Weapons.RPL_541_2000_liters_Fuel_Tank__)

    class Pylon9:
        R_550_Magic_2 = (9, Weapons.R_550_Magic_2)
        Matra_Magic_II = (9, Weapons.Matra_Magic_II)
        Smokewinder___red = (9, Weapons.Smokewinder___red)
        Smokewinder___white = (9, Weapons.Smokewinder___white)
        Smokewinder___blue = (9, Weapons.Smokewinder___blue)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.AFAC, task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.CAP


class MiG_15bis(PlaneType):
    id = "MiG-15bis"
    flyable = True
    height = 3.7
    width = 10.08
    length = 10.11
    fuel_max = 1172
    max_speed = 992
    category = "Air"
    radio_frequency = 3.75

    class Pylon1:
        FAB_50 = (1, Weapons.FAB_50)
        FAB_100M = (1, Weapons.FAB_100M)
        PTB400_MIG15 = (1, Weapons.PTB400_MIG15)
        PTB600_MIG15 = (1, Weapons.PTB600_MIG15)
        PTB300_MIG15 = (1, Weapons.PTB300_MIG15)

    class Pylon2:
        FAB_50 = (2, Weapons.FAB_50)
        FAB_100M = (2, Weapons.FAB_100M)
        PTB400_MIG15 = (2, Weapons.PTB400_MIG15)
        PTB600_MIG15 = (2, Weapons.PTB600_MIG15)
        PTB300_MIG15 = (2, Weapons.PTB300_MIG15)

    pylons = {1, 2}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept]
    task_default = task.CAP


class MiG_21Bis(PlaneType):
    id = "MiG-21Bis"
    flyable = True
    height = 4.125
    width = 7.154
    length = 14.5
    fuel_max = 2280
    max_speed = 2509.2
    chaff = 32
    flare = 32
    charge_total = 64
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 124,
                2: 150,
                4: 131,
                8: 133,
                16: 123,
                17: 132,
                9: 122,
                18: 127,
                5: 141,
                10: 124,
                20: 138,
                11: 134,
                3: 121,
                6: 126,
                12: 125,
                13: 135,
                7: 130,
                14: 137,
                19: 129,
                15: 136
            },
        },
    }

    class Pylon1:
        UB_16UM___16_S_5M = (1, Weapons.UB_16UM___16_S_5M)
        S_24B__ = (1, Weapons.S_24B__)
        S_24A = (1, Weapons.S_24A)
        FAB_100 = (1, Weapons.FAB_100)
        FAB_250 = (1, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (1, Weapons.RBK_250_PTAB_2_5M)
        FAB_250_M54_TU = (1, Weapons.FAB_250_M54_TU)
        SAB_100 = (1, Weapons.SAB_100)
        R_3R = (1, Weapons.R_3R)
        R_3S = (1, Weapons.R_3S)
        RS_2US = (1, Weapons.RS_2US)
        R_60 = (1, Weapons.R_60)
        R_60M_ = (1, Weapons.R_60M_)
        R_60M_x_2 = (1, Weapons.R_60M_x_2)
        R_60_x_2 = (1, Weapons.R_60_x_2)
        Fuel_Tank_490_L__21_ = (1, Weapons.Fuel_Tank_490_L__21_)

    class Pylon2:
        UB_16UM___16_S_5M = (2, Weapons.UB_16UM___16_S_5M)
        UB_32M___32_S_5M = (2, Weapons.UB_32M___32_S_5M)
        S_24B__ = (2, Weapons.S_24B__)
        S_24A = (2, Weapons.S_24A)
        FAB_100_x_4 = (2, Weapons.FAB_100_x_4)
        FAB_100 = (2, Weapons.FAB_100)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        BetAB_500 = (2, Weapons.BetAB_500)
        BetAB_500ShP = (2, Weapons.BetAB_500ShP)
        RBK_250_PTAB_2_5M = (2, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (2, Weapons.RBK_500_PTAB_10_5)
        BL755 = (2, Weapons.BL755)
        SAB_100 = (2, Weapons.SAB_100)
        Kh_66_Grom__21__APU_68 = (2, Weapons.Kh_66_Grom__21__APU_68)
        R_13M = (2, Weapons.R_13M)
        R_13M1 = (2, Weapons.R_13M1)
        R_3R = (2, Weapons.R_3R)
        R_3S = (2, Weapons.R_3S)
        RS_2US = (2, Weapons.RS_2US)
        R_55 = (2, Weapons.R_55)
        R_60 = (2, Weapons.R_60)
        R_60M_ = (2, Weapons.R_60M_)
        R_60M_x_2 = (2, Weapons.R_60M_x_2)
        R_60_x_2 = (2, Weapons.R_60_x_2)
        UPK_23_250_ = (2, Weapons.UPK_23_250_)

    class Pylon3:
        RN_24 = (3, Weapons.RN_24)
        RN_28 = (3, Weapons.RN_28)
        SPS_141_100__21_ = (3, Weapons.SPS_141_100__21_)
        Fuel_Tank_490_L_Central__21_ = (3, Weapons.Fuel_Tank_490_L_Central__21_)
        Fuel_Tank_800_L__21_ = (3, Weapons.Fuel_Tank_800_L__21_)

    class Pylon4:
        UB_16UM___16_S_5M = (4, Weapons.UB_16UM___16_S_5M)
        UB_32M___32_S_5M = (4, Weapons.UB_32M___32_S_5M)
        S_24B__ = (4, Weapons.S_24B__)
        S_24A = (4, Weapons.S_24A)
        FAB_100_x_4 = (4, Weapons.FAB_100_x_4)
        FAB_100 = (4, Weapons.FAB_100)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        BetAB_500 = (4, Weapons.BetAB_500)
        BetAB_500ShP = (4, Weapons.BetAB_500ShP)
        RBK_250_PTAB_2_5M = (4, Weapons.RBK_250_PTAB_2_5M)
        RBK_500_PTAB_10_5 = (4, Weapons.RBK_500_PTAB_10_5)
        BL755 = (4, Weapons.BL755)
        SAB_100 = (4, Weapons.SAB_100)
        Kh_66_Grom__21__APU_68 = (4, Weapons.Kh_66_Grom__21__APU_68)
        R_13M = (4, Weapons.R_13M)
        R_13M1 = (4, Weapons.R_13M1)
        R_3R = (4, Weapons.R_3R)
        R_3S = (4, Weapons.R_3S)
        RS_2US = (4, Weapons.RS_2US)
        R_55 = (4, Weapons.R_55)
        R_60 = (4, Weapons.R_60)
        R_60M_ = (4, Weapons.R_60M_)
        R_60M_x_2_ = (4, Weapons.R_60M_x_2_)
        R_60_x_2_ = (4, Weapons.R_60_x_2_)
        UPK_23_250_ = (4, Weapons.UPK_23_250_)

    class Pylon5:
        UB_16UM___16_S_5M = (5, Weapons.UB_16UM___16_S_5M)
        S_24B__ = (5, Weapons.S_24B__)
        S_24A = (5, Weapons.S_24A)
        FAB_100 = (5, Weapons.FAB_100)
        FAB_250 = (5, Weapons.FAB_250)
        RBK_250_PTAB_2_5M = (5, Weapons.RBK_250_PTAB_2_5M)
#ERRR {40A24F07-CD7D-4F83-89A2-39B2258B62C6}
        FAB_250_M54_TU = (5, Weapons.FAB_250_M54_TU)
        SAB_100 = (5, Weapons.SAB_100)
        R_3R = (5, Weapons.R_3R)
        R_3S = (5, Weapons.R_3S)
        RS_2US = (5, Weapons.RS_2US)
        R_60 = (5, Weapons.R_60)
        R_60M_ = (5, Weapons.R_60M_)
        R_60M_x_2_ = (5, Weapons.R_60M_x_2_)
        R_60_x_2_ = (5, Weapons.R_60_x_2_)
        Fuel_Tank_490_L__21_ = (5, Weapons.Fuel_Tank_490_L__21_)

    class Pylon6:
        ASO_2 = (6, Weapons.ASO_2)
        SPRD_99 = (6, Weapons.SPRD_99)

    class Pylon7:
        Smoke___white___21 = (7, Weapons.Smoke___white___21)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.Intercept, task.CAP, task.Escort, task.CAS, task.GroundAttack]
    task_default = task.CAP


class MQ_9_Reaper(PlaneType):
    id = "MQ-9 Reaper"
    group_size_max = 1
    height = 4.77
    width = 20
    length = 11
    fuel_max = 1300
    max_speed = 400
    eplrs = True

    class Pylon1:
        GBU_12 = (1, Weapons.GBU_12)
        GBU_38 = (1, Weapons.GBU_38)
        AGM114x2_OH_58 = (1, Weapons.AGM114x2_OH_58)
        AGM_114K___4 = (1, Weapons.AGM_114K___4)

    class Pylon2:
        GBU_12 = (2, Weapons.GBU_12)
        GBU_38 = (2, Weapons.GBU_38)
        AGM114x2_OH_58 = (2, Weapons.AGM114x2_OH_58)

    class Pylon3:
        GBU_12 = (3, Weapons.GBU_12)
        GBU_38 = (3, Weapons.GBU_38)
        AGM114x2_OH_58 = (3, Weapons.AGM114x2_OH_58)

    class Pylon4:
        GBU_12 = (4, Weapons.GBU_12)
        GBU_38 = (4, Weapons.GBU_38)
        AGM114x2_OH_58 = (4, Weapons.AGM114x2_OH_58)
        AGM_114K___4 = (4, Weapons.AGM_114K___4)

    pylons = {1, 2, 3, 4}

    tasks = [task.GroundAttack, task.CAS, task.AFAC, task.Reconnaissance]
    task_default = task.Reconnaissance


class TF_51D(PlaneType):
    id = "TF-51D"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 501
    max_speed = 763.2
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
    }

    pylons = {}

    tasks = [task.Reconnaissance]
    task_default = task.Reconnaissance


plane_map = {
    "Tornado GR4": Tornado_GR4,
    "Tornado IDS": Tornado_IDS,
    "F/A-18A": F_A_18A,
    "F/A-18C": F_A_18C,
    "MiG-29S": MiG_29S,
    "MiG-29A": MiG_29A,
    "F-14A": F_14A,
    "Tu-22M3": Tu_22M3,
    "F-4E": F_4E,
    "B-52H": B_52H,
    "MiG-27K": MiG_27K,
    "F-111F": F_111F,
    "A-10A": A_10A,
    "Su-27": Su_27,
    "MiG-29G": MiG_29G,
    "MiG-23MLD": MiG_23MLD,
    "Su-25": Su_25,
    "Su-25TM": Su_25TM,
    "Su-25T": Su_25T,
    "Su-33": Su_33,
    "MiG-25PD": MiG_25PD,
    "MiG-25RBT": MiG_25RBT,
    "Su-30": Su_30,
    "Su-34": Su_34,
    "Su-17M4": Su_17M4,
    "MiG-31": MiG_31,
    "Tu-95MS": Tu_95MS,
    "Su-24M": Su_24M,
    "Su-24MR": Su_24MR,
    "Tu-160": Tu_160,
    "F-117A": F_117A,
    "B-1B": B_1B,
    "S-3B": S_3B,
    "S-3B Tanker": S_3B_Tanker,
    "Mirage 2000-5": Mirage_2000_5,
    "F-15C": F_15C,
    "F-15E": F_15E,
    "MiG-29K": MiG_29K,
    "Tu-142": Tu_142,
    "C-130": C_130,
    "An-26B": An_26B,
    "An-30M": An_30M,
    "C-17A": C_17A,
    "A-50": A_50,
    "E-3A": E_3A,
    "IL-78M": IL_78M,
    "E-2C": E_2C,
    "IL-76MD": IL_76MD,
    "F-16C bl.50": F_16C_bl_50,
    "F-16C bl.52d": F_16C_bl_52d,
    "F-16A": F_16A,
    "F-16A MLU": F_16A_MLU,
    "RQ-1A Predator": RQ_1A_Predator,
    "Yak-40": Yak_40,
    "A-10C": A_10C,
    "KC-135": KC_135,
    "P-51D": P_51D,
    "FW-190D9": FW_190D9,
    "Bf-109K-4": Bf_109K_4,
    "C-101EB": C_101EB,
    "C-101CC": C_101CC,
    "F-5E": F_5E,
    "F-5E-3": F_5E_3,
    "F-86F Sabre": F_86F_Sabre,
    "Hawk": Hawk,
    "L-39C": L_39C,
    "L-39ZA": L_39ZA,
    "M-2000C": M_2000C,
    "MiG-15bis": MiG_15bis,
    "MiG-21Bis": MiG_21Bis,
    "MQ-9 Reaper": MQ_9_Reaper,
    "TF-51D": TF_51D,
}
