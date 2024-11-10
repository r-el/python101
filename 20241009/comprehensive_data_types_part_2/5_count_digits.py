def count_digits_in_number(number):
    digit_count = {i:0 for i in range(10)}
    
    number = abs(number)
    
    while number:
        digit_count[number%10] += 1
        number //=10
    
    return digit_count


# # Example usage
number = int(input("Please enter a number: "))
digit_count_dict = count_digits_in_number(number)
print(digit_count_dict)