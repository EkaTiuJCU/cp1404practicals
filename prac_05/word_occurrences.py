"""Estimate time: 20 minutes
"""

def main():
    text = input("Text: ")
    words = text.split()
    word_to_count = {}

    for word in words:
        word = word.lower()
        word_to_count[word] = word_to_count.get(word, 0) + 1

    sorted_words = sorted(word_to_count.keys())
    max_word_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_to_count[word]}")

main()