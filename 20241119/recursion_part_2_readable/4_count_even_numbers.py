def count_even_numbers(arr: list[int], i=0) -> int:
    # Base case
    if i == len(arr):
        return 0
    return int(arr[i] % 2 == 0) + count_even_numbers(arr, i + 1)

# Example usage:
print(count_even_numbers([1, 2, 3, 4, 5]))  # Output: 2