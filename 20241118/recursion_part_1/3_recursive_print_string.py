def recursive_print_string(s):
    print(s)
    recursive_print_string(s[:-1])

recursive_print_string("example")