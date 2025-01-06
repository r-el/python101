def add_reminder(reminders, date, task):
    if date in reminders:
        reminders[date].append(task)
    else:
        reminders[date] = [task]

def remove_reminder(reminders, date, task):
    if date in reminders:
        reminders[date].remove(task)
    else:
        print("Date not found")

def print_reminders(reminders):
    for date, tasks in reminders.items():
        print(f"Date: {date}, Tasks: {', '.join(tasks)}")

reminders = {}
add_reminder(reminders, "2024-09-15", "Doctor's Appointment")
add_reminder(reminders, "2024-09-15", "Grocery Shopping")
remove_reminder(reminders, "2024-09-15", "Meeting")
print_reminders(reminders)