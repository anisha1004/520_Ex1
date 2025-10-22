def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
     

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    # Use a generator expression for a memory-efficient and concise solution.
    # 1. `enumerate(lst)` provides each element's (index, value) pair.
    # 2. `if index % 2 == 0` filters for elements at even positions (0, 2, 4, ...).
    # 3. `and value % 2 != 0` further filters for elements whose value is odd.
    # 4. `sum()` adds the values that satisfy both conditions.
    return sum(value for index, value in enumerate(lst) if index % 2 == 0 and value % 2 != 0)

