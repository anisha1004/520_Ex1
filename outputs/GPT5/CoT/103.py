def rounded_avg(n, m):
    """Compute the average of all integers from n through m (inclusive),
    round to the nearest integer (Python's rounding rules), and return its binary
    representation as a string prefixed with '0b'. If n > m, return -1.

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
    avg_rounded = round((n + m) / 2)
    return bin(avg_rounded)
