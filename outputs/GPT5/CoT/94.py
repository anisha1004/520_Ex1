def skjkasdkd(lst):
    """Return the sum of digits of the largest prime value in the list.
    If the list contains no primes, return 0.
    """
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True  # 2, 3
        if n % 2 == 0 or n % 3 == 0:
            return n in (2, 3)  # catches even/3-multiples > 3
        i = 5
        # Check factors of form 6k ± 1 up to sqrt(n)
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    max_prime = None
    for n in lst:
        if n > 1 and is_prime(n):
            if max_prime is None or n > max_prime:
                max_prime = n

    if max_prime is None:
        return 0

    return sum(int(d) for d in str(max_prime))

