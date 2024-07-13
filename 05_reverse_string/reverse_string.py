def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]

print("reverse_string('awesome') returned", reverse_string('awesome'))  # Expected output: 'emosewa'
print("reverse_string('sauce') returned", reverse_string('sauce'))  # Expected output: 'ecuas'