def count_even_numbers(arr, i=0): return 0 if i == len(arr) else (arr[i] % 2 == 0) + count_even_numbers(arr, i+1) 

# Example usage:
print(count_even_numbers([1, 2, 3, 4, 5]))  # Output: 2