import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))

print("Matrix:")
print(matrix)

number = int(input("Enter a number to search in the matrix: "))

found = False
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == number:
            found = True
            print(f"Number {number} found at position ({i}, {j})")
            print("Frame around the number:")

            # הדפסת המספרים שמקיפים את המספר
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < matrix.shape[0] and 0 <= nj < matrix.shape[1]:
                        print(f"({ni}, {nj}): {matrix[ni, nj]}")
            break
    if found:
        break

if not found:
    print(f"Number {number} not found in the matrix.")
    