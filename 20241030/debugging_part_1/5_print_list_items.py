# shgiaa: TypeError: object of type 'int' has no len()
""" tikun: להוסיף בדיקה לפני הלולאה שהפרמטר שהתקבל הוא רשימה
if not isinstance(items, list):
    print("The parameter is not a list")
    return
"""
def print_list_items(items):
    for i in range(len(items)):
        print(items[i])

print_list_items([10, 20, 30, 40])
print_list_items(12345)