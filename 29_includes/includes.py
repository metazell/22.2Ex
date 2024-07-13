def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    if isinstance(collection, dict):
        return sought in collection.values()

    if isinstance(collection, (list, str, tuple)):
        if start is None:
            return sought in collection
        return sought in collection[start:]

    if isinstance(collection, set):
        return sought in collection

    return False

# Test cases
print("includes([1, 2, 3], 1) returned", includes([1, 2, 3], 1))  # Expected output: True
print("includes([1, 2, 3], 1, 2) returned", includes([1, 2, 3], 1, 2))  # Expected output: False
print("includes('hello', 'o') returned", includes('hello', 'o'))  # Expected output: True
print("includes(('Elmo', 5, 'red'), 'red', 1) returned", includes(('Elmo', 5, 'red'), 'red', 1))  # Expected output: True
print("includes({1, 2, 3}, 1) returned", includes({1, 2, 3}, 1))  # Expected output: True
print("includes({1, 2, 3}, 1, 3) returned", includes({1, 2, 3}, 1, 3))  # Expected output: True
print("includes({'apple': 'red', 'berry': 'blue'}, 'blue') returned", includes({'apple': 'red', 'berry': 'blue'}, 'blue'))  # Expected output: True