"""Eastside Library Study Rooms: waitlist for full days."""


def waitlist_position(waitlist, team):
    """Return the team's place in line (1 is first), or 0 when not on the waitlist."""
    if team not in waitlist:
        return 0
    return waitlist.index(team) + 1
