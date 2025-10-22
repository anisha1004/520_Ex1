def rounded_avg(n, m):
    """Compute the average of all integers from n through m (inclusive),
    round to the nearest integer using Python's "bankers rounding" (round-half-to-even),
    and return the binary representation as a string. If n > m, return -1.

    Examples:
        >>> rounded_avg(1, 5)
        '0b11'
        >>> rounded_avg(7, 5)
        -1
        >>> rounded_avg(10, 20)
        '0b1111'
        >>> rounded_avg(20, 33)
        '0b11010'
    """
    if n > m:
        return -1

    s = n + m  # Average of consecutive integers n..m is (n + m) / 2
    if s % 2 == 0:
        avg_rounded = s // 2
    else:
        # Bankers rounding (round half to even) without using floats:
        lower = s // 2          # floor((n+m)/2)
        upper = lower + 1       # ceil((n+m)/2)
        avg_rounded = lower if lower % 2 == 0 else upper

    return bin(avg_rounded)

