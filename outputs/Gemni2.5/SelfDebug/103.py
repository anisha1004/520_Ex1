def rounded_avg(n: int, m: int):
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
    
    # Handle the primary invalid case where the start is greater than the end.
    if n > m:
        return -1

    # Bug 1 Correction: Use a direct mathematical formula for the average
    # of a consecutive sequence of integers. This is O(1) and avoids creating
    # a potentially huge list in memory, which would be inefficient and could
    # cause a MemoryError for large n and m.
    # Bug 3 Correction: Ensure float division '/' is used, not integer '//',
    # to preserve the decimal part for correct rounding.
    average = (n + m) / 2
    
    # Bug 2 Correction: Use Python's standard round() function. The examples
    # confirm that its "round half to even" behavior is the desired logic.
    # For example, (20+33)/2 = 26.5, which round() correctly rounds to 26.
    rounded_value = round(average)
    
    # Convert the final integer to its binary string representation.
    return bin(rounded_value)
