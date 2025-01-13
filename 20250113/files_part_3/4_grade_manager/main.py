from grade_manager import GradeManager

def print_menu():
    print("\n=== מערכת ניהול ציונים ===")
    print("1. הוספת תלמיד חדש")
    print("2. הוספת ציון לתלמיד")
    print("3. הצגת ממוצע של תלמיד במקצוע")
    print("4. הצגת כל הציונים של תלמיד")
    print("5. יציאה")
    print("=" * 25)

def main():
    manager = GradeManager()
    
    while True:
        print_menu()
        choice = input("בחר אפשרות (1-5): ")
        
        if choice == "1":
            id = input("הכנס מספר זהות: ")
            name = input("הכנס שם תלמיד: ")
            if manager.add_student(id, name):
                print("התלמיד נוסף בהצלחה")
            else:
                print("תלמיד כבר קיים במערכת")
                
        elif choice == "2":
            id = input("הכנס מספר זהות: ")
            subject = input("הכנס שם מקצוע: ")
            try:
                grade = float(input("הכנס ציון: "))
                if manager.add_grade(id, subject, grade):
                    print("הציון נוסף בהצלחה")
                else:
                    print("תלמיד לא נמצא")
            except ValueError:
                print("ציון לא תקין")
                
        elif choice == "3":
            id = input("הכנס מספר זהות: ")
            subject = input("הכנס שם מקצוע: ")
            student = manager.get_student(id)
            if student:
                average = student.get_average(subject)
                print(f"הציון במקצוע {subject}: {average}")
            else:
                print("תלמיד לא נמצא")
                
        elif choice == "4":
            id = input("הכנס מספר זהות: ")
            student = manager.get_student(id)
            if student:
                print(f"\nציוני התלמיד {student.name}:")
                for subject, grades in student.grades.items():
                    print(f"{subject}:")
                    print(f"  ציונים: {', '.join(str(g) for g in grades)}")
                    print(f"  ממוצע: {student.get_average(subject):.2f}")
                print(f"ממוצע כללי: {student.get_average():.2f}")
            else:
                print("תלמיד לא נמצא")
                
        elif choice == "5":
            print("להתראות!")
            break
            
        else:
            print("אפשרות לא תקינה")

if __name__ == "__main__":
    main()
