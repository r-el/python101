def reverse_string(string: str) -> str:
    return string[::-1]

def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)

def count_palindromes(strings) -> int:
    return sum(is_palindrome(s) for s in strings) # True=1, False=0


# usage examples
print(reverse_string("hello"))  # 'olleh'
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(count_palindromes(["racecar", "hello", "level", "world"]))  # 2
