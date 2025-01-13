def write_hello_world(filename: str) -> None:
    """
    Writes 'Hello, World!' to the specified file
    
    Args:
        filename (str): The name of the file to write to
    """
    with open(filename, 'w') as file:
        file.write("Hello, World!")

def print_file_content(filename: str) -> None:
    """
    Prints the content of the specified file
    
    Args:
        filename (str): The name of the file to read from
    """
    pass
    with open(filename, 'r') as file:
        print(file.read())

if __name__ == "__main__":
    write_hello_world("example.txt")
    print_file_content("example.txt")