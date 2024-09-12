# Prompt the user for 3 inputs
input1 = input("Enter the first input: ")
input2 = input("Enter the second input: ")
input3 = input("Enter the third input: ")

result1 = str(input1) + str(input2)
result2 = str(input1) + str(input3)
result3 = str(input2) + str(input3)

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)

int_input1 = int(input("Enter the first integer: "))
int_input2 = int(input("Enter the second integer: "))
int_input3 = int(input("Enter the third integer: "))

int_result1 = int_input1 + int_input2
int_result2 = int_input1 + int_input3
int_result3 = int_input2 + int_input3

print("Integer Result 1:", int_result1)
print("Integer Result 2:", int_result2)
print("Integer Result 3:", int_result3)