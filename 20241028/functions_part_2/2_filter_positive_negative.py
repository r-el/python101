def filter_positive_numbers(numbers, positive):
    return [num for num in numbers if num > 0] if positive else[num for num in numbers if num < 0]

# usage examples
print(filter_positive_numbers([1, -2, 3, -4, 5], True))  # [1, 3, 5]
print(filter_positive_numbers([1, -2, 3, -4, 5], False))  # [-2, -4]