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
    # Filter by group
    g_match_rows = find_matching_inds(event_group, get_list_column(1, timeline))
    # Check if one row was found, if not filter by group as well
    # if len(y_match_rows) == 1:
    #     return_row = y_match_rows[0]
    if len(y_match_rows) == 0 or len(g_match_rows) == 0:
        # If no entry exists, return special number to show it
        # print("In len = 0 statement of find_event")
        # print(y_match_rows)
        return_row = -1
    else:
        # Find overlap between two filters
        # print(y_match_rows, g_match_rows)
        yg_match_rows = [x for x in y_match_rows if x in g_match_rows]
        if len(yg_match_rows) == 0:
            return_row = -1
        else:
            return_row = yg_match_rows[0] # Take sole element in list
    
    return return_row

def add_event(event_year, event_group, event_desc, timeline):
    """
    Given event details, appends event to timeline then orders 
    timeline by year, then group.
    event_year and event_group are ints, event_desc is a string,
    timeline is a list.
    Returns a new timeline and success code if there were no
    conflicts.
    """
    if find_event(event_year, event_group, timeline) == -1:
        timeline.append([event_year, event_group, event_desc])
        was_successful = 1
    else:
        was_successful = 0
        
    return  was_successful, reorder_timeline(timeline)

def remove_event(event_year, event_group, timeline):
    """
    Given event year and group, removes event from timeline.
    event_year, event_group are ints
    timeline is 2-D list
    Returns a new timeline and success code if event was successfully
    removed.
    """
    # print("before removing event")
    # print(timeline)
    remove_row = find_event(event_year, event_group, timeline)
    if remove_row != -1:
        timeline.remove(timeline[remove_row])
        was_successful = 1
    else:
        was_successful = 0
    
    # print("after removing event")
    # print(timeline)

    return was_successful, timeline

def move_event(old_event_year, event_group, new_event_year, timeline):
    """
    Given event details and a target year, changes year of event, then
    reorders timeline.
    old_event_year, new_event_year, and event_group are all ints,
    timeline is a list.
    Returns a new timeilne and a 1 if successful or the original
    timeline and a 0 if not.
    """
    # print(get_list_column(0, timeline))
    event_ind = find_event(old_event_year, event_group, timeline)
    # Check if there already exists an entry with same year-group info
    if find_event(new_event_year, event_group, timeline) != -1:
        # print(f"found events: {find_event(new_event_year, event_group, timeline)}")
        was_successful = 0
    else:
        was_successful = 1
        print(event_ind)
        timeline[event_ind][0] = new_event_year
        timeline = reorder_timeline(timeline)

    # Return success code for use in bulk mover
    return was_successful, timeline

def bulk_move_events(lower_bound, upper_bound, group_list, year_offset, timeline):
    """
    Given a timespan and group numbers, moves all events of given groups 
    within the timespan (including bounds) by given year offset.
    lower_bound, upper_bound, and year offset are ints
    group_list is a 1-D list
    timeline is a 2-D list
    positive timeoffset moves events forward in time; negative, backwards
    Returns a new timeline and 1 if successful and a 0 if not.
    """
    backup_timeline = timeline
    year_list = get_list_column(0, timeline)
    was_successful = 0
    # Determine which direction to move through list, starting from end 
    # if moving events forwards, starting from beginning otherwise
    if year_offset < 0:
        range_bounds = (0, len(year_list), 1)
    elif year_offset > 0:
        range_bounds = (len(year_list) - 1, -1, -1)
    for i in range(range_bounds[0], range_bounds[1], range_bounds[2]):
        is_in_range = year_list[i] > lower_bound and year_list[i] < upper_bound
        is_in_group = timeline[i][1] in group_list or -1 in group_list
        if is_in_range and is_in_group:
            old_year = timeline[i][0]
            event_group = timeline[i][1]
            new_event_year = old_year + year_offset
            was_successful, timeline = move_event(old_year, event_group, 
                                                  new_event_year, timeline)
            # Abort program if we encounter a single year-group clash
            # print(f"On {i}, was successful = {was_successful}")
            if not was_successful:
                timeline = backup_timeline
                break
    
    return was_successful, timeline