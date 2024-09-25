import random as rnd

car_companies = [
    "Toyota", "Ford", "Chevrolet", "Honda", "Nissan", 
    "BMW", "Mercedes", "Volkswagen", "Audi", "Hyundai", 
    "Kia", "Mazda", "Subaru", "Lexus", "Jeep", 
    "Dodge", "Ram", "GMC", "Tesla", "Volvo"
]

car_prices = [rnd.randint(10000, 100000) for _ in range(1000)]

production_years = list(range(1970, 2026))

car_colors = [
    "Red", "Blue", "Green", "Black", "White", 
    "Silver", "Gray", "Yellow", "Orange", "Purple", 
    "Brown", "Gold", "Beige", "Pink", "Maroon", 
    "Navy", "Teal", "Turquoise", "Magenta", "Lime", 
    "Olive", "Coral", "Ivory", "Lavender", "Mint", 
    "Peach", "Plum", "Tan", "Cyan", "Indigo"
]

ratings = list(range(1, 11))


# 10 random cars
cars = []
for _ in range(10):
    car = [
        rnd.choice(car_companies),  # שם החברה של הרכב
        rnd.choice(car_prices),     # מחיר הרכב
        rnd.choice(production_years), # שנת הייצור
        rnd.choice(car_colors),     # צבע הרכב
        rnd.choice(ratings)         # הדירוג שלו
    ]
    cars.append(car)

# print(cars)
for car in cars:
    print(f"Company: {car[0]}, Price: {car[1]}, Year: {car[2]}, Color: {car[3]}, Rating: {car[4]}")

# car with the highest rating
highest_rated_car = max(cars, key=lambda x: x[4])
print("\nHighest Rated Car:")
print(f"Company: {highest_rated_car[0]}, Price: {highest_rated_car[1]}, Year: {highest_rated_car[2]}, Color: {highest_rated_car[3]}, Rating: {highest_rated_car[4]}")

# car with the lowest rating
most_expensive_car = max(cars, key=lambda x: x[1])
print("\nMost Expensive Car:")
print(f"Company: {most_expensive_car[0]}, Price: {most_expensive_car[1]}, Year: {most_expensive_car[2]}, Color: {most_expensive_car[3]}, Rating: {most_expensive_car[4]}")

# car with the lowest rating
oldest_car = min(cars, key=lambda x: x[2])
print("\nOldest Car:")
print(f"Company: {oldest_car[0]}, Price: {oldest_car[1]}, Year: {oldest_car[2]}, Color: {oldest_car[3]}, Rating: {oldest_car[4]}")