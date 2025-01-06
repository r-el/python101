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