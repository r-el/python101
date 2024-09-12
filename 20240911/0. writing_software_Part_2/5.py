discount = float(input("Please enter the current discount percentage in the store: "))

product1_name = input("Please enter the name of product 1: ")
product1_price = float(input("Please enter the price of product 1: "))

product2_name = input("Please enter the name of product 2: ")
product2_price = float(input("Please enter the price of product 2: "))

product3_name = input("Please enter the name of product 3: ")
product3_price = float(input("Please enter the price of product 3: "))

product1_discounted_price = product1_price * (1 - discount/100)
product2_discounted_price = product2_price * (1 - discount/100)
product3_discounted_price = product3_price * (1 - discount/100)

print(f"Product 1: {product1_name}")
print(f"Original Price: {product1_price}")
print(f"Discounted Price: {product1_discounted_price}")

print(f"Product 2: {product2_name}")
print(f"Original Price: {product2_price}")
print(f"Discounted Price: {product2_discounted_price}")

print(f"Product 3: {product3_name}")
print(f"Original Price: {product3_price}")
print(f"Discounted Price: {product3_discounted_price}")