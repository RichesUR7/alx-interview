#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins
needed to meet a given amount total.

The function `makeChange` takes a list of coin values and a total amount,
and returns the minimum number of coins needed to make up that amount. If
it's not possible to make that total with the given coins, the function
returns -1.
"""

from collections import deque


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (List[int]): The values of the coins in possession.
        total (int): The total amount to be achieved.

    Returns:
        int: The fewest number of coins needed to meet total, or -1 if it
        cannot be met.
    """
    if total <= 0:
        return 0

    # Sort coins to improve efficiency
    coins.sort()

    # Initialize the queue for BFS
    queue = deque([(0, 0)])  # (current sum, number of coins used)
    visited = set([0])  # To avoid revisiting the same sum

    while queue:
        current_sum, num_coins = queue.popleft()

        # Try to add each coin to the current sum
        for coin in coins:
            new_sum = current_sum + coin

            if new_sum == total:
                return num_coins + 1
            if new_sum > total:
                break
            if new_sum not in visited:
                visited.add(new_sum)
                queue.append((new_sum, num_coins + 1))

    return -1
