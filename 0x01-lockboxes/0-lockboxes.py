#!/usr/bin/python3
"""loocked"""


def canUnlockAll(boxes):
    """
    Check if it's possible to unlock all the boxes based on a set of keys.

    Parameters:
    - boxes : A list of lists.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    """
    keys_collected = set()
    boxes_count = len(boxes)
    keys_count = 0

    for key in boxes[0]:
        if key not in keys_collected and 0 < key < boxes_count:
            keys_collected.add(key)
            keys_count += 1

    index = 0
    while index < len(keys_collected):
        current_key = keys_collected.pop()
        for key in boxes[current_key]:
            if key not in keys_collected and 0 < key < boxes_count:
                keys_collected.add(key)
                keys_count += 1
        index += 1

    return keys_count == boxes_count - 1

