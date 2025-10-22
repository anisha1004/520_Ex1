def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    
    # Bug 3 Correction: Handle repeated factors (like 2 in 2048) by
    # repeatedly dividing by the same factor until it's no longer possible.
    # Start with the smallest prime, 2.
    while n % 2 == 0:
        # If n is 2, this will be the last step.
        if n == 2:
            return 2
        n //= 2
        
    # At this point, n must be odd. We can now iterate through odd numbers.
    # Start with the next prime, 3.
    factor = 3
    
    # Bug 1 Correction: Only iterate up to the square root of the remaining n.
    # If a larger prime factor existed, its corresponding smaller factor would
    # have already been found and divided out.
    while factor * factor <= n:
        # Repeatedly divide by the current factor.
        if n % factor == 0:
            n //= factor
        else:
            # Only move to the next odd number if division is not possible.
            factor += 2
            
    # Bug 2 Correction: After the loop, the remaining value of n is guaranteed
    # to be the largest prime factor. For example, for n=77, the loop divides
    # by 7, leaving n=11. The loop terminates, and we must return the remaining n.
    return n

