num1 = int(input("הכנס מספר שלם ראשון: "))
num2 = int(input("הכנס מספר שלם שני: "))
num3 = int(input("הכנס מספר שלם שלישי: "))

# מיון המספרים מהקטן לגדול
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

print("המספרים ממוינים מהקטן לגדול: ", num1, num2, num3)

# מיון המספרים מהגדול לקטן
if num1 < num2:
    num1, num2 = num2, num1
if num2 < num3:
    num2, num3 = num3, num2
if num1 < num2:
    num1, num2 = num2, num1

print("המספרים ממוינים מהגדול לקטן: ", num1, num2, num3)