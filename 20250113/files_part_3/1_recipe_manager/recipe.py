class Recipe:
    def __init__(self, name="", ingredients="", instructions=""):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def to_file_format(self):
        return f"###{self.name}\n\n###{self.ingredients}\n{self.instructions}"

    def __str__(self):
        return (f"\n{'=' * 40}\n"
                f"המתכון: {self.name}\n"
                f"{'=' * 40}\n\n"
                f"מרכיבים:\n{self.ingredients}\n\n"
                f"הוראות הכנה:\n{self.instructions}\n"
                f"{'=' * 40}")
