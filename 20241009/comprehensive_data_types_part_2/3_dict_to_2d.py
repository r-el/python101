def dict_to_2d_list(input_dict):
    return [[key, val] for key, val in input_dict.items()]

def dict_to_2d_tuple(input_dict):
    return tuple((key, val) for key, val in input_dict.items())


# Example usage
input_dict = {
    "product1": 100,
    "product2": 200,
    "product3": 300,
    "product4": 400,
    "product5": 500
}

list_2d = dict_to_2d_list(input_dict)
tuple_2d = dict_to_2d_tuple(input_dict)

print("2D List:", list_2d)
print("2D Tuple:", tuple_2d)
