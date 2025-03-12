def reverse_the_setence_preserving_spaces(sentence):
    words = sentence.split()
    reverseSentence =""
    for word in words:
        reverseSentence = word + " " + reverseSentence
    return reverseSentence

sent= "REDDY RAMANA IS NAME MY"
print(f"Given sentence is--> {sent}")
print("Reversed Sentence is--> ", reverse_the_setence_preserving_spaces(sent))
