#!/usr/bin/python3
"""
This module contains a function that checks if all boxes can be opened.

A box is represented as a list of keys, and a key is represented as an integer.
A key can open the box with the same number as the key.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Parameters:
    boxes (list of list of int): The boxes with their keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    total_boxes = len(boxes)
    unlocked = [False] * total_boxes
    unlocked[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < total_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
