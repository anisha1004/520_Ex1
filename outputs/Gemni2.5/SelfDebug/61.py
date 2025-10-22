def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # Bug 1: Only checking the final count. A naive implementation might simply
    # count the total number of '(' and ')' and return True if they are equal.
    # This would fail for cases like ")(" where the counts are equal, but the
    # order is incorrect. The correction is to use a running balance counter.
    # The balance must never become negative, which would indicate a closing
    # bracket appearing before an opening one.

    # Bug 2: Not checking for unmatched opening brackets at the end. An
    # implementation might correctly check for negative balances but fail to
    # verify that the final balance is zero. For an input like "((" or "(()",
    # the balance would never be negative, but the string is still invalid.
    # The correction is to return True only if the final balance is exactly 0
    # after the entire string has been processed.

    # Edge Case: Empty string. An empty string "" has no brackets, so it is
    # technically correctly bracketed. The loop will not run, the initial
    # balance of 0 will be maintained, and the function will correctly return
    # `balance == 0`, which is True.

    balance = 0
    for char in brackets:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        # If balance is negative at any point, it means a closing bracket
        # appeared without a corresponding open one.
        if balance < 0:
            return False
            
    # If the loop completes, the final balance must be zero for the
    # string to be correctly bracketed. A non-zero balance indicates
    # unmatched opening brackets.
    return balance == 0
