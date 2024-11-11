def print_square(width: int, height: int):
    """מדפיסה ריבוע בגודל רצוי"""
    [print("* " * width) for _ in range(height)]
    
def print_square_by_symbol(width: int, height: int, symbol:str):
    """מדפיסה ריבוע של סמל בגודל רצוי"""
    [print(f"{symbol} " * width) for _ in range(height)]
    
def print_squares(width: int, height: int, symbol:str):
    print_square(10, 10)
    print_square_by_symbol(width, height, symbol)
    
# main
print_squares(5, 5, "@")