negative_number = int(input("Please enter a negative number: "))

if negative_number >= 0:
    print("The number is not negative.")
else:
    for num in range(negative_number, 1):
        print(num)