import random

def create_square_matrix(n):
    return [[random.randint(1, 3) for _ in range(n)] for _ in range(n)]

def sum_diagonals(matrix):
    n = len(matrix)
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    anti_diagonal_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    return main_diagonal_sum + anti_diagonal_sum

def sum_first_and_last_columns(matrix):
    first_column_sum = sum(row[0] for row in matrix)
    last_column_sum = sum(row[-1] for row in matrix)
    return first_column_sum + last_column_sum

def sum_matrix_frame(matrix):
    n = len(matrix)
    top_row_sum = sum(matrix[0])
    bottom_row_sum = sum(matrix[-1])
    left_column_sum = sum(matrix[i][0] for i in range(1, n - 1))
    right_column_sum = sum(matrix[i][-1] for i in range(1, n - 1))
    return top_row_sum + bottom_row_sum + left_column_sum + right_column_sum

n = int(input("הכנס מספר ליצירת מטריצה ריבועית: "))
matrix = create_square_matrix(n)

print("Matrix:")
for row in matrix:
    print(row)

print("\nSum of diagonals:")
print(sum_diagonals(matrix))

print("\nSum of the first and last columns:")
print(sum_first_and_last_columns(matrix))

print("\nSum of the matrix frame:")
print(sum_matrix_frame(matrix))
