import rnd

random_nums = [rnd.randint(1, 101) for _ in range(200)]

even_nums = []
odd_nums = []

[even_nums.append(num) if num % 2 == 0 else odd_nums.append(num) for num in random_nums]

print(odd_nums)
print(even_nums)