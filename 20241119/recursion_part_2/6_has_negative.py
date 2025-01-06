def has_negative(arr, i=0): return False if i == len(arr) else True if arr[i] < 0 else has_negative(arr, i+1)

# Example usage:
print(has_negative([1, 2, -3, 4]))  # Output: True
print(has_negative([1, 2, 3]))      # Output: False