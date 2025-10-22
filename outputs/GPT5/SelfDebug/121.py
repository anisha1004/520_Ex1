from typing import List

def solution(lst: List[int]) -> int:
    """Given a non-empty list of integers, return the sum of all odd elements that are in even positions (0-based).

    Even positions: indices 0, 2, 4, ...

    Examples
    >>> solution([5, 8, 7, 1])
    12
    >>> solution([3, 3, 3, 3, 3])
    9
    >>> solution([30, 13, 24, 321])
    0
    >>> solution([-5, 2, -7, 4])  # odd elements at even indices: -5 and -7
    -12
    >>> solution([])  # Though problem says non-empty, handle gracefully
    0
    """
    # Sum values at even indices (0, 2, 4, ...) that are odd.
    # Using v % 2 != 0 works for negatives as well in Python.
    return sum(v for i, v in enumerate(lst) if i % 2 == 0 and v % 2 != 0)
