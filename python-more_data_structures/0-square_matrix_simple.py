#!/usr/bin/python3
"""
0-square_matrix_simple.py
Contains a function to compute the square of all integers in a matrix
"""


def square_matrix_simple(matrix=[]):
    """
    Compute the square of all integers in a 2D matrix.

    Args:
        matrix (list of lists of int): The input 2D array

    Returns:
        list of lists of int: New matrix with squared values
    """
    return [[x ** 2 for x in row] for row in matrix]
