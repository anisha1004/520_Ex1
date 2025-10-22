def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b.
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    >>> greatest_common_divisor(0, 0)
    0
    >>> greatest_common_divisor(-12, 18)
    6
    """
    # Handle the special case where both numbers are zero.
    if a == 0 and b == 0:
        return 0

    # Work with non-negative values for correctness with negatives.
    a, b = abs(a), abs(b)

    # Euclidean algorithm.
    while b != 0:
        a, b = b, a % b
    return a
