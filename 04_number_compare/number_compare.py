def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a>b:
        return 'first is greater'
    
    elif b>a:
        return 'second is greater'
    
    else:
        return 'numbers equal'

print("number_compare(1, 1) returned", number_compare(1, 1))  # Expected output: 'Numbers are equal'
print("number_compare(-1, 1) returned", number_compare(-1, 1))  # Expected output: 'Second is greater'
print("number_compare(1, -2) returned", number_compare(1, -2))  # Expected output: 'First is greater'
