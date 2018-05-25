from .terrain import Terrain, Airport, Runway, ParkingSlot, MapView, Graph
from .. import mapping
from datetime import datetime, timezone
import random


class Abu_Musa_Island_Airport(Airport):
    id = 1
    name = "Abu Musa Island Airport"
    position = mapping.Point(-31505.274308, -121335.307759)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Abu_Musa_Island_Airport, self).__init__()

        self.runways.append(Runway(80))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-31265.763702393, -121984.875), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-31235.46484375, -121986.890625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-31243.45123291, -122057.5), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-31250.574249268, -122125.46862793), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-31279.804626465, -122121.92980957), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-31309.128890991, -122118.99987793), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-31295.628936768, -121981.8671875), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-31277.535095215, -122054.63250732), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))


class Bandar_Abbas_Intl(Airport):
    id = 2
    name = "Bandar Abbas Intl"
    position = mapping.Point(115765.878906, 14257.979004)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Bandar_Abbas_Intl, self).__init__()

        self.runways.append(Runway(30))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(117866.4609375, 15125.921875), large=False, heli=True,
                airplanes=True, slot_name='H06', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(117837.9140625, 15109.524414062), large=False, heli=True,
                airplanes=True, slot_name='H05', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(117425.7890625, 14748.6171875), large=False, heli=True,
                airplanes=True, slot_name='F18', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(117804.578125, 15091.114257813), large=False, heli=True,
                airplanes=True, slot_name='H04', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(117522.1875, 14800.170898438), large=False, heli=True,
                airplanes=True, slot_name='F26', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(117360.3828125, 14704.897460938), large=False, heli=True,
                airplanes=True, slot_name='F14', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(117540.203125, 14730.545898437), large=False, heli=True,
                airplanes=True, slot_name='F25', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(117775.2109375, 15075.1875), large=False, heli=True,
                airplanes=True, slot_name='H03', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(117743.1953125, 15057.58203125), large=False, heli=True,
                airplanes=True, slot_name='H02', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(117714.4375, 15041.0546875), large=False, heli=True,
                airplanes=True, slot_name='H01', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(117173.0625, 14596.526367188), large=False, heli=False,
                airplanes=True, slot_name='F06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(117108.421875, 14492.866210938), large=False, heli=True,
                airplanes=True, slot_name='F05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(117458.1796875, 14765.735351562), large=False, heli=True,
                airplanes=True, slot_name='F20', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(117394.0390625, 14731.680664063), large=False, heli=True,
                airplanes=True, slot_name='F16', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(117199.3515625, 14609.822265625), large=False, heli=False,
                airplanes=True, slot_name='F08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(117226.8359375, 14625.44140625), large=False, heli=False,
                airplanes=True, slot_name='F10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(117490.5859375, 14782.98828125), large=False, heli=True,
                airplanes=True, slot_name='F24', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(117252.96875, 14637.84375), large=False, heli=False,
                airplanes=True, slot_name='F12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(114862.4375, 13292.00390625), large=False, heli=True,
                airplanes=True, slot_name='B01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(118610.6875, 15614.309570313), large=False, heli=True,
                airplanes=True, slot_name='H07', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(117259.2421875, 14586.579101563), large=False, heli=False,
                airplanes=True, slot_name='F11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(117510.171875, 14713.8359375), large=False, heli=True,
                airplanes=True, slot_name='F23', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(117478.5859375, 14696.862304687), large=False, heli=True,
                airplanes=True, slot_name='F21', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(117349.328125, 14625.948242188), large=False, heli=True,
                airplanes=True, slot_name='F13', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(116987.875, 14514.458984375), large=False, heli=True,
                airplanes=True, slot_name='F04', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(118995.8125, 15455.526367188), large=False, heli=True,
                airplanes=True, slot_name='H08', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(117022.2109375, 14532.935546875), large=False, heli=True,
                airplanes=True, slot_name='F03', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(117444.71875, 14680.668945312), large=False, heli=True,
                airplanes=True, slot_name='F19', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(117041.2890625, 14476.92578125), large=False, heli=True,
                airplanes=True, slot_name='F02', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(117194.609375, 14550.9453125), large=False, heli=False,
                airplanes=True, slot_name='F07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(117413.171875, 14662.9140625), large=False, heli=True,
                airplanes=True, slot_name='F17', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(114962.6171875, 13344.315429687), large=False, heli=True,
                airplanes=True, slot_name='B02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(117382.3203125, 14645.4296875), large=False, heli=True,
                airplanes=True, slot_name='F15', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(117225.671875, 14569.0859375), large=False, heli=False,
                airplanes=True, slot_name='F09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(115060.4921875, 13396.690429688), large=False, heli=True,
                airplanes=True, slot_name='B03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(117009.34375, 14458.671875), large=False, heli=True,
                airplanes=True, slot_name='F01', length=25.0, width=20.0, height=11.0, shelter=False))


class Bandar_Lengeh(Airport):
    id = 3
    name = "Bandar Lengeh"
    position = mapping.Point(41536.408234, -140987.327942)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Bandar_Lengeh, self).__init__()

        self.runways.append(Runway(80))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(41385.64441061, -140533.0625), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(41388.109597206, -140563.28137207), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(41378.870973349, -140597.828125), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(41378.61730814, -140629.703125), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(41366.503915787, -140661.09368896), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))


class Al_Dhafra_AB(Airport):
    id = 4
    name = "Al Dhafra AB"
    position = mapping.Point(-211027.78125, -173240.007813)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Al_Dhafra_AB, self).__init__()

        self.runways.append(Runway(130))
        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-210753.59375, -174987.828125), large=False, heli=False,
                airplanes=True, slot_name='101', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-210738.890625, -174976.171875), large=False, heli=False,
                airplanes=True, slot_name='102', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-210724.75, -174964.015625), large=False, heli=False,
                airplanes=True, slot_name='103', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-210709.84375, -174953.484375), large=False, heli=False,
                airplanes=True, slot_name='104', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-210696.1875, -174943.125), large=False, heli=False,
                airplanes=True, slot_name='105', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-210682.4375, -174931.9375), large=False, heli=False,
                airplanes=True, slot_name='106', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-210666.671875, -174920.859375), large=False, heli=False,
                airplanes=True, slot_name='107', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-210652.953125, -174908.875), large=False, heli=False,
                airplanes=True, slot_name='108', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-210651.359375, -175023.734375), large=False, heli=True,
                airplanes=True, slot_name='100', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-210601.875, -174985.15625), large=False, heli=True,
                airplanes=True, slot_name='99', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-209540.390625, -173990.90625), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-209558.765625, -173965.96875), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-209577.546875, -173939.96875), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-209600.78125, -173906.734375), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-209906.78125, -173724.078125), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-209936.15625, -173687.703125), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-209963.703125, -173650.125), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-210102.4375, -173366.640625), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-210124.65625, -173385.578125), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-210148.28125, -173403.0625), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-210170.453125, -173422.140625), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-210207.34375, -173375.03125), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-210183.765625, -173357.53125), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-210161.890625, -173337.8125), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-210139, -173319.609375), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-210220.765625, -173310.390625), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-210243.0625, -173281.46875), large=False, heli=False,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-210267.515625, -173249.625), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-210293.96875, -173216.171875), large=False, heli=False,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-210264.84375, -173205.9375), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-210243.90625, -173233.375), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-210219.8125, -173264.03125), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-210197.484375, -173292.78125), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-210277.453125, -173142), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-210301.453125, -173158.78125), large=False, heli=False,
                airplanes=True, slot_name='25', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-210323, -173179.140625), large=False, heli=False,
                airplanes=True, slot_name='26', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-210344.60581236, -173198.93424279), large=False, heli=False,
                airplanes=True, slot_name='27', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-210312.625, -173096.9375), large=False, heli=False,
                airplanes=True, slot_name='28', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-210335.09375, -173115.859375), large=False, heli=False,
                airplanes=True, slot_name='29', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-210357.0625, -173135.28125), large=False, heli=False,
                airplanes=True, slot_name='30', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-210380.96875, -173152.078125), large=False, heli=False,
                airplanes=True, slot_name='31', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-210348.296875, -173051.296875), large=False, heli=False,
                airplanes=True, slot_name='32', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-210370, -173070.921875), large=False, heli=False,
                airplanes=True, slot_name='33', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-210392.36756929, -173090.18393736), large=False, heli=False,
                airplanes=True, slot_name='34', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-210415.84375, -173107.4375), large=False, heli=False,
                airplanes=True, slot_name='35', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-210442.71875, -173061.96875), large=False, heli=False,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-210467.171875, -173029.234375), large=False, heli=False,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-210486.046875, -173005.515625), large=False, heli=False,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-210509.296875, -172972.78125), large=False, heli=False,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-210528.390625, -172948.03125), large=False, heli=False,
                airplanes=True, slot_name='40', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-210546.984375, -172923.875), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-210560.515625, -172904.71875), large=False, heli=False,
                airplanes=True, slot_name='42', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-210579.78125, -172880.015625), large=False, heli=False,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-210597.9375, -172855.609375), large=False, heli=False,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-210613.171875, -172836.453125), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-210632.0625, -172811.421875), large=False, heli=False,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-210650.5625, -172787.328125), large=False, heli=False,
                airplanes=True, slot_name='47', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-210770.578125, -172726.015625), large=False, heli=False,
                airplanes=True, slot_name='48', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-210792.359375, -172698.03125), large=False, heli=False,
                airplanes=True, slot_name='49', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-210814.25, -172669.5625), large=False, heli=False,
                airplanes=True, slot_name='50', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-210836.984375, -172642.109375), large=False, heli=False,
                airplanes=True, slot_name='51', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-210858.03125, -172615.09375), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-210880.546875, -172588.4375), large=False, heli=False,
                airplanes=True, slot_name='53', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-210803.3125, -172778.078125), large=False, heli=False,
                airplanes=True, slot_name='54', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-210826.34375, -172747.421875), large=False, heli=False,
                airplanes=True, slot_name='55', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-210848.046875, -172719.40625), large=False, heli=False,
                airplanes=True, slot_name='56', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-210870.5, -172690.671875), large=False, heli=False,
                airplanes=True, slot_name='57', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-210891.28125, -172662.84375), large=False, heli=False,
                airplanes=True, slot_name='58', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-210913.25, -172635.953125), large=False, heli=False,
                airplanes=True, slot_name='59', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-210903.59375, -172482.828125), large=False, heli=False,
                airplanes=True, slot_name='70', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-210920.609375, -172460.890625), large=False, heli=False,
                airplanes=True, slot_name='71', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-210939.15625, -172437.796875), large=False, heli=False,
                airplanes=True, slot_name='72', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-210956.84375, -172414.8125), large=False, heli=False,
                airplanes=True, slot_name='73', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-210974.921875, -172392.125), large=False, heli=False,
                airplanes=True, slot_name='74', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-210992.703125, -172368.734375), large=False, heli=False,
                airplanes=True, slot_name='75', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-211009.5625, -172347.953125), large=False, heli=False,
                airplanes=True, slot_name='76', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-211027.5, -172324.265625), large=False, heli=False,
                airplanes=True, slot_name='77', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-211044.71875, -172302.1875), large=False, heli=False,
                airplanes=True, slot_name='78', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-211062.25, -172279.78125), large=False, heli=False,
                airplanes=True, slot_name='79', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-210856.234375, -172452.15625), large=False, heli=False,
                airplanes=True, slot_name='60', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-210874.53125, -172428.90625), large=False, heli=False,
                airplanes=True, slot_name='61', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-210892.953125, -172405.671875), large=False, heli=False,
                airplanes=True, slot_name='62', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-210910.890625, -172381.96875), large=False, heli=False,
                airplanes=True, slot_name='63', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-210928.640625, -172359.78125), large=False, heli=False,
                airplanes=True, slot_name='64', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-210946.84375, -172336.5625), large=False, heli=False,
                airplanes=True, slot_name='65', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-210964.53125, -172313.59375), large=False, heli=False,
                airplanes=True, slot_name='66', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-210981.890625, -172291.625), large=False, heli=False,
                airplanes=True, slot_name='67', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-210999.1875, -172269.5), large=False, heli=False,
                airplanes=True, slot_name='68', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-211017.5, -172245.109375), large=False, heli=False,
                airplanes=True, slot_name='69', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-211041.5625, -172455.484375), large=False, heli=False,
                airplanes=True, slot_name='80', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-211053.40625, -172440.515625), large=False, heli=False,
                airplanes=True, slot_name='81', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-211064.765625, -172426.125), large=False, heli=False,
                airplanes=True, slot_name='82', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-211075.828125, -172411.6875), large=False, heli=False,
                airplanes=True, slot_name='83', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-211087.25, -172397.359375), large=False, heli=False,
                airplanes=True, slot_name='84', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-211098.53125, -172383.09375), large=False, heli=False,
                airplanes=True, slot_name='85', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-211108.953125, -172369.859375), large=False, heli=False,
                airplanes=True, slot_name='86', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-211376, -172039.078125), large=False, heli=True,
                airplanes=True, slot_name='90', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-211342.46875, -172082.640625), large=False, heli=True,
                airplanes=True, slot_name='89', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-211308.171875, -172127.265625), large=False, heli=True,
                airplanes=True, slot_name='88', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-211271.171875, -172172.375), large=False, heli=True,
                airplanes=True, slot_name='87', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-211282.578125, -171743.0625), large=False, heli=True,
                airplanes=True, slot_name='91', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-211392.921875, -171600.78125), large=False, heli=True,
                airplanes=True, slot_name='94', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-211441.25, -171645.421875), large=False, heli=True,
                airplanes=True, slot_name='95', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-211346.625, -171766.546875), large=False, heli=True,
                airplanes=True, slot_name='92', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-211381.125, -171828.46875), large=False, heli=True,
                airplanes=True, slot_name='93', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-211491.421875, -171687.265625), large=False, heli=True,
                airplanes=True, slot_name='96', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-211546.625, -171721.40625), large=False, heli=True,
                airplanes=True, slot_name='97', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-212630.109375, -172441.59375), large=False, heli=False,
                airplanes=True, slot_name='185', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-212647.9375, -172417.09375), large=False, heli=False,
                airplanes=True, slot_name='186', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-212667.21875, -172393.0625), large=False, heli=False,
                airplanes=True, slot_name='187', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-212686.078125, -172369), large=False, heli=False,
                airplanes=True, slot_name='188', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-212703.734375, -172344.890625), large=False, heli=False,
                airplanes=True, slot_name='189', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-213346.8125, -171661.484375), large=False, heli=True,
                airplanes=True, slot_name='190', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-213959.375, -171335.515625), large=False, heli=False,
                airplanes=True, slot_name='197', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-213944, -171323.875), large=False, heli=False,
                airplanes=True, slot_name='196', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-213927.1875, -171310.484375), large=False, heli=False,
                airplanes=True, slot_name='195', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-213911.21875, -171298.546875), large=False, heli=False,
                airplanes=True, slot_name='194', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-213895.25, -171286.28125), large=False, heli=False,
                airplanes=True, slot_name='193', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-213876.609375, -171272.75), large=False, heli=False,
                airplanes=True, slot_name='192', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-214253.640625, -171562.40625), large=False, heli=False,
                airplanes=True, slot_name='198', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-214268.921875, -171574.15625), large=False, heli=False,
                airplanes=True, slot_name='199', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-214284.859375, -171588.578125), large=False, heli=False,
                airplanes=True, slot_name='200', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-214301.25, -171600.0625), large=False, heli=False,
                airplanes=True, slot_name='201', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-214316.96875, -171612.6875), large=False, heli=False,
                airplanes=True, slot_name='202', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-214333.96875, -171628.296875), large=False, heli=False,
                airplanes=True, slot_name='203', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-214497.71875, -171752.078125), large=False, heli=False,
                airplanes=True, slot_name='204', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-214503.8125, -171732.25), large=False, heli=False,
                airplanes=True, slot_name='205', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-214534.515625, -171741.265625), large=False, heli=False,
                airplanes=True, slot_name='209', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-214529.265625, -171761.28125), large=False, heli=False,
                airplanes=True, slot_name='208', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-214515.578125, -171699.25), large=False, heli=False,
                airplanes=True, slot_name='206', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-214521.609375, -171680.265625), large=False, heli=False,
                airplanes=True, slot_name='207', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-214544.03125, -171707.671875), large=False, heli=False,
                airplanes=True, slot_name='210', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-214551.421875, -171688.875), large=False, heli=False,
                airplanes=True, slot_name='211', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-214657.1875, -171677.78125), large=False, heli=False,
                airplanes=True, slot_name='212', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-214660.921875, -171657.859375), large=False, heli=False,
                airplanes=True, slot_name='213', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(-214692.671875, -171663.03125), large=False, heli=False,
                airplanes=True, slot_name='217', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-214689.625, -171683.4375), large=False, heli=False,
                airplanes=True, slot_name='216', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(-214668.265625, -171624.078125), large=False, heli=False,
                airplanes=True, slot_name='214', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(-214671.9375, -171604.34375), large=False, heli=False,
                airplanes=True, slot_name='215', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(-214700.1875, -171629.734375), large=False, heli=False,
                airplanes=True, slot_name='218', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(-214702.625, -171609.59375), large=False, heli=False,
                airplanes=True, slot_name='219', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(-214565.421875, -171553.78125), large=False, heli=False,
                airplanes=True, slot_name='220', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(-214567.515625, -171533.90625), large=False, heli=False,
                airplanes=True, slot_name='221', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(-214570.28125, -171499.21875), large=False, heli=False,
                airplanes=True, slot_name='222', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(-214572.296875, -171479.015625), large=False, heli=False,
                airplanes=True, slot_name='223', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(-214596.46875, -171557.09375), large=False, heli=False,
                airplanes=True, slot_name='224', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(-214597.59375, -171536.09375), large=False, heli=False,
                airplanes=True, slot_name='225', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(-214602.15625, -171502.390625), large=False, heli=False,
                airplanes=True, slot_name='226', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(-214603.5625, -171482.109375), large=False, heli=False,
                airplanes=True, slot_name='227', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(-214751.625, -171451.328125), large=False, heli=False,
                airplanes=True, slot_name='228', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(-214750.59375, -171431), large=False, heli=False,
                airplanes=True, slot_name='229', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(-214782.375, -171449.75), large=False, heli=False,
                airplanes=True, slot_name='232', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(-214781.546875, -171429.25), large=False, heli=False,
                airplanes=True, slot_name='233', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(-214747.796875, -171396.40625), large=False, heli=False,
                airplanes=True, slot_name='230', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(-214780.34375, -171395.015625), large=False, heli=False,
                airplanes=True, slot_name='234', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(-214747.078125, -171376.046875), large=False, heli=False,
                airplanes=True, slot_name='231', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(-214778.921875, -171374.34375), large=False, heli=False,
                airplanes=True, slot_name='235', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(-214900.171875, -171304.40625), large=False, heli=False,
                airplanes=True, slot_name='236', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(-214896.9375, -171284.15625), large=False, heli=False,
                airplanes=True, slot_name='237', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(-214932.18347921, -171298.78974972), large=False, heli=False,
                airplanes=True, slot_name='240', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(-214928.25, -171278.453125), large=False, heli=False,
                airplanes=True, slot_name='241', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(-214890.484375, -171249.1875), large=False, heli=False,
                airplanes=True, slot_name='238', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(-214921.625, -171244.4375), large=False, heli=False,
                airplanes=True, slot_name='242', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(-214886.890625, -171229.484375), large=False, heli=False,
                airplanes=True, slot_name='239', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(-214917.78125, -171224.25), large=False, heli=False,
                airplanes=True, slot_name='243', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(-214903.390625, -171158.171875), large=False, heli=False,
                airplanes=True, slot_name='244', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(-214897.34375, -171139.578125), large=False, heli=False,
                airplanes=True, slot_name='245', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(-214933.53125, -171149.453125), large=False, heli=False,
                airplanes=True, slot_name='248', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(-214927.546875, -171130.21875), large=False, heli=False,
                airplanes=True, slot_name='249', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(-214887.984375, -171106), large=False, heli=False,
                airplanes=True, slot_name='246', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(-214881.8125, -171087.15625), large=False, heli=False,
                airplanes=True, slot_name='247', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(-214917.9375, -171097.46875), large=False, heli=False,
                airplanes=True, slot_name='250', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(-214910.984375, -171077.625), large=False, heli=False,
                airplanes=True, slot_name='251', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(-214250.828125, -172216.921875), large=False, heli=True,
                airplanes=False, slot_name='191', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(-213414.375, -173007.84375), large=False, heli=False,
                airplanes=True, slot_name='169', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=179, position=mapping.Point(-213398.6875, -173027.6875), large=False, heli=False,
                airplanes=True, slot_name='168', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=180, position=mapping.Point(-213383.359375, -173047.671875), large=False, heli=False,
                airplanes=True, slot_name='167', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=181, position=mapping.Point(-213367.71875, -173067.5625), large=False, heli=False,
                airplanes=True, slot_name='166', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=182, position=mapping.Point(-213353.21875, -173087.0625), large=False, heli=False,
                airplanes=True, slot_name='165', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=183, position=mapping.Point(-213319.09375, -173130.328125), large=False, heli=False,
                airplanes=True, slot_name='164', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=184, position=mapping.Point(-213303.234375, -173150.25), large=False, heli=False,
                airplanes=True, slot_name='163', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=185, position=mapping.Point(-213287.640625, -173170.3125), large=False, heli=False,
                airplanes=True, slot_name='162', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=186, position=mapping.Point(-213272.15625, -173190.015625), large=False, heli=False,
                airplanes=True, slot_name='161', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=187, position=mapping.Point(-213257.1875, -173209.625), large=False, heli=False,
                airplanes=True, slot_name='160', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=188, position=mapping.Point(-213222.484375, -173253.609375), large=False, heli=False,
                airplanes=True, slot_name='159', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=189, position=mapping.Point(-213206.78125, -173273.640625), large=False, heli=False,
                airplanes=True, slot_name='158', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=190, position=mapping.Point(-213191.390625, -173293.78125), large=False, heli=False,
                airplanes=True, slot_name='157', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=191, position=mapping.Point(-213175.84375, -173313.46875), large=False, heli=False,
                airplanes=True, slot_name='156', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=192, position=mapping.Point(-213160.78125, -173333.015625), large=False, heli=False,
                airplanes=True, slot_name='155', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=193, position=mapping.Point(-213449.9375, -173037.21875), large=False, heli=False,
                airplanes=True, slot_name='184', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=194, position=mapping.Point(-213434, -173058.359375), large=False, heli=False,
                airplanes=True, slot_name='183', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=195, position=mapping.Point(-213418.625, -173077.828125), large=False, heli=False,
                airplanes=True, slot_name='182', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=196, position=mapping.Point(-213401.859375, -173099.5), large=False, heli=False,
                airplanes=True, slot_name='181', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=197, position=mapping.Point(-213385.71875, -173119.015625), large=False, heli=False,
                airplanes=True, slot_name='180', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=198, position=mapping.Point(-213349.84375, -173165.40625), large=False, heli=False,
                airplanes=True, slot_name='179', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=199, position=mapping.Point(-213333.875, -173186.140625), large=False, heli=False,
                airplanes=True, slot_name='178', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=200, position=mapping.Point(-213318.59375, -173205.125), large=False, heli=False,
                airplanes=True, slot_name='177', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=201, position=mapping.Point(-213301.6875, -173227.015625), large=False, heli=False,
                airplanes=True, slot_name='176', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=202, position=mapping.Point(-213285.890625, -173247.34375), large=False, heli=False,
                airplanes=True, slot_name='175', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=203, position=mapping.Point(-213256.9375, -173284.890625), large=False, heli=False,
                airplanes=True, slot_name='174', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=204, position=mapping.Point(-213240.90625, -173305.203125), large=False, heli=False,
                airplanes=True, slot_name='173', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=205, position=mapping.Point(-213225.59375, -173324.5625), large=False, heli=False,
                airplanes=True, slot_name='172', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=206, position=mapping.Point(-213208.640625, -173346.296875), large=False, heli=False,
                airplanes=True, slot_name='171', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=207, position=mapping.Point(-213192.625, -173366.46875), large=False, heli=False,
                airplanes=True, slot_name='170', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=208, position=mapping.Point(-212562.15625, -174157.390625), large=False, heli=False,
                airplanes=True, slot_name='149', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=209, position=mapping.Point(-212546.859375, -174177.640625), large=False, heli=False,
                airplanes=True, slot_name='148', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=210, position=mapping.Point(-212530.953125, -174197.609375), large=False, heli=False,
                airplanes=True, slot_name='147', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=211, position=mapping.Point(-212515.125, -174218.03125), large=False, heli=False,
                airplanes=True, slot_name='146', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=212, position=mapping.Point(-212500.53125, -174237.265625), large=False, heli=False,
                airplanes=True, slot_name='145', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=213, position=mapping.Point(-212462.109375, -174286.53125), large=False, heli=False,
                airplanes=True, slot_name='138', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=214, position=mapping.Point(-212445.4375, -174307.53125), large=False, heli=False,
                airplanes=True, slot_name='137', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=215, position=mapping.Point(-212428.90625, -174328.484375), large=False, heli=False,
                airplanes=True, slot_name='136', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=216, position=mapping.Point(-212413.65625, -174348.34375), large=False, heli=False,
                airplanes=True, slot_name='135', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=217, position=mapping.Point(-212397.828125, -174368.875), large=False, heli=False,
                airplanes=True, slot_name='134', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=218, position=mapping.Point(-212382.796875, -174388.078125), large=False, heli=False,
                airplanes=True, slot_name='133', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=219, position=mapping.Point(-212425.34375, -174432.640625), large=False, heli=False,
                airplanes=True, slot_name='139', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=220, position=mapping.Point(-212441.3125, -174411.8125), large=False, heli=False,
                airplanes=True, slot_name='140', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=221, position=mapping.Point(-212457.671875, -174390.5625), large=False, heli=False,
                airplanes=True, slot_name='141', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=222, position=mapping.Point(-212474.171875, -174369.515625), large=False, heli=False,
                airplanes=True, slot_name='142', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=223, position=mapping.Point(-212490.234375, -174349.125), large=False, heli=False,
                airplanes=True, slot_name='143', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=224, position=mapping.Point(-212505.328125, -174329.3125), large=False, heli=False,
                airplanes=True, slot_name='144', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=225, position=mapping.Point(-212544.484375, -174279.578125), large=False, heli=False,
                airplanes=True, slot_name='150', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=226, position=mapping.Point(-212561, -174258.40625), large=False, heli=False,
                airplanes=True, slot_name='151', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=227, position=mapping.Point(-212577.484375, -174237.203125), large=False, heli=False,
                airplanes=True, slot_name='152', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=228, position=mapping.Point(-212593.453125, -174217.109375), large=False, heli=False,
                airplanes=True, slot_name='153', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=229, position=mapping.Point(-212608.71875, -174196.765625), large=False, heli=False,
                airplanes=True, slot_name='154', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=230, position=mapping.Point(-212359.125, -174711.84375), large=False, heli=False,
                airplanes=True, slot_name='132', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=231, position=mapping.Point(-212343.15625, -174699.640625), large=False, heli=False,
                airplanes=True, slot_name='131', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=232, position=mapping.Point(-212325.72694429, -174687.24730267), large=False, heli=False,
                airplanes=True, slot_name='130', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=233, position=mapping.Point(-212310.296875, -174674.375), large=False, heli=False,
                airplanes=True, slot_name='129', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=234, position=mapping.Point(-212294.28125, -174662.15625), large=False, heli=False,
                airplanes=True, slot_name='128', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=235, position=mapping.Point(-212277.484375, -174651.28125), large=False, heli=False,
                airplanes=True, slot_name='127', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=236, position=mapping.Point(-212260.578125, -174638.21875), large=False, heli=False,
                airplanes=True, slot_name='126', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=237, position=mapping.Point(-212246, -174625.625), large=False, heli=False,
                airplanes=True, slot_name='125', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=238, position=mapping.Point(-212038.359375, -174593.625), large=False, heli=False,
                airplanes=True, slot_name='124', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=239, position=mapping.Point(-212021.390625, -174580.609375), large=False, heli=False,
                airplanes=True, slot_name='123', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=240, position=mapping.Point(-212005.90625, -174567.859375), large=False, heli=False,
                airplanes=True, slot_name='122', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=241, position=mapping.Point(-211989.84375, -174555.65625), large=False, heli=False,
                airplanes=True, slot_name='121', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=242, position=mapping.Point(-211974.03125, -174543.53125), large=False, heli=False,
                airplanes=True, slot_name='120', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=243, position=mapping.Point(-211956.28125, -174531.421875), large=False, heli=False,
                airplanes=True, slot_name='119', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=244, position=mapping.Point(-211940.65625, -174520.34375), large=False, heli=False,
                airplanes=True, slot_name='118', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=245, position=mapping.Point(-211662.65625, -174298.671875), large=False, heli=False,
                airplanes=True, slot_name='116', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=246, position=mapping.Point(-211647.21875, -174287.078125), large=False, heli=False,
                airplanes=True, slot_name='115', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=247, position=mapping.Point(-211630.40625, -174273.859375), large=False, heli=False,
                airplanes=True, slot_name='114', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=248, position=mapping.Point(-211614.515625, -174261.75), large=False, heli=False,
                airplanes=True, slot_name='113', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=249, position=mapping.Point(-211598.828125, -174249.09375), large=False, heli=False,
                airplanes=True, slot_name='112', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=250, position=mapping.Point(-211582.796875, -174237.265625), large=False, heli=False,
                airplanes=True, slot_name='111', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=251, position=mapping.Point(-211565.96875, -174223.921875), large=False, heli=False,
                airplanes=True, slot_name='110', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=252, position=mapping.Point(-211549.765625, -174212.0625), large=False, heli=False,
                airplanes=True, slot_name='109', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=253, position=mapping.Point(-211593.0625, -171758.296875), large=False, heli=True,
                airplanes=True, slot_name='98', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Dubai_Intl(Airport):
    id = 5
    name = "Dubai Intl"
    position = mapping.Point(-100594.371094, -88875.371094)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Dubai_Intl, self).__init__()

        self.runways.append(Runway(300))
        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-101536.4765625, -88944.609375), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-101659.375, -88752.8359375), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-101462.375, -89063.1484375), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-101388.6875, -89181.7734375), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-101315.046875, -89300.40625), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-101203.3125, -89477.7734375), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-101112.15625, -89624.046875), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-100964.2734375, -89861.078125), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-101749.0703125, -88995.5234375), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-101675.1171875, -89113.984375), large=False, heli=True,
                airplanes=True, slot_name='24', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-101561.53125, -89295.6484375), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-101487.359375, -89414.203125), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-101376.21875, -89591.71875), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-101265.203125, -89769.21875), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-101173.9453125, -89915.6640625), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-101099.3203125, -90033.625), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-101018.578125, -90142.0546875), large=False, heli=True,
                airplanes=True, slot_name='31', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-100962.6171875, -90228.7265625), large=False, heli=True,
                airplanes=True, slot_name='32', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-100923.15625, -90291.8671875), large=False, heli=True,
                airplanes=True, slot_name='33', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-100896.03125, -90335.1640625), large=False, heli=True,
                airplanes=True, slot_name='34', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-100738.2734375, -90219.8671875), large=False, heli=True,
                airplanes=True, slot_name='13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-100851.9921875, -90038.515625), large=False, heli=True,
                airplanes=True, slot_name='14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-101959.875, -88561.6640625), large=False, heli=True,
                airplanes=True, slot_name='78', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-102106.109375, -88329.0390625), large=False, heli=True,
                airplanes=True, slot_name='79', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-102200.828125, -88179.2578125), large=False, heli=True,
                airplanes=True, slot_name='80', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-102248.1015625, -88104.5625), large=False, heli=True,
                airplanes=True, slot_name='81', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-102346.46875, -87933.84375), large=False, heli=True,
                airplanes=True, slot_name='82', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-102129.5703125, -87898.8203125), large=False, heli=True,
                airplanes=True, slot_name='77', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-102036.5546875, -88049.2265625), large=False, heli=True,
                airplanes=True, slot_name='76', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-101989.90625, -88124.5390625), large=False, heli=True,
                airplanes=True, slot_name='75', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-101896.5859375, -88274.7734375), large=False, heli=True,
                airplanes=True, slot_name='74', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-101847.671875, -88353.609375), large=False, heli=True,
                airplanes=True, slot_name='73', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-102313.96875, -87531.265625), large=False, heli=True,
                airplanes=True, slot_name='83', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-102387.859375, -87411.6328125), large=False, heli=True,
                airplanes=True, slot_name='84', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-102462.0859375, -87294.1171875), large=False, heli=True,
                airplanes=True, slot_name='85', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-102536.390625, -87175.875), large=False, heli=True,
                airplanes=True, slot_name='86', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-102695.9296875, -87089.921875), large=False, heli=True,
                airplanes=True, slot_name='87', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-102817.328125, -87160.484375), large=False, heli=True,
                airplanes=True, slot_name='88', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-102931.9296875, -87026.546875), large=False, heli=True,
                airplanes=True, slot_name='89', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-102816.234375, -86948.8515625), large=False, heli=True,
                airplanes=True, slot_name='90', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-102700.3828125, -86872.484375), large=False, heli=True,
                airplanes=True, slot_name='91', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-103094.5546875, -86333.859375), large=False, heli=True,
                airplanes=True, slot_name='93', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-103177.71875, -86203.2578125), large=False, heli=True,
                airplanes=True, slot_name='94', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-103353.5, -85889.2265625), large=False, heli=True,
                airplanes=True, slot_name='96', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-103269.9375, -86032.7421875), large=False, heli=True,
                airplanes=True, slot_name='95', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-103040.6875, -86446.234375), large=False, heli=True,
                airplanes=True, slot_name='92', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-99332.8515625, -90198.265625), large=False, heli=True,
                airplanes=True, slot_name='35', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-99406.8515625, -90079.671875), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-99481.0234375, -89961.21875), large=False, heli=True,
                airplanes=True, slot_name='37', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-99555.0625, -89842.875), large=False, heli=True,
                airplanes=True, slot_name='38', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-99629.1015625, -89724.2734375), large=False, heli=True,
                airplanes=True, slot_name='39', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-99703.1875, -89605.8203125), large=False, heli=True,
                airplanes=True, slot_name='40', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-99777.078125, -89487.34375), large=False, heli=True,
                airplanes=True, slot_name='41', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-99851.1875, -89368.8046875), large=False, heli=True,
                airplanes=True, slot_name='42', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-99925.3125, -89250.3828125), large=False, heli=True,
                airplanes=True, slot_name='43', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-99999.3125, -89131.8125), large=False, heli=True,
                airplanes=True, slot_name='44', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-100073.328125, -89013.4296875), large=False, heli=True,
                airplanes=True, slot_name='45', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-100147.5625, -88894.953125), large=False, heli=True,
                airplanes=True, slot_name='46', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-100221.703125, -88776.6171875), large=False, heli=True,
                airplanes=True, slot_name='47', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-100295.7265625, -88658.046875), large=False, heli=True,
                airplanes=True, slot_name='48', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-100369.921875, -88539.5), large=False, heli=True,
                airplanes=True, slot_name='49', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-100438.53125, -88423.4375), large=False, heli=True,
                airplanes=True, slot_name='50', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-100651.109375, -88089.3515625), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-100624.90625, -88130.9921875), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-100605.1015625, -88162.640625), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-100585.3515625, -88194.265625), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-100565.5625, -88225.8515625), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-100545.890625, -88257.5), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-100526.0546875, -88289.015625), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-100506.4140625, -88320.65625), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-100486.6484375, -88352.234375), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-100466.6796875, -88383.2265625), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-100759.609375, -87915.8203125), large=False, heli=True,
                airplanes=True, slot_name='68', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-100657.40625, -87912.3046875), large=False, heli=True,
                airplanes=True, slot_name='67', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-101014.34375, -87369.8828125), large=False, heli=True,
                airplanes=True, slot_name='69', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-101076.9765625, -87270.375), large=False, heli=True,
                airplanes=True, slot_name='70', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-101121.0625, -87200.46875), large=False, heli=True,
                airplanes=True, slot_name='71', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-101183.078125, -87099.3984375), large=False, heli=True,
                airplanes=True, slot_name='72', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-99985.4375, -90875.6953125), large=False, heli=True,
                airplanes=True, slot_name='08', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-99873.3984375, -91056.0546875), large=False, heli=True,
                airplanes=True, slot_name='07', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-99738.8046875, -91171.65625), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-99663.0625, -91289.9453125), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-99537.1015625, -91276.390625), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-99579.9609375, -91209.5859375), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-100065.21875, -91519.8671875), large=False, heli=True,
                airplanes=True, slot_name='11', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-100187.125, -91478.0625), large=False, heli=True,
                airplanes=True, slot_name='12', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-99960.6015625, -91457.8359375), large=False, heli=True,
                airplanes=True, slot_name='10', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-99874.8046875, -91394.8984375), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-99799.125, -90966.65625), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-99872.3046875, -90849.5546875), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-100497.671875, -87813.1015625), large=False, heli=True,
                airplanes=True, slot_name='63', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-100618.0546875, -87887.703125), large=False, heli=True,
                airplanes=True, slot_name='66', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-100578.3203125, -87862.75), large=False, heli=True,
                airplanes=True, slot_name='65', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-100537.796875, -87838.5390625), large=False, heli=True,
                airplanes=True, slot_name='64', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-100556.3359375, -88000.8359375), large=False, heli=True,
                airplanes=True, slot_name='61', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-100516.890625, -87976.8125), large=False, heli=True,
                airplanes=True, slot_name='62', length=43.057953, width=40.0, height=None, shelter=False))


class Al_Maktoum_Intl(Airport):
    id = 6
    name = "Al Maktoum Intl"
    position = mapping.Point(-140127.671875, -110068.890625)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Al_Maktoum_Intl, self).__init__()

        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-140247.46875, -111218.859375), large=False, heli=True,
                airplanes=False, slot_name='14', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-140281.8125, -111163.859375), large=False, heli=True,
                airplanes=False, slot_name='15', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-140326.34375, -111096.9921875), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-140379.34375, -111012.0078125), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-140440.5625, -110914.25), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-140480.5, -110850.671875), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-140599.609375, -110660.484375), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-140639.375, -110596.9140625), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-140390.921875, -111313.609375), large=False, heli=True,
                airplanes=True, slot_name='13', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-140454.625, -111354.0625), large=False, heli=True,
                airplanes=True, slot_name='12', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-140518.203125, -111393.875), large=False, heli=True,
                airplanes=True, slot_name='11', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-140582.734375, -111433.1171875), large=False, heli=True,
                airplanes=True, slot_name='10', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-140645.640625, -111473.8046875), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-140722.90625, -111520.4375), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-140790.96875, -111564.296875), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-140850.3125, -111599.6953125), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-140914.453125, -111641.09375), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-140990.578125, -111687.625), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-141062.953125, -111732.8125), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-141126.9375, -111772.5390625), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-141185.28125, -111808.8671875), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-141080.796875, -110527.4375), large=False, heli=True,
                airplanes=True, slot_name='32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-141148.859375, -110569.9296875), large=False, heli=True,
                airplanes=True, slot_name='31', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-141216.65625, -110612.328125), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-141284.890625, -110654.765625), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-140794.828125, -110664.1640625), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-140921.125, -110743.0390625), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-141031.3125, -110811.5546875), large=False, heli=True,
                airplanes=True, slot_name='24', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-141141.5625, -110880.546875), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-141306.859375, -110984.15625), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-141417.03125, -111052.765625), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-141527.3125, -111121.5546875), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-140832.234375, -110287.03125), large=False, heli=True,
                airplanes=True, slot_name='33', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-140871.578125, -110223.59375), large=False, heli=True,
                airplanes=True, slot_name='34', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-140916.234375, -110151.0859375), large=False, heli=True,
                airplanes=True, slot_name='35', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-140968.875, -110065.84375), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-141051.25, -109933.40625), large=False, heli=True,
                airplanes=True, slot_name='37', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-141130.1875, -109806.7578125), large=False, heli=True,
                airplanes=True, slot_name='38', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-141199.640625, -109696.5234375), large=False, heli=True,
                airplanes=True, slot_name='39', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-142040.546875, -108353.59375), large=False, heli=True,
                airplanes=True, slot_name='40', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-142093.671875, -108268.6484375), large=False, heli=True,
                airplanes=True, slot_name='41', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-142146.84375, -108184), large=False, heli=True,
                airplanes=True, slot_name='42', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-142200, -108099.609375), large=False, heli=True,
                airplanes=True, slot_name='43', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-142306.203125, -107929.921875), large=False, heli=True,
                airplanes=True, slot_name='44', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-142354.046875, -107853.8515625), large=False, heli=True,
                airplanes=True, slot_name='45', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-142393.96875, -107790.3203125), large=False, heli=True,
                airplanes=True, slot_name='46', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-142433.953125, -107726.8046875), large=False, heli=True,
                airplanes=True, slot_name='47', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-142473.46875, -107663.3203125), large=False, heli=True,
                airplanes=True, slot_name='48', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-142513.34375, -107599.7109375), large=False, heli=True,
                airplanes=True, slot_name='49', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-142553.671875, -107536.515625), large=False, heli=True,
                airplanes=True, slot_name='50', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-141037.265625, -112023.875), large=False, heli=True,
                airplanes=True, slot_name='69', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-140973.65625, -111984.0625), large=False, heli=True,
                airplanes=True, slot_name='68', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-140909.609375, -111945.3046875), large=False, heli=True,
                airplanes=True, slot_name='67', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-140845.65625, -111906.21875), large=False, heli=True,
                airplanes=True, slot_name='66', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-140700.015625, -111815.2734375), large=False, heli=True,
                airplanes=True, slot_name='65', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-140640.75, -111779.59375), large=False, heli=True,
                airplanes=True, slot_name='64', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-140577.8125, -111738.1875), large=False, heli=True,
                airplanes=True, slot_name='63', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-140501.125, -111691.53125), large=False, heli=True,
                airplanes=True, slot_name='62', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-140427.5, -111648.375), large=False, heli=True,
                airplanes=True, slot_name='61', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-140363.9375, -111607.9921875), large=False, heli=True,
                airplanes=True, slot_name='60', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-140306.78125, -111569.875), large=False, heli=True,
                airplanes=True, slot_name='59', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-143019.234375, -109123.5546875), large=False, heli=True,
                airplanes=True, slot_name='54', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-142960.53125, -109087.5), large=False, heli=True,
                airplanes=True, slot_name='53', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-142896.40625, -109047.9296875), large=False, heli=True,
                airplanes=True, slot_name='52', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-142769.03125, -108970.9921875), large=False, heli=True,
                airplanes=True, slot_name='51', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-143099.71875, -108999.578125), large=False, heli=True,
                airplanes=True, slot_name='58', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-142975.6875, -108925.21875), large=False, heli=True,
                airplanes=True, slot_name='57', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-142912.75, -108885.8046875), large=False, heli=True,
                airplanes=True, slot_name='56', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-142848.734375, -108847.640625), large=False, heli=True,
                airplanes=True, slot_name='55', length=43.057953, width=40.0, height=None, shelter=False))


class Fujairah_Intl(Airport):
    id = 7
    name = "Fujairah Intl"
    position = mapping.Point(-117531.972946, 7939.275818)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Fujairah_Intl, self).__init__()

        self.runways.append(Runway(290))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-117293.855896, 8304.8382568359), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-117250.05471802, 8540.6785888672), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-117313.23373413, 8519.846862793), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-117374.25790405, 8477.9990234375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))


class Tunb_Island_AFB(Airport):
    id = 8
    name = "Tunb Island AFB"
    position = mapping.Point(10515.440918, -92440.328125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Tunb_Island_AFB, self).__init__()

        self.runways.append(Runway(30))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(10327.60546875, -92808.609375), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(10350.327148438, -92838.28125), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(10314.954101562, -92779.4453125), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(10298.874023438, -92745.8203125), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))


class Havadarya(Airport):
    id = 9
    name = "Havadarya"
    position = mapping.Point(109297.832031, -6278.723145)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Havadarya, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(109336.5078125, -6856.7329101562), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(109384.078125, -6866.2290039062), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(109391.328125, -6827.91796875), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(109372.765625, -7220.5141601563), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(109348.53125, -7215.0922851562), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(109324.28125, -7210.333984375), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(109299.640625, -7204.5014648437), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(109272.7265625, -7198.9184570313), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(109248.265625, -7192.9721679687), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(109245.078125, -7286.328125), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(109239.9765625, -7311.9379882812), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(109234.546875, -7339.5024414062), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(109228.7421875, -7366.6391601562), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(109344.4453125, -6815.3627929687), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))


class Khasab(Airport):
    id = 10
    name = "Khasab"
    position = mapping.Point(-219.726892, -177.707709)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Khasab, self).__init__()

        self.runways.append(Runway(190))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-1017.2598266602, -602.64483642578), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-993.78546142578, -596.85540771484), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-970.39038085937, -590.92138671875), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-946.86694335938, -585.11224365234), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-923.39343261719, -579.32574462891), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-899.84790039063, -573.57952880859), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-876.40319824219, -567.68103027344), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-787.23937988281, -547.58770751953), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-763.80834960937, -541.49548339844), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-740.30584716797, -535.81024169922), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-714.90942382813, -530.10400390625), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-673.22117416432, -522.01122705626), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))


class Lar_Airbase(Airport):
    id = 11
    name = "Lar Airbase"
    position = mapping.Point(168977.578922, -182359.639734)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Lar_Airbase, self).__init__()

        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(168556.390625, -182527.234375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(168561.5625, -182399.140625), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(168562.390625, -182481.734375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(168562.109375, -182430.84375), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(168614.578125, -182785.015625), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))


class Al_Minhad_AB(Airport):
    id = 12
    name = "Al Minhad AB"
    position = mapping.Point(-126013.707153, -89133.460938)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Al_Minhad_AB, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-126253.08361816, -89660.172302246), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-126302.70910645, -89660.520629883), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-126353.11022949, -89659.443786621), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-126253.17944336, -89561.108947754), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-126302.8203125, -89560.616333008), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-126353.41662598, -89559.875244141), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-126252.84289551, -89459.989013672), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-126302.9921875, -89459.988525391), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-126353.63293457, -89458.822753906), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-126315.5078125, -89380.320251465), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-126353.45446777, -89388.752197266), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-126353.33312988, -89500.376831055), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-126302.64611816, -89499.628967285), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-126252.89318848, -89499.913757324), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-126253.06750488, -89599.119384766), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-126302.78125, -89598.968688965), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-126353.2578125, -89599.073547363), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-126378.796875, -90475.5), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-126378.93737793, -90433.34362793), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-126378.7734375, -90392.5859375), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-126378.62463379, -90350.187866211), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-126378.9765625, -90309.515625), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-126379.34362793, -90267.74987793), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-126378.59375, -90226.6796875), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-126378.328125, -90184.28125), large=False, heli=False,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-126378.71081543, -90143.51550293), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-126317.85949707, -90475.913452148), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-126318.03112793, -90434.05480957), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-126317.89868164, -90393.296386719), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-126317.72705078, -90351.29675293), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-126317.21862793, -90309.63293457), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-126318.00012207, -90268.30480957), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-126317.5234375, -90227.2890625), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-126317.69555664, -90185.58581543), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-126317.62487793, -90144.21105957), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-126315.45324707, -89229.179931641), large=False, heli=False,
                airplanes=True, slot_name='40', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-126315.69543457, -89204.4609375), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-126314.4453125, -89028.7265625), large=False, heli=True,
                airplanes=True, slot_name='42', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-126335.625, -88954.890640259), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-126381.17199707, -88950.023422241), large=False, heli=True,
                airplanes=True, slot_name='43', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-126320.47387695, -88654.495857239), large=False, heli=True,
                airplanes=True, slot_name='47', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-126369.56311035, -88862.332321167), large=False, heli=True,
                airplanes=True, slot_name='44', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-126370.4251709, -88802.528015137), large=False, heli=True,
                airplanes=True, slot_name='45', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-126370.60241699, -88747.73041153), large=False, heli=True,
                airplanes=True, slot_name='46', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-126380.29626465, -88651.143424988), large=False, heli=True,
                airplanes=True, slot_name='48', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-126312.14245605, -88090.050231934), large=False, heli=True,
                airplanes=True, slot_name='49', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-126312.02441406, -88000.29095459), large=False, heli=True,
                airplanes=True, slot_name='50', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-126312.03369141, -87610.740844727), large=False, heli=False,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-126311.96899414, -87586.267211914), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-126312.19165039, -87562.348022461), large=False, heli=False,
                airplanes=True, slot_name='53', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-126312.15795898, -87538.94140625), large=False, heli=False,
                airplanes=True, slot_name='54', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-126312.00500488, -87515.07409668), large=False, heli=False,
                airplanes=True, slot_name='55', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-126311.92248535, -87488.044921875), large=False, heli=False,
                airplanes=True, slot_name='56', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-126342.4822998, -87617.952758789), large=False, heli=False,
                airplanes=True, slot_name='57', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-126342.41821289, -87587.591064453), large=False, heli=False,
                airplanes=True, slot_name='58', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-126342.60693359, -87557.223388672), large=False, heli=False,
                airplanes=True, slot_name='59', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-126342.60864258, -87527.473510742), large=False, heli=False,
                airplanes=True, slot_name='60', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-126342.72473145, -87497.182617188), large=False, heli=False,
                airplanes=True, slot_name='61', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-126515.6953125, -90985.948486328), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-126580.08117676, -90985.940673828), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-126580.07641602, -90906.190673828), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-126515.65429688, -90906.147460938), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))


class Qeshm_Island(Airport):
    id = 13
    name = "Qeshm Island"
    position = mapping.Point(64800.714844, -33383.481445)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Qeshm_Island, self).__init__()

        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(65148.21875, -33696.6328125), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(65102.96484375, -33751.9140625), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(65058.5234375, -33805.59375), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(65014.59375, -33858.51953125), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(64968.7109375, -33909.875), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(64922.87109375, -33966.51953125), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(64865.3828125, -34016.39453125), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(64812.84765625, -34082.34765625), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(64761.55859375, -34141.59765625), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(64731.578125, -33924.45703125), large=False, heli=True,
                airplanes=True, slot_name='11', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(64689.7890625, -33968.71875), large=False, heli=True,
                airplanes=True, slot_name='12', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(64773.828125, -33869.1015625), large=False, heli=True,
                airplanes=True, slot_name='10', length=43.057953, width=40.0, height=None, shelter=False))


class Sharjah_Intl(Airport):
    id = 14
    name = "Sharjah Intl"
    position = mapping.Point(-92544.089844, -73373.601563)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Sharjah_Intl, self).__init__()

        self.runways.append(Runway(300))
        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-93511.0078125, -72815.6015625), large=False, heli=True,
                airplanes=True, slot_name='46', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-93548.203125, -72841.1015625), large=False, heli=True,
                airplanes=True, slot_name='45', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-93586.015625, -72865.5078125), large=False, heli=True,
                airplanes=True, slot_name='44', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-93732.7265625, -72655.046875), large=False, heli=True,
                airplanes=True, slot_name='47', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-93450.328125, -73049.34375), large=False, heli=True,
                airplanes=True, slot_name='41', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-93490.078125, -72985.984375), large=False, heli=True,
                airplanes=True, slot_name='42', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-93408.4765625, -73111.5703125), large=False, heli=True,
                airplanes=True, slot_name='40', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-93367.296875, -73174.4140625), large=False, heli=True,
                airplanes=True, slot_name='39', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-93326.421875, -73237.0546875), large=False, heli=True,
                airplanes=True, slot_name='38', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-93286.046875, -73300.328125), large=False, heli=True,
                airplanes=True, slot_name='37', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-93172.2265625, -73366.796875), large=False, heli=True,
                airplanes=True, slot_name='34', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-93209.9609375, -73391.234375), large=False, heli=True,
                airplanes=True, slot_name='35', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-93247.484375, -73415.765625), large=False, heli=True,
                airplanes=True, slot_name='36', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-93138.5078125, -73583.796875), large=False, heli=True,
                airplanes=True, slot_name='30', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-93100.859375, -73559.40625), large=False, heli=True,
                airplanes=True, slot_name='29', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-93063.2578125, -73534.875), large=False, heli=True,
                airplanes=True, slot_name='28', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-93030.09375, -73750.25), large=False, heli=True,
                airplanes=True, slot_name='24', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-92992.53125, -73726.1875), large=False, heli=True,
                airplanes=True, slot_name='23', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-92954.671875, -73701.6484375), large=False, heli=True,
                airplanes=True, slot_name='22', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-93091.609375, -73656.0546875), large=False, heli=True,
                airplanes=True, slot_name='27', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-93054.171875, -73631.4921875), large=False, heli=True,
                airplanes=True, slot_name='26', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-93016.234375, -73606.9296875), large=False, heli=True,
                airplanes=True, slot_name='25', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-93125.2890625, -73439.4140625), large=False, heli=True,
                airplanes=True, slot_name='31', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-93163.140625, -73464.140625), large=False, heli=True,
                airplanes=True, slot_name='32', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-93200.71875, -73488.53125), large=False, heli=True,
                airplanes=True, slot_name='33', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-92966.6875, -73998.8671875), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-93066.765625, -74065.2265625), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-93166.5859375, -74131.7734375), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-93268.15625, -74195.6484375), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-93167.578125, -74350.6953125), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-93066.546875, -74286.0859375), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-92967.390625, -74218.4609375), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-92869.6796875, -74147.6015625), large=False, heli=True,
                airplanes=True, slot_name='14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-92321.4296875, -75170.703125), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-92380.546875, -75232.515625), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-92480.5234375, -75270.234375), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-92361.0703125, -74968.0546875), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-92377.6484375, -74942.921875), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-92393.9765625, -74917.7421875), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-92410.21875, -74892.4765625), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-92184.296875, -75476.1328125), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-91881.9140625, -75455.484375), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-91838.046875, -75521.953125), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-91805.5078125, -75572.7109375), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-91775.453125, -75618.5), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-91745.53125, -75664.6875), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-93530.78125, -72922.8984375), large=False, heli=True,
                airplanes=True, slot_name='43', length=43.057953, width=40.0, height=None, shelter=False))


class Sirri_Island(Airport):
    id = 15
    name = "Sirri Island"
    position = mapping.Point(-26946.104553, -170745.015625)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Sirri_Island, self).__init__()

        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-27713.302612305, -170052.375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-27754.28125, -169999.1875), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))


class Tunb_Kochak(Airport):
    id = 16
    name = "Tunb Kochak"
    position = mapping.Point(9023.430176, -109467.078125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Tunb_Kochak, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(8992.48046875, -109345.625), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(9012.076171875, -109348.078125), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=11.0, shelter=False))


class Sir_Abu_Nuayr(Airport):
    id = 17
    name = "Sir Abu Nuayr"
    position = mapping.Point(-103102.869351, -202973.057313)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Sir_Abu_Nuayr, self).__init__()

        self.runways.append(Runway(280))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-103018.5859375, -203142.71875), large=False, heli=True,
                airplanes=True, slot_name='01', length=25.0, width=20.0, height=11.0, shelter=False))


class PersianGulf(Terrain):
    center = {"lat": 0, "long": 0}
    bounds = mapping.Rectangle(-218768.750000, -392081.937500, 197357.906250, 333129.125000)
    map_view_default = MapView(bounds.center(), 1000000)
    city_graph = None
    temperature = [
        (10, 20),
        (11, 20),
        (13, 22),
        (16, 26),
        (18, 30),
        (20, 36),
        (24, 39),
        (25, 40),
        (22, 37),
        (20, 32),
        (16, 26),
        (12, 22)
    ]
    assert(len(temperature) == 12)

    def random_season_temperature(self, dt: datetime):
        return random.randint(self.temperature[dt.month][0], self.temperature[dt.month][1])

    def __init__(self):
        super(PersianGulf, self).__init__("PersianGulf")
        self.bullseye_blue = {"x": PersianGulf.bounds.center().x, "y": PersianGulf.bounds.center().y}
        self.bullseye_red = {"x": PersianGulf.bounds.center().x, "y": PersianGulf.bounds.center().y}

        self.airports['Abu Musa Island Airport'] = Abu_Musa_Island_Airport()
        self.airports['Bandar Abbas Intl'] = Bandar_Abbas_Intl()
        self.airports['Bandar Lengeh'] = Bandar_Lengeh()
        self.airports['Al Dhafra AB'] = Al_Dhafra_AB()
        self.airports['Dubai Intl'] = Dubai_Intl()
        self.airports['Al Maktoum Intl'] = Al_Maktoum_Intl()
        self.airports['Fujairah Intl'] = Fujairah_Intl()
        self.airports['Tunb Island AFB'] = Tunb_Island_AFB()
        self.airports['Havadarya'] = Havadarya()
        self.airports['Khasab'] = Khasab()
        self.airports['Lar Airbase'] = Lar_Airbase()
        self.airports['Al Minhad AB'] = Al_Minhad_AB()
        self.airports['Qeshm Island'] = Qeshm_Island()
        self.airports['Sharjah Intl'] = Sharjah_Intl()
        self.airports['Sirri Island'] = Sirri_Island()
        self.airports['Tunb Kochak'] = Tunb_Kochak()
        self.airports['Sir Abu Nuayr'] = Sir_Abu_Nuayr()

    def abu_musa_island_airport(self) -> Airport:
        return self.airports["Abu Musa Island Airport"]

    def bandar_abbas_intl(self) -> Airport:
        return self.airports["Bandar Abbas Intl"]

    def bandar_lengeh(self) -> Airport:
        return self.airports["Bandar Lengeh"]

    def al_dhafra_ab(self) -> Airport:
        return self.airports["Al Dhafra AB"]

    def dubai_intl(self) -> Airport:
        return self.airports["Dubai Intl"]

    def al_maktoum_intl(self) -> Airport:
        return self.airports["Al Maktoum Intl"]

    def fujairah_intl(self) -> Airport:
        return self.airports["Fujairah Intl"]

    def tunb_island_afb(self) -> Airport:
        return self.airports["Tunb Island AFB"]

    def havadarya(self) -> Airport:
        return self.airports["Havadarya"]

    def khasab(self) -> Airport:
        return self.airports["Khasab"]

    def lar_airbase(self) -> Airport:
        return self.airports["Lar Airbase"]

    def al_minhad_ab(self) -> Airport:
        return self.airports["Al Minhad AB"]

    def qeshm_island(self) -> Airport:
        return self.airports["Qeshm Island"]

    def sharjah_intl(self) -> Airport:
        return self.airports["Sharjah Intl"]

    def sirri_island(self) -> Airport:
        return self.airports["Sirri Island"]

    def tunb_kochak(self) -> Airport:
        return self.airports["Tunb Kochak"]

    def sir_abu_nuayr(self) -> Airport:
        return self.airports["Sir Abu Nuayr"]
