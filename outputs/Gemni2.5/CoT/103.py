def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.

    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    # Step 1: Handle the edge case where the range is invalid.
    if n > m:
        return -1

    # Step 2: Calculate the average of the arithmetic series.
    # The average of a sequence of numbers in an arithmetic progression
    # is simply the average of the first and last terms.
    # This is more efficient than summing all numbers and then dividing.
    average = (n + m) / 2

    # Step 3: Round the average to the nearest integer.
    # Python's built-in round() function handles this correctly,
    # rounding .5 cases to the nearest even integer (e.g., round(2.5) -> 2).
    rounded_value = round(average)

    # Step 4: Convert the rounded integer to its binary string representation.
    # The bin() function returns a string prefixed with "0b".
    return bin(rounded_value)

