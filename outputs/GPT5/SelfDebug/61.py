def correct_bracketing(brackets: str) -> bool:
    """brackets is a string of '(' and ')'.
    Return True if every opening bracket has a corresponding closing bracket and order is valid.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    >>> correct_bracketing("")
    True
    """
    # Edge cases & potential pitfalls considered and addressed:
    # 1) Early closing: if at any point closes exceed opens, it's invalid -> return False immediately.
    # 2) Final balance: after scanning all chars, count must be zero (all opens closed).
    # 3) Non-parenthesis characters: though spec says only '(' and ')', guard by returning False if others appear.
    count = 0
    for ch in brackets:
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1
            if count < 0:  # more closing than opening at some point
                return False
        else:
            return False  # invalid character
    return count == 0
