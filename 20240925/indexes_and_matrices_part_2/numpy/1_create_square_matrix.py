import numpy as np

n = int(input("הכנס מספר ליצירת מטריצה ריבועית: "))

matrix = np.arange(1, n*n + 1).reshape(n, n)
# matrix = np.random.randint(1, 100, size=(n, n))

print("Matrix:")
print(matrix)
