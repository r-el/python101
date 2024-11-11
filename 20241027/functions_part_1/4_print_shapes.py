def print_square(width: int, height: int):
    """מדפיסה ריבוע בגודל רצוי"""
    [print("* " * width) for _ in range(height)]
    
def print_rectangle(width: int, height: int):
    """מדפיסה מלבן בגודל רצוי"""
    [print("*" * width) for _ in range(height)]
 
def print_right_arrow(size: int):
    """מדפיסה חץ ימינה בגודל רצוי"""
    [print("* "*i) for i in range(1, size+1)] + [print("* "*i) for i in range(size-1,0,-1)]
    

# calling the functions
print_square(10, 10)
print()
print_square(8, 20)
print()
print_right_arrow(12)