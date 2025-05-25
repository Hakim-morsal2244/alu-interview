#!/usr/bin/python3
"""
0-rain module
Calculate how much water is retained after raining.
"""


def rain(walls):
    """
    Calculate total units of water retained after raining.

    Args:
        walls (list): List of non-negative integers representing wall heights.

    Returns:
        int: Total amount of rainwater retained.
    """
    if not walls:
        return 0

    total_water = 0
    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                total_water += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                total_water += right_max - walls[right]
            right -= 1

    return total_water
