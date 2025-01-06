import random

def generate_and_sort():
    # Generate a list of 100 random numbers
    arr = random.sample(range(1, 1000), 100)

    # Bubble sort with iteration count
    def bubble_sort(arr):
        n = len(arr)
        iterations = 0
        
        for i in range(n):
            swapped = False
            
            for j in range(0, n-i-1):
                iterations += 1
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr, iterations

    # Selection sort with iteration count
    def selection_sort(arr):
        n = len(arr)
        iterations = 0
        
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                iterations += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr, iterations

    # Copy the array for both sorting algorithms
    arr_copy = arr[:]
    
    # Sort using bubble sort
    _, bubble_iterations = bubble_sort(arr)
    
    # Sort using selection sort
    _, selection_iterations = selection_sort(arr_copy)
    
    # Print the number of iterations for each sort
    print(f"Bubble sort iterations: {bubble_iterations}")
    print(f"Selection sort iterations: {selection_iterations}")
    
    # Determine which sort was more efficient
    if bubble_iterations < selection_iterations:
        print("Bubble sort was more efficient.")
    else:
        print("Selection sort was more efficient.")

# Call the function
generate_and_sort()