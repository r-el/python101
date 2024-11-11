def analyze_sentence(sentence: str) -> tuple:
    words = sentence.split()
    num_words = len(words)
    num_letters = sum(1 for char in sentence if char.isalpha())
    return num_words, num_letters

# Example usage
sentence = "Hello, world! This is a test sentence with 123 numbers."
result = analyze_sentence(sentence)
print(result)  # (10, 40)