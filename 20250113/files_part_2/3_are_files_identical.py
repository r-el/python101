def are_files_identical(file1: str, file2: str) -> bool:
    """
    Compares the contents of two files line by line to determine if they are identical.

    Args:
        file1 (str): The name of the first file.
        file2 (str): The name of the second file.

    Returns:
        bool: True if the files are identical, False otherwise.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            
            if not line1 and not line2:
                return True
            if line1 != line2:
                return False

if __name__ == "__main__":
    # Example usage
    file1 = "file1.txt"
    file2 = "file2.txt"
    result = are_files_identical(file1, file2)
    print(result)