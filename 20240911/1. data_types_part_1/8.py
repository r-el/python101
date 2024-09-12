# הדפיסו את התוצאה לפי שלושת הסעיפים הקודמים.
# .8 המר את כל המשתנים הבאים ל:
# א. str
# ב. int
# ג. float
# ד. bool
# אם קרתה שגיאה, נסו להבין למה.
# a. first_num = 10
# b. first_str = “1”
# c. second_str = “hello”
# d. third_str = “5.7”
# e. first_bool = True
# f. second_bool = False
# g. second_num = 15.5

first_num = 10
first_str = "1"
second_str = "hello"
third_str = "5.7"
first_bool = True
second_bool = False
second_num = 15.5

# א. str
print(str(first_num)) # 10
print(str(first_str)) # 1
print(str(second_str)) # hello
print(str(third_str)) # 5.7
print(str(first_bool)) # True
print(str(second_bool)) # False
print(str(second_num)) # 15.5

# ב. int
print(int(first_num)) # 10
print(int(first_str)) # 1
# print(int(second_str)) # ValueError: invalid literal for int() with base 10: 'hello'
# print(int(third_str)) # ValueError: invalid literal for int() with base 10: '5.7'
print(int(first_bool)) # 1
print(int(second_bool)) # 0
print(int(second_num)) # 15

# ג. float
print(float(first_num)) # 10.0
print(float(first_str)) # 1.0
# print(float(second_str)) # ValueError: could not convert string to float: 'hello'
print(float(third_str)) # 5.7
print(float(first_bool)) # 1.0
print(float(second_bool)) # 0.0
print(float(second_num)) # 15.5

# ד. bool
print(bool(first_num)) # True
print(bool(first_str)) # True
print(bool(second_str)) # True
print(bool(third_str)) # True
print(bool(first_bool)) # True
print(bool(second_bool)) # False
print(bool(second_num)) # True