def recursive_power(base, exponent):
    # Base case
    if exponent == 0:
        return 1
    
     # For negative exponents
    elif exponent < 0:
        return 1 / recursive_power(base, -exponent)
    
    return base * recursive_power(base, exponent - 1)

print(recursive_power(2, 3)) # 8
print(recursive_power(2, -3)) # 0.125

