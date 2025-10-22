def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Bug 1 & 2 Correction: Handle negative inputs and ensure the
    # result is always non-negative, which is the standard
    # mathematical convention for GCD. This also correctly handles
    # one of the inputs being zero (e.g., gcd(-10, 0) -> 10).
    a = abs(a)
    b = abs(b)

    # The Euclidean algorithm to find the GCD.
    # It iteratively uses the property that gcd(a, b) = gcd(b, a % b).
    # The loop terminates when b becomes 0, at which point a is the GCD.
    while b:
        a, b = b, a % b
    
    return a
