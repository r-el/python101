a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# temp = a
# a = b
# b = c
# c = temp
a, b, c = b, c, a

print("After circular swapping:")
print("a =", a)
print("b =", b)
print("c =", c)