def factorial(n):
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # 120