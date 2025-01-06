def has_consecutive_duplicates(arr): return False if len(arr) < 2 else True if arr[0] == arr[1] else has_consecutive_duplicates(arr[1:])

# Example usage:
print(has_consecutive_duplicates([1, 2, 2, 3]))  # Output: True
print(has_consecutive_duplicates([1, 2, 3]))     # Output: False