"""Mutating functions."""

__author__ = "730544766"


def manual_append(list1: list[int], number: int) -> None:
    """Function 1."""
    list1.append(number)


a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(list2: list[int]) -> None:
    """Function 2."""
    position: int = 0
    while len(list2) > position:
        x = list2[position] * 2
        list2[position] = x
        position += 1


b: list[int] = [1, 2, 3]
double(b)
print(b)