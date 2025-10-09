from ics import Calendar
from collections import defaultdict
from datetime import datetime
import sys

# Replace 'your_calendar.ics' with your file path
ics_file_path = 'petsit.ics'

# Read and parse the calendar file
with open(ics_file_path, 'r', encoding='utf-8') as f:
    calendar = Calendar(f.read())

# Count events per day
events_per_day = defaultdict(int)

for event in calendar.events:
    event_date = event.begin.date()
    events_per_day[event_date] += 1

# Output the results
for date in sorted(events_per_day):
    print(f"{date}, {events_per_day[date]}")
