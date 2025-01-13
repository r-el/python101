from task_manager import TaskManager

def print_menu():
    print("\n=== מנהל המשימות ===")
    print("1. הצג את כל המשימות")
    print("2. הוסף משימה חדשה")
    print("3. סמן משימה כבוצעה")
    print("4. מחק משימה")
    print("5. יציאה")
    print("=" * 20)

def main():
    manager = TaskManager()
    
    while True:
        print_menu()
        choice = input("בחר אפשרות (1-5): ")
        print()
        
        if choice == "1":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("אין משימות")
            else:
                for i, task in enumerate(tasks):
                    status = "בוצע" if task.completed else "לא בוצע"
                    print(f"{i+1}. {task.title} - {task.description}")
                    print(f"   תאריך יעד: {task.due_date}")
                    print(f"   סטטוס: {status}\n")
        
        elif choice == "2":
            title = input("הכנס כותרת: ")
            description = input("הכנס תיאור: ")
            due_date = input("הכנס תאריך יעד: ")
            manager.add_task(title, description, due_date)
            print("המשימה נוספה בהצלחה")
        
        elif choice == "3":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("אין משימות")
                continue  # Returns to the start of the while loop
                
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.title}")
            
            try:
                index = int(input("בחר מספר משימה לסימון כבוצעה: ")) - 1
                if manager.mark_task_completed(index):
                    print("המשימה סומנה כבוצעה")
                else:
                    print("מספר משימה לא תקין")
            except ValueError:
                print("קלט לא תקין")
        
        elif choice == "4":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("אין משימות")
                continue  # Returns to the start of the while loop
                
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.title}")
            
            try:
                index = int(input("בחר מספר משימה למחיקה: ")) - 1
                if manager.delete_task(index):
                    print("המשימה נמחקה בהצלחה")
                else:
                    print("מספר משימה לא תקין")
            except ValueError:
                print("קלט לא תקין")
        
        elif choice == "5":
            print("להתראות!")
            break
        
        else:
            print("אפשרות לא תקינה")

if __name__ == "__main__":
    main()
