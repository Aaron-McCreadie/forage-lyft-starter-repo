import unittest
from ..engine import CapuletEngine, WilloughbyEngine, SternmanEngine


class TestCapuletEngine(unittest.TestCase):

    def test_need_service(self):
        engine = CapuletEngine(0, 29999)
        self.assertFalse(engine.needs_service())

        engine = CapuletEngine(0, 30001)
        self.assertTrue(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service(self):
        engine = WilloughbyEngine(0, 59999)
        self.assertFalse(engine.needs_service())

        engine = WilloughbyEngine(0, 60001)
        self.assertTrue(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):

    def test_needs_service(self):
        engine = SternmanEngine(False)
        self.asserFalse(engine.nedds_service())

        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

        if __name__ == '__main__':
            unittest.main()