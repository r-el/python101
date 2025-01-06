def word_count(text):
    words = text.split(" ")
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

text = "This is a sample text with some repeated words. This is a test."
result = word_count(text)
print(result["This"])