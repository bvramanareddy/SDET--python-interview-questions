def find_most_repeated_char_and_count(string):

    chars = [ch for ch in string]
    print(chars)
    charDict = {}

    for char in chars:
        charDict[char]= charDict.get(char, 0)+1

    print(charDict)
    most_repeatedChar = max(charDict, key=charDict.get)
    max_count= charDict[most_repeatedChar]
    print(f" Most Repeated Char is {most_repeatedChar}")
    print(f" Most repeated char appeared {max_count}")


find_most_repeated_char_and_count("ABBCCCDDDD")