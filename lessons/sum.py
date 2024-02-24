"""Summing the elements of a list using different loops!"""

__author__ = "730544766"


def w_sum(vals: list[float]) -> float:
    """Part 1!"""
    index = 0
    total = 0.0
    while len(vals) > index:
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Part 2!!"""
    total = 0.0
    for numbers in vals:
        total += numbers
    return total


def f_range_sum(vals: list[float]) -> float:
    """Part 3!!!"""
    total = 0.0
    for idx in range(0, len(vals)):
        total += float(vals[idx])
    return total