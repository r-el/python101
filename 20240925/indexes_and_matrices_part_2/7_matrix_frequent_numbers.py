import numpy as np
from collections import Counter

matrix = np.random.randint(0, 10, size=(7, 7)) # 0-9

print("Matrix:")
print(matrix)

def print_most_1frequent_numbers(matrix):
    for col in range(matrix.shape[1]):
        column_data = matrix[:, col]
        counter = Counter(column_data)
        most_common = counter.most_common(2)
        print(f"Column {col + 1}: {most_common}")

print("\nMost frequent numbers in each column:")
print_most_frequent_numbers(matrix)

# סיבוב המטריצה 90 מעלות שמאלה
rotated_matrix = np.rot90(matrix)

print("\nRotated Matrix:")
print(rotated_matrix)

print("\nMost frequent numbers in each column of the rotated matrix:")
print_most_frequent_numbers(rotated_matrix)