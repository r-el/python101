# count = 0

# while True:
#     number = int(input("Please enter a number: "))
#     if number == -1:
#         break
#     count += 1

# print(f"You entered numbers {count} times.")

count = 0
number = int(input("Please enter a number: "))

while number != -1:
    count += 1
    number = int(input("Please enter a number: "))

print(f"You entered numbers {count} times.")