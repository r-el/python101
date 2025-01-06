

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return median

numbers = [1, 3, 5, 7, 9]
print("Median:", calculate_median(numbers))
numbers = [1, 2, 3, 4, 5, 6]
print("Median:", calculate_median(numbers))