import numpy as np

# יצירת מטריצה בגודל 10 על 10
matrix = np.random.randint(1, 100, size=(10, 10))

print("Matrix:")
print(matrix)

# א. הדפסת האיברים במיקום הזוגי והאי זוגי
even_elements = matrix[::, ::2]
odd_elements = matrix[::, 1::2]

print("\nEven positioned elements:")
print(even_elements)

print("\nOdd positioned elements:")
print(odd_elements)

# ב. הדפסת כל וקטור בקפיצות של 3
print("\nVectors with step of 3:")
for row in matrix:
    print(row[::3])