products = {
    "product1": 100,
    "product2": 200,
    "product3": 300,
    "product4": 400,
    "product5": 500
}

reversed_products = {value: key for key, value in products.items()}

# reversed_products = {}
# for key, value in products.items():
#     reversed_products[value] = key

print(reversed_products)