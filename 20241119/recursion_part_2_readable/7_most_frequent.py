def most_frequent(arr: list[int], i=0, max_num=float('-inf'), max_count=0) -> int:
    if not arr: return
    if len(arr) == 1: return arr[0]
    
    # Base case
    if i == len(arr) - 1: return max_num

    # Main logic
    max_c = max(max_count, arr.count(arr[i]))
    max_n = arr[i] if max_c >= max_count else max_num
    
    return most_frequent(arr, i + 1, max_num=max_n, max_count=max_c)
    
# Example usage:
print(most_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2]))  # Output: 3