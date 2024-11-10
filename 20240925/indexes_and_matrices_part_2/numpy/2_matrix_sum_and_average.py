import numpy as np

# יצירת מטריצה בגודל 5 על 10 (50 תאים)
matrix = np.random.randint(1, 100, size=(5, 10))

print("Matrix:")
print(matrix) # <class 'numpy.ndarray'> 

# א. הדפסת סכום כל האיברים
sum_of_elements = np.sum(matrix)
print("\nSum of all elements:")
print(sum_of_elements)

# ב. הדפסת ממוצע כל האיברים
average_of_elements = np.mean(matrix)
print("\nAverage of all elements:")
print(average_of_elements)