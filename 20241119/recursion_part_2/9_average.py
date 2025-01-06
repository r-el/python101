def average(arr, t=0, c=0): # t=total, c=count 
    return (t/c if c != 0 else 0) if c == len(arr) else average(arr, arr[c] + t, 1 + c)

# Example usage:
print(average([1, 2, 3, 4]))  # Output: 2.5