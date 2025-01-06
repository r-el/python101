def average(arr: list[int], total=0, count=0):
    # Base case
    if count == len(arr): # 0 or the len(arr)
        return (total/count if count != 0 else 0)
    
    return average(arr, arr[count] + total, 1 + count) 

# Example usage:
print(average([1, 2, 3, 4]))  # Output: 2.5