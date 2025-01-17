def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    return [item for item in l1 if item in l2]

print("intersection([1, 2, 3], [2, 3, 4]) returned", intersection([1, 2, 3], [2, 3, 4]))  # Expected output: [2, 3]
print("intersection([1, 2, 3], [1, 2, 3, 4]) returned", intersection([1, 2, 3], [1, 2, 3, 4]))  # Expected output: [1, 2, 3]
print("intersection([1, 2, 3], [3, 4]) returned", intersection([1, 2, 3], [3, 4]))  # Expected output: [3]
print("intersection([1, 2, 3], [4, 5, 6]) returned", intersection([1, 2, 3], [4, 5, 6]))  # Expected output: []