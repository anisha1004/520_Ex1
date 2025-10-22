from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, return a tuple (sum, product).
    Empty sum is 0 and empty product is 1.

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([-1, 2, -3])
    (-2, 6)
    """
    total_sum = 0
    total_product = 1
    for x in numbers:
        total_sum += x
        total_product *= x
    return total_sum, total_product
