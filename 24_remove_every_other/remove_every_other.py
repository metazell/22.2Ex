def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    return lst[::2]

lst = [1, 2, 3, 4, 5]

print("remove_every_other(lst) returned", remove_every_other(lst))  # Expected output: [1, 3, 5]
print("Original lst after function call:", lst)  # Expected output: [1, 2, 3, 4, 5]