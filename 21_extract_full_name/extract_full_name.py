def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    return [f"{person['first']} {person['last']}" for person in people]

names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
]

print("extract_full_names(names) returned", extract_full_names(names))  # Expected output: ['Ada Lovelace', 'Grace Hopper']

more_names = [
    {'first': 'Alan', 'last': 'Turing'},
    {'first': 'Katherine', 'last': 'Johnson'},
    {'first': 'Margaret', 'last': 'Hamilton'},
]

print("extract_full_names(more_names) returned", extract_full_names(more_names))  # Expected output: ['Alan Turing', 'Katherine Johnson', 'Margaret Hamilton']
print("extract_full_names([]) returned", extract_full_names([]))  # Expected output: []