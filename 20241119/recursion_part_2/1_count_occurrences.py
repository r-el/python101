def count_occurrences(char, string): return 0 if not string else (1 if string[0] == char else 0) + count_occurrences(char, string[1:])

# Example usage:
print(count_occurrences('a', 'banana'))  # Output: 3