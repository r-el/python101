from glossary_manager import GlossaryManager

def print_menu():
    print("\n=== מילון מונחים ===")
    print("1. חיפוש מונח")
    print("2. הוספת מונח חדש")
    print("3. עדכון הגדרה")
    print("4. הצגת כל המונחים")
    print("5. יציאה")
    print("=" * 20)

def main():
    manager = GlossaryManager()

    while True:
        print_menu()
        choice = input("בחר אפשרות (1-5): ")
        print()

        if choice == "1":
            term = input("הכנס מונח לחיפוש: ")
            entry = manager.search_term(term)
            if entry:
                print(f"הגדרה: {entry.definition}")
            else:
                print("מונח לא נמצא")

        elif choice == "2":
            term = input("הכנס מונח חדש: ")
            definition = input("הכנס הגדרה: ")
            if manager.add_term(term, definition):
                print("המונח נוסף בהצלחה")
            else:
                print("המונח כבר קיים")

        elif choice == "3":
            term = input("הכנס מונח לעדכון: ")
            if manager.search_term(term):
                new_definition = input("הכנס הגדרה חדשה: ")
                manager.update_term(term, new_definition)
                print("ההגדרה עודכנה בהצלחה")
            else:
                print("מונח לא נמצא")

        elif choice == "4":
            terms = manager.get_all_terms()
            if terms:
                print("רשימת המונחים:")
                for term in terms:
                    entry = manager.search_term(term)
                    print(f"{term} | {entry.definition}")
            else:
                print("המילון ריק")

        elif choice == "5":
            print("להתראות!")
            break

        else:
            print("אפשרות לא תקינה")

if __name__ == "__main__":
    main()
