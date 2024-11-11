def sum_multiple_numbers(*args):
    return sum(args)

def avg_multiple_numbers(*args):
    return sum_multiple_numbers(*args) / len(args)

def max_multiple_numbers(*args):
    return max(args)

# main
print(sum_multiple_numbers(1, 2, 3, 4, 5))
print(avg_multiple_numbers(1, 2, 3, 4, 5))
print(max_multiple_numbers(1, 2, 3, 4, 5))
