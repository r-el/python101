def binary_search_strings_bool(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Example usage
arr = ["Aba", "Ima", "Saba", "Savta"]
target = "Savta"
print(binary_search_strings_bool(arr, target))  # Output: True