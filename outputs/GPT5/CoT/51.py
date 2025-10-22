def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns it without vowels (a, e, i, o, u; both cases).

    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\\nghijklm")
    'bcdf\\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = "aeiouAEIOU"
    return text.translate({ord(ch): None for ch in vowels})
