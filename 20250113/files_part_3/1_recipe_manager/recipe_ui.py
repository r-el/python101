from recipe import Recipe

class RecipeUI:
    @staticmethod
    def display_menu():
        print("\n1. יצירת מתכון חדש")
        print("2. קריאת מתכון קיים")
        print("3. יציאה")
        return input("\nבחר אפשרות (1-3): ")

    @staticmethod
    def create_recipe_input():
        print("\n=== יצירת מתכון חדש ===")
        name = input("שם המתכון: ")
        print("\nהכנס את המרכיבים (מופרדים בפסיקים):")
        ingredients = input()
        print("\nהכנס את הוראות ההכנה (לחץ Enter פעמיים לסיום):")
        instructions = []
        while True:
            instruction = input()
            if instruction == "":
                break
            instructions.append(instruction)
        return Recipe(name, ingredients, "\n".join(instructions))

    @staticmethod
    def display_recipe(recipe):
        if recipe:
            print(recipe)

    @staticmethod
    def display_recipes(recipes):
        if not recipes:
            print("\nאין מתכונים להצגה.")
            return
            
        print(f"\nנמצאו {len(recipes)} מתכונים:")
        for recipe in recipes:
            print(recipe)
