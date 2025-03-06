from collections import Counter

def count_words_occurrence_in_sentence(sentence):
    words = sentence.split()  # Split sentence into words
    word_counts = Counter(words)  # Count occurrences

    for word, count in word_counts.items():
        print(f'"{word}" appeared {count} time{"s" if count > 1 else ""}')

# Example usage:
count_words_occurrence_in_sentence("HELLO WELCOME TO TO PYTHON PYTHON PROGRAMMINg")
