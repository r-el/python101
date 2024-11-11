def is_prime(num: int) -> bool:
    if num <= 1: return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False

    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]


# usage examples
print(is_prime(7))  # True
print(is_prime(10))  # False
print(filter_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [2, 3, 5, 7]