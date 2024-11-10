import random as rnd

# יצירת מטריצה ריבועית בגודל 5 על 5 עם מספרים אקראיים
matrix = [[rnd.randint(1, 3) for _ in range(5)] for _ in range(5)]
print("Matrix:")
for row in matrix:
    print(row)

# א. הדפסת מספר השורה בה סכום האיברים הוא הגדול ביותר
row_sums = [sum(row) for row in matrix]
max_sum_row = row_sums.index(max(row_sums))
print("\nRow with the maximum sum of elements:", max_sum_row + 1)

# ב. הדפסת מספר השורה בה סכום האיברים הוא הקטן ביותר
min_sum_row = row_sums.index(min(row_sums))
print("\nRow with the minimum sum of elements:", min_sum_row + 1)

# ג. סיבוב המטריצה 90 מעלות ימינה
# rotated_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix) - 1, -1, -1)]
rotated_matrix = list(zip(*matrix[::-1]))
print("\nRotated Matrix:")
for row in rotated_matrix:
    print(row)
