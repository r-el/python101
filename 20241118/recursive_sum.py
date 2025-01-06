# # With [:] slicing
# def recursive_sum(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + recursive_sum(arr[1:])

# Without slicing
def recursive_sum(arr, i=0):
    if i == len(arr):
        return 0
    else:
        return arr[i] + recursive_sum(arr, i + 1)

arr = [1, 2, 3, 4, 5]
print(recursive_sum(arr)) # 15
