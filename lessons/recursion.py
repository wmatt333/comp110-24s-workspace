"""Writing a Recursive Function."""

__author__ = "730544766"


def f(n: int, k: int) -> int:
    """Recursion function that adds k each time."""
    if n == 0:
        return n
    else:
        return f(n - 1, k) + k