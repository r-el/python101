def has_consecutive_duplicates(arr: list[int]) -> bool:
    if len(arr) < 2:
        return False
    if arr[0] == arr[1]:
        return True
    return has_consecutive_duplicates(arr[1:])

# Example usage:
print(has_consecutive_duplicates([1, 2, 2, 3]))  # Output: True
print(has_consecutive_duplicates([1, 2, 3]))     # Output: False