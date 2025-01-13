from glossary_entry import GlossaryEntry

class GlossaryManager:
    def __init__(self, filename="glossary.txt"):
        self.filename = filename
        self.entries = {}
        self.load_entries()

    def load_entries(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    if '|' in line:
                        term, definition = line.strip().split('|', 1)
                        self.entries[term.strip()] = GlossaryEntry(term.strip(), definition.strip())
        except FileNotFoundError:
            pass

    def save_entries(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            # Sort entries by term when saving
            sorted_entries = sorted(self.entries.values(), key=lambda x: x.term)
            for entry in sorted_entries:
                file.write(f"{entry}\n")

    def search_term(self, term):
        return self.entries.get(term)

    def add_term(self, term, definition):
        if term not in self.entries:
            self.entries[term] = GlossaryEntry(term, definition)
            self.save_entries()
            return True
        return False

    def update_term(self, term, new_definition):
        if term in self.entries:
            self.entries[term].definition = new_definition
            self.save_entries()
            return True
        return False

    def get_all_terms(self):
        return sorted(self.entries.keys())
