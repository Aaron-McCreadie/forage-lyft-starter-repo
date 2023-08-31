import unittest
from ..tires.octoprime_tires import OctoprimeTires
from ..tires.carrigan_tires import CarriganTires


class TestOctoprimeTires(unittest.TestCase):

    def test_needs_service_true(self):
        tires = OctoprimeTires([0.8, 0.8, 0.8, 0.8])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires = OctoprimeTires([0.7, 0.7, 0.7, 0.7])
        self.assertFalse(tires.needs_service())


class TestCarriganTires(unittest.TestCase):

    def test_needs_service_true_single_threshold(self):
        tires = CarriganTires([0.8, 0.8, 0.8, 0.9])
        self.assertTrue(tires.needs_service())

    def test_needs_service_true_all_threshold(self):
        tires = CarriganTires([0.91, 0.92, 0.93, 0.94])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        self.assertFalse(tires.needs_service())


if __name__ == "__main__":
    unittest.main()
