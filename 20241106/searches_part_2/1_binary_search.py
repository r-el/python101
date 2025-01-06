def binary_search(arr, num):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == num:
            return mid
        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1
