def is_sorted(arr: list[int], i=0) -> bool:
    if i == len(arr) - 1:
        return True
    
    return False if arr[i] > arr[i+1] else is_sorted(arr, i + 1)

# Example usage:
print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([3, 2, 1]))     # Output: False