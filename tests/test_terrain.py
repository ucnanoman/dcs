import unittest
import dcs


class CaucasusTest(unittest.TestCase):

    def test_parking_slots(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())
        large_slots = m.terrain.batumi().free_parking_slots(dcs.planes.KC_135)
        self.assertEqual(len(large_slots), 3)

        slots = m.terrain.batumi().free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), len(m.terrain.batumi().parking_slots))
        for x in slots[-3:]:
            self.assertTrue(x.large, "the last 3 slots on batumi should be large")

        slot = m.terrain.batumi().free_parking_slot(dcs.planes.A_10C)
        slot.unit_id = 1

        slots = m.terrain.batumi().free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 9)

        slot.unit_id = None
        slots = m.terrain.batumi().free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 10)

        hslots = m.terrain.batumi().free_parking_slots(dcs.helicopters.UH_1H)
        for x in hslots[-3:]:
            self.assertTrue(x.large, "the last 3 slots on batumi should be large")

    def test_parking_large_used(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        for x in range(1, 4):
            large_slot = m.terrain.batumi().free_parking_slot(dcs.planes.KC_135)
            self.assertIsNotNone(large_slot)
            large_slot.unit_id = x

        self.assertIsNone(m.terrain.batumi().free_parking_slot(dcs.planes.KC_135))

    def test_parking_mixed_used(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        used = []
        for x in range(1, 3):
            large_slot = m.terrain.batumi().free_parking_slot(dcs.planes.KC_135)
            self.assertIsNotNone(large_slot)
            large_slot.unit_id = x
            used.append(large_slot)

        self.assertIsNotNone(m.terrain.batumi().free_parking_slot(dcs.planes.KC_135))

        for x in range(3, 10):
            slot = m.terrain.batumi().free_parking_slot(dcs.planes.A_10A)
            self.assertIsNotNone(slot)
            slot.unit_id = x
            used.append(slot)

        slot = m.terrain.batumi().free_parking_slot(dcs.planes.A_10A)
        self.assertTrue(slot.large)

        self.assertEqual(len(used)+1, len(m.terrain.batumi().parking_slots))


class NevataTest(unittest.TestCase):

    def test_parking_slots(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Nevada())
        slots = m.terrain.nellis().free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 104)

        slot = m.terrain.nellis().free_parking_slot(dcs.planes.A_10C)
        slot.unit_id = 1

        slots = m.terrain.nellis().free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 103)

        slot.unit_id = None
        slots = m.terrain.nellis().free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 104)

        hslots = m.terrain.nellis().free_parking_slots(dcs.helicopters.UH_1H)
        self.assertEqual(len(hslots), 14)

        slots = m.terrain.nellis().free_parking_slots(dcs.planes.KC_135)
