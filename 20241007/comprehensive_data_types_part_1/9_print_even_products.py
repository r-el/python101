products = {f"product{i}": i for i in range(1,30)}

for key, val in products.items():
    if val % 2 == 0:
        print(f"{key}: {val}")