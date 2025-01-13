from recipe_manager import RecipeManager

def main():
    try:
        # Create and run the recipe manager
        recipe_manager = RecipeManager()
        recipe_manager.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Recipe Manager!")

if __name__ == "__main__":
    main()
