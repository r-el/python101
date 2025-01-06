# shgiaa: ZeroDivisionError: division by zero
""" tikun: להוסיף בדיקה לפני החלוקה כדי לוודא שהמכנה לא שווה לאפס
if len(numbers) == 0:
    return 0
"""
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
print("Average:", calculate_average(numbers))
numbers = []
print("Average:", calculate_average(numbers))