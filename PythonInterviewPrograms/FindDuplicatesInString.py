def find_the_duplicates_in_a_given_string(string):
    duplicateStrings = set()
    uniqueString = set()
    for ch in string.lower():  # Just converting the String to lower if required only to case sensitive is matters
        if ch in uniqueString:
            duplicateStrings.add(ch)
        else:
            uniqueString.add(ch)
    return duplicateStrings


string = "RaaMmaNNar"

print(find_the_duplicates_in_a_given_string(string))
