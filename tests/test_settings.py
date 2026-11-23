import unittest

from app.settings import ROOM_HOURS_PER_DAY


class SettingsTests(unittest.TestCase):
    def test_capacity_is_a_positive_number(self):
        self.assertGreater(ROOM_HOURS_PER_DAY, 0)
