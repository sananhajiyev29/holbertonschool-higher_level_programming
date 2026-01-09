#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.

    Returns the modified list.
    If idx is negative or out of range, return the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    return my_list[:idx] + my_list[idx + 1:]
