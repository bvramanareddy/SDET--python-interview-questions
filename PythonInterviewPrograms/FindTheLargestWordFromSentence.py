def find_the_largest_word_from_Sentence(sentence):
    words = sentence.split(" ")
    largest_word = ""
    for word in words:
        if (len(word) > len(largest_word)):
            largest_word = word
    return largest_word


sentence = "Hi my name is RAMANA reddy"
print(f"Given Sentence is => {sentence}")
print(f"The largest word is {find_the_largest_word_from_Sentence(sentence)}")
