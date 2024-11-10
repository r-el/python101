def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key, value in dict1.items():
        if key in merged_dict:
            merged_dict[key].append(value)
        else:
            merged_dict[key] = [value]
            
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key].append(value)
        else:
            merged_dict[key] = [value]
    return merged_dict

# Example usage
dict1 = {
    "product1": 100,
    "product2": 200,
    "product3": 300,
}

dict2 = {
    "product2": 250,
    "product3": 300,
    "product4": 400,
}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)