def are_files_identical(file1, file2):
    try:
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            while True:
                chunk1 = f1.read(4096)
                chunk2 = f2.read(4096)
                
                if chunk1 != chunk2:
                    return False
                
                if not chunk1:  # End of file
                    return True
    except FileNotFoundError:
        return False

# Example usage:
print(are_files_identical('file1.txt', 'file2.txt'))