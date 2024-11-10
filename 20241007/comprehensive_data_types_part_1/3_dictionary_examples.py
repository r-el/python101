first_dict = {
    1: 'str1',
    2: 'str2',
    3: 'str3'
}
print("first_dict:", first_dict)

second_dict = {
    True: 'str1', 
    False: 'str2',
    True: 'str3' 
} # second_dict[True] = 'str3' 
print("second_dict:", second_dict)

third_dict = {
    (1,2): {"my", "set", 1}, 
    (3,4): {"my", "set", 2},
    (5,6): {"my", "set", 3} 
} # type( (1) ) = int # type( tuple(1) ) = tuple
print("third_dict:", third_dict)

fourth_dict = {
    # {1,2}: 1, # TypeError: unhashable type: 'set'
    # {3,4}: 2, # TypeError: unhashable type: 'set'
    # {5,6}: 3  # TypeError: unhashable type: 'set'
}
print("fourth_dict:", fourth_dict)

fifth_dict = {
    # [1,2]: True, # TypeError: unhashable type: 'list'
    # [3,4]: False, # TypeError: unhashable type: 'list'
    # [5,6]: True  # TypeError: unhashable type: 'list'
}
print("fifth_dict:", fifth_dict)

sixth_dict = {
    # {1:1,2:2}: 1, # TypeError: unhashable type: 'dict'
    # {3:3,4:4}: 2, # TypeError: unhashable type: 'dict'
    # {5:5,6:6}: 3  # TypeError: unhashable type: 'dict'
}
print("sixth_dict:", sixth_dict)