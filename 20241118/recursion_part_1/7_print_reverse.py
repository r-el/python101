def print_reverse(number):
    # Base case
    if number < 1:
        return
    
    # Print the last digit
    print(number % 10, end='')
    
    # Recursive call with number divided by 10
    print_reverse(number // 10)
    
# Incorrect recursive function to demonstrate the concept
def print_reverse_incorrect(number):
    # Base case
    if number < 1:
        return
    
    # Recursive call with number divided by 10
    print_reverse_incorrect(number // 10)
    
    # Print the last digit
    print(number % 10, end='')

# Example usage
print_reverse(12345)
print()  # For newline

print_reverse_incorrect(12345)
print()  # For newline