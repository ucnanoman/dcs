# This file is generated from plane_export.lua

from .weapons_data import Weapons


class PlaneType:
    id = ""
    group_size_max = 4
    large_parking_slot = False
    fuel_max = 0
    ammo_type = None
    gun_max = 100
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Air"

    pylons = {}

    tasks = ['Nothing']


class Tornado_GR4(PlaneType):
    id = "Tornado GR4"
    fuel_max = 4663
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        BOZ_107 = Weapons.BOZ_107
        Sky_Shadow_ECM_Pod = Weapons.Sky_Shadow_ECM_Pod

    class Pylon2:
        TORNADO_Fuel_tank = Weapons.TORNADO_Fuel_tank

    class Pylon3:
        AIM_9M = Weapons.AIM_9M
        ALARM = Weapons.ALARM
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon4:
        GBU_16 = Weapons.GBU_16
        ALARM = Weapons.ALARM
        Sea_Eagle = Weapons.Sea_Eagle
        GBU_27 = Weapons.GBU_27

    class Pylon5:
        GBU_12 = Weapons.GBU_12
        AN_AAQ_28_LITENING = Weapons.AN_AAQ_28_LITENING

    class Pylon6:
        GBU_12 = Weapons.GBU_12

    class Pylon7:
        GBU_12 = Weapons.GBU_12

    class Pylon8:
        GBU_12 = Weapons.GBU_12

    class Pylon9:
        GBU_16 = Weapons.GBU_16
        ALARM = Weapons.ALARM
        Sea_Eagle = Weapons.Sea_Eagle
        GBU_27 = Weapons.GBU_27

    class Pylon10:
        AIM_9M = Weapons.AIM_9M
        ALARM = Weapons.ALARM
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon11:
        TORNADO_Fuel_tank = Weapons.TORNADO_Fuel_tank

    class Pylon12:
        BOZ_107 = Weapons.BOZ_107
        Sky_Shadow_ECM_Pod = Weapons.Sky_Shadow_ECM_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = ["Pinpoint Strike", "Ground Attack", "SEAD", "AFAC", "Antiship Strike""Reconnaissance"]
    task_default = "Ground Attack"


class Tornado_IDS(PlaneType):
    id = "Tornado IDS"
    fuel_max = 4663
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        BOZ_107 = Weapons.BOZ_107
        Sky_Shadow_ECM_Pod = Weapons.Sky_Shadow_ECM_Pod

    class Pylon2:
        AGM_88C_ = Weapons.AGM_88C_
        Kormoran = Weapons.Kormoran
        TORNADO_Fuel_tank = Weapons.TORNADO_Fuel_tank

    class Pylon3:
        AIM_9M = Weapons.AIM_9M
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon4:
        GBU_16 = Weapons.GBU_16
        AGM_88C_ = Weapons.AGM_88C_
        Kormoran = Weapons.Kormoran

    class Pylon5:
        Mk_82 = Weapons.Mk_82

    class Pylon6:
        Mk_82 = Weapons.Mk_82

    class Pylon7:
        Mk_82 = Weapons.Mk_82

    class Pylon8:
        Mk_82 = Weapons.Mk_82

    class Pylon9:
        GBU_16 = Weapons.GBU_16
        AGM_88C_ = Weapons.AGM_88C_
        Kormoran = Weapons.Kormoran

    class Pylon10:
        AIM_9M = Weapons.AIM_9M
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon11:
        AGM_88C_ = Weapons.AGM_88C_
        Kormoran = Weapons.Kormoran
        TORNADO_Fuel_tank = Weapons.TORNADO_Fuel_tank

    class Pylon12:
        BOZ_107 = Weapons.BOZ_107
        Sky_Shadow_ECM_Pod = Weapons.Sky_Shadow_ECM_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = ["Pinpoint Strike", "Ground Attack", "SEAD", "AFAC", "Antiship Strike""Reconnaissance"]
    task_default = "Ground Attack"


class F_A_18A(PlaneType):
    id = "F/A-18A"
    fuel_max = 6531
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        AIM_7M = Weapons.AIM_7M
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        AGM_84A = Weapons.AGM_84A
        AGM_88C_ = Weapons.AGM_88C_
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        LAU_117_AGM_65E = Weapons.LAU_117_AGM_65E
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_16 = Weapons.GBU_16
        MER_2_MK_82 = Weapons.MER_2_MK_82
        Mk_84 = Weapons.Mk_84
        _2_Mk_20_Rockeye = Weapons._2_Mk_20_Rockeye

    class Pylon3:
        AIM_7M = Weapons.AIM_7M
        AGM_84A = Weapons.AGM_84A
        AGM_88C_ = Weapons.AGM_88C_
        MER_2_MK_82 = Weapons.MER_2_MK_82
        Fuel_tank_330_gal = Weapons.Fuel_tank_330_gal

    class Pylon4:
        AIM_7M = Weapons.AIM_7M
        AN_AAS_38_FLIR = Weapons.AN_AAS_38_FLIR

    class Pylon5:
        Fuel_tank_330_gal = Weapons.Fuel_tank_330_gal

    class Pylon6:
        AIM_7M = Weapons.AIM_7M
        AN_ASQ_173_LST_SCAM = Weapons.AN_ASQ_173_LST_SCAM

    class Pylon7:
        AIM_7M = Weapons.AIM_7M
        AGM_84A = Weapons.AGM_84A
        AGM_88C_ = Weapons.AGM_88C_
        MER_2_MK_82 = Weapons.MER_2_MK_82
        Fuel_tank_330_gal = Weapons.Fuel_tank_330_gal

    class Pylon8:
        AIM_7M = Weapons.AIM_7M
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        AGM_84A = Weapons.AGM_84A
        AGM_88C_ = Weapons.AGM_88C_
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        LAU_117_AGM_65E = Weapons.LAU_117_AGM_65E
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_16 = Weapons.GBU_16
        MER_2_MK_82 = Weapons.MER_2_MK_82
        Mk_84 = Weapons.Mk_84
        _2_Mk_20_Rockeye = Weapons._2_Mk_20_Rockeye

    class Pylon9:
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Pinpoint Strike", "CAS", "Ground Attack", "Runway Attack", "SEAD", "AFAC", "Antiship Strike""Reconnaissance"]
    task_default = "CAP"


class F_A_18C(PlaneType):
    id = "F/A-18C"
    fuel_max = 6531
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        AGM_84A = Weapons.AGM_84A
        AGM_84E = Weapons.AGM_84E
        AGM_88C_ = Weapons.AGM_88C_
        LAU_117_AGM_65E = Weapons.LAU_117_AGM_65E
        AGM_154C = Weapons.AGM_154C
        AGM_62 = Weapons.AGM_62
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_16 = Weapons.GBU_16
        MER_2_MK_82 = Weapons.MER_2_MK_82
        Mk_84 = Weapons.Mk_84
        _2_Mk_20_Rockeye = Weapons._2_Mk_20_Rockeye
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G

    class Pylon3:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M
        AGM_84A = Weapons.AGM_84A
        AGM_84E = Weapons.AGM_84E
        AGM_88C_ = Weapons.AGM_88C_
        MER_2_MK_82 = Weapons.MER_2_MK_82
        Fuel_tank_330_gal_ = Weapons.Fuel_tank_330_gal_
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_16 = Weapons.GBU_16
        Mk_84 = Weapons.Mk_84
        _2_Mk_20_Rockeye = Weapons._2_Mk_20_Rockeye
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_

    class Pylon4:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M
        AN_AAS_38_FLIR = Weapons.AN_AAS_38_FLIR

    class Pylon5:
        Fuel_tank_330_gal_ = Weapons.Fuel_tank_330_gal_
        AN_AAQ_28_LITENING = Weapons.AN_AAQ_28_LITENING

    class Pylon6:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M
        AN_ASQ_173_LST_SCAM = Weapons.AN_ASQ_173_LST_SCAM

    class Pylon7:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M
        AGM_84A = Weapons.AGM_84A
        AGM_84E = Weapons.AGM_84E
        AGM_88C_ = Weapons.AGM_88C_
        MER_2_MK_82 = Weapons.MER_2_MK_82
        Fuel_tank_330_gal_ = Weapons.Fuel_tank_330_gal_
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_16 = Weapons.GBU_16
        Mk_84 = Weapons.Mk_84
        _2_Mk_20_Rockeye = Weapons._2_Mk_20_Rockeye
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_

    class Pylon8:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        AGM_84A = Weapons.AGM_84A
        AGM_84E = Weapons.AGM_84E
        AGM_88C_ = Weapons.AGM_88C_
        LAU_117_AGM_65E = Weapons.LAU_117_AGM_65E
        AGM_154C = Weapons.AGM_154C
        AGM_62 = Weapons.AGM_62
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_16 = Weapons.GBU_16
        MER_2_MK_82 = Weapons.MER_2_MK_82
        Mk_84 = Weapons.Mk_84
        _2_Mk_20_Rockeye = Weapons._2_Mk_20_Rockeye
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_

    class Pylon9:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Pinpoint Strike", "CAS", "Ground Attack", "Runway Attack", "SEAD", "AFAC", "Antiship Strike""Reconnaissance"]
    task_default = "CAP"


class MiG_29S(PlaneType):
    id = "MiG-29S"
    fuel_max = 3500
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon3:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        R_27T = Weapons.R_27T
        R_27ET = Weapons.R_27ET
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Fuel_tank_1150L_MiG_29 = Weapons.Fuel_tank_1150L_MiG_29
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon4:
        Fuel_tank_1500L = Weapons.Fuel_tank_1500L
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon5:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        R_27T = Weapons.R_27T
        R_27ET = Weapons.R_27ET
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Fuel_tank_1150L_MiG_29 = Weapons.Fuel_tank_1150L_MiG_29
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon6:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon7:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "AFAC", "Ground Attack", "CAS", "Runway Attack""Antiship Strike"]
    task_default = "CAP"


class MiG_29A(PlaneType):
    id = "MiG-29A"
    fuel_max = 3380
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        R_73 = Weapons.R_73
        R_60M = Weapons.R_60M
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon3:
        R_27R = Weapons.R_27R
        R_27T = Weapons.R_27T
        R_27ER = Weapons.R_27ER
        R_27ET = Weapons.R_27ET
        R_73 = Weapons.R_73
        R_60M = Weapons.R_60M
        Fuel_tank_1150L_MiG_29 = Weapons.Fuel_tank_1150L_MiG_29
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon4:
        Fuel_tank_1500L = Weapons.Fuel_tank_1500L
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon5:
        R_27R = Weapons.R_27R
        R_27T = Weapons.R_27T
        R_27ER = Weapons.R_27ER
        R_27ET = Weapons.R_27ET
        R_73 = Weapons.R_73
        R_60M = Weapons.R_60M
        Fuel_tank_1150L_MiG_29 = Weapons.Fuel_tank_1150L_MiG_29
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon6:
        R_73 = Weapons.R_73
        R_60M = Weapons.R_60M
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon7:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "AFAC", "Ground Attack", "CAS", "Runway Attack""Antiship Strike"]
    task_default = "CAP"


class F_14A(PlaneType):
    id = "F-14A"
    fuel_max = 7348
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        AIM_54C = Weapons.AIM_54C
        AIM_7M = Weapons.AIM_7M

    class Pylon3:
        Fuel_tank_367_gal = Weapons.Fuel_tank_367_gal

    class Pylon4:
        AIM_54C = Weapons.AIM_54C

    class Pylon5:
        AIM_54C = Weapons.AIM_54C

    class Pylon6:
        AIM_7M = Weapons.AIM_7M

    class Pylon7:
        AIM_7M = Weapons.AIM_7M

    class Pylon8:
        AIM_54C = Weapons.AIM_54C

    class Pylon9:
        AIM_54C = Weapons.AIM_54C

    class Pylon10:
        Fuel_tank_367_gal = Weapons.Fuel_tank_367_gal

    class Pylon11:
        AIM_54C = Weapons.AIM_54C
        AIM_7M = Weapons.AIM_7M

    class Pylon12:
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept""Reconnaissance"]
    task_default = "Intercept"


class Tu_22M3(PlaneType):
    id = "Tu-22M3"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 50000
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        Kh_22N = Weapons.Kh_22N
        MER_9_FAB_250 = Weapons.MER_9_FAB_250

    class Pylon2:
        MER_9_FAB_250 = Weapons.MER_9_FAB_250

    class Pylon3:
        Kh_22N = Weapons.Kh_22N
        FAB_500_33 = Weapons.FAB_500_33
        FAB_250_33 = Weapons.FAB_250_33

    class Pylon4:
        MER_9_FAB_250 = Weapons.MER_9_FAB_250

    class Pylon5:
        Kh_22N = Weapons.Kh_22N
        MER_9_FAB_250 = Weapons.MER_9_FAB_250

    pylons = {1, 2, 3, 4, 5}

    tasks = ["Antiship Strike", "Ground Attack""Runway Attack"]
    task_default = "Antiship Strike"


class F_4E(PlaneType):
    id = "F-4E"
    fuel_max = 4864
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        _3_Mk_20_Rockeye = Weapons._3_Mk_20_Rockeye
        MER_6_Mk_82 = Weapons.MER_6_Mk_82
        Mk_84 = Weapons.Mk_84
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        LAU_61___19_2_75__rockets_MK151_HE = Weapons.LAU_61___19_2_75__rockets_MK151_HE
        LAU_61_3___57_2_75__rockets_MK151__HE_ = Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_
        LAU_61___19_2_75__rockets_MK156_WP = Weapons.LAU_61___19_2_75__rockets_MK156_WP
        F_4_Fuel_tank_W = Weapons.F_4_Fuel_tank_W
        AGM_45B_ = Weapons.AGM_45B_

    class Pylon2:
        LAU_7___2_AIM_9M = Weapons.LAU_7___2_AIM_9M
        LAU_7___2_AIM_9P = Weapons.LAU_7___2_AIM_9P
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        _3_Mk_20_Rockeye = Weapons._3_Mk_20_Rockeye
        _3_Mk_82 = Weapons._3_Mk_82
        Mk_84 = Weapons.Mk_84
        LAU_88_AGM_65K_2 = Weapons.LAU_88_AGM_65K_2
        LAU_88_AGM_65D_2 = Weapons.LAU_88_AGM_65D_2
        AGM_45B_ = Weapons.AGM_45B_
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        LAU_61_3___57_2_75__rockets_MK151__HE_ = Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_
        LAU_7___AN_ASQ_T50 = Weapons.LAU_7___AN_ASQ_T50

    class Pylon3:
        AIM_7M = Weapons.AIM_7M
        ALQ_131 = Weapons.ALQ_131

    class Pylon4:
        AIM_7M = Weapons.AIM_7M

    class Pylon5:
        F_4_Fuel_tank_C = Weapons.F_4_Fuel_tank_C

    class Pylon6:
        AIM_7M = Weapons.AIM_7M

    class Pylon7:
        AIM_7M = Weapons.AIM_7M

    class Pylon8:
        LAU_7___2_AIM_9M = Weapons.LAU_7___2_AIM_9M
        LAU_7___2_AIM_9P = Weapons.LAU_7___2_AIM_9P
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        _3_Mk_20_Rockeye = Weapons._3_Mk_20_Rockeye
        _3_Mk_82 = Weapons._3_Mk_82
        Mk_84 = Weapons.Mk_84
        LAU_88_AGM_65K_2_ = Weapons.LAU_88_AGM_65K_2_
        LAU_88_AGM_65D_2_ = Weapons.LAU_88_AGM_65D_2_
        AGM_45B_ = Weapons.AGM_45B_
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        LAU_61_3___57_2_75__rockets_MK151__HE_ = Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_

    class Pylon9:
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        _3_Mk_20_Rockeye = Weapons._3_Mk_20_Rockeye
        MER_6_Mk_82 = Weapons.MER_6_Mk_82
        Mk_84 = Weapons.Mk_84
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        LAU_61___19_2_75__rockets_MK151_HE = Weapons.LAU_61___19_2_75__rockets_MK151_HE
        LAU_61_3___57_2_75__rockets_MK151__HE_ = Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_
        LAU_61___19_2_75__rockets_MK156_WP = Weapons.LAU_61___19_2_75__rockets_MK156_WP
        F_4_Fuel_tank_W = Weapons.F_4_Fuel_tank_W
        AGM_45B_ = Weapons.AGM_45B_

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Ground Attack", "CAS", "Pinpoint Strike", "SEAD", "AFAC", "Reconnaissance""Antiship Strike"]
    task_default = "CAP"


class B_52H(PlaneType):
    id = "B-52H"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 141135
    chaff = 1125
    flare = 192
    charge_total = 1317
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        MER_12_Mk_82 = Weapons.MER_12_Mk_82
        HSAB_9_Mk_20_Rockeye = Weapons.HSAB_9_Mk_20_Rockeye
        HSAB_9_Mk_84 = Weapons.HSAB_9_Mk_84
        MER_6_AGM_86C = Weapons.MER_6_AGM_86C

    class Pylon2:
        _27_Mk_82 = Weapons._27_Mk_82
        AGM_86C_8 = Weapons.AGM_86C_8
        AGM_84A_8 = Weapons.AGM_84A_8

    class Pylon3:
        MER_12_Mk_82 = Weapons.MER_12_Mk_82
        HSAB_9_Mk_20_Rockeye = Weapons.HSAB_9_Mk_20_Rockeye
        HSAB_9_Mk_84 = Weapons.HSAB_9_Mk_84
        MER_6_AGM_86C = Weapons.MER_6_AGM_86C
        HSAB_9GBU_31 = Weapons.HSAB_9GBU_31

    pylons = {1, 2, 3}

    tasks = ["Ground Attack", "Runway Attack", "Pinpoint Strike", "Antiship Strike""CAS"]
    task_default = "Ground Attack"


class MiG_27K(PlaneType):
    id = "MiG-27K"
    fuel_max = 4500
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon2:
        Kh_25ML_ = Weapons.Kh_25ML_
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25MR = Weapons.Kh_25MR
        Kh_29L_ = Weapons.Kh_29L_
        Kh_29T_ = Weapons.Kh_29T_
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        MER_6_2_FAB_250 = Weapons.MER_6_2_FAB_250
        R_60M = Weapons.R_60M

    class Pylon3:
        R_60M = Weapons.R_60M
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM

    class Pylon4:
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M

    class Pylon5:
        Fuel_tank_800L = Weapons.Fuel_tank_800L

    class Pylon6:
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M

    class Pylon7:
        R_60M = Weapons.R_60M
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM

    class Pylon8:
        Kh_25ML_ = Weapons.Kh_25ML_
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25MR = Weapons.Kh_25MR
        Kh_29L_ = Weapons.Kh_29L_
        Kh_29T_ = Weapons.Kh_29T_
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        MER_6_2_FAB_250 = Weapons.MER_6_2_FAB_250
        R_60M = Weapons.R_60M

    pylons = {2, 3, 4, 5, 6, 7, 8}

    tasks = ["Pinpoint Strike", "CAS", "Ground Attack", "Runway Attack", "SEAD""Antiship Strike"]
    task_default = "Ground Attack"


class F_111F(PlaneType):
    id = "F-111F"
    fuel_max = 15500
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        MER_6_Mk_82 = Weapons.MER_6_Mk_82
        MER_6_Mk_20_Rockeye = Weapons.MER_6_Mk_20_Rockeye
        MER_6_BLU_107 = Weapons.MER_6_BLU_107
        Mk_84 = Weapons.Mk_84
        GBU_28 = Weapons.GBU_28
        GBU_15 = Weapons.GBU_15
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_24 = Weapons.GBU_24
        AIM_9M = Weapons.AIM_9M

    class Pylon2:
        MER_6_Mk_82 = Weapons.MER_6_Mk_82
        MER_6_Mk_20_Rockeye = Weapons.MER_6_Mk_20_Rockeye
        MER_6_BLU_107 = Weapons.MER_6_BLU_107
        Mk_84 = Weapons.Mk_84
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_24 = Weapons.GBU_24
        AIM_9M = Weapons.AIM_9M

    class Pylon3:
        Pavetack_F_111 = Weapons.Pavetack_F_111

    class Pylon4:
        _6_Mk_82 = Weapons._6_Mk_82
        Mk_20_Rockeye__6 = Weapons.Mk_20_Rockeye__6
        Mk_84 = Weapons.Mk_84
        GBU_28 = Weapons.GBU_28
        GBU_15 = Weapons.GBU_15
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_24 = Weapons.GBU_24

    class Pylon5:
        MER_6_Mk_82 = Weapons.MER_6_Mk_82
        MER_6_Mk_20_Rockeye = Weapons.MER_6_Mk_20_Rockeye
        MER_6_BLU_107 = Weapons.MER_6_BLU_107
        Mk_84 = Weapons.Mk_84
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_24 = Weapons.GBU_24
        AIM_9M = Weapons.AIM_9M

    class Pylon6:
        MER_6_Mk_82 = Weapons.MER_6_Mk_82
        MER_6_Mk_20_Rockeye = Weapons.MER_6_Mk_20_Rockeye
        MER_6_BLU_107 = Weapons.MER_6_BLU_107
        Mk_84 = Weapons.Mk_84
        GBU_28 = Weapons.GBU_28
        GBU_15 = Weapons.GBU_15
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_24 = Weapons.GBU_24
        AIM_9M = Weapons.AIM_9M

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = ["Ground Attack", "Runway Attack", "Pinpoint Strike""AFAC"]
    task_default = "Ground Attack"


class A_10A(PlaneType):
    id = "A-10A"
    fuel_max = 5029
    chaff = 240
    flare = 120
    charge_total = 480
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        LAU_105___2_AIM_9M = Weapons.LAU_105___2_AIM_9M
        LAU_105_1_AIM_9M_L = Weapons.LAU_105_1_AIM_9M_L
        LAU_105_1_CATM_9M_L = Weapons.LAU_105_1_CATM_9M_L
        LAU_105___2_AIM_9P = Weapons.LAU_105___2_AIM_9P
        ALQ_131 = Weapons.ALQ_131
        ALQ_184 = Weapons.ALQ_184
        Smokewinder___red_smk = Weapons.Smokewinder___red_smk
        Smokewinder___green = Weapons.Smokewinder___green
        Smokewinder___blue_smk = Weapons.Smokewinder___blue_smk
        Smokewinder___white = Weapons.Smokewinder___white
        Smokewinder___yellow = Weapons.Smokewinder___yellow
        Smokewinder___orange = Weapons.Smokewinder___orange
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        CBU_97 = Weapons.CBU_97
        Mk_82 = Weapons.Mk_82
        LAU_105_AIS_ASQ_T50_L = Weapons.LAU_105_AIS_ASQ_T50_L

    class Pylon2:
        Mk_82 = Weapons.Mk_82
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
        CBU_97 = Weapons.CBU_97

    class Pylon3:
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65D_2 = Weapons.LAU_88_AGM_65D_2
        LAU_88_AGM_65H_2_L = Weapons.LAU_88_AGM_65H_2_L
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_CATM_65K = Weapons.LAU_117_CATM_65K
        LAU_117_TGM_65D = Weapons.LAU_117_TGM_65D
        LAU_117_TGM_65G = Weapons.LAU_117_TGM_65G
        LAU_117_TGM_65H = Weapons.LAU_117_TGM_65H
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        _3_Mk_82 = Weapons._3_Mk_82
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
        CBU_97 = Weapons.CBU_97

    class Pylon4:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        _3_Mk_82 = Weapons._3_Mk_82
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
        Fuel_Tank_FT600 = Weapons.Fuel_Tank_FT600
        CBU_97 = Weapons.CBU_97

    class Pylon5:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        CBU_97 = Weapons.CBU_97

    class Pylon6:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        Fuel_Tank_FT600 = Weapons.Fuel_Tank_FT600
        CBU_97 = Weapons.CBU_97

    class Pylon7:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        CBU_97 = Weapons.CBU_97

    class Pylon8:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        _3_Mk_82 = Weapons._3_Mk_82
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
        Fuel_Tank_FT600 = Weapons.Fuel_Tank_FT600
        CBU_97 = Weapons.CBU_97

    class Pylon9:
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65D_2_ = Weapons.LAU_88_AGM_65D_2_
        LAU_88_AGM_65H_2_R = Weapons.LAU_88_AGM_65H_2_R
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_CATM_65K = Weapons.LAU_117_CATM_65K
        LAU_117_TGM_65D = Weapons.LAU_117_TGM_65D
        LAU_117_TGM_65G = Weapons.LAU_117_TGM_65G
        LAU_117_TGM_65H = Weapons.LAU_117_TGM_65H
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        _3_Mk_82 = Weapons._3_Mk_82
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
        CBU_97 = Weapons.CBU_97

    class Pylon10:
        Mk_82 = Weapons.Mk_82
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
        CBU_97 = Weapons.CBU_97

    class Pylon11:
        LAU_105___2_AIM_9M = Weapons.LAU_105___2_AIM_9M
        LAU_105_1_AIM_9M_R = Weapons.LAU_105_1_AIM_9M_R
        LAU_105_1_CATM_9M_R = Weapons.LAU_105_1_CATM_9M_R
        LAU_105___2_AIM_9P = Weapons.LAU_105___2_AIM_9P
        ALQ_131 = Weapons.ALQ_131
        ALQ_184 = Weapons.ALQ_184
        Smokewinder___red_smk = Weapons.Smokewinder___red_smk
        Smokewinder___green = Weapons.Smokewinder___green
        Smokewinder___blue_smk = Weapons.Smokewinder___blue_smk
        Smokewinder___white = Weapons.Smokewinder___white
        Smokewinder___yellow = Weapons.Smokewinder___yellow
        Smokewinder___orange = Weapons.Smokewinder___orange
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        CBU_97 = Weapons.CBU_97
        Mk_82 = Weapons.Mk_82
        LAU_105_AIS_ASQ_T50_R = Weapons.LAU_105_AIS_ASQ_T50_R

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = ["Ground Attack", "CAS", "AFAC", "Runway Attack""Antiship Strike"]
    task_default = "CAS"


class Su_27(PlaneType):
    id = "Su-27"
    fuel_max = 9400
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__left_ = Weapons.L005_Sorbtsiya_ECM_pod__left_
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        R_73 = Weapons.R_73
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon3:
        R_73 = Weapons.R_73
        R_27R = Weapons.R_27R
        R_27T = Weapons.R_27T
        R_27ER = Weapons.R_27ER
        R_27ET = Weapons.R_27ET
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        SAB_100 = Weapons.SAB_100
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon4:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        SAB_100 = Weapons.SAB_100
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon5:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        SAB_100 = Weapons.SAB_100
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon6:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        SAB_100 = Weapons.SAB_100
        MER_6_FAB_100 = Weapons.MER_6_FAB_100

    class Pylon7:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        SAB_100 = Weapons.SAB_100
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon8:
        R_73 = Weapons.R_73
        R_27R = Weapons.R_27R
        R_27T = Weapons.R_27T
        R_27ER = Weapons.R_27ER
        R_27ET = Weapons.R_27ET
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        SAB_100 = Weapons.SAB_100
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon9:
        R_73 = Weapons.R_73
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon10:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__right_ = Weapons.L005_Sorbtsiya_ECM_pod__right_
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = ["CAP", "Intercept", "Escort", "Fighter Sweep", "AFAC", "Ground Attack", "Runway Attack""Antiship Strike"]
    task_default = "CAP"


class MiG_29G(PlaneType):
    id = "MiG-29G"
    fuel_max = 3380
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        R_73 = Weapons.R_73
        R_60M = Weapons.R_60M
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon3:
        R_27R = Weapons.R_27R
        R_73 = Weapons.R_73
        R_60M = Weapons.R_60M
        Fuel_tank_1150L_MiG_29 = Weapons.Fuel_tank_1150L_MiG_29
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon4:
        Fuel_tank_1500L = Weapons.Fuel_tank_1500L

    class Pylon5:
        R_27R = Weapons.R_27R
        R_73 = Weapons.R_73
        R_60M = Weapons.R_60M
        Fuel_tank_1150L_MiG_29 = Weapons.Fuel_tank_1150L_MiG_29
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon6:
        R_73 = Weapons.R_73
        R_60M = Weapons.R_60M
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon7:
        R_60M = Weapons.R_60M
        R_73 = Weapons.R_73
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept""AFAC"]
    task_default = "CAP"


class MiG_23MLD(PlaneType):
    id = "MiG-23MLD"
    fuel_max = 3800
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon2:
        R_24R = Weapons.R_24R
        R_24T = Weapons.R_24T
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_250 = Weapons.FAB_250
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62

    class Pylon3:
        R_60M_2 = Weapons.R_60M_2
        R_60M = Weapons.R_60M
        S_24B_ = Weapons.S_24B_
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62

    class Pylon4:
        Fuel_tank_800L = Weapons.Fuel_tank_800L

    class Pylon5:
        R_60M_2_ = Weapons.R_60M_2_
        R_60M = Weapons.R_60M
        S_24B_ = Weapons.S_24B_
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62

    class Pylon6:
        R_24R = Weapons.R_24R
        R_24T = Weapons.R_24T
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_250 = Weapons.FAB_250
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62

    pylons = {2, 3, 4, 5, 6}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Ground Attack""CAS"]
    task_default = "CAP"


class Su_25(PlaneType):
    id = "Su-25"
    fuel_max = 2835
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_60M = Weapons.R_60M
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        S_25L = Weapons.S_25L

    class Pylon3:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25ML_ = Weapons.Kh_25ML_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing

    class Pylon4:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25ML_ = Weapons.Kh_25ML_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon5:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_29L_ = Weapons.Kh_29L_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon6:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_29L_ = Weapons.Kh_29L_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon7:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25ML_ = Weapons.Kh_25ML_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon8:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25ML_ = Weapons.Kh_25ML_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing
        SPS_141 = Weapons.SPS_141

    class Pylon9:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        S_25L = Weapons.S_25L

    class Pylon10:
        R_60M = Weapons.R_60M
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = ["Ground Attack", "Runway Attack", "Pinpoint Strike", "CAS", "AFAC""Antiship Strike"]
    task_default = "CAS"


class Su_25TM(PlaneType):
    id = "Su-25TM"
    fuel_max = 3790
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_60M = Weapons.R_60M
        MPS_410 = Weapons.MPS_410
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        S_25L = Weapons.S_25L
        R_73_ = Weapons.R_73_

    class Pylon3:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25ML_ = Weapons.Kh_25ML_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing

    class Pylon4:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25ML_ = Weapons.Kh_25ML_
        APU_8___8_9A4172_Vikhr = Weapons.APU_8___8_9A4172_Vikhr
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon5:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500kr = Weapons.KAB_500kr
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        S_25L = Weapons.S_25L
        Kh_29L_ = Weapons.Kh_29L_
        Kh_29T_ = Weapons.Kh_29T_
        Kh_58U_ = Weapons.Kh_58U_
        Kh_31A_ = Weapons.Kh_31A_
        Kh_31P_ = Weapons.Kh_31P_
        Kh_35_ = Weapons.Kh_35_
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon6:
        Mercury_LLTV_Pod = Weapons.Mercury_LLTV_Pod
        Kopyo_radar_pod = Weapons.Kopyo_radar_pod
        L_081_Fantasmagoria_ELINT_pod = Weapons.L_081_Fantasmagoria_ELINT_pod

    class Pylon7:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500kr = Weapons.KAB_500kr
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        S_25L = Weapons.S_25L
        Kh_29L_ = Weapons.Kh_29L_
        Kh_29T_ = Weapons.Kh_29T_
        Kh_58U_ = Weapons.Kh_58U_
        Kh_31A_ = Weapons.Kh_31A_
        Kh_31P_ = Weapons.Kh_31P_
        Kh_35_ = Weapons.Kh_35_
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon8:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25ML_ = Weapons.Kh_25ML_
        APU_8___8_9A4172_Vikhr = Weapons.APU_8___8_9A4172_Vikhr
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon9:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25ML_ = Weapons.Kh_25ML_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing

    class Pylon10:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        S_25L = Weapons.S_25L
        R_73_ = Weapons.R_73_

    class Pylon11:
        R_60M = Weapons.R_60M
        MPS_410_ = Weapons.MPS_410_
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = ["Ground Attack", "Runway Attack", "Pinpoint Strike", "CAS", "SEAD", "AFAC""Antiship Strike"]
    task_default = "CAS"


class Su_25T(PlaneType):
    id = "Su-25T"
    fuel_max = 3790
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_60M = Weapons.R_60M
        MPS_410 = Weapons.MPS_410
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        S_25L = Weapons.S_25L
        R_73_ = Weapons.R_73_

    class Pylon3:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25ML_ = Weapons.Kh_25ML_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing

    class Pylon4:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25ML_ = Weapons.Kh_25ML_
        APU_8___8_9A4172_Vikhr = Weapons.APU_8___8_9A4172_Vikhr
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon5:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500kr = Weapons.KAB_500kr
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_29L_ = Weapons.Kh_29L_
        Kh_29T_ = Weapons.Kh_29T_
        Kh_58U_ = Weapons.Kh_58U_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon6:
        Mercury_LLTV_Pod = Weapons.Mercury_LLTV_Pod
        L_081_Fantasmagoria_ELINT_pod = Weapons.L_081_Fantasmagoria_ELINT_pod

    class Pylon7:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500kr = Weapons.KAB_500kr
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_29L_ = Weapons.Kh_29L_
        Kh_29T_ = Weapons.Kh_29T_
        Kh_58U_ = Weapons.Kh_58U_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon8:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25ML_ = Weapons.Kh_25ML_
        APU_8___8_9A4172_Vikhr = Weapons.APU_8___8_9A4172_Vikhr
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon9:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        Kh_25MPU_ = Weapons.Kh_25MPU_
        Kh_25ML_ = Weapons.Kh_25ML_
        S_25L = Weapons.S_25L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        Fuel_tank_800L_Wing = Weapons.Fuel_tank_800L_Wing

    class Pylon10:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100_ = Weapons.MBD_2_67U___4_FAB_100_
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        S_25L = Weapons.S_25L
        R_73_ = Weapons.R_73_

    class Pylon11:
        R_60M = Weapons.R_60M
        MPS_410_ = Weapons.MPS_410_
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = ["Ground Attack", "Runway Attack", "Pinpoint Strike", "CAS", "SEAD", "AFAC""Antiship Strike"]
    task_default = "CAS"


class Su_33(PlaneType):
    id = "Su-33"
    fuel_max = 9400
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__left_ = Weapons.L005_Sorbtsiya_ECM_pod__left_
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        R_73 = Weapons.R_73
        FAB_250 = Weapons.FAB_250
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon3:
        R_73 = Weapons.R_73
        R_27R = Weapons.R_27R
        R_27T = Weapons.R_27T
        R_27ET = Weapons.R_27ET
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_25_OFM = Weapons.S_25_OFM
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon4:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_25_OFM = Weapons.S_25_OFM
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon5:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon6:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        BetAB_500 = Weapons.BetAB_500
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon7:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62

    class Pylon8:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon9:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_25_OFM = Weapons.S_25_OFM
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon10:
        R_73 = Weapons.R_73
        R_27R = Weapons.R_27R
        R_27T = Weapons.R_27T
        R_27ET = Weapons.R_27ET
        R_27ER = Weapons.R_27ER
        FAB_250 = Weapons.FAB_250
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_500_M62 = Weapons.FAB_500_M62
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_25_OFM = Weapons.S_25_OFM
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon11:
        R_73 = Weapons.R_73
        FAB_250 = Weapons.FAB_250
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon12:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__right_ = Weapons.L005_Sorbtsiya_ECM_pod__right_
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "AFAC", "CAS", "Ground Attack", "Runway Attack""Antiship Strike"]
    task_default = "CAP"


class MiG_25PD(PlaneType):
    id = "MiG-25PD"
    fuel_max = 15245
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_40R = Weapons.R_40R
        R_40T = Weapons.R_40T
        R_60M = Weapons.R_60M

    class Pylon2:
        R_40R = Weapons.R_40R
        R_40T = Weapons.R_40T

    class Pylon3:
        R_40R = Weapons.R_40R
        R_40T = Weapons.R_40T

    class Pylon4:
        R_40R = Weapons.R_40R
        R_40T = Weapons.R_40T
        R_60M = Weapons.R_60M

    pylons = {1, 2, 3, 4}

    tasks = ["CAP", "Escort", "Fighter Sweep""Intercept"]
    task_default = "Intercept"


class MiG_25RBT(PlaneType):
    id = "MiG-25RBT"
    fuel_max = 15245

    class Pylon1:
        R_60M = Weapons.R_60M
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP

    class Pylon2:
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP

    class Pylon3:
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP

    class Pylon4:
        R_60M = Weapons.R_60M
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP

    pylons = {1, 2, 3, 4}

    tasks = ["Reconnaissance", "AFAC""Ground Attack"]
    task_default = "Reconnaissance"


class Su_30(PlaneType):
    id = "Su-30"
    fuel_max = 9400
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__left_ = Weapons.L005_Sorbtsiya_ECM_pod__left_
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    class Pylon2:
        R_73 = Weapons.R_73

    class Pylon3:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        R_27T = Weapons.R_27T
        R_27ET = Weapons.R_27ET
        R_73 = Weapons.R_73
        Kh_31P = Weapons.Kh_31P
        Kh_31A = Weapons.Kh_31A
        Kh_29L = Weapons.Kh_29L
        Kh_29T = Weapons.Kh_29T
        Kh_59M = Weapons.Kh_59M
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_25_OFM = Weapons.S_25_OFM
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        FAB_1500_M54 = Weapons.FAB_1500_M54
        KAB_1500L = Weapons.KAB_1500L
        MER_6_FAB_250 = Weapons.MER_6_FAB_250

    class Pylon4:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        R_27ET = Weapons.R_27ET
        Kh_31P = Weapons.Kh_31P
        Kh_31A = Weapons.Kh_31A
        Kh_29L = Weapons.Kh_29L
        Kh_29T = Weapons.Kh_29T
        BetAB_500 = Weapons.BetAB_500
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        MER_6_FAB_250 = Weapons.MER_6_FAB_250

    class Pylon5:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        Kh_35 = Weapons.Kh_35
        BetAB_500 = Weapons.BetAB_500
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        KAB_1500L = Weapons.KAB_1500L
        MER_6_FAB_250 = Weapons.MER_6_FAB_250

    class Pylon6:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        Kh_35 = Weapons.Kh_35
        BetAB_500 = Weapons.BetAB_500
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        MER_6_FAB_250 = Weapons.MER_6_FAB_250

    class Pylon7:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        R_27ET = Weapons.R_27ET
        Kh_31P = Weapons.Kh_31P
        Kh_31A = Weapons.Kh_31A
        Kh_29L = Weapons.Kh_29L
        Kh_29T = Weapons.Kh_29T
        BetAB_500 = Weapons.BetAB_500
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        MER_6_FAB_250 = Weapons.MER_6_FAB_250

    class Pylon8:
        R_27R = Weapons.R_27R
        R_27ER = Weapons.R_27ER
        R_27T = Weapons.R_27T
        R_27ET = Weapons.R_27ET
        R_73 = Weapons.R_73
        Kh_31P = Weapons.Kh_31P
        Kh_31A = Weapons.Kh_31A
        Kh_29L = Weapons.Kh_29L
        Kh_29T = Weapons.Kh_29T
        Kh_59M = Weapons.Kh_59M
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_25_OFM = Weapons.S_25_OFM
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        FAB_1500_M54 = Weapons.FAB_1500_M54
        KAB_1500L = Weapons.KAB_1500L
        MER_6_FAB_250 = Weapons.MER_6_FAB_250

    class Pylon9:
        R_73 = Weapons.R_73

    class Pylon10:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__right_ = Weapons.L005_Sorbtsiya_ECM_pod__right_
        Smoke_Generator___red_smk = Weapons.Smoke_Generator___red_smk
        Smoke_Generator___green = Weapons.Smoke_Generator___green
        Smoke_Generator___blue_smk = Weapons.Smoke_Generator___blue_smk
        Smoke_Generator___white = Weapons.Smoke_Generator___white
        Smoke_Generator___yellow = Weapons.Smoke_Generator___yellow
        Smoke_Generator___orange = Weapons.Smoke_Generator___orange

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "AFAC", "SEAD", "Antiship Strike", "CAS", "Pinpoint Strike", "Ground Attack""Runway Attack"]
    task_default = "CAP"


class Su_34(PlaneType):
    id = "Su-34"
    fuel_max = 9800
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__left_ = Weapons.L005_Sorbtsiya_ECM_pod__left_

    class Pylon2:
        R_73 = Weapons.R_73
        R_77 = Weapons.R_77
        FAB_250 = Weapons.FAB_250

    class Pylon3:
        R_73 = Weapons.R_73
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MR = Weapons.Kh_25MR
        Kh_29T = Weapons.Kh_29T
        Kh_31A = Weapons.Kh_31A
        Kh_31P = Weapons.Kh_31P
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        KAB_1500L = Weapons.KAB_1500L
        MER_3_3_RBK_250_PTAB_1M = Weapons.MER_3_3_RBK_250_PTAB_1M
        MER_3_3_RBK_500_PTAB_2_5M = Weapons.MER_3_3_RBK_500_PTAB_2_5M
        MER_3_3_FAB_100 = Weapons.MER_3_3_FAB_100
        MER_3_3_FAB_250 = Weapons.MER_3_3_FAB_250
        MER_3_3_FAB_500 = Weapons.MER_3_3_FAB_500
        MER_3_3_BetAB_500 = Weapons.MER_3_3_BetAB_500
        SAB_100 = Weapons.SAB_100

    class Pylon4:
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MR = Weapons.Kh_25MR
        Kh_29T = Weapons.Kh_29T
        Kh_29L = Weapons.Kh_29L
        Kh_31A = Weapons.Kh_31A
        Kh_31P = Weapons.Kh_31P
        Kh_59M = Weapons.Kh_59M
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        FAB_1500_M54 = Weapons.FAB_1500_M54
        KAB_1500L = Weapons.KAB_1500L
        MER_3_3_RBK_250_PTAB_1M = Weapons.MER_3_3_RBK_250_PTAB_1M
        MER_3_3_RBK_500_PTAB_2_5M = Weapons.MER_3_3_RBK_500_PTAB_2_5M
        MER_3_3_FAB_100 = Weapons.MER_3_3_FAB_100
        MER_3_3_FAB_250 = Weapons.MER_3_3_FAB_250
        MER_3_3_FAB_500 = Weapons.MER_3_3_FAB_500
        MER_3_3_BetAB_500 = Weapons.MER_3_3_BetAB_500
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        SAB_100 = Weapons.SAB_100

    class Pylon5:
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MR = Weapons.Kh_25MR
        Kh_29T = Weapons.Kh_29T
        Kh_29L = Weapons.Kh_29L
        Kh_31A = Weapons.Kh_31A
        Kh_31P = Weapons.Kh_31P
        BetAB_500 = Weapons.BetAB_500
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        MER_3_3_RBK_250_PTAB_1M = Weapons.MER_3_3_RBK_250_PTAB_1M
        MER_3_3_FAB_100 = Weapons.MER_3_3_FAB_100
        MER_3_3_FAB_250 = Weapons.MER_3_3_FAB_250
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        SAB_100 = Weapons.SAB_100

    class Pylon6:
        BetAB_500 = Weapons.BetAB_500
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        FAB_1500_M54 = Weapons.FAB_1500_M54
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        KAB_1500L = Weapons.KAB_1500L
        MER_3_3_RBK_250_PTAB_1M = Weapons.MER_3_3_RBK_250_PTAB_1M
        MER_3_3_RBK_500_PTAB_2_5M = Weapons.MER_3_3_RBK_500_PTAB_2_5M
        MER_3_3_FAB_100 = Weapons.MER_3_3_FAB_100
        MER_3_3_FAB_250 = Weapons.MER_3_3_FAB_250
        MER_3_3_FAB_500 = Weapons.MER_3_3_FAB_500
        MER_3_3_BetAB_500 = Weapons.MER_3_3_BetAB_500
        SAB_100 = Weapons.SAB_100

    class Pylon7:
        BetAB_500 = Weapons.BetAB_500
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        MER_3_3_RBK_250_PTAB_1M = Weapons.MER_3_3_RBK_250_PTAB_1M
        MER_3_3_RBK_500_PTAB_2_5M = Weapons.MER_3_3_RBK_500_PTAB_2_5M
        MER_3_3_FAB_100 = Weapons.MER_3_3_FAB_100
        MER_3_3_FAB_250 = Weapons.MER_3_3_FAB_250
        MER_3_3_FAB_500 = Weapons.MER_3_3_FAB_500
        MER_3_3_BetAB_500 = Weapons.MER_3_3_BetAB_500
        SAB_100 = Weapons.SAB_100

    class Pylon8:
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MR = Weapons.Kh_25MR
        Kh_29T = Weapons.Kh_29T
        Kh_29L = Weapons.Kh_29L
        Kh_31A = Weapons.Kh_31A
        Kh_31P = Weapons.Kh_31P
        BetAB_500 = Weapons.BetAB_500
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        MER_3_3_RBK_250_PTAB_1M = Weapons.MER_3_3_RBK_250_PTAB_1M
        MER_3_3_FAB_100 = Weapons.MER_3_3_FAB_100
        MER_3_3_FAB_250 = Weapons.MER_3_3_FAB_250
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        SAB_100 = Weapons.SAB_100

    class Pylon9:
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MR = Weapons.Kh_25MR
        Kh_29T = Weapons.Kh_29T
        Kh_29L = Weapons.Kh_29L
        Kh_31A = Weapons.Kh_31A
        Kh_31P = Weapons.Kh_31P
        Kh_59M = Weapons.Kh_59M
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        FAB_1500_M54 = Weapons.FAB_1500_M54
        KAB_1500L = Weapons.KAB_1500L
        MER_3_3_RBK_250_PTAB_1M = Weapons.MER_3_3_RBK_250_PTAB_1M
        MER_3_3_RBK_500_PTAB_2_5M = Weapons.MER_3_3_RBK_500_PTAB_2_5M
        MER_3_3_FAB_100 = Weapons.MER_3_3_FAB_100
        MER_3_3_FAB_250 = Weapons.MER_3_3_FAB_250
        MER_3_3_FAB_500 = Weapons.MER_3_3_FAB_500
        MER_3_3_BetAB_500 = Weapons.MER_3_3_BetAB_500
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        SAB_100 = Weapons.SAB_100

    class Pylon10:
        R_73 = Weapons.R_73
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MR = Weapons.Kh_25MR
        Kh_29T = Weapons.Kh_29T
        Kh_31A = Weapons.Kh_31A
        Kh_31P = Weapons.Kh_31P
        BetAB_500 = Weapons.BetAB_500
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        KAB_1500L = Weapons.KAB_1500L
        MER_3_3_RBK_250_PTAB_1M = Weapons.MER_3_3_RBK_250_PTAB_1M
        MER_3_3_RBK_500_PTAB_2_5M = Weapons.MER_3_3_RBK_500_PTAB_2_5M
        MER_3_3_FAB_100 = Weapons.MER_3_3_FAB_100
        MER_3_3_FAB_250 = Weapons.MER_3_3_FAB_250
        MER_3_3_FAB_500 = Weapons.MER_3_3_FAB_500
        MER_3_3_BetAB_500 = Weapons.MER_3_3_BetAB_500
        SAB_100 = Weapons.SAB_100
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF

    class Pylon11:
        R_73 = Weapons.R_73
        FAB_250 = Weapons.FAB_250

    class Pylon12:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__right_ = Weapons.L005_Sorbtsiya_ECM_pod__right_

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = ["AFAC", "SEAD", "Antiship Strike", "CAS", "Pinpoint Strike", "Ground Attack""Runway Attack"]
    task_default = "Ground Attack"


class Su_17M4(PlaneType):
    id = "Su-17M4"
    fuel_max = 3770
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        MER_4_FAB_250 = Weapons.MER_4_FAB_250
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        MER_4_RBK_250_PTAB_1M = Weapons.MER_4_RBK_250_PTAB_1M
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        MER_6_2_FAB_250 = Weapons.MER_6_2_FAB_250
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25MR = Weapons.Kh_25MR
        Fuel_tank_1150L = Weapons.Fuel_tank_1150L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    class Pylon2:
        R_60M = Weapons.R_60M

    class Pylon3:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        MER_4_FAB_250 = Weapons.MER_4_FAB_250
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        MER_4_RBK_250_PTAB_1M = Weapons.MER_4_RBK_250_PTAB_1M
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        MER_6_2_FAB_250 = Weapons.MER_6_2_FAB_250
        MER_6_4_FAB_250 = Weapons.MER_6_4_FAB_250
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25MR = Weapons.Kh_25MR
        Kh_29L = Weapons.Kh_29L
        Kh_29T = Weapons.Kh_29T
        Kh_58U = Weapons.Kh_58U
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod
        SPS_141 = Weapons.SPS_141

    class Pylon4:
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        MER_4_FAB_250 = Weapons.MER_4_FAB_250
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        MER_4_RBK_250_PTAB_1M = Weapons.MER_4_RBK_250_PTAB_1M
        MER_6_2_FAB_250 = Weapons.MER_6_2_FAB_250
        Fuel_tank_1150L = Weapons.Fuel_tank_1150L
        Fuel_tank_800L = Weapons.Fuel_tank_800L

    class Pylon5:
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        MER_4_FAB_250 = Weapons.MER_4_FAB_250
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        MER_4_RBK_250_PTAB_1M = Weapons.MER_4_RBK_250_PTAB_1M
        MER_6_2_FAB_250 = Weapons.MER_6_2_FAB_250
        Fuel_tank_1150L = Weapons.Fuel_tank_1150L
        Fuel_tank_800L = Weapons.Fuel_tank_800L

    class Pylon6:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        MER_4_FAB_250 = Weapons.MER_4_FAB_250
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        MER_4_RBK_250_PTAB_1M = Weapons.MER_4_RBK_250_PTAB_1M
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        MER_6_4_FAB_250 = Weapons.MER_6_4_FAB_250
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25MR = Weapons.Kh_25MR
        Kh_29L = Weapons.Kh_29L
        Kh_29T = Weapons.Kh_29T
        Kh_58U = Weapons.Kh_58U
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM
        SPPU_22_1_Gun_pod = Weapons.SPPU_22_1_Gun_pod

    class Pylon7:
        R_60M = Weapons.R_60M

    class Pylon8:
        B_8M1___20_S_8OFP2 = Weapons.B_8M1___20_S_8OFP2
        FAB_100 = Weapons.FAB_100
        SAB_100 = Weapons.SAB_100
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        MER_4_FAB_250 = Weapons.MER_4_FAB_250
        MER_6_2_FAB_250 = Weapons.MER_6_2_FAB_250
        MBD_2_67U___4_FAB_100 = Weapons.MBD_2_67U___4_FAB_100
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        MER_4_RBK_250_PTAB_1M = Weapons.MER_4_RBK_250_PTAB_1M
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25MR = Weapons.Kh_25MR
        Fuel_tank_1150L = Weapons.Fuel_tank_1150L
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        B_8M1___20_S_8TsM = Weapons.B_8M1___20_S_8TsM

    pylons = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = ["Ground Attack", "CAS", "Pinpoint Strike", "SEAD", "AFAC", "Runway Attack""Antiship Strike"]
    task_default = "Ground Attack"


class MiG_31(PlaneType):
    id = "MiG-31"
    fuel_max = 15500
    category = "Interceptor"

    class Pylon1:
        R_40R = Weapons.R_40R
        R_40T = Weapons.R_40T
        R_60M_2 = Weapons.R_60M_2

    class Pylon2:
        R_33 = Weapons.R_33

    class Pylon3:
        R_33 = Weapons.R_33

    class Pylon4:
        R_33 = Weapons.R_33

    class Pylon5:
        R_33 = Weapons.R_33

    class Pylon6:
        R_40R = Weapons.R_40R
        R_40T = Weapons.R_40T
        R_60M_2_ = Weapons.R_60M_2_

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = ["CAP", "Escort", "Fighter Sweep""Intercept"]
    task_default = "Intercept"


class Tu_95MS(PlaneType):
    id = "Tu-95MS"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 87000
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        Kh_65_6 = Weapons.Kh_65_6

    pylons = {1}

    tasks = ["Pinpoint Strike"]
    task_default = "Pinpoint Strike"


class Su_24M(PlaneType):
    id = "Su-24M"
    fuel_max = 11700
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_60M_2 = Weapons.R_60M_2
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        SAB_100 = Weapons.SAB_100
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        FAB_250 = Weapons.FAB_250
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25MR = Weapons.Kh_25MR

    class Pylon2:
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        Kh_29L = Weapons.Kh_29L
        Kh_29T = Weapons.Kh_29T
        Kh_31A = Weapons.Kh_31A
        Kh_31P = Weapons.Kh_31P
        Kh_58U = Weapons.Kh_58U
        Kh_59M = Weapons.Kh_59M
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25MR = Weapons.Kh_25MR
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        SAB_100 = Weapons.SAB_100
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        KAB_1500L = Weapons.KAB_1500L
        FAB_1500_M54 = Weapons.FAB_1500_M54
        Fuel_tank_3000L = Weapons.Fuel_tank_3000L

    class Pylon3:
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        SAB_100 = Weapons.SAB_100
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_

    class Pylon4:
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_250 = Weapons.FAB_250
        SAB_100 = Weapons.SAB_100
        KAB_1500L = Weapons.KAB_1500L
        FAB_1500_M54 = Weapons.FAB_1500_M54

    class Pylon5:
        Fuel_tank_2000L = Weapons.Fuel_tank_2000L
        L_081_Fantasmagoria_ELINT_pod = Weapons.L_081_Fantasmagoria_ELINT_pod
        FAB_250 = Weapons.FAB_250
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M

    class Pylon6:
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        SAB_100 = Weapons.SAB_100
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        S_24B_ = Weapons.S_24B_

    class Pylon7:
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        Kh_29L = Weapons.Kh_29L
        Kh_29T = Weapons.Kh_29T
        Kh_31A = Weapons.Kh_31A
        Kh_31P = Weapons.Kh_31P
        Kh_58U = Weapons.Kh_58U
        Kh_59M = Weapons.Kh_59M
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25MR = Weapons.Kh_25MR
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        FAB_250 = Weapons.FAB_250
        FAB_500_M62 = Weapons.FAB_500_M62
        RBK_500_PTAB_10_5 = Weapons.RBK_500_PTAB_10_5
        RBK_500U_PTAB_1M = Weapons.RBK_500U_PTAB_1M
        BetAB_500 = Weapons.BetAB_500
        BetAB_500ShP = Weapons.BetAB_500ShP
        KAB_500L = Weapons.KAB_500L
        KAB_500kr = Weapons.KAB_500kr
        KMGU_2___96_AO_2_5RT = Weapons.KMGU_2___96_AO_2_5RT
        KMGU_2___96_PTAB_2_5KO = Weapons.KMGU_2___96_PTAB_2_5KO
        SAB_100 = Weapons.SAB_100
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        KAB_1500L = Weapons.KAB_1500L
        FAB_1500_M54 = Weapons.FAB_1500_M54
        Fuel_tank_3000L = Weapons.Fuel_tank_3000L

    class Pylon8:
        R_60M_2_ = Weapons.R_60M_2_
        MER_6_FAB_100 = Weapons.MER_6_FAB_100
        RBK_250_PTAB_2_5M = Weapons.RBK_250_PTAB_2_5M
        SAB_100 = Weapons.SAB_100
        UB_32A___32_S_5KO = Weapons.UB_32A___32_S_5KO
        B_8M1___20_S_8KOM = Weapons.B_8M1___20_S_8KOM
        FAB_250 = Weapons.FAB_250
        B_13L___5_S_13_OF = Weapons.B_13L___5_S_13_OF
        S_24B_ = Weapons.S_24B_
        S_25_OFM = Weapons.S_25_OFM
        Kh_25ML = Weapons.Kh_25ML
        Kh_25MPU = Weapons.Kh_25MPU
        Kh_25MR = Weapons.Kh_25MR

    pylons = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = ["Ground Attack", "CAS", "Antiship Strike", "SEAD", "Pinpoint Strike", "AFAC""Runway Attack"]
    task_default = "Ground Attack"


class Su_24MR(PlaneType):
    id = "Su-24MR"
    fuel_max = 11700
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        R_60M_2 = Weapons.R_60M_2

    class Pylon2:
        Fuel_tank_3000L = Weapons.Fuel_tank_3000L

    class Pylon5:
        Fuel_tank_2000L = Weapons.Fuel_tank_2000L
        Tangazh_ELINT_pod = Weapons.Tangazh_ELINT_pod
        Shpil_2M_Laser_Intelligence_Pod = Weapons.Shpil_2M_Laser_Intelligence_Pod

    class Pylon7:
        Fuel_tank_3000L = Weapons.Fuel_tank_3000L

    class Pylon8:
        ETHER = Weapons.ETHER

    pylons = {1, 2, 5, 7, 8}

    tasks = ["AFAC""Reconnaissance"]
    task_default = "Reconnaissance"


class Tu_160(PlaneType):
    id = "Tu-160"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 157000
    chaff = 72
    flare = 72
    charge_total = 144
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        Kh_65_6 = Weapons.Kh_65_6

    class Pylon2:
        Kh_65_6 = Weapons.Kh_65_6

    pylons = {1, 2}

    tasks = ["Pinpoint Strike"]
    task_default = "Pinpoint Strike"


class F_117A(PlaneType):
    id = "F-117A"
    fuel_max = 3840

    class Pylon1:
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27

    class Pylon2:
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27

    pylons = {1, 2}

    tasks = ["Pinpoint Strike"]
    task_default = "Pinpoint Strike"


class B_1B(PlaneType):
    id = "B-1B"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 88450
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        MK_82_28 = Weapons.MK_82_28
        CBU87_10 = Weapons.CBU87_10
        CBU97_10 = Weapons.CBU97_10
        B_1B_Mk_84_8 = Weapons.B_1B_Mk_84_8
        GBU_31_8 = Weapons.GBU_31_8
        GBU_31V3B_8 = Weapons.GBU_31V3B_8
        AGM_154C_4 = Weapons.AGM_154C_4
        GBU_38_16 = Weapons.GBU_38_16

    class Pylon2:
        MK_82_28 = Weapons.MK_82_28
        CBU87_10 = Weapons.CBU87_10
        CBU97_10 = Weapons.CBU97_10
        B_1B_Mk_84_8 = Weapons.B_1B_Mk_84_8
        GBU_31_8 = Weapons.GBU_31_8
        GBU_31V3B_8 = Weapons.GBU_31V3B_8
        AGM_154C_4 = Weapons.AGM_154C_4
        GBU_38_16 = Weapons.GBU_38_16

    class Pylon3:
        MK_82_28 = Weapons.MK_82_28
        CBU87_10 = Weapons.CBU87_10
        CBU97_10 = Weapons.CBU97_10
        B_1B_Mk_84_8 = Weapons.B_1B_Mk_84_8
        GBU_31_8 = Weapons.GBU_31_8
        GBU_31V3B_8 = Weapons.GBU_31V3B_8
        AGM_154C_4 = Weapons.AGM_154C_4
        GBU_38_16 = Weapons.GBU_38_16

    pylons = {1, 2, 3}

    tasks = ["Ground Attack", "Runway Attack", "Pinpoint Strike""CAS"]
    task_default = "Ground Attack"


class S_3B(PlaneType):
    id = "S-3B"
    group_size_max = 1
    fuel_max = 5500
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Tanker"

    class Pylon1:
        _3_Mk_82 = Weapons._3_Mk_82
        _3_Mk_20_Rockeye = Weapons._3_Mk_20_Rockeye
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_20 = Weapons.Mk_20
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        AGM_84A = Weapons.AGM_84A
        AGM_84E = Weapons.AGM_84E
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        LAU_61_3___57_2_75__rockets_MK151__HE_ = Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_
        Fuel_tank_S_3 = Weapons.Fuel_tank_S_3

    class Pylon2:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_20 = Weapons.Mk_20

    class Pylon3:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_20 = Weapons.Mk_20

    class Pylon4:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_20 = Weapons.Mk_20

    class Pylon5:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_20 = Weapons.Mk_20

    class Pylon6:
        _3_Mk_82 = Weapons._3_Mk_82
        _3_Mk_20_Rockeye = Weapons._3_Mk_20_Rockeye
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_20 = Weapons.Mk_20
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        AGM_84A = Weapons.AGM_84A
        AGM_84E = Weapons.AGM_84E
        LAU_10___4_ZUNI_MK_71 = Weapons.LAU_10___4_ZUNI_MK_71
        LAU_61_3___57_2_75__rockets_MK151__HE_ = Weapons.LAU_61_3___57_2_75__rockets_MK151__HE_
        Fuel_tank_S_3 = Weapons.Fuel_tank_S_3

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = ["Ground Attack", "Antiship Strike""Pinpoint Strike"]
    task_default = "Antiship Strike"


class S_3B_Tanker(PlaneType):
    id = "S-3B Tanker"
    group_size_max = 1
    fuel_max = 5500
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Tanker"

    pylons = {}

    tasks = ["Refueling"]
    task_default = "Refueling"


class Mirage_2000_5(PlaneType):
    id = "Mirage 2000-5"
    fuel_max = 3160
    chaff = 112
    flare = 16
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"

    class Pylon1:
        R_550_Magic_2 = Weapons.R_550_Magic_2

    class Pylon2:
        Super_530D = Weapons.Super_530D
        MICA_RF = Weapons.MICA_RF
        MICA_IR = Weapons.MICA_IR
        M2000_Fuel_tank = Weapons.M2000_Fuel_tank

    class Pylon3:
        MICA_IR = Weapons.MICA_IR
        MICA_RF = Weapons.MICA_RF

    class Pylon4:
        MICA_IR = Weapons.MICA_IR
        MICA_RF = Weapons.MICA_RF

    class Pylon5:
        M2000_Fuel_tank = Weapons.M2000_Fuel_tank

    class Pylon6:
        MICA_IR = Weapons.MICA_IR
        MICA_RF = Weapons.MICA_RF

    class Pylon7:
        MICA_IR = Weapons.MICA_IR
        MICA_RF = Weapons.MICA_RF

    class Pylon8:
        Super_530D = Weapons.Super_530D
        MICA_RF = Weapons.MICA_RF
        MICA_IR = Weapons.MICA_IR
        M2000_Fuel_tank = Weapons.M2000_Fuel_tank

    class Pylon9:
        R_550_Magic_2 = Weapons.R_550_Magic_2

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "AFAC""Reconnaissance"]
    task_default = "CAP"


class F_15C(PlaneType):
    id = "F-15C"
    fuel_max = 6103
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        Smokewinder___red_smk = Weapons.Smokewinder___red_smk
        Smokewinder___green = Weapons.Smokewinder___green
        Smokewinder___blue_smk = Weapons.Smokewinder___blue_smk
        Smokewinder___white = Weapons.Smokewinder___white
        Smokewinder___yellow = Weapons.Smokewinder___yellow
        Smokewinder___orange = Weapons.Smokewinder___orange
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        Fuel_tank_610_gal = Weapons.Fuel_tank_610_gal

    class Pylon3:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P

    class Pylon4:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M

    class Pylon5:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M

    class Pylon6:
        Fuel_tank_610_gal = Weapons.Fuel_tank_610_gal

    class Pylon7:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M

    class Pylon8:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_7M = Weapons.AIM_7M

    class Pylon9:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P

    class Pylon10:
        Fuel_tank_610_gal = Weapons.Fuel_tank_610_gal

    class Pylon11:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        Smokewinder___red_smk = Weapons.Smokewinder___red_smk
        Smokewinder___green = Weapons.Smokewinder___green
        Smokewinder___blue_smk = Weapons.Smokewinder___blue_smk
        Smokewinder___white = Weapons.Smokewinder___white
        Smokewinder___yellow = Weapons.Smokewinder___yellow
        Smokewinder___orange = Weapons.Smokewinder___orange
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = ["CAP", "Escort", "Fighter Sweep""Intercept"]
    task_default = "CAP"


class F_15E(PlaneType):
    id = "F-15E"
    fuel_max = 10246
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        Fuel_tank_610_gal = Weapons.Fuel_tank_610_gal
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65E = Weapons.LAU_117_AGM_65E
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        AGM_154C = Weapons.AGM_154C
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B

    class Pylon3:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M

    class Pylon4:
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_12 = Weapons.GBU_12
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105

    class Pylon5:
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_12 = Weapons.GBU_12
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105

    class Pylon6:
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_12 = Weapons.GBU_12
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105

    class Pylon7:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B

    class Pylon8:
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_12 = Weapons.GBU_12
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105

    class Pylon9:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B

    class Pylon10:
        Fuel_tank_610_gal = Weapons.Fuel_tank_610_gal
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        Mk_84 = Weapons.Mk_84

    class Pylon11:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B

    class Pylon12:
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_12 = Weapons.GBU_12
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105

    class Pylon13:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B

    class Pylon14:
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_12 = Weapons.GBU_12
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105

    class Pylon15:
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_12 = Weapons.GBU_12
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105

    class Pylon16:
        Mk_82 = Weapons.Mk_82
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_12 = Weapons.GBU_12
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105

    class Pylon17:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M

    class Pylon18:
        Fuel_tank_610_gal = Weapons.Fuel_tank_610_gal
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        GBU_27 = Weapons.GBU_27
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        GBU_38 = Weapons.GBU_38
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65E = Weapons.LAU_117_AGM_65E
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        AGM_154C = Weapons.AGM_154C
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G

    class Pylon19:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Pinpoint Strike", "CAS", "Ground Attack", "Runway Attack", "AFAC""Reconnaissance"]
    task_default = "Ground Attack"


class MiG_29K(PlaneType):
    id = "MiG-29K"
    fuel_max = 4500
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon3:
        R_73 = Weapons.R_73
        L005_Sorbtsiya_ECM_pod__left_ = Weapons.L005_Sorbtsiya_ECM_pod__left_

    pylons = {3}

    tasks = ["SEAD", "Antiship Strike", "CAS", "CAP", "Escort", "Fighter Sweep", "Ground Attack", "Intercept", "AFAC", "Pinpoint Strike""Runway Attack"]
    task_default = "CAP"


class Tu_142(PlaneType):
    id = "Tu-142"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 87000
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        Kh_35_6 = Weapons.Kh_35_6

    pylons = {1}

    tasks = ["Antiship Strike""Reconnaissance"]
    task_default = "Antiship Strike"


class C_130(PlaneType):
    id = "C-130"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 20830
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2

    pylons = {}

    tasks = ["Transport"]
    task_default = "Transport"


class An_26B(PlaneType):
    id = "An-26B"
    group_size_max = 1
    fuel_max = 5500
    chaff = 384
    flare = 384
    charge_total = 768
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = ["Transport"]
    task_default = "Transport"


class An_30M(PlaneType):
    id = "An-30M"
    group_size_max = 1
    fuel_max = 8300
    chaff = 192
    flare = 192
    charge_total = 384
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = ["Transport""Reconnaissance"]
    task_default = "Transport"


class C_17A(PlaneType):
    id = "C-17A"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 132405
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2

    pylons = {}

    tasks = ["Transport"]
    task_default = "Transport"


class A_50(PlaneType):
    id = "A-50"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 70000
    chaff = 192
    flare = 192
    charge_total = 384
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "AWACS"

    pylons = {}

    tasks = ["AWACS"]
    task_default = "AWACS"


class E_3A(PlaneType):
    id = "E-3A"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 65000
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "AWACS"

    pylons = {}

    tasks = ["AWACS"]
    task_default = "AWACS"


class IL_78M(PlaneType):
    id = "IL-78M"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 90000
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Tanker"

    pylons = {}

    tasks = ["Refueling"]
    task_default = "Refueling"


class E_2C(PlaneType):
    id = "E-2C"
    group_size_max = 1
    fuel_max = 5624
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "AWACS"

    pylons = {}

    tasks = ["AWACS"]
    task_default = "AWACS"


class IL_76MD(PlaneType):
    id = "IL-76MD"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 80000
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    pylons = {}

    tasks = ["Transport"]
    task_default = "Transport"


class F_16C_bl_50(PlaneType):
    id = "F-16C bl.50"
    fuel_max = 3104
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P

    class Pylon3:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_88_AGM_65K_3 = Weapons.LAU_88_AGM_65K_3
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65H_2_L = Weapons.LAU_88_AGM_65H_2_L
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_88_AGM_65D_2 = Weapons.LAU_88_AGM_65D_2
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        _2xGBU_12 = Weapons._2xGBU_12
        GBU_27 = Weapons.GBU_27
        AGM_154C = Weapons.AGM_154C
        AGM_88C_ = Weapons.AGM_88C_

    class Pylon4:
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        Fuel_tank_370_gal = Weapons.Fuel_tank_370_gal
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        GBU_27 = Weapons.GBU_27

    class Pylon5:
        Lantirn_F_16 = Weapons.Lantirn_F_16
        AN_AAQ_28_LITENING = Weapons.AN_AAQ_28_LITENING

    class Pylon6:
        ALQ_131 = Weapons.ALQ_131
        Fuel_tank_300_gal = Weapons.Fuel_tank_300_gal

    class Pylon7:
        Fuel_tank_370_gal = Weapons.Fuel_tank_370_gal
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        GBU_27 = Weapons.GBU_27

    class Pylon8:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        LAU_88_AGM_65K_3 = Weapons.LAU_88_AGM_65K_3
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65H_2_L = Weapons.LAU_88_AGM_65H_2_L
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_88_AGM_65D_2 = Weapons.LAU_88_AGM_65D_2
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        _2xGBU_12_ = Weapons._2xGBU_12_
        GBU_27 = Weapons.GBU_27
        AGM_154C = Weapons.AGM_154C
        AGM_88C_ = Weapons.AGM_88C_

    class Pylon9:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P

    class Pylon10:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Pinpoint Strike", "CAS", "Ground Attack", "Runway Attack", "AFAC", "Reconnaissance""Antiship Strike"]
    task_default = "CAP"


class F_16C_bl_52d(PlaneType):
    id = "F-16C bl.52d"
    fuel_max = 3104
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P

    class Pylon3:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65H_2_L = Weapons.LAU_88_AGM_65H_2_L
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_88_AGM_65D_2 = Weapons.LAU_88_AGM_65D_2
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        _2xGBU_12 = Weapons._2xGBU_12
        GBU_27 = Weapons.GBU_27
        AGM_154C = Weapons.AGM_154C
        AGM_88C_ = Weapons.AGM_88C_

    class Pylon4:
        Fuel_tank_370_gal = Weapons.Fuel_tank_370_gal
        AGM_154C = Weapons.AGM_154C
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        GBU_27 = Weapons.GBU_27

    class Pylon5:
        Lantirn_F_16 = Weapons.Lantirn_F_16
        AN_AAQ_28_LITENING = Weapons.AN_AAQ_28_LITENING

    class Pylon6:
        ALQ_131 = Weapons.ALQ_131
        ALQ_184 = Weapons.ALQ_184
        Fuel_tank_300_gal = Weapons.Fuel_tank_300_gal

    class Pylon7:
        Fuel_tank_370_gal = Weapons.Fuel_tank_370_gal
        AGM_154C = Weapons.AGM_154C
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        GBU_27 = Weapons.GBU_27

    class Pylon8:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65H_2_R = Weapons.LAU_88_AGM_65H_2_R
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_88_AGM_65D_2_ = Weapons.LAU_88_AGM_65D_2_
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        GBU_31_V_3_B = Weapons.GBU_31_V_3_B
        CBU_87 = Weapons.CBU_87
        CBU_97 = Weapons.CBU_97
        CBU_103 = Weapons.CBU_103
        CBU_105 = Weapons.CBU_105
        _2xGBU_12_ = Weapons._2xGBU_12_
        GBU_27 = Weapons.GBU_27
        AGM_154C = Weapons.AGM_154C
        AGM_88C_ = Weapons.AGM_88C_

    class Pylon9:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P

    class Pylon10:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Pinpoint Strike", "CAS", "Ground Attack", "Runway Attack", "SEAD", "AFAC", "Reconnaissance""Antiship Strike"]
    task_default = "CAP"


class F_16A(PlaneType):
    id = "F-16A"
    fuel_max = 3104
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = Weapons.AIM_120B
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        AIM_120B = Weapons.AIM_120B
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P

    class Pylon3:
        AIM_120B = Weapons.AIM_120B
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        Mk_20 = Weapons.Mk_20
        _2_Mk_20_Rockeye = Weapons._2_Mk_20_Rockeye
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65H_2_L = Weapons.LAU_88_AGM_65H_2_L
        LAU_88_AGM_65D_2 = Weapons.LAU_88_AGM_65D_2
        AIM_7M = Weapons.AIM_7M
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        AGM_119B_Penguin = Weapons.AGM_119B_Penguin

    class Pylon4:
        Fuel_tank_370_gal = Weapons.Fuel_tank_370_gal
        Mk_20 = Weapons.Mk_20
        _3_Mk_20_Rockeye = Weapons._3_Mk_20_Rockeye
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D

    class Pylon6:
        ALQ_131 = Weapons.ALQ_131
        ALQ_184 = Weapons.ALQ_184
        Fuel_tank_300_gal = Weapons.Fuel_tank_300_gal

    class Pylon7:
        Fuel_tank_370_gal = Weapons.Fuel_tank_370_gal
        Mk_20 = Weapons.Mk_20
        _3_Mk_20_Rockeye = Weapons._3_Mk_20_Rockeye
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D

    class Pylon8:
        AIM_120B = Weapons.AIM_120B
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        Mk_20 = Weapons.Mk_20
        _2_Mk_20_Rockeye = Weapons._2_Mk_20_Rockeye
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65H_2_R = Weapons.LAU_88_AGM_65H_2_R
        LAU_88_AGM_65D_2_ = Weapons.LAU_88_AGM_65D_2_
        AIM_7M = Weapons.AIM_7M
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        AGM_119B_Penguin = Weapons.AGM_119B_Penguin

    class Pylon9:
        AIM_120B = Weapons.AIM_120B
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P

    class Pylon10:
        AIM_120B = Weapons.AIM_120B
        AIM_9M = Weapons.AIM_9M
        AIM_9P = Weapons.AIM_9P
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 6, 7, 8, 9, 10}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Pinpoint Strike", "CAS", "Ground Attack", "Runway Attack", "SEAD", "AFAC", "Reconnaissance""Antiship Strike"]
    task_default = "CAP"


class F_16A_MLU(PlaneType):
    id = "F-16A MLU"
    fuel_max = 3104
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"

    class Pylon1:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    class Pylon2:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M

    class Pylon3:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        AGM_119B_Penguin = Weapons.AGM_119B_Penguin
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65H_2_L = Weapons.LAU_88_AGM_65H_2_L
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_88_AGM_65D_2 = Weapons.LAU_88_AGM_65D_2
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        _2xGBU_12 = Weapons._2xGBU_12
        AGM_154C = Weapons.AGM_154C

    class Pylon4:
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        Fuel_tank_370_gal = Weapons.Fuel_tank_370_gal
        AGM_119B_Penguin = Weapons.AGM_119B_Penguin
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31

    class Pylon5:
        Lantirn_F_16 = Weapons.Lantirn_F_16
        AN_AAQ_28_LITENING = Weapons.AN_AAQ_28_LITENING

    class Pylon6:
        ALQ_131 = Weapons.ALQ_131
        Fuel_tank_300_gal = Weapons.Fuel_tank_300_gal

    class Pylon7:
        Fuel_tank_370_gal = Weapons.Fuel_tank_370_gal
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        AGM_119B_Penguin = Weapons.AGM_119B_Penguin
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31

    class Pylon8:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        GBU_10 = Weapons.GBU_10
        GBU_12 = Weapons.GBU_12
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        AGM_119B_Penguin = Weapons.AGM_119B_Penguin
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_88_AGM_65H_2_R = Weapons.LAU_88_AGM_65H_2_R
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        LAU_88_AGM_65D_2_ = Weapons.LAU_88_AGM_65D_2_
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        Mk_82AIR = Weapons.Mk_82AIR
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        GBU_38 = Weapons.GBU_38
        GBU_31 = Weapons.GBU_31
        _2xGBU_12_ = Weapons._2xGBU_12_
        AGM_154C = Weapons.AGM_154C

    class Pylon9:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M

    class Pylon10:
        AIM_120B = Weapons.AIM_120B
        AIM_120C = Weapons.AIM_120C
        AIM_9M = Weapons.AIM_9M
        AN_ASQ_T50_TCTS_Pod = Weapons.AN_ASQ_T50_TCTS_Pod

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Intercept", "Pinpoint Strike", "CAS", "Ground Attack", "Runway Attack", "AFAC", "Reconnaissance""Antiship Strike"]
    task_default = "CAP"


class RQ_1A_Predator(PlaneType):
    id = "RQ-1A Predator"
    group_size_max = 1
    fuel_max = 200

    class Pylon1:
        AGM_114K = Weapons.AGM_114K

    class Pylon2:
        AGM_114K = Weapons.AGM_114K

    pylons = {1, 2}

    tasks = ["Ground Attack", "AFAC""Reconnaissance"]
    task_default = "Reconnaissance"


class Yak_40(PlaneType):
    id = "Yak-40"
    group_size_max = 1
    fuel_max = 3080

    pylons = {}

    tasks = ["Transport"]
    task_default = "Transport"


class A_10C(PlaneType):
    id = "A-10C"
    fuel_max = 5029
    chaff = 240
    flare = 120
    charge_total = 480
    chaff_charge_size = 1
    flare_charge_size = 2

    class Pylon1:
        LAU_105___2_AIM_9M = Weapons.LAU_105___2_AIM_9M
        Mk_82 = Weapons.Mk_82
        LAU_105_1_AIM_9M_L = Weapons.LAU_105_1_AIM_9M_L
        LAU_105 = Weapons.LAU_105
        LAU_105_2_CATM_9M = Weapons.LAU_105_2_CATM_9M
        LAU_105_1_CATM_9M_L = Weapons.LAU_105_1_CATM_9M_L
        ALQ_131 = Weapons.ALQ_131
        Smokewinder___red_smk = Weapons.Smokewinder___red_smk
        Smokewinder___green = Weapons.Smokewinder___green
        Smokewinder___blue_smk = Weapons.Smokewinder___blue_smk
        Smokewinder___white = Weapons.Smokewinder___white
        Smokewinder___yellow = Weapons.Smokewinder___yellow
        Smokewinder___orange = Weapons.Smokewinder___orange
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50LGB = Weapons.BDU_50LGB
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        ALQ_184 = Weapons.ALQ_184
        CBU_97 = Weapons.CBU_97
        LAU_105_AIS_ASQ_T50_L = Weapons.LAU_105_AIS_ASQ_T50_L

    class Pylon2:
        Mk_82 = Weapons.Mk_82
        AN_AAQ_28_LITENING = Weapons.AN_AAQ_28_LITENING
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        CBU_97 = Weapons.CBU_97
        BDU_50LGB = Weapons.BDU_50LGB
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2

    class Pylon3:
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        LAU_88_AGM_65D_ONE = Weapons.LAU_88_AGM_65D_ONE
        LAU_88_AGM_65D_2 = Weapons.LAU_88_AGM_65D_2
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        GBU_10 = Weapons.GBU_10
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        LAU_68_3___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_MK1__Practice_
        LAU_68_3___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68_3___7_2_75__rockets_MK5__HE_
        LAU_68_3___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_MK61__Practice_
        LAU_68_3___7_2_75__rockets_M151__HE_ = Weapons.LAU_68_3___7_2_75__rockets_M151__HE_
        LAU_68_3___7_2_75__rockets_M156__WP_ = Weapons.LAU_68_3___7_2_75__rockets_M156__WP_
        LAU_68_3___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_WTU1B__Practice_
        LAU_68_3___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68_3___7_2_75__rockets_M274__Practice_smoke_
        LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = Weapons.LAU_131x3_HYDRA_70_MK1
        LAU_131x3_HYDRA_70_MK5 = Weapons.LAU_131x3_HYDRA_70_MK5
        LAU_131x3_HYDRA_70_MK61 = Weapons.LAU_131x3_HYDRA_70_MK61
        LAU_131x3_HYDRA_70_M151 = Weapons.LAU_131x3_HYDRA_70_M151
        LAU_131x3_HYDRA_70_M156 = Weapons.LAU_131x3_HYDRA_70_M156
        LAU_131x3_HYDRA_70_WTU1B = Weapons.LAU_131x3_HYDRA_70_WTU1B
        LAU_131x3_HYDRA_70_M257 = Weapons.LAU_131x3_HYDRA_70_M257
        LAU_131x3_HYDRA_70_M274 = Weapons.LAU_131x3_HYDRA_70_M274
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = Weapons.MXU_648_TP
        BRU_42_LS = Weapons.BRU_42_LS
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_88_AGM_65H = Weapons.LAU_88_AGM_65H
        LAU_88_AGM_65H_2_L = Weapons.LAU_88_AGM_65H_2_L
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_TGM_65D = Weapons.LAU_117_TGM_65D
        LAU_117_TGM_65G = Weapons.LAU_117_TGM_65G
        LAU_117_TGM_65H = Weapons.LAU_117_TGM_65H
        LAU_117_CATM_65K = Weapons.LAU_117_CATM_65K
        BRU_42_3_GBU_12 = Weapons.BRU_42_3_GBU_12
        CBU_97 = Weapons.CBU_97
        CBU_105 = Weapons.CBU_105
        CBU_103 = Weapons.CBU_103
        BDU_50LGB = Weapons.BDU_50LGB
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        _3_SUU_25___8_LUU_2 = Weapons._3_SUU_25___8_LUU_2

    class Pylon4:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Fuel_Tank_FT600 = Weapons.Fuel_Tank_FT600
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        CBU_87 = Weapons.CBU_87
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        LAU_68_3___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_MK1__Practice_
        LAU_68_3___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68_3___7_2_75__rockets_MK5__HE_
        LAU_68_3___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_MK61__Practice_
        LAU_68_3___7_2_75__rockets_M151__HE_ = Weapons.LAU_68_3___7_2_75__rockets_M151__HE_
        LAU_68_3___7_2_75__rockets_M156__WP_ = Weapons.LAU_68_3___7_2_75__rockets_M156__WP_
        LAU_68_3___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_WTU1B__Practice_
        LAU_68_3___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68_3___7_2_75__rockets_M274__Practice_smoke_
        LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = Weapons.LAU_131x3_HYDRA_70_MK1
        LAU_131x3_HYDRA_70_MK5 = Weapons.LAU_131x3_HYDRA_70_MK5
        LAU_131x3_HYDRA_70_MK61 = Weapons.LAU_131x3_HYDRA_70_MK61
        LAU_131x3_HYDRA_70_M151 = Weapons.LAU_131x3_HYDRA_70_M151
        LAU_131x3_HYDRA_70_M156 = Weapons.LAU_131x3_HYDRA_70_M156
        LAU_131x3_HYDRA_70_WTU1B = Weapons.LAU_131x3_HYDRA_70_WTU1B
        LAU_131x3_HYDRA_70_M257 = Weapons.LAU_131x3_HYDRA_70_M257
        LAU_131x3_HYDRA_70_M274 = Weapons.LAU_131x3_HYDRA_70_M274
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = Weapons.MXU_648_TP
        BRU_42_LS = Weapons.BRU_42_LS
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        BRU_42_3_GBU_12 = Weapons.BRU_42_3_GBU_12
        CBU_97 = Weapons.CBU_97
        CBU_105 = Weapons.CBU_105
        CBU_103 = Weapons.CBU_103
        BDU_50LGB = Weapons.BDU_50LGB
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        _3_Mk_82 = Weapons._3_Mk_82

    class Pylon5:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        CBU_87 = Weapons.CBU_87
        MXU_648_TP = Weapons.MXU_648_TP
        BRU_42_LS = Weapons.BRU_42_LS
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        CBU_97 = Weapons.CBU_97
        CBU_105 = Weapons.CBU_105
        CBU_103 = Weapons.CBU_103
        BDU_50LGB = Weapons.BDU_50LGB
        _3_Mk_82 = Weapons._3_Mk_82
        _3_Mk_82AIR = Weapons._3_Mk_82AIR

    class Pylon6:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        CBU_87 = Weapons.CBU_87
        MXU_648_TP = Weapons.MXU_648_TP
        BRU_42_LS = Weapons.BRU_42_LS
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        CBU_97 = Weapons.CBU_97
        BDU_50LGB = Weapons.BDU_50LGB
        Fuel_Tank_FT600 = Weapons.Fuel_Tank_FT600

    class Pylon7:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        CBU_87 = Weapons.CBU_87
        MXU_648_TP = Weapons.MXU_648_TP
        BRU_42_LS = Weapons.BRU_42_LS
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        CBU_97 = Weapons.CBU_97
        CBU_105 = Weapons.CBU_105
        CBU_103 = Weapons.CBU_103
        BDU_50LGB = Weapons.BDU_50LGB
        _3_Mk_82 = Weapons._3_Mk_82
        _3_Mk_82AIR = Weapons._3_Mk_82AIR

    class Pylon8:
        Mk_82 = Weapons.Mk_82
        Mk_84 = Weapons.Mk_84
        Fuel_Tank_FT600 = Weapons.Fuel_Tank_FT600
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        CBU_87 = Weapons.CBU_87
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        LAU_68_3___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_MK1__Practice_
        LAU_68_3___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68_3___7_2_75__rockets_MK5__HE_
        LAU_68_3___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_MK61__Practice_
        LAU_68_3___7_2_75__rockets_M151__HE_ = Weapons.LAU_68_3___7_2_75__rockets_M151__HE_
        LAU_68_3___7_2_75__rockets_M156__WP_ = Weapons.LAU_68_3___7_2_75__rockets_M156__WP_
        LAU_68_3___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_WTU1B__Practice_
        LAU_68_3___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68_3___7_2_75__rockets_M274__Practice_smoke_
        LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = Weapons.LAU_131x3_HYDRA_70_MK1
        LAU_131x3_HYDRA_70_MK5 = Weapons.LAU_131x3_HYDRA_70_MK5
        LAU_131x3_HYDRA_70_MK61 = Weapons.LAU_131x3_HYDRA_70_MK61
        LAU_131x3_HYDRA_70_M151 = Weapons.LAU_131x3_HYDRA_70_M151
        LAU_131x3_HYDRA_70_M156 = Weapons.LAU_131x3_HYDRA_70_M156
        LAU_131x3_HYDRA_70_WTU1B = Weapons.LAU_131x3_HYDRA_70_WTU1B
        LAU_131x3_HYDRA_70_M257 = Weapons.LAU_131x3_HYDRA_70_M257
        LAU_131x3_HYDRA_70_M274 = Weapons.LAU_131x3_HYDRA_70_M274
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = Weapons.MXU_648_TP
        BRU_42_LS = Weapons.BRU_42_LS
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        BRU_42_3_GBU_12 = Weapons.BRU_42_3_GBU_12
        CBU_97 = Weapons.CBU_97
        CBU_105 = Weapons.CBU_105
        CBU_103 = Weapons.CBU_103
        BDU_50LGB = Weapons.BDU_50LGB
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        _3_Mk_82 = Weapons._3_Mk_82

    class Pylon9:
        LAU_117_AGM_65K = Weapons.LAU_117_AGM_65K
        LAU_88_AGM_65D_ONE = Weapons.LAU_88_AGM_65D_ONE
        LAU_88_AGM_65D_2_ = Weapons.LAU_88_AGM_65D_2_
        LAU_88_AGM_65D_3 = Weapons.LAU_88_AGM_65D_3
        LAU_117_AGM_65D = Weapons.LAU_117_AGM_65D
        Mk_84 = Weapons.Mk_84
        Mk_82 = Weapons.Mk_82
        _3_Mk_82 = Weapons._3_Mk_82
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        GBU_10 = Weapons.GBU_10
        GBU_31 = Weapons.GBU_31
        GBU_38 = Weapons.GBU_38
        CBU_87 = Weapons.CBU_87
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        LAU_68_3___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_MK1__Practice_
        LAU_68_3___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68_3___7_2_75__rockets_MK5__HE_
        LAU_68_3___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_MK61__Practice_
        LAU_68_3___7_2_75__rockets_M151__HE_ = Weapons.LAU_68_3___7_2_75__rockets_M151__HE_
        LAU_68_3___7_2_75__rockets_M156__WP_ = Weapons.LAU_68_3___7_2_75__rockets_M156__WP_
        LAU_68_3___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68_3___7_2_75__rockets_WTU1B__Practice_
        LAU_68_3___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68_3___7_2_75__rockets_M274__Practice_smoke_
        LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68_3___7_2_75__rockets_M257__Parachute_illumination_
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = Weapons.LAU_131x3_HYDRA_70_MK1
        LAU_131x3_HYDRA_70_MK5 = Weapons.LAU_131x3_HYDRA_70_MK5
        LAU_131x3_HYDRA_70_MK61 = Weapons.LAU_131x3_HYDRA_70_MK61
        LAU_131x3_HYDRA_70_M151 = Weapons.LAU_131x3_HYDRA_70_M151
        LAU_131x3_HYDRA_70_M156 = Weapons.LAU_131x3_HYDRA_70_M156
        LAU_131x3_HYDRA_70_WTU1B = Weapons.LAU_131x3_HYDRA_70_WTU1B
        LAU_131x3_HYDRA_70_M257 = Weapons.LAU_131x3_HYDRA_70_M257
        LAU_131x3_HYDRA_70_M274 = Weapons.LAU_131x3_HYDRA_70_M274
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = Weapons.MXU_648_TP
        BRU_42_LS = Weapons.BRU_42_LS
        BRU_42_3_BDU_33 = Weapons.BRU_42_3_BDU_33
        LAU_117_AGM_65H = Weapons.LAU_117_AGM_65H
        LAU_117_AGM_65G = Weapons.LAU_117_AGM_65G
        LAU_88_AGM_65H = Weapons.LAU_88_AGM_65H
        LAU_88_AGM_65H_2_R = Weapons.LAU_88_AGM_65H_2_R
        LAU_88_AGM_65H_3 = Weapons.LAU_88_AGM_65H_3
        LAU_117_TGM_65D = Weapons.LAU_117_TGM_65D
        LAU_117_TGM_65G = Weapons.LAU_117_TGM_65G
        LAU_117_TGM_65H = Weapons.LAU_117_TGM_65H
        LAU_117_CATM_65K = Weapons.LAU_117_CATM_65K
        BRU_42_3_GBU_12 = Weapons.BRU_42_3_GBU_12
        CBU_97 = Weapons.CBU_97
        CBU_105 = Weapons.CBU_105
        CBU_103 = Weapons.CBU_103
        BDU_50LGB = Weapons.BDU_50LGB
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        _3_Mk_82AIR = Weapons._3_Mk_82AIR
        _3_SUU_25___8_LUU_2 = Weapons._3_SUU_25___8_LUU_2

    class Pylon10:
        Mk_82 = Weapons.Mk_82
        SUU_25___8_LUU_2 = Weapons.SUU_25___8_LUU_2
        AN_AAQ_28_LITENING = Weapons.AN_AAQ_28_LITENING
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        CBU_87 = Weapons.CBU_87
        LAU_68___7_2_75__rockets_MK1__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK1__Practice_
        LAU_68___7_2_75__rockets_MK5__HE_ = Weapons.LAU_68___7_2_75__rockets_MK5__HE_
        LAU_68___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_68___7_2_75__rockets_MK61__Practice_
        LAU_68___7_2_75__rockets_M151__HE_ = Weapons.LAU_68___7_2_75__rockets_M151__HE_
        LAU_68___7_2_75__rockets_M156_WP_ = Weapons.LAU_68___7_2_75__rockets_M156_WP_
        LAU_68___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_68___7_2_75__rockets_WTU1B__Practice_
        LAU_68___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_68___7_2_75__rockets_M257__Parachute_illumination_
        LAU_68___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_68___7_2_75__rockets_M274__Practice_smoke_
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131___7_2_75__rockets_Mk1__Practice_ = Weapons.LAU_131___7_2_75__rockets_Mk1__Practice_
        LAU_131___7_2_75__rockets_MK5__HE_ = Weapons.LAU_131___7_2_75__rockets_MK5__HE_
        LAU_131___7_2_75__rockets_MK61__Practice_ = Weapons.LAU_131___7_2_75__rockets_MK61__Practice_
        LAU_131___7_2_75__rockets_M151__HE_ = Weapons.LAU_131___7_2_75__rockets_M151__HE_
        LAU_131___7_2_75__rockets_M156__WP_ = Weapons.LAU_131___7_2_75__rockets_M156__WP_
        LAU_131___7_2_75__rockets_WTU1B__Practice_ = Weapons.LAU_131___7_2_75__rockets_WTU1B__Practice_
        LAU_131___7_2_75__rockets_M257__Parachute_illumination_ = Weapons.LAU_131___7_2_75__rockets_M257__Parachute_illumination_
        LAU_131___7_2_75__rockets_M274__Practice_smoke_ = Weapons.LAU_131___7_2_75__rockets_M274__Practice_smoke_
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        CBU_97 = Weapons.CBU_97
        BDU_50LGB = Weapons.BDU_50LGB

    class Pylon11:
        LAU_105___2_AIM_9M = Weapons.LAU_105___2_AIM_9M
        Smokewinder___red_smk = Weapons.Smokewinder___red_smk
        Smokewinder___green = Weapons.Smokewinder___green
        Smokewinder___blue_smk = Weapons.Smokewinder___blue_smk
        Smokewinder___white = Weapons.Smokewinder___white
        Smokewinder___yellow = Weapons.Smokewinder___yellow
        Smokewinder___orange = Weapons.Smokewinder___orange
        ALQ_131 = Weapons.ALQ_131
        GBU_12 = Weapons.GBU_12
        BDU_50LD = Weapons.BDU_50LD
        BDU_50HD = Weapons.BDU_50HD
        Mk_82AIR = Weapons.Mk_82AIR
        Mk_82 = Weapons.Mk_82
        CBU_87 = Weapons.CBU_87
        BDU_50LGB = Weapons.BDU_50LGB
        CBU_97 = Weapons.CBU_97
        LAU_105_1_AIM_9M_R = Weapons.LAU_105_1_AIM_9M_R
        LAU_105 = Weapons.LAU_105
        ALQ_184 = Weapons.ALQ_184
        LAU_105_2_CATM_9M = Weapons.LAU_105_2_CATM_9M
        LAU_105_1_CATM_9M_R = Weapons.LAU_105_1_CATM_9M_R
        LAU_105_AIS_ASQ_T50_R = Weapons.LAU_105_AIS_ASQ_T50_R

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = ["Ground Attack", "CAS", "AFAC", "Runway Attack""Antiship Strike"]
    task_default = "CAS"


class KC_135(PlaneType):
    id = "KC-135"
    group_size_max = 1
    large_parking_slot = True
    fuel_max = 90700.0
    category = "Tanker"

    pylons = {}

    tasks = ["Refueling"]
    task_default = "Refueling"


class P_51D(PlaneType):
    id = "P-51D"
    fuel_max = 732

    class Pylon1:
        HVAR = Weapons.HVAR
        HVAR_Smoke_Generator = Weapons.HVAR_Smoke_Generator

    class Pylon2:
        HVAR = Weapons.HVAR

    class Pylon3:
        HVAR = Weapons.HVAR

    class Pylon4:
        AN_M64 = Weapons.AN_M64
        Drop_Tank_75Gal = Weapons.Drop_Tank_75Gal
        HVAR = Weapons.HVAR

    class Pylon5:
        HVAR = Weapons.HVAR

    class Pylon6:
        HVAR = Weapons.HVAR

    class Pylon7:
        AN_M64 = Weapons.AN_M64
        Drop_Tank_75Gal = Weapons.Drop_Tank_75Gal
        HVAR = Weapons.HVAR

    class Pylon8:
        HVAR = Weapons.HVAR

    class Pylon9:
        HVAR = Weapons.HVAR

    class Pylon10:
        HVAR = Weapons.HVAR
        HVAR_Smoke_Generator = Weapons.HVAR_Smoke_Generator

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = ["CAP", "Escort", "Fighter Sweep", "Ground Attack", "CAS", "AFAC", "Runway Attack""Antiship Strike"]
    task_default = "CAS"


