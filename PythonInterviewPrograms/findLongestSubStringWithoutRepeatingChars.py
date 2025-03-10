def find_the_longest_subString_WithoutRepeating_Chars(string):
    char_set= set()
    left =0
    max_length =0
    for right in range(len(string)):
        while string[right] in char_set:
            char_set.remove(string[left])
            left = left +1
        else:
            char_set.add(string[right])
            max_length = max(max_length, right-left +1)
    return max_length

print(find_the_longest_subString_WithoutRepeating_Chars("abcabcbb"))