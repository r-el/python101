def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def find_string_with_letters(sorted_list, first_letter, second_letter):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid][0] == first_letter:
            # Perform binary search within the found string to find the second_letter
            return binary_search(sorted_list[mid], second_letter)
        elif sorted_list[mid][0] < first_letter:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Test examples
sorted_list = ["abc", "bde", "cfg", "dhk", "eij"]
print(find_string_with_letters(sorted_list, 'c', 'f'))  # Should print True
print(find_string_with_letters(sorted_list, 'b', 'a'))  # Should print False
print(find_string_with_letters(sorted_list, 'd', 'h'))  # Should print True
print(find_string_with_letters(sorted_list, 'e', 'k'))  # Should print False