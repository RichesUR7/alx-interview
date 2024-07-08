#!/usr/bin/python3
"""
Module for calculating minimum operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): The number of H characters to achieve

    Returns:
        int: The minimum number of operations
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
