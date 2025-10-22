def remove_vowels(text: str) -> str:
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    # Bug 1 Correction: Define a set of both uppercase and lowercase vowels
    # for a case-insensitive check. Using a set provides fast O(1) lookups.
    vowels = "aeiouAEIOU"
    
    # Bug 2 Correction: Use a generator expression with ''.join(). This is highly
    # efficient as it avoids creating an intermediate list in memory and avoids
    # the O(n^2) complexity of repeated string concatenation.
    # Edge Case 3 is also handled correctly, as any character not in the
    # 'vowels' set (including numbers, punctuation, newlines, etc.) will be kept.
    return "".join(char for char in text if char not in vowels)
