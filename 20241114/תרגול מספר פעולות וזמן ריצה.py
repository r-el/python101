#חשב עבור כל פונקציה

#מה מספר ה*פעולות* שהפונקציה עושה?? (print, return = פעולה)

#מה סדר גודל זמן הריצה של הפונקציה??


# פונקציה 1
def func1(n):
    return n + 1

# פונקציה 2
def func2(arr):
    for i in arr:
        print(i)

# פונקציה 3
def func3(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# פונקציה 4
def func4(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)

# פונקציה 5
def func5(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

# פונקציה 6
def func6(arr):
    for i in arr:
        for j in range(len(arr)):
            print(i, j)

# פונקציה 7
def func7(n):
    for i in range(n):
        for j in range(i, n):
            print(i, j)

# פונקציה 8
def func8(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

# פונקציה 9
def func9(n):
    i = n
    while i > 1:
        print(i)
        i = i // 2

# פונקציה 10
def func10(n):
    for i in range(n):
        for j in range(int(n**0.5)):
            print(i, j)

# פונקציה 11
def func11(n):
    if n <= 1:
        return 1
    return func11(n - 1) + func11(n - 2)

# פונקציה 12
def func12(n):
    if n <= 1:
        return
    for i in range(n):
        print(i)
    func12(n // 2)

# פונקציה 13
def func13(n):
    for i in range(n):
        print(i)
    for j in range(2 * n):
        print(j)

# פונקציה 14
def func14(n):
    for i in range(n):
        print(i)
    for j in range(n):
        for k in range(10):
            print(j, k)

# פונקציה 15
def func15(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                print(i, j, k)

# פונקציה 16
def func16(arr):
    n = len(arr)
    for i in range(n):
        print(i)
    for j in range(n):
        for k in range(j, n):
            print(j, k)

# פונקציה 17
def func17(n):
    i = 1
    while i < n:
        for j in range(i):
            print(j)
        i *= 2

# פונקציה 18
def func18(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                print(i, j)

# פונקציה 19
def func19(n):
    i = n
    while i > 1:
        for j in range(i):
            print(j)
        i = i // 2

# פונקציה 20
def func20(arr):
    for i in range(len(arr)):
        print(arr[i])
    if len(arr) > 1:
        func20(arr[1:])
