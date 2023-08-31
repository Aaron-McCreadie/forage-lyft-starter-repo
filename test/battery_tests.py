import unittest
from datetime import date, timedelta
from ..battery import NubbinBattery, SpindlerBattery


class TestNubbinBattery(unittest.TestCase):

    # needs_service every 4 years or 1460 days
    def test_need_service(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=1459)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

        last_service_date = current_date - timedelta(days=1461)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):

    # needs_service every 3 years or 1095 days
    def test_needs_service(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=1094)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

        last_service_date = current_date - timedelta(days=1096)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
