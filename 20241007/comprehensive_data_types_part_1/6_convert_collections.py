# א. המרת רשימה אחת לטאפל, אחת למחרוזת ואחת לסט
list1 = [1,2,3]
list2 = ['a', 'b', 'c', 1, 2]
list3 = [True, False, True]

list_to_tuple = tuple(list1)
list_to_string = "".join(map(str, list2))
list_to_set = set(list3)

print("List to Tuple:", list_to_tuple)
print("List to String:", list_to_string)
print("List to Set:", list_to_set)
print()


# ב. המרת טאפל אחד לרשימה, אחד למחרוזת ואחד לסט
tuple1 = (4, 5, 6)
tuple2 = ('d', 'e', 'f', 1, 2)
tuple3 = (False, True, False)

tuple_to_list = list(tuple1)
tuple_to_string = "".join(map(str, tuple2))
tuple_to_set = set(tuple3)

print("Tuple to List:", tuple_to_list)
print("Tuple to String:", tuple_to_string)
print("Tuple to Set:", tuple_to_set)
print()


# ג. המרת מחרוזת אחת לרשימה, אחת לטאפל ואחת לסט
string1 = "hello"
string2 = "world"
string3 = "python"

string_to_list = list(string1)
string_to_tuple = tuple(string2)
string_to_set = set(string3)

print("String to List:", string_to_list)
print("String to Tuple:", string_to_tuple)
print("String to Set:", string_to_set)
print()

# ד. המרת סט אחד לרשימה, אחד לטאפל ואחד למחרוזת
set1 = {7, 8, 9}
set2 = {'g', 'h', 'i'}
set3 = {True, False}

set_to_list = list(set1)
set_to_tuple = tuple(set2)
set_to_string = "".join(map(str,set3))

print("Set to List:", set_to_list)
print("Set to Tuple:", set_to_tuple)
print("Set to String:", set_to_string)






















# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = [True, False, True]

# tuple1 = (4, 5, 6)
# tuple2 = ('d', 'e', 'f')
# tuple3 = (False, True, False)

# string1 = "hello"
# string2 = "world"
# string3 = "python"

# set1 = {7, 8, 9}
# set2 = {'g', 'h', 'i'}
# set3 = {True, False}

# # א. המרת רשימה אחת לטאפל, אחת למחרוזת ואחת לסט
# list_to_tuple = tuple(list1)
# list_to_string = ''.join(map(str, list2))
# list_to_set = set(list3)

# # ב. המרת טאפל אחד לרשימה, אחד למחרוזת ואחד לסט
# tuple_to_list = list(tuple1)
# tuple_to_string = ''.join(tuple2)
# tuple_to_set = set(tuple3)

# # ג. המרת מחרוזת אחת לרשימה, אחת לטאפל ואחת לסט
# string_to_list = list(string1)
# string_to_tuple = tuple(string2)
# string_to_set = set(string3)

# # ד. המרת סט אחד לרשימה, אחד לטאפל ואחד למחרוזת
# set_to_list = list(set1)
# set_to_tuple = tuple(set2)
# set_to_string = ''.join(map(str, set3))
