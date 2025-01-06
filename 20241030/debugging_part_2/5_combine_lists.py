def combine_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

list1 = [1, 2, 3, 4]
list2 = [5, 6]
print("Combined list:", combine_lists(list1, list2))