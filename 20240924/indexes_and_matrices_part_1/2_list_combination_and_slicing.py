items = []

for _ in range(5):
    item = input("Please enter an item: ")
    items.append(item)
print(items)
print() # For spacing

print("Last item:", items[-1]) 
items.remove(items[-1])
print("Last item removed:", items)
print() # For spacing


print("Last item:", items[-1])
last_item = items.pop()
print("Last item popped:", last_item)
print() # For spacing



new_item = input("Please enter another item: ")
items.insert(0, new_item)
print("First item added:", items)
print() # For spacing


another_item = input("Please enter one more item: ")
items.insert(-1, another_item)
print("Second to last item added:", items)

# (BONUS) Insert to last index using insert() method
# items.insert(len(items), "Last item")
# print("Last item added:", items)
