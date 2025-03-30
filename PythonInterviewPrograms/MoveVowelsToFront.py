def move_vowels_to_front(string):
    vowelsString = []
    cosonentString = []
    for c in string:
        if isVowel(c):
            vowelsString.append(c)
        else:
            cosonentString.append(c)
    return ''.join(vowelsString) + ''.join(cosonentString)


def isVowel(ch):
    return ch in "AEIOUaeiou"



print(move_vowels_to_front(input("Enter the String ")))

