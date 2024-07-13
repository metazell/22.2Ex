def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    return lst.count(search_term)

print("frequency([1, 4, 3, 4, 4], 4) returned", frequency([1, 4, 3, 4, 4], 4))  # Expected output: 3
print("frequency([1, 4, 3], 7) returned", frequency([1, 4, 3], 7))  # Expected output: 0