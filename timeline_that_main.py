#!/usr/bin/env python3

"""
|<--------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|

timeline_that
by Philip deZonia
Made to help with planning out stories by adding and moving around events
Started on 10/3/20 (Fall) in Philadelphia
"""

import json

import output_functions
import event_functions

print("Welcome to Timeline That!")

# Initialize variables
# Each entry in list is of format [int, int, string]
timeline = []
# Use dummy list early on for testing
timeline = [[10000, 0, "War was beginning"],
            [10010, 1, "Paris trip"],
            [10005, 2, "mp3 players dominant"]]
keep_running = True

# Start main loop
while keep_running:
    # Create newlines for readability
    print("")
    print("")
    # Ask user to choose an action    
    print("Available actions:")
    print("0: exit program \t 1: print timeline \t 2: add event")
    user_choice = int(input("Choose an action: "))

    # Make corresponding action
    if user_choice == 0:
        keep_running = False
    elif user_choice == 1:
        prompt = ("Enter group numbers to print separated by spaces " +
                  "(use -1 to print all): ")
        groups_to_print = [int(group) for group in input(prompt).split()]
        print("")
        output_functions.print_timeline(groups_to_print, timeline)
    elif user_choice == 2:
        event_input = input("Enter year, group number, and description: ")
        [year, group, desc] = event_input.split(" ", 2)
        timeline = event_functions.add_event(int(year), int(group), desc, timeline)
    else:
        print("Invalid choice")


# End of program work
print("Program closed")