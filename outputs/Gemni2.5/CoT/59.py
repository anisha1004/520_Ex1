def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    >>> largest_prime_factor(600851475143)
    6857
    """
    largest_factor = -1

    # Divide out all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # n must be odd at this point.
    # Iterate through odd numbers starting from 3 up to sqrt(n).
    d = 3
    while d * d <= n:
        # While d is a factor, divide it out
        while n % d == 0:
            largest_factor = d
            n //= d
        d += 2

    # If n is still greater than 2 at the end, the remaining n is a prime factor.
    # This happens if the largest prime factor is > sqrt of the original n.
    if n > 2:
        largest_factor = n
        
    return largest_factor
