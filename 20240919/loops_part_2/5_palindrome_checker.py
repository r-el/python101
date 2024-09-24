num = input("Please enter a number: ")

if num.isdigit():
    number = int(num)
    str_number = str(number)

    if str_number == str_number[::-1]:
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")
else:
    print("Invalid input. Please enter a valid number.")

# # O(n/2)
# if num.isdigit():
#     for i in range(len(num)//2):
#         if num[i] != num[-1-i]:
#             print(f"{num} is not a palindrome")
#             break
#     else:
#         print(f"{num} is a palindrome")
# else:
#     print("Invalid input. Please enter a valid number.")

# in 1 line
# print(f"{num} is a palindrome") if num.isdigit() and num == num[::-1] else print(f"{num} is not a palindrome") if num.isdigit() else print("Invalid input. Please enter a valid number.")

