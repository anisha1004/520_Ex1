def remove_vowels(text: str) -> str:
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
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
    # This solution uses a generator expression within the ''.join() method.
    # 1. It iterates through each character ('char') in the input 'text'.
    # 2. For each 'char', it converts it to lowercase (char.lower()) and checks
    #    if it is NOT in the string of vowels 'aeiou'.
    # 3. If the character is not a vowel, it is included in the generator.
    # 4. ''.join() efficiently concatenates all the yielded characters
    #    from the generator into the final result string.
    return "".join(char for char in text if char.lower() not in 'aeiou')


