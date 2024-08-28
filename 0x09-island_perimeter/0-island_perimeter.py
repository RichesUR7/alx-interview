#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): A list of lists of integers
        representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    return sum(
        4 - 2 * (r > 0 and grid[r - 1][c]) - 2 * (c > 0 and grid[r][c - 1])
        for r in range(len(grid))
        for c in range(len(grid[0]))
        if grid[r][c] == 1
    )
