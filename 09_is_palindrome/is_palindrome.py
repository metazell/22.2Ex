def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    cleaned_phrase = ''.join(char.lower() for char in phrase if char.isalnum())
    return cleaned_phrase == cleaned_phrase[::-1]

print("is_palindrome('tacocat') returned", is_palindrome('tacocat'))  # Expected output: True
print("is_palindrome('noon') returned", is_palindrome('noon'))  # Expected output: True
print("is_palindrome('robert') returned", is_palindrome('robert'))  # Expected output: False
print("is_palindrome('taco cat') returned", is_palindrome('taco cat'))  # Expected output: True
print("is_palindrome('Noon') returned", is_palindrome('Noon'))  # Expected output: True
print("is_palindrome('A man, a plan, a canal, Panama') returned", is_palindrome('A man, a plan, a canal, Panama'))  # Expected output: True