def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b.

    Uses the Euclidean algorithm and returns a non-negative result.
    For a = b = 0, returns 0.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    >>> greatest_common_divisor(-24, 18)
    6
    >>> greatest_common_divisor(0, 7)
    7
    >>> greatest_common_divisor(0, 0)
    0
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
