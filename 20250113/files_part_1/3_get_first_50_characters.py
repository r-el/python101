def get_first_50_characters(filename: str) -> str:
    """
    Returns the first 50 characters of the specified file
    
    Args:
        filename (str): The name of the file to read from
    
    Returns:
        str: The first 50 characters of the file
    """
    with open(filename, 'r') as file:
        return file.read(50)

if __name__ == "__main__":
    # Example usage
    filename = "example.txt"
    first_50_characters = get_first_50_characters(filename)
    print(first_50_characters)
    print(len(first_50_characters))