from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([1, 1, 1])
    (3, 1)
    >>> sum_product([10, 0, 10])
    (20, 0)
    """
    # The sum of an empty list is 0 by definition, which sum() handles.
    total_sum = sum(numbers)

    # The product of an empty list is 1 (the multiplicative identity).
    # Initialize the product to 1 to handle the empty list case correctly.
    total_product = 1
    for number in numbers:
        total_product *= number
        
    return (total_sum, total_product)
