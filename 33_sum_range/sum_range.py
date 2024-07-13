def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

    if end is None or end >= len(nums):
        end = len(nums) - 1

    return sum(nums[start:end + 1])

nums = [1, 2, 3, 4]

print("sum_range(nums) returned", sum_range(nums))  # Expected output: 10
print("sum_range(nums, 1) returned", sum_range(nums, 1))  # Expected output: 9
print("sum_range(nums, end=2) returned", sum_range(nums, end=2))  # Expected output: 6
print("sum_range(nums, 1, 3) returned", sum_range(nums, 1, 3))  # Expected output: 9
print("sum_range(nums, 1, 99) returned", sum_range(nums, 1, 99))  # Expected output: 9
print("sum_range(nums, 0, 1) returned", sum_range(nums, 0, 1))  # Expected output: 3
print("sum_range(nums, 2, 2) returned", sum_range(nums, 2, 2))  # Expected output: 3
