def count_words_occurances(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word,0)+1

    for word, count in word_counts.items():
        print(f"{word} appeared {count} times")


count_words_occurances("Hi MY My name is is RAMANA RAMANA RAMANA")