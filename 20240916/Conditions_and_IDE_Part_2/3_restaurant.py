# תפריט מנות עיקריות
# (name ,price, time) 
main_courses = {
    'א': ('פרגיות', 80, 15),
    'ב': ('חזה עוף', 50, 10),
    'ג': ('דג מושט', 40, 20),
}
# תפריט תוספות
side_dishes = {
    'א': ('אורז', 25, 8),
    'ב': ('צ\'יפס', 20, 12),
    'ג': ('בטטה מטוגנת', 15, 15),
    'ד': ('בלי תוספת', 0, 0)
}

# הצגת תפריט מנות עיקריות
print("בחר מנה עיקרית:")
for key, value in main_courses.items():
    print(f"{key}. {value[0]} - {value[1]} ש\"ח")

# קבלת בחירת המשתמש למנה עיקרית
main_choice = input("הכנס את הבחירה שלך (א/ב/ג): ").strip()

if main_choice not in main_courses:
    print("בחירה לא חוקית")
    exit()

main_course = main_courses[main_choice]

# הצגת תפריט תוספות
print("בחר תוספת:")
for key, value in side_dishes.items():
    print(f"{key}. {value[0]} - {value[1]} ש\"ח")
side_choice = input("הכנס את הבחירה שלך (א/ב/ג/ד): ").strip()

if side_choice not in side_dishes:
    print("בחירה לא חוקית")
    exit()

side_dish = side_dishes[side_choice]

# חישוב מחיר וזמן הכנה כולל
total_price = main_course[1] + side_dish[1]
total_time = main_course[2] + side_dish[2]

# הצגת פרטי ההזמנה למשתמש
print(f"הזמנה בוצעה בהצלחה! פרטי ההזמנה שלך:")
print(f"מנה עיקרית: {main_course[0]} - {main_course[1]} ש\"ח")
print(f"תוספת: {side_dish[0]} - {side_dish[1]} ש\"ח")
print(f"מחיר כולל: {total_price} ש\"ח")
print(f"זמן הכנה כולל: {total_time} דקות")

# טיפ?
tip_choice = input("האם תרצה להוסיף טיפ? (כן/לא): ").strip().lower()

if tip_choice == 'כן':
    total_price *= 1.1  # הוספת 10% טיפ למחיר הכולל
    print(f"תודה! המחיר החדש כולל טיפ: {total_price:.2f} ש\"ח")
else:
    print("אל תחזור למסעדה שלנו יותר")  # הודעה במקרה של אי הוספת טיפ