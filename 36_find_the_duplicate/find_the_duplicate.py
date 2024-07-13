def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    seen = set()
    
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    
    return None

print("find_the_duplicate([1, 2, 1, 4, 3, 12]) returned", find_the_duplicate([1, 2, 1, 4, 3, 12]))  # Expected output: 1
print("find_the_duplicate([6, 1, 9, 5, 3, 4, 9]) returned", find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))  # Expected output: 9
print("find_the_duplicate([2, 1, 3, 4]) is None", find_the_duplicate([2, 1, 3, 4]) is None)  # Expected output: True
