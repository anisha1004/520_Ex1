def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    >>> largest_prime_factor(27)
    3
    >>> largest_prime_factor(2 * 3 * 5 * 97)
    97
    """
    # Ensure we work with positive integers
    n = abs(n)

    # Strip out factors of 2 first
    max_pf = 1
    while n % 2 == 0:
        max_pf = 2
        n //= 2

    # Now n is odd; test odd divisors up to sqrt(n), updating sqrt bound as n shrinks
    f = 3
    while f * f <= n:
        if n % f == 0:
            max_pf = f
            while n % f == 0:
                n /= f
            n = int(n)
        f += 2

    # If at the end n > 1, it is a prime factor larger than any tested
    if n > 1:
        max_pf = int(n)

    return max_pf
