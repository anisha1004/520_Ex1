def add(lst):
    """Given a non-empty list of integers, return the sum of the even elements located at odd indices.

    Examples:
        >>> add([4, 2, 6, 7])
        2
        >>> add([0])
        0
        >>> add([1, 4, 3, 8, 5, 10])
        22
        >>> add([2, -4, 6, -8])
        -12
    """
    return sum(x for x in lst[1::2] if x % 2 == 0)

