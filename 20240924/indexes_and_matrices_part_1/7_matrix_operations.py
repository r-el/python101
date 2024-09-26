import random as rnd

def create_matrix(rows, cols):
    return [[rnd.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

matrix1 = create_matrix(5, 5)
matrix2 = create_matrix(5, 5)
matrix3 = create_matrix(5, 5)

# print two numbers from each row
def print_two_numbers_from_each_row(matrix):
    for row in matrix:
        print(row[0], row[1])

print("Matrix 1:")
print_two_numbers_from_each_row(matrix1)
print("\nMatrix 2:")
print_two_numbers_from_each_row(matrix2)
print("\nMatrix 3:")
print_two_numbers_from_each_row(matrix3)

# Print the size of each matrix
def print_matrix_size(matrix):
    print(f"Matrix size: {len(matrix)}x{len(matrix[0])}")

print("\nSizes of the matrices:")
print_matrix_size(matrix1)
print_matrix_size(matrix2)
print_matrix_size(matrix3)

# Remove 4 rows: 2 by pop and 2 by remove
def modify_matrix(matrix):
    popped_rows = [matrix.pop(), matrix.pop()]
    matrix.remove(matrix[0])
    matrix.remove(matrix[0])
    return popped_rows

popped_rows1 = modify_matrix(matrix1)
popped_rows2 = modify_matrix(matrix2)
popped_rows3 = modify_matrix(matrix3)

# Insert the popped rows back to the first and last positions
def insert_popped_rows(matrix, popped_rows):
    matrix.insert(0, popped_rows[0])
    matrix.append(popped_rows[1])

insert_popped_rows(matrix1, popped_rows1)
insert_popped_rows(matrix2, popped_rows2)
insert_popped_rows(matrix3, popped_rows3)

# Print each internal list in different orders
def print_list_orders(matrix):
    for row in matrix:
        print("Original:", row)
        print("Reversed:", row[::-1])
        mid = len(row) // 2
        print("Start to middle:", row[:mid])
        print("Middle to end:", row[mid:])
        print()

print("\nMatrix 1 orders:")
print_list_orders(matrix1)
print("\nMatrix 2 orders:")
print_list_orders(matrix2)
print("\nMatrix 3 orders:")
print_list_orders(matrix3)
