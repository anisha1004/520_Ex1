def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    >>> greatest_common_divisor(0, 5)
    5
    >>> greatest_common_divisor(12, -18)
    6
    """
    # The Euclidean algorithm finds the GCD of two numbers.
    # The absolute value is taken to ensure the result is positive,
    # as GCD is conventionally a non-negative integer.
    a = abs(a)
    b = abs(b)
    
    while b:
        a, b = b, a % b
    return a

