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

def reorder_timeline(timeline):
    """
    Given a timeline, sorts entries by year then group number.
    timeline is a list.
    Returns a new timeline
    """
    return sorted(timeline, key = lambda x: (x[0], x[1]))

def get_list_column(col_ind, grid_list):
    """
    Returns the specified column of a 2d list.
    """
    return [grid_list[i][col_ind] for i in range(len(grid_list))]

def find_matching_inds(search_val, search_list):
    return [i for i, x in enumerate(search_list) if x == search_val]

def find_event(event_year, event_group, timeline):
    """
    Given an event year and group number, returns the list index of that
    event in the main timeline.
    event_year, event_group are ints, timeline is a 2d list.
    returns a row index in timeline (an int)
    """
    # Filter by year
    y_match_rows = find_matching_inds(event_year, get_list_column(0, timeline))
    print(f"get_list_column: {get_list_column(0, timeline)}")
    print(f"y_match_rows: {y_match_rows}")
    # Check if one row was found, if not filter by group as well
    if len(y_match_rows) == 1:
        print("in unique case")
        print(y_match_rows[0])
        return_row = y_match_rows[0]
    else:
        # Filter just by group
        g_match_rows = find_matching_inds(event_group, get_list_column(1, timeline))
        # Find overlap between two filters
        y_row_set = set(y_match_rows)
        g_row_set = set(g_match_rows)
        print("in else")
        print(y_match_rows, g_match_rows)
        print(y_row_set & g_row_set)
        return_ind_set = y_row_set & g_row_set
        popped_return_ind = return_ind_set.pop()
        print(popped_return_ind)
        return_row = popped_return_ind
    
    return return_row

def add_event(event_year, event_group, event_desc, timeline):
    """
    Given event details, appends event to timeline then orders 
    timeline by year, then group.
    event_year and event_group are ints, event_desc is a string,
    timeline is a list.
    Returns a new timeline
    """
    timeline.append([event_year, event_group, event_desc])
    return reorder_timeline(timeline)

def move_event(old_event_year, event_group, new_event_year, timeline):
    """
    Given event details and a target year, changes year of event, then
    reorders timeline.
    old_event_year, new_event_year, and event_group are all ints,
    timeline is a list.
    Returns a new timeilne
    """
    print(get_list_column(0, timeline))
    event_ind = find_event(old_event_year, event_group, timeline)
    print(event_ind)