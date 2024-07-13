def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    num_counts = {}
    
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    
    max_count = max(num_counts.values())
    
    for num, count in num_counts.items():
        if count == max_count:
            return num
        
print("mode([1, 2, 1]) returned", mode([1, 2, 1]))  # Expected output: 1
print("mode([2, 2, 3, 3, 2]) returned", mode([2, 2, 3, 3, 2]))  # Expected output: 2