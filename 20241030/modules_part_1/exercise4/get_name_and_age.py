print("start of get_name_and_age.py") 
def get_name_and_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")
print("end of get_name_and_age.py")