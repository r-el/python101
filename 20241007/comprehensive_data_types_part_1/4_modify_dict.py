my_dict = {
    1: 'str1',
    2: 'str2',
    3: 'str3',
    4: 'str4',
    5: 'str5'
}

print("Original dictionary values:")
for key in my_dict:
    print(f"Key {key}: {my_dict[key]}")

del my_dict[1]
del my_dict[2]

my_dict[3] = 'new_str3'
my_dict[4] = 'new_str4'
my_dict[5] = 'new_str5'

print("\nModified dictionary values:")
for key in my_dict:
    print(f"Key {key}: {my_dict[key]}")
