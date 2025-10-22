def correct_bracketing(brackets: str) -> bool:
    """Return True if every '(' has a corresponding ')' and no prefix is invalid.

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
    balance = 0
    for ch in brackets:
        if ch == '(':
            balance += 1
        elif ch == ')':
            if balance == 0:
                return False
            balance -= 1
        else:
            # If any unexpected character appears, treat as invalid.
            return False
    return balance == 0

