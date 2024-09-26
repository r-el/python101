list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]

# א. יצירת משתנה שיכיל את שלושת הרשימות מחוברות
combined_list = list1 + list2 + list3

# ב. הדפסת הרשימות בצורתן המקורית ע"י חיתוך אינדקסים
print("Original lists:")
print("List 1:", combined_list[:len(list1)])
print("List 2:", combined_list[len(list1):len(list1) + len(list2)])
print("List 3:", combined_list[len(list1) + len(list2):])

# ג. הדפסת הרשימה מהסוף להתחלה ע"י חיתוך אינדקסים
print("Combined list reversed:", combined_list[::-1])

# ד. הדפסת הרשימה מהתחלה עד האמצע כולל
mid_index = (len(combined_list) - 1) // 2
print("From start to middle:", combined_list[:mid_index + 1])

# ה. הדפסת הרשימה מהאמצע עד הסוף
print("From middle to end:", combined_list[mid_index + 1:])