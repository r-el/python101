products = {f"product{i}": i*100 for i in range(1,11)}

# for key in products:
#     print(f"{key}: {products[key]}")

for key, val in products.items():
    print(f"{key}: {val}")
    
elements = (i for i in range(1,11))

for element in elements:
    print(element, end=" ")
print() # For a new line
