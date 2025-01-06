def fibonacci(n):
    # Base case
    if n <= 1:
        return n
    
    # Recursive case
    return fibonacci(n - 2) + fibonacci(n - 1)

# Example usage
print(fibonacci(3))  # 2
print(fibonacci(40))  # 34