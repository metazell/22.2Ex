def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    result= {}

    for i, key in enumerate(keys):
        if i < len(values):
            result[key] = values[i]
        else:
            result[key] = None
    
    return result

print("two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]) returned", two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))  # Expected output: {'x': 9, 'y': 8, 'z': 7}
print("two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) returned", two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))  # Expected output: {'a': 1, 'b': 2, 'c': 3, 'd': None}
print("two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]) returned", two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))  # Expected output: {'a': 1, 'b': 2, 'c': 3}
