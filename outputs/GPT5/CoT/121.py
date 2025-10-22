def solution(lst):
    """Given a non-empty list of integers, return the sum of all odd elements at even indices (0-based).

    Examples:
    >>> solution([5, 8, 7, 1])
    12
    >>> solution([3, 3, 3, 3, 3])
    9
    >>> solution([30, 13, 24, 321])
    0
    >>> solution([-5, 2, -7, 4])
    -12
    """
    return sum(x for x in lst[::2] if x & 1)

