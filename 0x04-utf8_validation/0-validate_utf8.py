#!/usr/bin/python3
"""
UTF-8 Validation Module.
"""


def validUTF8(data):
    """
    Validate whether a given list of integers represents a sequence of
    valid UTF-8 encoded bytes.

    Args:
        data (list[int]): A list of integers representing byte values.

    Returns:
        bool: True if the data is a valid UTF-8 sequence, False otherwise.
    """
    num_bytes_to_process = 0
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        if num_bytes_to_process == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes_to_process += 1
                mask >>= 1

            if num_bytes_to_process == 0:
                continue

            if num_bytes_to_process == 1 or num_bytes_to_process > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes_to_process -= 1

    return num_bytes_to_process == 0
