def sum_two(num1: int, num2: int) -> int:
    return num1 + num2

def sum_four(num1: int, num2: int, num3: int, num4: int) -> int:
    return sum_two(num1, num2) + sum_two(num3, num4)

# call the functions
print(sum_two(1, 2) + sum_two(3,4))
print(sum_four(1, 2, 3, 4))