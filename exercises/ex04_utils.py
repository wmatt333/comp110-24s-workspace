"""List utils."""

__author__ = 720310785

def all(inp: list[int], val: int) -> bool:
    """Tell if list is all one number."""
    idx: int = 0
    while idx < len(inp):
        if val != inp[idx]:
            return False
        idx += 1
    return True

def max(inp: list[int]) -> int:
    """Find max in list."""
    idx: int = 0
    if len(inp) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = inp[0]
    while idx < len(inp):
        if inp[idx] > max_num:
            max_num = inp[idx]
        idx += 1
    return max_num

def is_equal(inp1: list[int], inp2: list[int]) -> bool:
    """Check if two lists are equal."""

    if len(inp1) != len(inp2):
        return False
    else:
        idx: int = 0
        while idx < len(inp1):
            if inp1[idx] != inp2[idx]:
                return False
            idx += 1
    return True

def extend(inp1: list[int], inp2: list[int]) -> None:
    idx: int = 0
    while idx < len(inp2):
        inp1.append(inp2[idx])
        idx += 1
