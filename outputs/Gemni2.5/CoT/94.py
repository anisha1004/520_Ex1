def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    def is_prime(n):
        """
        An efficient helper function to check if a number is prime.
        It handles non-integers and numbers less than 2, then uses an
        optimized loop that checks divisors of the form 6k ± 1.
        """
        # A prime must be an integer and greater than 1.
        if not isinstance(n, int) or n <= 1:
            return False
        # 2 and 3 are prime.
        if n <= 3:
            return True
        # Numbers divisible by 2 or 3 are not prime (excluding 2 and 3 themselves).
        if n % 2 == 0 or n % 3 == 0:
            return False
        # Check for prime factors of the form 6k ± 1 up to sqrt(n).
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    try:
        # Use a generator expression for memory efficiency.
        # It finds the largest prime without storing all primes in a list.
        largest_prime = max(num for num in lst if is_prime(num))
    except ValueError:
        # This block executes if the generator is empty (no primes found in lst),
        # in which case max() raises a ValueError.
        return 0
    
    # Convert the largest prime to a string to iterate over its digits,
    # convert each digit character back to an int, and sum them up.
    return sum(int(digit) for digit in str(largest_prime))
