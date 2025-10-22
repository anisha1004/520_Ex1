def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2
        add([1, 2, 3, 4, 5, 6]) ==> 10 # 2 (at index 1) + 4 (at index 3) + 6 (at index 5)
        add([10, 20, 30, 40]) ==> 60 # 20 (at index 1) + 40 (at index 3)
        add([1, 3, 5, 7, 9]) ==> 0 # No even numbers
        add([2, 4, 6, 8, 10]) ==> 12 # 4 (at index 1) + 8 (at index 3)
    """
    # A generator expression is used for a concise and memory-efficient solution.
    # 1. `enumerate(lst)` gets each (index, value) pair.
    # 2. `if index % 2 != 0` filters for odd indices.
    # 3. `and value % 2 == 0` filters for even values.
    # 4. `sum(...)` adds up the values that pass both filters.
    return sum(value for index, value in enumerate(lst) if index % 2 != 0 and value % 2 == 0)
