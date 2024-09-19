total_sum = 0

while True:
    user_input = input("Please enter a number (0 to stop): ")
    number = float(user_input)
    
    if number == 0:
        break
    
    total_sum += number

print(f"The total sum of the numbers entered is: {total_sum}")