"""Functions that implement sorting algorithms."""


__author__ = "730544766"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    counter1: int = len(x) - 1
    counter2: int = len(x) - 2
    while counter1 > -1:
        while counter2 > -1:
            min: int = x[counter1]
            if min < x[counter2]:
                value: int = x[counter2]
                x[counter2] = x[counter1]
                x[counter1] = value
                counter2 -= 1
            else:
                counter2 -= 1
        counter1 -= 1
        counter2 = counter1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    counter1: int = 0
    counter2: int = 0
    while counter1 < len(x):
        while counter2 < len(x):
            if x[counter1] > x[counter2]:
                value: int = x[counter2]
                x[counter2] = x[counter1]
                x[counter1] = value
                counter2 += 1
            else:
                counter2 += 1
        counter1 += 1
        counter2 = counter1
    return None
