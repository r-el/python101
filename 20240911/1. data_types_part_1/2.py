num_str1 = "10"
num_str2 = "20"
num_str3 = "30"

num_int1 = 40
num_int2 = 50
num_int3 = 60

result_str = num_str1 + num_str2 + num_str3
print("Addition of numbers as strings:", result_str)

result_int = num_int1 + num_int2 + num_int3
print("Addition of numbers as integers:", result_int)

result_str_conversion = str(num_int1) + num_str1
print("Addition of an integer and a string:", result_str_conversion)

result_int_conversion = int(num_str1) + num_int1
print("Addition of a string and an integer:", result_int_conversion)