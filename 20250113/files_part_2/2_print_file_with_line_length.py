def print_file_with_line_length(filename: str):
    """
    Prints the content of the specified file line by line.
    Each line is prefixed with its length in characters, followed by two asterisks,
    the content of the line, and two asterisks at the end to denote the end of the line.
    
    Args:
        filename (str): The name of the file to read from
    """
    with open(filename, 'r') as file:
        for line in file:
            line_length = len(line.strip())
            print(f"{line_length} **{line.strip()}**")

if __name__ == "__main__":
    # Example usage
    filename = "example.txt"
    print_file_with_line_length(filename)