#!/usr/bin/env python3

"""
|<--------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|

testing_script
by Philip deZonia
Runs various tests
"""

import output_functions as of
import event_functions as ef

base_group = 0
music_group = 1
trip_group = 2
# Use dummy list for testing
timeline = [[10000, base_group, "War was beginning"],
            [10005, music_group, "mp3 players dominant"],
            [10010, trip_group, "Paris trip"]]

# Test printing list
print("\n\noriginal list, all groups, print check")
of.print_timeline([-1], timeline)
print("original list, AYBABTU group, print check")
of.print_timeline([base_group], timeline)
print("original list, music player group, print check")
of.print_timeline([music_group], timeline)
print("original list, personal travel group, print check")
of.print_timeline([trip_group], timeline)

# Test adding an event
print("\nAdding an event to AYBABTU timeline")
was_successful, timeline = ef.add_event(10005, base_group, "What happened?", timeline)
print(f"Was it succesful? {was_successful}, expected 1")
print("all groups, add event check")
of.print_timeline([-1], timeline)
print(f"Attempting to add event with same year-group info")
was_successful, timeline = ef.add_event(10005, base_group, 
                                         "Something's wrong", timeline)
print(f"Was it succesful? {was_successful}, expected 0")
print("all groups, add event check")
of.print_timeline([-1], timeline)

# Test event finder
print("\nFinding event with unique year in AYBABTU timeline")
find_row = ef.find_event(10000, base_group, timeline)
print(f"Row found: {find_row}, expected 0")
print("Finding event with nonunique year in AYBABTU timeline")
find_row = ef.find_event(10005, base_group, timeline)
print(f"Row found: {find_row}, expected 1")
print("Finding event with nonunique year in MP3 timeline")
find_row = ef.find_event(10005, music_group, timeline)
print(f"Row found: {find_row}, expected 2")
print("Attempting to find event that doesn't exist")
find_row = ef.find_event(20000, trip_group, timeline)
print(f"Row found: {find_row}, expected -1")

# Test event mover
print("\nMoving event in AYBABTU timeline from 10005 to 10010")
was_successful, timeline = ef.move_event(10005, base_group, 10010, timeline)
of.print_timeline([-1], timeline)
print(f"Was it succesful? {was_successful}, expected 1")
print("Expected output order: wwb, mpd, wh, pt")
print("Attempting to move event in AYBABTU timeline from 10010 to 10000")
was_successful, timeline = ef.move_event(10010, base_group, 10000, timeline)
of.print_timeline([-1], timeline)
print(f"Was it succesful? {was_successful}, expected 0")
print("Expected output order: wwb, mpd, wh, pt")

# Add some events for next test
was_successful, timeline = ef.add_event(10015, 0, "Someone set us up the bomb", 
                                        timeline)
was_successful, timeline = ef.add_event(10012, 1, "Pandora radio is a thing", 
                                        timeline)
was_successful, timeline = ef.add_event(10020, 2, "Japan trip", timeline)
print("Added 3 events")
print("All groups")
of.print_timeline([-1], timeline)

# Test event bulk mover
print("\nBulk moving events ...")
x = range(0, 10)
print(x[0], x[9])
x = range(9, -1)
print(x[0], x[9])