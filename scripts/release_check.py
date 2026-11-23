"""Release check: run after each deploy with the deployed folder (course starter app)."""
import os
import sys

release, environment = sys.argv[1], sys.argv[2]
sys.path.insert(0, release)  # import the deployed files, not the repository's

from settings import ROOM_HOURS_PER_DAY
from rooms import hours_left
from waitlist import waitlist_position

print(f"Release check: {environment}")
print(open(os.path.join(release, "BUILD_INFO.txt")).read().strip())
print("Bookable room hours per day:", ROOM_HOURS_PER_DAY)
print("Open room hours with 18 booked:", hours_left(ROOM_HOURS_PER_DAY, 18))
print("Place in line of the first on the waitlist:", waitlist_position(["Robins", "Falcons"], "Robins"))
print("Release check finished.")
