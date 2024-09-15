num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)
middle = num1 + num2 + num3 - smallest - largest

if smallest + largest > middle:
    print("The sum of the smallest and largest numbers is greater than the middle number.")
else:
    print("The sum of the smallest and largest numbers is not greater than the middle number.")