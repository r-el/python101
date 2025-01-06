# shgiaa: TypeError: create_list() takes 1 positional argument but 2 were given
""" tikun:
def create_list(n, step=1):
    return [i for i in range(n, 0, -step)]
"""
def create_list(n):
    return [i for i in range(n, 0, -1)]

print(create_list(5))
print(create_list(5, 2))