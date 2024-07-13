def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    to_swap = to_swap.lower()
    result = []
    
    for char in phrase:
        if char.lower() == to_swap:
            if char.islower():
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)
    
    return ''.join(result)

print("flip_case('Aaaahhh', 'a') returned", flip_case('Aaaahhh', 'a'))  # Expected output: 'aAAAhhh'
print("flip_case('Aaaahhh', 'A') returned", flip_case('Aaaahhh', 'A'))  # Expected output: 'aAAAhhh'
print("flip_case('Aaaahhh', 'h') returned", flip_case('Aaaahhh', 'h'))  # Expected output: 'AaaaHHH'