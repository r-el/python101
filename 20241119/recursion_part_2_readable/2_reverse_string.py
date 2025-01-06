def reverse_string(string: str) -> str:
    # Base case
    if len(string) == 0 or len(string) == 1 :
        return string
   
    return string[-1] + reverse_string(string[1:-1]) + string[0]

# Example usage:
print(reverse_string('12345'))  # Output: 'olleh'