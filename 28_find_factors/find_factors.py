def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

print("find_factors(10) returned", find_factors(10))  # Expected output: [1, 2, 5, 10]
print("find_factors(11) returned", find_factors(11))  # Expected output: [1, 11]
print("find_factors(111) returned", find_factors(111))  # Expected output: [1, 3, 37, 111]
print("find_factors(321421) returned", find_factors(321421))  # Expected output: [1, 293, 1097, 321421]