from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, return a tuple consisting of the sum
    and the product of all the integers in the list.
    Empty sum should be 0 and empty product should be 1.

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Sum works naturally for empty lists (returns 0).
    total_sum = sum(numbers)

    # Product must start at 1; loop avoids potential issues with older Python versions without math.prod.
    total_product = 1
    for x in numbers:
        total_product *= x

    return total_sum, total_product

