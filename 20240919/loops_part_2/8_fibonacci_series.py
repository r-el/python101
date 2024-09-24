num = int(input("הכנס מספר: "))

fib_series = [1, 1]
while len(fib_series) < num:
    fib_series.append(fib_series[-1] + fib_series[-2])

print(fib_series)
fib_series = fib_series[:num]

print(" ".join(map(str, fib_series)))

print("סכום הסדרה:", sum(fib_series))
