import unittest
import dcs


class BasicTests(unittest.TestCase):

    def test_basic_keys(self):
        m = dcs.mission.Mission()
        d = m.dict()
        self.assertIn("version", d)
        self.assertIn("map", d)
        self.assertGreaterEqual(d["start_time"], 0)

    def test_finding(self):
        m = dcs.mission.Mission()

        usa = m.country("USA")
        caucasus = m.terrain  # type: dcs.terrain.Caucasus
        batumi = caucasus.batumi()
        self.assertIsNotNone(usa)
        px, py = batumi.random_unit_zone().center()
        vg = m.vehicle_group(usa, "Tanks", dcs.countries.USA.Vehicle.Armor.MBT_M1A2_Abrams, px, py)
        self.assertIsInstance(vg, dcs.unitgroup.VehicleGroup)
        pg = m.plane_group_inflight(usa, "Airgroup 1", dcs.planes.A_10C, px + 200, py + 200, 2000)
        self.assertIsInstance(pg, dcs.unitgroup.PlaneGroup)
        pg = m.plane_group_inflight(usa, "Airgroup 2", dcs.planes.M_2000C, px + 200, py + 200, 2000)
        self.assertIsInstance(pg, dcs.unitgroup.PlaneGroup)
        found_g = m.find_group("Tanks", "exact")
        self.assertIsInstance(found_g, dcs.unitgroup.VehicleGroup)

        found_g = m.find_group("Tank", "exact")
        self.assertIsNone(found_g)

        found_g = m.find_group("Tank", "match")
        self.assertIsInstance(found_g, dcs.unitgroup.VehicleGroup)

        found_g = m.find_group("Airgroup")
        self.assertIsNone(found_g)

        found_g = m.find_group("Airgroup", "match")
        self.assertIsInstance(found_g, dcs.unitgroup.PlaneGroup)

        found_g = m.find_group("Airgroup 1")
        self.assertIsInstance(found_g, dcs.unitgroup.PlaneGroup)
        self.assertEqual(found_g.units[0].unit_type, dcs.planes.A_10C)
