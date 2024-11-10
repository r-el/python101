import numpy as np

# יצירת מטריצה ריבועית בגודל 5 על 5 עם מספרים אקראיים
matrix = np.random.randint(1, 100, size=(5, 5))

print("Matrix:")
print(matrix)

# א. הדפסת מספר השורה בה סכום האיברים הוא הגדול ביותר
row_sums = np.sum(matrix, axis=1)
max_sum_row = np.argmax(row_sums)
print("\nRow with the maximum sum of elements:", max_sum_row + 1)

# ב. הדפסת מספר השורה בה סכום האיברים הוא הקטן ביותר
min_sum_row = np.argmin(row_sums)
print("\nRow with the minimum sum of elements:", min_sum_row + 1)

# ג. סיבוב המטריצה 90 מעלות ימינה
rotated_matrix = np.rot90(matrix, -1)

print("\nRotated Matrix:")
print(rotated_matrix)

# חישוב מחדש של סעיפים א' ו-ב' עבור המטריצה המסובבת
rotated_row_sums = np.sum(rotated_matrix, axis=1)
rotated_max_sum_row = np.argmax(rotated_row_sums)
rotated_min_sum_row = np.argmin(rotated_row_sums)

print("\nRow with the maximum sum of elements in the rotated matrix:", rotated_max_sum_row + 1)
print("\nRow with the minimum sum of elements in the rotated matrix:", rotated_min_sum_row + 1)
