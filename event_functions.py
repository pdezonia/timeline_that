"""
|<--------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|

event_functions.py
Defines functions for creating, editing, and removing events
of timeline.
by Philip deZonia
"""

def break_up_input(num_segments, input_string):
    """
    Converts a string into n segments using the first n spaces
    as breaks where n is the number of segments.
    Returns n segments.
    I just realized that there is a single python function for this.
    """
    pass

def add_event(event_year, event_group, event_desc, timeline):
    """
    Given event details, appends event to timeline then orders 
    timeline by year, then group.
    event_year and event_group are ints, event_desc is a string,
    timeline is a list.
    """
    timeline.append([event_year, event_group, event_desc])
    return sorted(timeline, key = lambda x: (x[0], x[1]))