def word_count(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    sample_text = "Python is powerful and fun to learn with VS Code."
    print("Text:", sample_text)
    print("Word count:", word_count(sample_text))
