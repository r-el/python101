def bubble_sort_partial(arr, k):
    n = min(len(arr), k)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort_partial(arr, k):
    n = min(len(arr), k)
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# main
arr = [64, 34, 25, 12, 22, 11, 90, 45, 67, 89, 23, 78]
k = 10
print("Bubble Sort Partial:", bubble_sort_partial(arr.copy(), k))
print("Selection Sort Partial:", selection_sort_partial(arr.copy(), k))