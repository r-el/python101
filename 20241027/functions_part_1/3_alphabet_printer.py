def get_ascii_range(_from: str, _to: str ) -> [] :
    return [chr(int_char) for int_char in range(ord(_from), (ord(_to)) +1)]

def print_english_alphabet():
    print(*get_ascii_range('a', 'z'))
    
def print_hebrew_alphabet():
    print(*get_ascii_range('א', 'ת'))
    
# call the functions
print_english_alphabet()
print_hebrew_alphabet()