"""
|<--------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|

output_functions.py
Defines functions for getting timelines out there into the world
of timeline
by Philip deZonia
"""

def print_timeline(groups_to_print, timeline):
    """
    Given a timeline (list) and a list of groups in that timeline
    to print, prints all events with their year and description, 
    pretty formatting included. Assumes list is ordered properly.
    """
    print("Year \t Description")
    for entry in timeline:
        if entry[1] in groups_to_print or -1 in groups_to_print:
            year = entry[0]
            desc = entry[2]
            print(f"{year} \t {desc}")