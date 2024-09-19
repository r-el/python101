print("בר בית קפה קטן - תפריט משקאות")
print("1. קפה שחור")
print("2. נס קפה")
print("3. שוקו")

choice = input("בחר את המשקה שלך (1/2/3): ")

if choice == '1':
    drink = "קפה שחור"
elif choice == '2':
    drink = "נס קפה"
elif choice == '3':
    drink = "שוקו"
else:
    print("בחירה לא חוקית")
    exit()

sugar = input("האם אתה רוצה סוכר במשקה? (yes/no): ")

if sugar.lower() == 'yes':
    sugar_text = "עם סוכר"
elif sugar.lower() == 'no':
    sugar_text = "ללא סוכר"
else:  
    print("בחירה לא חוקית")
    exit()

print(f"ההזמנה שלך בדרך: {drink} {sugar_text}")