def print_numbers_to_zero(number):
    # Base case
    if number < 0:
        return

    # Print the current number
    print(number)

    print_numbers_to_zero(number - 1)

# Example usage
print_numbers_to_zero(5)
