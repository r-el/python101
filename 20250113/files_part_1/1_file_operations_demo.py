
# a. Difference between RAM and non-volatile memory:
# RAM - volatile memory that resets when computer is off
# Non-volatile memory - retains data even when computer is off

# b. Examples of non-volatile memory:
# - Hard Disk Drive (HDD)
# - Solid State Drive (SSD) 
# - DVD/CD disk
# - USB/Flash drive


def demonstrate_file_close():
    """Demonstrates the purpose of close()"""
    # close() is used to free up resources used by the file
    # if not closed, the file may not be accessible by other programs
    # or the file may not be saved properly
    file = open("example.txt", "w")
    file.write("some text")
    file.close()  # important to close the file after use

def demonstrate_read_mode():
    """Demonstrates read mode operations"""
    with open("example.txt", "r") as f:
        content = f.read()
    print_file_content("example.txt")

def demonstrate_write_mode():
    """Demonstrates write mode operations"""
    with open("example.txt", "w") as f:
        f.write("new content")
    print_file_content("example.txt")

def demonstrate_append_mode():
    """Demonstrates append mode operations"""
    with open("example.txt", "a") as f:
        f.write("\nappended text")
    print_file_content("example.txt")

def explain_memory_and_files():
    """Main function demonstrating different file operations"""
    demonstrate_file_close()
    demonstrate_read_mode()
    demonstrate_write_mode()
    demonstrate_append_mode()

        
def print_file_content(filename):
    """ This function prints the content of a file """
    with open(filename, "r") as f:
        content = f.read()
        print("content:", content)

if __name__ == "__main__":
    explain_memory_and_files()