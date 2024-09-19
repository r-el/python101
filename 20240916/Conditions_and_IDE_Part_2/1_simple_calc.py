num1, num2 = float(input("Enter the first number: ")), float(input("Enter the second number: "))

operators = ["+", "-", "*", "/", "%", "**"]
operator = input(f"Enter the operator {operators}: " )
if operator in operators:
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        if num2 != 0:
            print(num1/num2)
        else : print("Error: division by zero")
    elif operator == "%":
        if num2 != 0:
            print(num1%num2)
        else : print("Error: modulo by zero")
    elif operator == "**":
        print(num1**num2)
else:
    print("Operator not support")
