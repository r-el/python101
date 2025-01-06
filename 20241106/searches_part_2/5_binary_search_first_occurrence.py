def binary_search_first_occurrence(arr, num) -> int:
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        while arr[mid] == num:
            if arr[mid - 1] != num:
                return mid
            
        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(binary_search_first_occurrence(arr, target))  # Output: 1