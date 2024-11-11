# class exercise #
def sum_all_elements(*args):
    return [i for i in args] # sum(args)

# usage
print(sum_all_elements(1, 2, 3, 4, 5))  # 15
print(sum_all_elements(1, 2, 3))  # 6
print(sum_all_elements(1, 2))  # 3