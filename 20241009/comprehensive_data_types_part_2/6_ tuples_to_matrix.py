def tuples_to_2d_matrix(tuples_list):
    return [[*t] for t in tuples_list]


# Example usage
tuples_list = [(1, 5, 3), (5, 4, 3, 2, 1), (10, 20)]
matrix = tuples_to_2d_matrix(tuples_list)

for row in matrix:
    print(row)