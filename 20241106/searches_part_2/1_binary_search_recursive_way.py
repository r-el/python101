def binary_search_recursive(arr, num, left=0, right=None):
    # init high
    if right is None:
        right = len(arr) - 1
    
    # num not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == num:
        return mid
    if arr[mid] < num:
        return binary_search_recursive(arr, num, left=mid + 1, right=right)
    else:
        return binary_search_recursive(arr, num, left=left, right=mid - 1)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 10
print(binary_search_recursive(arr, num))