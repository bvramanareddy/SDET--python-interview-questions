def count_Char_Occurance(string):
    count_char = {}
    for ch in string:
        count_char[ch] = count_char.get(ch, 0) + 1

    for ch, count in count_char.items():
        print(f"{ch} appeared {count} times")


count_Char_Occurance("ABBCCDDEEE")
