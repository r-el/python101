def has_negative(arr: list[int], i=0) -> bool:
    if i == len(arr):
        return False
    return True if arr[i] < 0 else has_negative(arr, i+1)

# Example usage:
print(has_negative([1, 2, -3, 4]))  # Output: True
print(has_negative([1, 2, 3]))      # Output: False