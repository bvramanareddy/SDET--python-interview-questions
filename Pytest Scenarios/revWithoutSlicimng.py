def revStringWithoutSlice(string):
    revString = ""
    for char in string:
        revString= char + revString
    return revString
    print(f" The String given in {string} and Reversed String is {revString}")

string = input("Enter the String to Reverse: ")
print(revStringWithoutSlice(string))
