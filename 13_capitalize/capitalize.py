def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    if not phrase:
        return ""
    return phrase[0].upper() + phrase[1:]

print("capitalize('python') returned", capitalize('python'))  # Expected output: 'Python'
print("capitalize('only first word') returned", capitalize('only first word'))  # Expected output: 'Only first word'