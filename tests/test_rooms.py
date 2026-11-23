import unittest

from app.rooms import can_book, hours_left


class BookingTests(unittest.TestCase):
    def test_counts_open(self):
        self.assertEqual(hours_left(20, 15), 5)

    def test_never_below_zero(self):
        self.assertEqual(hours_left(20, 25), 0)

    def test_small_booking_fits(self):
        self.assertTrue(can_book(20, 18, hours=2))

    def test_full_day_refuses_booking(self):
        self.assertFalse(can_book(20, 20))
