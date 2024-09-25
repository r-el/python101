import rnd

numbers = [rnd.randint(1, 100) for _ in range(100)]

[print(i, end=" ") for i in numbers]
print() # For a new line

[print(i, end=" ") for i in numbers[::-1]] # reversed(numbers)
print() # For a new line
