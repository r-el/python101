def is_palindrome(n, rev_n=0):
    if n <= rev_n:
        return (rev_n == n) or (rev_n//10 == n)
    else:
        return is_palindrome(n // 10, (rev_n * 10) + (n % 10))  

print(is_palindrome(1234))
print(is_palindrome(1221))
print(is_palindrome(1001))
print(is_palindrome(121))
print(is_palindrome(11))
print(is_palindrome(12))
print(is_palindrome(1))
print(is_palindrome(0))
