from functools import reduce

numbers = [float(input("Enter a number: ")) for _ in range(5)]
print("Average:", sum(numbers) / len(numbers))

product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)