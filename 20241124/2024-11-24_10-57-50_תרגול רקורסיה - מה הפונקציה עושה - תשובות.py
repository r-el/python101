# שאלה 1
def func1(n):
    if n == 0:
        return 0
    return n + func1(n-1)

print(func1(4))
# aritmatics_progression(4) = 4 + 3 + 2 + 1 = 10


# שאלה 2
def func2(n):
    if n <= 1:
        return 1
    return n * func2(n-1)

print(func2(5))
# fuctorial(5) = 5 * 4 * 3 * 2 * 1 = 120


# שאלה 3
def func3(str):
    if len(str) <= 1:
        return str
    return func3(str[1:]) + str[0]

print(func3("hello"))
# reverse_string("hello") = "o" + "l" + "l" + "e" + "h" = "olleh"


# שאלה 4
def func4(n):
    if n <= 1:
        return n
    return func4(n-1) + func4(n-2)

print(func4(6))
# fib(6) = fib(5) + fib(4) = fib(4) + fib(3) + fib(3) + fib(2) = 8


# שאלה 5
def func5(n):
    if n < 10:
        return n
    return func5(n // 10) + n % 10

print(func5(1234))
# sum_digits(1234) = 1 + 2 + 3 + 4 = 10


# שאלה 6
def func6(a, b):
    if b == 0:
        return a
    return func6(b, a % b)

print(func6(48, 18))
# ממג"ב = מחלק משותף גדול ביותר
# gcd(48, 18) = gcd(18, 12) = gcd(12, 6) = gcd(6, 0) = 6


# שאלה 7
def func7(arr, i=0):
    if i >= len(arr):
        return 0
    return arr[i] + func7(arr, i+1)

print(func7([1, 2, 3, 4]))
# sum_array([1, 2, 3, 4]) = 1 + 2 + 3 + 4 = 10


# שאלה 8
def func8(n):
    if n <= 0:
        return 0
    return 1 + func8(n//2)

print(func8(16))
# count_divisions(16) = 4


# שאלה 9
def func9(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return func9(str[1:-1])

print(func9("radar"))
# is_palindrome("radar") = True


# שאלה 10
def func10(n, power):
    if power == 0:
        return 1
    return n * func10(n, power-1)

print(func10(2, 4))
# power(2, 4) = 2 * 2 * 2 * 2 = 16