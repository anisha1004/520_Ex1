def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
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
    # Use str.translate for efficiency and to preserve all non-vowel characters (including newlines and punctuation).
    # Handles both lowercase and uppercase vowels; leaves other Unicode characters unchanged.
    vowel_table = {ord(c): None for c in "aeiouAEIOU"}
    return text.translate(vowel_table)
