number_str = input("הכנס מספר עם לפחות 50 ספרות: ")

number_list = [int(digit) for digit in number_str]

# מציאת המספר שמופיע הכי הרבה פעמים
max_count = 0
max_digit = None

for digit in number_list:
    count = number_list.count(digit)
    if count > max_count:
        max_count = count
        max_digit = digit

print(f"המספר שמופיע הכי הרבה פעמים הוא: {max_digit}")
print(f"המספר הזה מופיע {max_count} פעמים")

print("המיקומים בהם מופיע המספר הם:", end=" ")
for index, digit in enumerate(number_list):
    if digit == max_digit:
        print(index, end=" ")