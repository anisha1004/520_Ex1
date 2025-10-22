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
    >>> correct_bracketing("")
    True
    >>> correct_bracketing("()()(()())")
    True
    >>> correct_bracketing("(()")
    False
    """
    balance = 0
    for bracket in brackets:
        if bracket == '(':
            balance += 1
        elif bracket == ')':
            balance -= 1
        
        # If balance is negative at any point,
        # it means a closing bracket appeared without a matching opening one.
        if balance < 0:
            return False
            
    # After checking all brackets, the balance must be exactly 0
    # for the string to be correctly bracketed.
    return balance == 0
