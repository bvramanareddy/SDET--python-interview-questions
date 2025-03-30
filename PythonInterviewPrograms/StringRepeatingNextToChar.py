def printTheSameCharacterNextToLetter(string):
    res_list = []
    unique= set()

    for char in string:
        res_list.append(char)
        if char in unique:
            res_list.append(char)
        unique.add(char)
        res_list.append(char)

    return ''.join(res_list)

print(printTheSameCharacterNextToLetter("abcd"))