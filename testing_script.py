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

# Use dummy list for testing
timeline = [[10000, 0, "War was beginning"],
            [10005, 1, "mp3 players dominant"],
            [10010, 2, "Paris trip"]]

# Test printing list
print("\n\noriginal list, all groups, print check")
of.print_timeline([-1], timeline)
print("original list, AYBABTU group, print check")
of.print_timeline([0], timeline)
print("original list, music player group, print check")
of.print_timeline([1], timeline)
print("original list, personal travel group, print check")
of.print_timeline([2], timeline)

# Test adding an event
print("\nAdding an event to AYBABTU timeline")
timeline = ef.add_event(10005, 0, "What happened?", timeline)
print("all groups, add event check")
of.print_timeline([-1], timeline)

# Test event finder
print("\nFinding event with unique year in AYBABTU timeline")
find_row = ef.find_event(10000, 0, timeline)
print(f"Row found: {find_row}")
print("Finding event with nonunique year in AYBABTU timeline")
find_row = ef.find_event(10005, 0, timeline)
print(f"Row found: {find_row}")
print("Finding event with nonunique year in MP3 timeline")
find_row = ef.find_event(10005, 1, timeline)
print(f"Row found: {find_row}")