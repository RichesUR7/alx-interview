#!/usr/bin/python3
"""
A module contains a function to rotate a 2D Matrix 90 degrees.
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Args:
        matrix (list of list of int): 2D matrix to rotate.

    The matrix must be edited in-place.
    """

    # transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    # for i in range(n):
    #     matrix[i].reverse()

    # reverse each row using list comprehension
    matrix[:] = [row[::-1] for row in matrix]
