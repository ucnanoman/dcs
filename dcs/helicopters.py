

class HelicopterType:
    id = ""
    group_size_max = 4
    large_parking_slot = False
    helicopter = True
    fuel_max = 0
    ammo_type = None
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Air"

    pylons = {}

    tasks = ['Nothing']


class Ka_50(HelicopterType):
    id = "Ka-50"
    fuel_max = 1450
    chaff = 0
    flare = 128


class AH_64A(HelicopterType):
    id = "AH-64A"
    fuel_max = 1157
    chaff = 30
    flare = 30
