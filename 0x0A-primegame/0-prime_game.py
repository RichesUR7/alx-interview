#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the overall winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the rounds.

    Returns:
        str: The name of the winner ('Maria' or 'Ben') or None if it's a tie.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    scores = {"Maria": 0, "Ben": 0}

    for n in nums:
        prime_count = sum(is_prime[: n + 1])
        if prime_count % 2 == 0:
            scores["Ben"] += 1
        else:
            scores["Maria"] += 1

    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    if scores["Ben"] > scores["Maria"]:
        return "Ben"
    return None
