import rnd as rnd

random_list = [rnd.randint(1, 100) for _ in range(10)]

print("Random list:", random_list)

user_number = int(input("Please enter a number: "))

if user_number in random_list:
    index = random_list.index(user_number)
    print(f"The number {user_number} is in the list at position {index}.")
    
    if index > 0:
        print(f"The number before {user_number} is {random_list[index - 1]}.")
    else:
        print(f"There is no number before {user_number}.")
    
    if index < len(random_list) - 1:
        print(f"The number after {user_number} is {random_list[index + 1]}.")
    else:
        print(f"There is no number after {user_number}.")
else:
    print(f"The number {user_number} is not in the list.")