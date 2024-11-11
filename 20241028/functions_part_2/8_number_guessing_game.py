import random

def print_menu():
    print("1. Start New Game")
    print("2. Exit")

def get_valid_input(prompt, input_type=int):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def start_new_game():
    print("Starting a new game...")
    while True:
        lower_bound = get_valid_input("Enter the lower bound of the range: ")
        upper_bound = get_valid_input("Enter the upper bound of the range: ")
        if lower_bound <= upper_bound:
            break
        else:
            print("Lower bound must be less than or equal to upper bound. Please try again.")
    max_attempts = get_valid_input("Enter the maximum number of attempts: ")
    
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while attempts < max_attempts:
        guess = get_valid_input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
        attempts += 1
        
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    
    if guess != secret_number:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")

def main():
    while True:
        print_menu()
        choice = get_valid_input("Enter your choice: ")
        
        if choice == 1:
            start_new_game()
        elif choice == 2:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()