def sort_people(people: list) -> list:
    def get_first_name(person):
        return person.split(", ")[0]

    def get_last_name(person):
        return person.split(", ")[1]

    def get_age(person):
        return int(person.split(", ")[2])

    while True:
        print("Choose an option to sort the list:")
        print("a. Sort by first names (ascending/descending)")
        print("b. Sort by last names (ascending/descending)")
        print("c. Sort by ages (ascending/descending)")
        print("d. Exit")
        
        choice = input("Enter your choice (a/b/c/d): ").strip().lower()
        
        if choice == 'a':
            order = input("Sort ascending or descending? (asc/desc): ").strip().lower()
            reverse = (order == 'desc')
            people.sort(key=get_first_name, reverse=reverse)
        elif choice == 'b':
            order = input("Sort ascending or descending? (asc/desc): ").strip().lower()
            reverse = (order == 'desc')
            people.sort(key=get_last_name, reverse=reverse)
        elif choice == 'c':
            order = input("Sort ascending or descending? (asc/desc): ").strip().lower()
            reverse = (order == 'desc')
            people.sort(key=get_age, reverse=reverse)
        elif choice == 'd':
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        print("Sorted list:")
        for person in people:
            print(person)
    
    return people

# Example usage
people_list = ["Ploni, Ben Ploni, 20", "Almoni, Ben Almoni, 25", "Someone, Else, 22"]
sorted_people = sort_people(people_list)