def find_the_longest_length_string(s):
    words= s.split(" ")
    max_length = max (len(word) for word in words)
    return f"The max length is {max_length}"

def find_the_Longest_Word_length(s):
    words = s.split(" ")
    for word in words:
        max_word = max(words, key=len)
        max_length = len(max_word)
    return f"{max_word} >>has the Maximum length as {max_length}"


print(find_the_longest_length_string("I LOVE Python Programming"))

print(find_the_Longest_Word_length("Python is Fast compared to JAVA"))

