def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter

    
print("multiple_letter_count('yay') returned", multiple_letter_count('yay')) 
print("multiple_letter_count('Yay') returned", multiple_letter_count('Yay'))  