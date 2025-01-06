def sort_by_length(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# main
arr = ["123", "1", "12345", "12", "1234", "123456"]
print(sort_by_length(arr))