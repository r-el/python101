# shgiaa: IndexError: list index out of range
""" tikun: להוסיף בדיקה לפני הפלט שהאינדקס המבוקש קיים ברשימה
if index1 >= len(lst) or index2 >= len(lst):
    print("The index is out of range")
    return
"""
def swap_elements(lst, index1, index2):
    if index1 >= len(lst) or index2 >= len(lst):
        print("The index is out of range")
        return
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

my_list = [10, 20, 30, 40]
print(swap_elements(my_list, 1, 3))
print(swap_elements(my_list, 1, 5))