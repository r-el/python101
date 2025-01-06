    # select sorting sort arr, and return int value of the iteration count
def selection_sort(arr : list, reverse=False) -> int:
    n = len(arr)
    count = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            count += 1
            if (arr[j] < arr[min_idx]) ^ reverse:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return count

# bubble sorting sort arr, and return int value of the iteration count, has reverse option
def bubble_sort(arr : list, reverse=False) -> int:
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(n-i-1):
            count += 1
            if (arr[j] > arr[j+1]) ^ reverse:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count
