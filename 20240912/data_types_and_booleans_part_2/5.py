a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if a == b == c:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")

if a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is not isosceles.")

# Pythagoras' theorem
if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    print("The triangle is right-angled.")
else:
    print("The triangle is not right-angled.")