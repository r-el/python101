def binary_search_occurrences_recursive(arr, num, left=0, right=None):
    # Init right
    if right is None:
        right = len(arr) - 1  

    # If num not found
    if left > right:
        return []

    mid = (left + right) // 2

    if arr[mid] == num:
        left_indices = binary_search_occurrences_recursive(arr, num, left, mid - 1)
        right_indices = binary_search_occurrences_recursive(arr, num, mid + 1, right)
        return left_indices + [mid] + right_indices
    elif arr[mid] < num:
        return binary_search_occurrences_recursive(arr, num, mid + 1, right)  # Search in the right half
    else:
        return binary_search_occurrences_recursive(arr, num, left, mid - 1)  # Search in the left half

def binary_search_occurrences(arr, num):
    indices = binary_search_occurrences_recursive(arr, num)
    
     # if not found
    if not indices:
        return 0
    # Single index
    elif len(indices) == 1:
        return indices[0]
    # Multiple indices
    else: 
        return indices

# Example usage
arr = [0, 1, 2, 3, 4, 5, 6, 7, 9, 9]
num = 9

result = binary_search_occurrences(arr, num)
print(result)
