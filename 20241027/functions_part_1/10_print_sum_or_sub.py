def sum_multiple_numbers(*args):
    return sum(args)

def subtract_multiple_numbers(*args):
    return args[0] - sum(args[1:])

def print_sum_or_sub(a:int, b:int, c:int, sum_or_sub:bool):
    if sum_or_sub:
        print(sum_multiple_numbers(a, b, c))
    else:
        print(subtract_multiple_numbers(a, b, c))
       
# main
print_sum_or_sub(1, 2, 3, True)
print_sum_or_sub(1, 2, 3, False)
