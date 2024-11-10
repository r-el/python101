matrix = [ [i * 10 + j + 1 for j in range(10)] for i in range(5)]

print("Matrix:")
for row in matrix:
    print(row)
    
sum_of_elements = 0
count_elements = 0
for row in matrix:
    for element in row:
        sum_of_elements += element
        count_elements += 1
        
average_of_elements = sum_of_elements / count_elements
print("\nSum of all elements:")
print(sum_of_elements)
print("\nAverage of all elements:")
print(average_of_elements)
print()
