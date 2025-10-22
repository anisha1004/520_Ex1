def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    Works for any n > 1.

    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    >>> largest_prime_factor(72)
    3
    >>> largest_prime_factor(99991 * 37)
    99991
    """
    # Remove factors of 2 first
    last_factor = 1
    while n % 2 == 0:
        last_factor = 2
        n //= 2
    # Now n is odd; test odd factors up to sqrt(n), shrinking n as we find factors
    f = 3
    while f * f <= n:
        while n % f == 0:
            last_factor = f
            n //= f
        f += 2
    # If n > 1, it's a prime factor larger than sqrt(original n)
    return n if n > 1 else last_factor
