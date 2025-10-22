from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Correction for Bug 1 & Edge Case: Correctly initialize for an empty list.
    # The sum's identity is 0, and the product's identity is 1.
    # This ensures that if the 'numbers' list is empty, the loop is skipped
    # and the function correctly returns (0, 1).
    total_sum = 0
    total_product = 1

    for num in numbers:
        # Correction for Bug 2: Handle non-integer elements gracefully.
        # Raise a TypeError if an element is not an integer to prevent a crash
        # during the arithmetic operations and enforce the function's contract.
        if not isinstance(num, int):
            raise TypeError("All elements in the input list must be integers.")
        
        total_sum += num
        total_product *= num
        
    return (total_sum, total_product)

