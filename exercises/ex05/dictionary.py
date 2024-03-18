"""Dictionary Assignment."""

__author__ = "730544766"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Function 1."""
    dict2: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in dict2:
            raise KeyError("error multiple of the same key!")
        dict2[dict1[key]] = key
    return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """Function 2."""
    dict2: dict[str, int] = {}
    result: str = ""
    highest_number: int = 0
    for key in dict1:
        if dict1[key] in dict2:
            dict2[dict1[key]] += 1
        else:
            dict2[dict1[key]] = 1
    for key in dict2:
        if dict2[key] > highest_number:
            highest_number = dict2[key]
            result = key
    return result


def count(list1: list[str]) -> dict[str, int]:
    """Function 3."""
    dict1: dict[str, int] = {}
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1
    return dict1


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Function 4."""
    dict1: dict[str, list[str]] = {}
    for elem in list1:
        if elem[0].lower() in dict1:
            dict1[elem[0].lower()] += [elem]
        else:
            dict1[elem[0].lower()] = [elem]
    return dict1


def update_attendance(dict1: dict[str, list[str]], day: str, name: str) -> None:
    """Fuction 5."""
    for key in dict1:
        if key == day and [name] != dict1[day]:
            dict1[key] += [name]
    if day not in dict1:
        dict1[day] = [name]