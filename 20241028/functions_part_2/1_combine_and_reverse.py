def combine_and_reverse(str1: str, str2: str, str3: str) -> str:
    combined_str = str1 + str2 + str3
    reversed_str = combined_str[::-1]
    return reversed_str

# usage
print(combine_and_reverse('hello', 'world', 'python'))  # 'nohtypdlrowolleh'
