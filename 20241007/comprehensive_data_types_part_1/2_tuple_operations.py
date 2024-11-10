str_set = ('a', 'b', 'c', 'd')
print(str_set)

print("str_set[0]:", str_set[0])

value = input("Enter a value: ")

"""
str_set.append(value) # AttributeError: 'tuple' object has no attribute 'append'
str_set.add(value) # AttributeError: 'tuple' object has no attribute 'add'
"""

str_set += tuple(value)
print(str_set)

