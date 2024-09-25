import math

size = 5
numbers = [int(input("Enter a number: ")) for _ in range(size)]

if numbers == sorted(numbers):
    print("The list is in ascending order.")
    print("Sum of all elements:", sum(numbers))
elif numbers == sorted(numbers, reverse=True):
    print("The list is in descending order.")
    size = 5
    numbers = [int(input("Enter a number: ")) for _ in range(size)]

    if numbers == sorted(numbers):
        print("The list is in ascending order.")
        print("Sum of all elements:", sum(numbers))
    elif numbers == sorted(numbers, reverse=True):
        print("The list is in descending order.")
        print("Product of all elements:", math.prod(numbers))
    else:
        print("The list is not in any specific order.")
        print("Average of all elements:", sum(numbers) / len(numbers))
    print("Product of all elements:", product)
else:
    print("The list is not in any specific order.")
    print("Average of all elements:", sum(numbers) / len(numbers))