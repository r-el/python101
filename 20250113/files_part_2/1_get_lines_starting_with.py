def get_lines_starting_with(filename: str, prefix: str) -> list:
    """
    Returns a list of lines from the specified file that start with the given prefix
    
    Args:
        filename (str): The name of the file to read from
        prefix (str): The prefix to match at the start of each line
    
    Returns:
        list: A list of lines that start with the given prefix
    """
    matching_lines = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip().startswith(prefix):
                matching_lines.append(line.strip())
    return matching_lines

if __name__ == "__main__":
    # Example usage
    filename = "example.txt"
    prefix = "Hello"
    lines = get_lines_starting_with(filename, prefix)
    print(lines)