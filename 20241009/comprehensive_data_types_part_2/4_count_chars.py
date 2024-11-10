def count_characters_in_string(input_string):
    if len(input_string) < 20:
        raise ValueError("The input string must be at least 20 characters long.")
    
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count


# Example usage
input_string = input("Please enter a string with at least 20 characters: ")
char_count_dict = count_characters_in_string(input_string)
print(char_count_dict)