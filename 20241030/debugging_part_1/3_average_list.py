# shgiaa: ZeroDivisionError: division by zero
# tikun: return 0 if len(numbers) == 0 else total / len(numbers)
# totzaa of empty list: 0
def average_list(numbers):
    total = sum(numbers)
    return total / len(numbers)

print(average_list([10, 20, 30, 40]))
print(average_list([]))