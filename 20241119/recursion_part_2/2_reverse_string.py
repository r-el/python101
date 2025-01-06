def reverse_string(s): return s if len(s) < 2 else reverse_string(s[1:]) + s[0]
def reverse_string(s): return s if len(s) < 2 else s[-1] + reverse_string(s[1:-1]) + s[0] 

# Example usage:
print(reverse_string('1234'))  # Output: '4321'
print(reverse_string('12345'))  # Output: '54321'
