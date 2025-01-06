def binary_search_occurrences(arr, num):
    def binary_search(arr, num):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == num:
                return mid
            elif arr[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    def find_first_occurrence(arr, num, start):
        low, high = 0, start
        first_occurrence_index = start
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == num:
                first_occurrence_index = mid
                high = mid - 1
            else:
                low = mid + 1
        return first_occurrence_index

    def find_last_occurrence(arr, num, start):
        low, high = start, len(arr) - 1
        last_occurrence_index = start
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == num:
                last_occurrence_index = mid
                low = mid + 1  # Continue searching in the right half for the last occurrence
            else:
                high = mid - 1
        return last_occurrence_index

    index = binary_search(arr, num)
    if index == -1:
        return 0

    first_occurrence = find_first_occurrence(arr, num, index)
    last_occurrence = find_last_occurrence(arr, num, index)
    return list(range(first_occurrence, last_occurrence + 1))



# Example usage
arr = [1, 2, 2, 2, 3, 3, 3, 4, 5]
target = 2
print(binary_search_occurrences(arr, target))  # Output: [1, 2, 3]

