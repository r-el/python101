numbers = []

while True:
    user_input = input("Enter a number or 'exit' to finish: ")
    
    if user_input.lower() == 'exit':
        if not numbers:
            print("You haven't entered any numbers. Please enter at least one number before exiting.")
        else:
            break
    else:
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    print("\nMenu:")
    print("a. Display the count of numbers entered")
    print("b. Display the sum of all numbers entered")
    print("c. Display the count of even and odd numbers")
    print("d. Display the largest and smallest number")
    print("e. Display the average of all numbers entered")
    print("f. Exit")

    choice = input("Choose an option: ").lower()

    if choice == 'a':
        print(f"Count of numbers entered: {len(numbers)}")
    elif choice == 'b':
        print(f"Sum of all numbers entered: {sum(numbers)}")
    elif choice == 'c':
        even_count = sum(1 for num in numbers if num % 2 == 0)
        odd_count = len(numbers) - even_count
        print(f"Count of even numbers: {even_count}")
        print(f"Count of odd numbers: {odd_count}")
    elif choice == 'd':
        print(f"Largest number: {max(numbers)}")
        print(f"Smallest number: {min(numbers)}")
    elif choice == 'e':
        print(f"Average of all numbers entered: {sum(numbers) / len(numbers)}")
    elif choice == 'f':
        break
    else:
        print("Invalid choice. Please choose a valid option.")