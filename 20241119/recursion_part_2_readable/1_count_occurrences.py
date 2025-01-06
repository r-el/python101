def count_occurrences(char: str, string: str) -> int:
    if not string:
        return 0
    return (1 if string[0] == char else 0) + count_occurrences(char, string[1:])

# Example usage:
print(count_occurrences('a', 'banana'))  # Output: 3