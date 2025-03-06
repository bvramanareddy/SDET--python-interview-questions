def reverse_each_word_sentence(sentence):
    words = sentence.split()
    rev_words = [word[::-1] for word in words]
    result= " ".join(rev_words)
    return result

print(reverse_each_word_sentence("abc de f"))
