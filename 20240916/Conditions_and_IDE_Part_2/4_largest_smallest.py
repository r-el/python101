num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


choice = input("What do you want to find, the largest or the smallest number? (largest/smallest): ")

if choice == "largest":
    if num1 > num2 and num1 > num3:
        print("The largest number is", num1)
    elif num2 > num1 and num2 > num3:
        print("The largest number is", num2)
    else:
        print("The largest number is", num3)
elif choice == "smallest":
    if num1 < num2 and num1 < num3:
        print("The smallest number is", num1)
    elif num2 < num1 and num2 < num3:
        print("The smallest number is", num2)
    else:
        print("The smallest number is", num3)
else:
    print("Invalid choice")
