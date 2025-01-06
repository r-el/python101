def where_is_my_chair(chair_number, answer):
    # Base case
    if chair_number == 0:
        return answer
    
    # Recursive call with chair_number - 1 and answer + 1
    return where_is_my_chair(chair_number - 1, answer + 1)
    
# Example usage
result = where_is_my_chair(5, 0)
print(result)
