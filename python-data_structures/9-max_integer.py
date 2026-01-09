#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Return the biggest integer in a list.

    If the list is empty, return None.
    """
    if len(my_list) == 0:
        return None

    max_val = my_list[0]

    for i in my_list:
        if i > max_val:
            max_val = i

    return max_val
