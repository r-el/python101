shopping_items = []
shopping_prices = []

while True:
    item = input("Enter the name of the item (or 'Done' to finish): ")
    if item.lower() == 'done':
        break
    price = float(input(f"Enter the price for {item}: "))
    shopping_items.append(item)
    shopping_prices.append(price)

while True:
    print("\nMenu:")
    print("a. Show shopping list")
    print("b. Add item to the list")
    print("c. Replace an item")
    print("d. Ask for the price of an item")
    print("e. Replace the price of an item")
    print("f. Delete an item from the list")
    print("g. Exit")

    choice = input("Choose an option: ").lower()

    if choice == 'a':
        print("\nShopping List:")
        for item, price in zip(shopping_items, shopping_prices):
            print(f"{item}: ₪{price:.2f}")

    elif choice == 'b':
        new_item = input("Enter the name of the new item: ")
        if new_item in shopping_items:
            print(f"{new_item} is already in the list.")
        else:
            new_price = float(input(f"Enter the price for {new_item}: "))
            shopping_items.append(new_item)
            shopping_prices.append(new_price)

    elif choice == 'c':
        old_item = input("Enter the name of the item to replace: ")
        if old_item not in shopping_items:
            print(f"{old_item} is not in the list.")
        else:
            new_item = input("Enter the name of the new item: ")
            if new_item in shopping_items:
                print(f"{new_item} is already in the list.")
            else:
                index = shopping_items.index(old_item)
                shopping_items[index] = new_item
                new_price = float(input(f"Enter the price for {new_item}: "))
                shopping_prices[index] = new_price

    elif choice == 'd':
        item = input("Enter the name of the item to ask for its price: ")
        if item in shopping_items:
            index = shopping_items.index(item)
            print(f"The price of {item} is ${shopping_prices[index]:.2f}")
        else:
            print(f"{item} is not in the list.")

    elif choice == 'e':
        item = input("Enter the name of the item to replace its price: ")
        if item in shopping_items:
            index = shopping_items.index(item)
            new_price = float(input(f"Enter the new price for {item}: "))
            shopping_prices[index] = new_price
        else:
            print(f"{item} is not in the list.")

    elif choice == 'f':
        item = input("Enter the name of the item to delete: ")
        if item in shopping_items:
            index = shopping_items.index(item)
            shopping_items.pop(index)
            shopping_prices.pop(index)
        else:
            print(f"{item} is not in the list.")

    elif choice == 'g':
        break

    else:
        print("Invalid choice. Please try again.")