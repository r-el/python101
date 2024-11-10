def is_submatrix(matrix, submatrix):
    rows_matrix = len(matrix)
    cols_matrix = len(matrix[0])
    rows_submatrix = len(submatrix)
    cols_submatrix = len(submatrix[0])

    for i in range(rows_matrix - rows_submatrix + 1):
        for j in range(cols_matrix - cols_submatrix + 1):
            match = True
            for k in range(rows_submatrix):
                for l in range(cols_submatrix):
                    if matrix[i + k][j + l] != submatrix[k][l]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

# Example matrices
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

submatrix = [
    [6, 7],
    [10, 11]
]

print("Matrix:")
for row in matrix:
    print(row)

print("\nSubmatrix:")
for row in submatrix:
    print(row)

if is_submatrix(matrix, submatrix):
    print("\nThe submatrix is a part of the matrix.")
else:
    print("\nThe submatrix is not a part of the matrix.")