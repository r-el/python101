def search_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return "Value not found"

def remove_value(lst, value):
    if value in lst:
        lst.remove(value)
    return lst

my_list = [1, 2, 3, 4, 5]
print(search_index(my_list, 3))
print(remove_value(my_list, 3))
print(search_index(my_list, 3))