def is_even(num):
    if num == 0:
        return True
    if num == 1:
        return False
    return is_even(num - 2)

# Test cases
print(is_even(4))  # True
print(is_even(7))  # False
print(is_even(0))  # True
print(is_even(1))  # False