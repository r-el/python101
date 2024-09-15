number = int(input("הכנס מספר דו ספרתי: "))

if 10 <= number <= 99:
    digit_sum = (number // 10) + (number % 10)
    
    if number % digit_sum == 0:
        print(True)
    else:
        print(False)
else:
    print("המספר שהוזן אינו דו ספרתי")