def reverse_dict(input_dict):
    reversed_dict = {}
    for key, value in input_dict.items():
        if value in reversed_dict:
            reversed_dict[value].append(key)
        else:
            reversed_dict[value] = [key]
    return reversed_dict

products = {
    "product1": 100,
    "product2": 200,
    "product3": 100,
    "product4": 400,
    "product5": 200,
    "product6": 300,
    "product7": 400,
    "product8": 500,
}

reversed_products = reverse_dict(products)

print(reversed_products)