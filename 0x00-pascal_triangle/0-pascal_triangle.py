#!/usr/bin/python3
"""Pascal Triangle Generator"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Parameters:
    n (int): The number of rows in Pascal's triangle to generate.

    Returns:
    List[List[int]]: A list of lists of integers representing
    Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [sum(pair) for pair in zip(last_row, last_row[1:])]
        row.append(1)
        triangle.append(row)
    return triangle
