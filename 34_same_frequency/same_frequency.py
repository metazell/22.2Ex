def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    def digit_count(num):
        count = {}
        for digit in str(num):
            count[digit] = count.get(digit, 0) + 1
        return count

    return digit_count(num1) == digit_count(num2)

# Test cases
print("same_frequency(551122, 221515) returned", same_frequency(551122, 221515))  # Expected output: True
print("same_frequency(321142, 3212215) returned", same_frequency(321142, 3212215))  # Expected output: False
print("same_frequency(1212, 2211) returned", same_frequency(1212, 2211))  # Expected output: True
