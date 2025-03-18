def isPanagram(sentence):
    set1 = set()
    for ch in sentence.lower():
        if ch >= 'a' and ch <= 'z':
            set1.add(ch)
    if len(set1) == 26:
        return f"{sentence} is an Panagram"
    else:
        return f"{sentence} is NOT A panagram"


sent = "abcDEFGHIJKLMNOPqrstuvwxyz";
notPAn = "hello world"
print(isPanagram(sent))
print(isPanagram(notPAn))
