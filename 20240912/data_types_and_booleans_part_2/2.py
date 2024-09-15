numbers = [int(input(f"Enter number {i}: ")) for i in range(3)]
print(numbers)

is_greater_15_and_less_than_150 = [(15 < num < 150) for num in numbers]
is_first_different = (numbers[0] != numbers[1]) and (numbers[0] != numbers[2])
is_first_equal = (numbers[0] == numbers[1]) or (numbers[0] == numbers[2])
is_second_equal_or_different = (numbers[1] == numbers[0]) or (numbers[1] != numbers[2])

print(is_greater_15_and_less_than_150, "–> Numbers are greater than 15 and less than 150")
print(is_first_different, "–> First number is different from both the second and third numbers")
print(is_first_equal, "–> First number is equal to the second or equal to the third")
print(is_second_equal_or_different, "Second number is equal to the first or different from the third")
print("~" * 50)


strings = [input(f"Enter string {i}: ") for i in range(3)]
numbers_from_strings = [int(s) for s in strings]
print(numbers_from_strings)

# Check if the numbers from strings are greater than 15 and less than 150
is_length_valid = [((15 < num < 150)) for num in numbers_from_strings]
print(is_length_valid, "Numbers from strings are greater than 15 and less than 150")

# Check if the first number from string is different from both the second and third numbers
is_first_string_different = (numbers_from_strings[0] != numbers_from_strings[1]) and (numbers_from_strings[0] != numbers_from_strings[2])
print(is_first_string_different, "First number from string is different from both the second and third numbers")

# Check if the first number from string is equal to the second or equal to the third
is_first_string_equal = (numbers_from_strings[0] == numbers_from_strings[1]) or (numbers_from_strings[0] == numbers_from_strings[2])
print(is_first_string_equal, "First number from string is equal to the second or equal to the third")

# Check if the second number from string is equal to the first or different from the third
is_second_string_equal_or_different = (numbers_from_strings[1] == numbers_from_strings[0]) or (numbers_from_strings[1] != numbers_from_strings[2])
print(is_second_string_equal_or_different, "Second number from string is equal to the first or different from the third")


