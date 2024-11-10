symbol = input("הכנס סמל: ")
n = int(input("הכנס מספר: "))

print("\nבחר אפשרות:")
print("(1) Make a square")
print("(2) Make an arrow")
print("(3) Make a pyramid")

choice = int(input())

# יצירת ריבוע
if choice == 1:
    for i in range(n):
        print((symbol + " ") * n)

# יצירת חץ
elif choice == 2:
    for i in range(n):
        print((symbol + " ") * (i + 1))
    for i in range(n - 1, 0, -1):
        print((symbol + " ") * i)

# יצירת פירמידה כמו משולש שווה צלעות
elif choice == 3:
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        symbols = (symbol + ' ') * i
        print(spaces + symbols)
else:
    print("בחירה לא תקינה")
