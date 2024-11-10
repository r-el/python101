import random

# Create a 5x5 matrix with random values between 1 and 100
matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]

print("Matrix:")
for row in matrix:
    print(row)

number = int(input("Enter a number to search in the matrix: "))

found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == number:
            found = True
            print(f"Number {number} found at position ({i}, {j})")
            print("Frame around the number:")

            # Print the numbers surrounding the found number
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue # Skip the current cell itself
                    new_i, new_j = i + dx, j + dy
                    if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[i]):
                        print(f"({new_i}, {new_j}): {matrix[new_i][new_j]}")
            break
    if found:
        break

if not found:
    print(f"Number {number} not found in the matrix.")
