# def  create_nested_dict(input_string):
    
        # symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

    
#     return result




# # Example usage
# input_string = input("Please enter a string containing words, numbers, and symbols: ")
# result = create_nested_dict(input_string)
# print(result)
























def create_nested_dict(input_string):
    words = input_string.split()
    print(words)
    nested_dict = {}
    
    # Count words
    for word in words:
        if word.isalpha():
            if word in nested_dict:
                nested_dict[word] += 1
            else:
                nested_dict[word] = 1
    
    # Count digits
    nested_dict["numbers"] = {str(i): 0 for i in range(10)}
    for char in input_string:
        if char.isdigit():
            nested_dict["numbers"][char] += 1
    
    # Count symbols
    symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
    nested_dict["symbols"] = {symbol: 0 for symbol in symbols}
    for char in input_string:
        if char in symbols:
            nested_dict["symbols"][char] += 1
    
    return nested_dict

# Example usage
input_string = input("Please enter a string containing words, numbers, and symbols: ")
result = create_nested_dict(input_string)
print(result)