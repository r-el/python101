# shgiaa: TypeError: 'int' object is not iterable
# tikun: lst += [value]

def add_to_list(lst, value):
    lst += value
    return lst

print(add_to_list([1, 2, 3], 4))