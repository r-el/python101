nested_list = [[5, 4, 3], [1, 10, -5], [10, 30, 15, 15], [200, 20], [5, -3, 500, 1]]
numbers_to_modify = [3, 15, -3, 500, 1, 20]

print("Original nested list:")
print(nested_list)

print("\nNumbers to modify:")
for sublist in nested_list:
    for (i, num) in enumerate(sublist):
        if num in numbers_to_modify:
            print(num, end=" ")
            sublist[i] = 0

print("\n\nModified nested list:")
print(nested_list)