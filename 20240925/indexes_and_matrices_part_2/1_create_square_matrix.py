n = int(input("הכנס מספר ליצירת מטריצה ריבועית: "))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(i * n + j + 1)
    matrix.append(row)
    
print("Matrix:")
for row in matrix:
    print(row)
print()
