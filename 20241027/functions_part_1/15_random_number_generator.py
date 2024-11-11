import random

def random_between_1_and_num(num: int) -> int:
    return random.randint(1, num)

# call the function
print(random_between_1_and_num(10))
print(random_between_1_and_num(20))
print(random_between_1_and_num(30))
print(random_between_1_and_num(40))