def print_reverse_string(s):
    # Base case
    if len(s) == 0:
        return
    
    # Print the last character
    print(s[-1], end='')
    
    # Recursive call with the string except the last character
    print_reverse_string(s[:-1])

# Example usage
print_reverse_string("example")
print()  # For newline

def print_reverse_string_incorrect(s):
    # Base case
    if len(s) == 0:
        return
    
    # Recursive call with the string except the last character
    print_reverse_string_incorrect(s[:-1])
    
    # Print the last character
    print(s[-1], end='')

# Example usage
print_reverse_string_incorrect("example")
print()  # For newline