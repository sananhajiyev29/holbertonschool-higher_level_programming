#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.

    Returns a new list of True or False for each element:
    True if the element is divisible by 2, False otherwise.
    """
    result = []

    for i in my_list:
        result.append(i % 2 == 0)

    return result
