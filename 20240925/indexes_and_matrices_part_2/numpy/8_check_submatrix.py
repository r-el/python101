import numpy as np

def is_submatrix(matrix, submatrix):
    rows_matrix, cols_matrix = matrix.shape
    rows_submatrix, cols_submatrix = submatrix.shape

    for i in range(rows_matrix - rows_submatrix + 1):
        for j in range(cols_matrix - cols_submatrix + 1):
            if np.array_equal(matrix[i:i+rows_submatrix, j:j+cols_submatrix], submatrix):
                return True
    return False

# Example matrices
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

submatrix = np.array([
    [6, 7],
    [10, 11]
])

print("Matrix:")
print(matrix)

print("\nSubmatrix:")
print(submatrix)

if is_submatrix(matrix, submatrix):
    print("\nThe submatrix is a part of the matrix.")
else:
    print("\nThe submatrix is not a part of the matrix.")