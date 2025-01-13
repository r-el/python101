def write_text_to_file(filename: str, text: str) -> bool:
    """
    Writes the specified text to the specified file
    
    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file
    
    Returns:
        bool: True if the text was written successfully, False if an error occurred
    """
    try:
        with open(filename, 'w') as file:
            file.write(text)
        return True
    except:
        return False

if __name__ == "__main__":
    # Example usage
    success = write_text_to_file("example.txt", "Hello, World!")
    print(success)  # Should print True

    failure = write_text_to_file("/nonexistent_directory/example.txt", "Hello, World!")
    print(failure)  # Should print False