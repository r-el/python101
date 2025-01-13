from recipe_ui import RecipeUI
from recipe_file_handler import RecipeFileHandler

class RecipeManager:
    def __init__(self):
        self.file_handler = RecipeFileHandler()
        self.ui = RecipeUI()

    def run(self):
        while True:
            choice = self.ui.display_menu()
            
            if choice == "1":
                recipe = self.ui.create_recipe_input()
                if self.file_handler.save_recipe(recipe):
                    print("\nהמתכון נשמר בהצלחה!")
            elif choice == "2":
                recipes = self.file_handler.read_all_recipes()
                if recipes:
                    self.ui.display_recipes(recipes)
                else:
                    print("\nאין מתכונים שמורים.")
            elif choice == "3":
                break
            else:
                print("אפשרות לא חוקית. נסה שוב.")

if __name__ == "__main__":
    manager = RecipeManager()
    manager.run()
