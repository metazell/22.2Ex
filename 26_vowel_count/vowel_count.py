def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = "aeiou"
    frequency = {}

    for char in phrase.lower():
        if char in vowels:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency

print("vowel_count('rithm school') returned", vowel_count('rithm school'))  # Expected output: {'i': 1, 'o': 2}
print("vowel_count('HOW ARE YOU? i am great!') returned", vowel_count('HOW ARE YOU? i am great!'))  # Expected output: {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
print("vowel_count('') returned", vowel_count(''))  # Expected output: {}