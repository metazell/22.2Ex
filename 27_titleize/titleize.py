def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    return phrase.title()

print("titleize('this is awesome') returned", titleize('this is awesome'))  # Expected output: 'This Is Awesome'
print("titleize('oNLy cAPITALIZe fIRSt') returned", titleize('oNLy cAPITALIZe fIRSt'))  # Expected output: 'Only Capitalize First'
