# assuming the rows in the matrix are equal in length
def binary_search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Example usage
matrix = [
    [1, 4, 5, 10],
    [33, 100, 123, 602],
    [700, 1050, 3000, 23000]
]
target = 123
print(binary_search_matrix(matrix, target))  # Output: True

target = 50
print(binary_search_matrix(matrix, target))  # Output: False