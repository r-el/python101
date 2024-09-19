import math

number = float(input("אנא הכנס מספר ממשי: "))

print("בחר אפשרות:")
print("א. לעגל למטה")
print("ב. לעגל למעלה")
print("ג. לעגל לפי כתיבה מדעית")

choice = input("הכנס את בחירתך (א/ב/ג): ")

if choice == 'א': # floor
    rounded_number = int(number) if number >= 0 else int(number) - 1 #If number is -3.5, int(number) will be -3, but we want -4
    print(f"המספר לפני העיגול: {number}")
    print(f"המספר אחרי העיגול למטה: {rounded_number}")
    # using modulo operator
    # rounded_number = number - number % 1
    # print(f"המספר אחרי העיגול למטה: {rounded_number}")
elif choice == 'ב': # ceil
    rounded_number = int(number) + 1 if number > 0 else int(number)
    print(f"המספר לפני העיגול: {number}")
    print(f"המספר אחרי העיגול למעלה: {rounded_number}")
elif choice == 'ג':
    rounded_number = "{:.2e}".format(number)
    print(f"המספר לפני העיגול: {number}")
    print(f"המספר אחרי העיגול לפי כתיבה מדעית: {rounded_number}")
else:
    print("בחירה לא תקפה")
    
