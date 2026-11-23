"""Eastside Library Study Rooms: open room hours."""


def hours_left(capacity, booked):
    """Return how many room hours are still open."""
    return max(capacity - booked, 0)


def can_book(capacity, booked, hours=1):
    """Return True when the booking fits in the open room hours."""
    return hours <= hours_left(capacity, booked)
