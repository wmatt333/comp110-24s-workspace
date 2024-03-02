"""Splitting a dictionary into two lists."""

__author__ = "730544766"


def get_keys(dictionary: dict[str, int]) -> list[str]:
    """Function 1."""
    total: list[str] = []
    for keys in dictionary:
        total.append(keys)
    return total


def get_values(dictionary: dict[str, int]) -> list[int]:
    """Function 2."""
    total: list[int] = []
    for keys in dictionary:
        total.append(dictionary[keys])
    return total