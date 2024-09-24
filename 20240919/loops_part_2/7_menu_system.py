users = {}
MAX_USERS = 3
MAX_ATTEMPTS = 3

def main_menu():
    print("תפריט ראשי:")
    print("א. כניסה למערכת")
    print("ב. יצירת משתמש")
    print("ג. יציאה מהמערכת")

def user_menu():
    print("תפריט משתמש:")
    print("א. להדפיס טקסט")
    print("ב. להחליף סיסמה")
    print("ג. למחוק את המשתמש")
    print("ד. לצאת מהמערכת ולחזור לתפריט הראשי")
    print("ה. לצאת לגמרי מהמערכת")

def create_user():
    if len(users) >= MAX_USERS:
        print("לא ניתן ליצור יותר משתמשים.")
        return
    while True:
        username = input("בחר שם משתמש (תעודת זהות): ")
        if username == "*":
            return
        if username in users:
            print("שם המשתמש כבר קיים.")
        else:
            break
    while True:
        password = input("בחר סיסמה: ")
        if password == "*":
            return
        users[username] = password
        print("המשתמש נוצר בהצלחה.")
        return

def login():
    while True:
        username = input("הכנס שם משתמש: ")
        if username == "*":
            return
        if username not in users:
            print("שם המשתמש לא קיים.")
        else:
            break
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        password = input("הכנס סיסמה: ")
        if password == "*":
            return
        if users[username] == password:
            print(f"ברוך הבא, {username}!")
            user_logged_in(username)
            return
        else:
            attempts += 1
            print("סיסמה שגויה.")
    print("נכשלת בכניסה למערכת.")

def user_logged_in(username):
    while True:
        user_menu()
        choice = input("בחר אופציה: ")
        if choice == "א":
            print("זהו טקסט לדוגמה.")
        elif choice == "ב":
            change_password(username)
        elif choice == "ג":
            delete_user(username)
            return
        elif choice == "ד":
            return
        elif choice == "ה":
            exit()
        else:
            print("בחירה לא חוקית.")

def change_password(username):
    while True:
        new_password = input("הכנס סיסמה חדשה: ")
        if new_password == "*":
            return
        users[username] = new_password
        print("הסיסמה שונתה בהצלחה.")
        return

def delete_user(username):
    del users[username]
    print("המשתמש נמחק בהצלחה.")

def main():
    while True:
        main_menu()
        choice = input("בחר אופציה: ")
        if choice == "א":
            login()
        elif choice == "ב":
            create_user()
        elif choice == "ג":
            print("יציאה מהמערכת.")
            break
        else:
            print("בחירה לא חוקית.")

if __name__ == "__main__":
    main()