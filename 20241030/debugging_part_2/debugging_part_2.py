# 1_task_management.py
def add_task(tasks, task_name, status='Pending'):
    tasks[task_name] = {'status': status}

def update_task_status(tasks, task_name, new_status):
    if task_name in tasks:
        tasks[task_name]['status'] = new_status
    else:
        print("Task not found")
    return tasks

def get_pending_tasks(tasks):
    pending_tasks = []
    for task, details in tasks.items():
        if details['status'] == 'Pending':
            pending_tasks.append(task)
    return pending_tasks

tasks = {}
add_task(tasks, "Task 1", "Pending")
add_task(tasks, "Task 2", "Completed")
add_task(tasks, "Task 3", "Pending")
print(get_pending_tasks(tasks))
print(update_task_status(tasks, "Task 4", "Completed"))
print(get_pending_tasks(tasks))


# 2_calculate_average.py
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
print("Average:", calculate_average(numbers))
numbers = []
print("Average:", calculate_average(numbers))


# 3_calculate_median.py
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return median

numbers = [1, 3, 5, 7, 9]
print("Median:", calculate_median(numbers))
numbers = [1, 2, 3, 4, 5, 6]
print("Median:", calculate_median(numbers))


# 4_employee_management.py
def add_employee(employees, name, salary):
    employees[name] = {'salary': salary}

def increase_salary(employees, name, amount):
    if name in employees:
        employees[name]['salary'] += amount
    else:
        print("Employee not found")
    return employees

employees = {}
add_employee(employees, "John", 50000)
add_employee(employees, "Jane", "60000")
print(increase_salary(employees, "John", 5000))
print(increase_salary(employees, "Doe", 5000))


# 5_combine_lists.py
def combine_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

list1 = [1, 2, 3, 4]
list2 = [5, 6]
print("Combined list:", combine_lists(list1, list2))


# 6_word_count.py
def word_count(text):
    words = text.split(" ")
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

text = "This is a sample text with some repeated words. This is a test."
result = word_count(text)
print(result["This"])


# 7_bank_account.py
def deposit(account, amount):
    account['balance'] += amount

def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds")
    else:
        account['balance'] -= amount

def get_balance(account):
    return account['balance']

def print_statement(account):
    print("Account balance:", get_balance(account)
    print("Transactions:")
    for transaction in account['transactions']:
        print(transaction)

account = {'balance': 100}
deposit(account, 50)
withdraw(account, 30)
withdraw(account, 200)
print_statement(account)


# 8_shipment_tracking.py
def add_package(shipments, tracking_number, details):
    shipments[tracking_number] = details

def update_package_status(shipments, tracking_number, status):
    if tracking_number in shipments:
        shipments[tracking_number]['status'] = status
    else:
        print(f"Tracking number {tracking_number} not found")

def get_package_details(shipments, tracking_number):
    return shipments[tracking_number]

def print_shipments(shipments):
    for tracking_number, details in shipments.items():
        print(f"Tracking Number: {tracking_number}, Status: {details['status']}, Destination: {details['destination']}")

shipments = {}
add_package(shipments, "ABC123", {'status': 'In Transit', 'destination': 'New York'})
add_package(shipments, "XYZ789", {'status': 'Delivered', 'destination': 'Los Angeles'})
update_package_status(shipments, "XYZ789", "Returned")
print_shipments(shipments)
print("Details for 'DEF456':", get_package_details(shipments, "DEF456"))


# 9_reminder_management.py
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


