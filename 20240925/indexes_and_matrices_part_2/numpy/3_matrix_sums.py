import numpy as np

# יצירת מטריצה ריבועית  
n = int(input("הכנס מספר ליצירת מטריצה ריבועית: "))
matrix = np.random.randint(1, 3, size=(n, n))

print("Matrix:")
print(matrix)

# א. חישוב סכום האלכסונים
main_diagonal_sum = np.trace(matrix)
anti_diagonal_sum = np.trace(np.fliplr(matrix))
total_diagonal_sum = main_diagonal_sum + anti_diagonal_sum

print("\nSum of diagonals:")
print(total_diagonal_sum)

# ב. חישוב סכום העמודה הראשונה והאחרונה
first_column_sum = np.sum(matrix[:, 0])
last_column_sum = np.sum(matrix[:, -1])
total_column_sum = first_column_sum + last_column_sum

print("\nSum of the first and last columns:")
print(total_column_sum)

# ג. חישוב סכום המסגרת של המטריצה
top_row_sum = np.sum(matrix[0, :])
bottom_row_sum = np.sum(matrix[-1, :])
left_column_sum = np.sum(matrix[1:-1, 0])
right_column_sum = np.sum(matrix[1:-1, -1])
frame_sum = top_row_sum + bottom_row_sum + left_column_sum + right_column_sum

print("\nSum of the matrix frame:")
print(frame_sum)
