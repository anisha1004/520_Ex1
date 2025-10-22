from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst, add the even elements that are at odd indices.

    Examples:
        >>> add([4, 2, 6, 7])
        2
        >>> add([1])
        0
        >>> add([1, 4, 3, 8])
        12
        >>> add([0, 1, 2, 3])
        0
        >>> add([-2, -4, -6, -8])  # odd indices: -4 and -8 (both even)
        -12
    """
    # Sum values at odd indices (1, 3, 5, ...) that are even
    return sum(v for i, v in enumerate(lst) if i % 2 == 1 and v % 2 == 0)

