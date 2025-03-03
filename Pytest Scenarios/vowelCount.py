def countVowels(string):
    vowels = set("aeiouAEIOU")
    vowelCount=0
    for char in string:
        if char in vowels:
            vowelCount+=1
    return vowelCount

print(countVowels("Ramana"))
