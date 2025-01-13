from recipe import Recipe

class RecipeFileHandler:
    def __init__(self, filename="recipe.txt"):
        self.filename = filename

    def read_recipe(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
                parts = content.split('###')
                parts = [part.strip() for part in parts[1:] if part.strip()]
                
                if len(parts) >= 2:
                    recipe_name = parts[0]
                    remaining = parts[1].split('\n', 1)
                    ingredients = remaining[0].strip()
                    instructions = remaining[1].strip() if len(remaining) > 1 else ""
                    return Recipe(recipe_name, ingredients, instructions)
                return None
        except FileNotFoundError:
            print("Error: Recipe file not found!")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def read_all_recipes(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if not content:  # Check if file is empty
                    return []
                    
                recipe_blocks = content.split('###')
                recipes = []
                
                for block in recipe_blocks:
                    if not block.strip():
                        continue
                        
                    parts = block.strip().split('\n')
                    if len(parts) >= 2:
                        recipe_name = parts[0].strip()
                        ingredients = parts[1].strip()
                        instructions = '\n'.join(parts[2:]).strip()
                        recipes.append(Recipe(recipe_name, ingredients, instructions))
                
                return recipes
        except FileNotFoundError:
            print("Error: Recipe file not found!")
            return []
        except Exception as e:
            print(f"Error reading file: {e}")
            return []

    def save_recipe(self, recipe):
        try:
            with open(self.filename, 'a', encoding='utf-8') as file:
                # Add a newline before the recipe only if file is not empty
                if file.tell() > 0:
                    file.write('\n')
                file.write(recipe.to_file_format())
            return True
        except Exception as e:
            print(f"שגיאה בשמירת המתכון: {e}")
            return False
