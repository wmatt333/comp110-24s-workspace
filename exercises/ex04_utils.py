"""List Utility Functions."""

__author__ = "730544766"


def all(numbers_list: list[int], check: int) -> bool:
    """Function 1."""
    for numbers in numbers_list:
        if numbers != check:
            return False
            quit()
    return True
    

def max(input: list[int]) -> int:
    """Function 2."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    high = 0
    for numbers in input:
        if numbers > high:
            high = numbers
    return high


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function 3."""
    if len(list1) != len(list2):
        return False
        quit()
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
            quit()
        index += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Function 4."""
    for numbers in list2:
        list1.append(numbers)
    print(list1)