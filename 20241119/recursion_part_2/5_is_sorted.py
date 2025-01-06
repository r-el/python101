def is_sorted(arr, i=0): return i == len(arr) - 1 or (arr[i] <= arr[i+1] and is_sorted(arr, i + 1))

# Example usage:
print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([3, 2, 1]))     # Output: False
