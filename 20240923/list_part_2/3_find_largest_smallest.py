import rnd as rnd

random_numbers = [rnd.randint(1, 10000) for _ in range(1000)]

smallest = largest = random_numbers[0]

for number in random_numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")