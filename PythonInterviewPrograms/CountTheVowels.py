#Question : Count the number of vowels in a given string.
# Explanation
def count_vowels(s):
  vowels = "aeiouAEIOU"
  return sum(1 for char in s if char in vowels)

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

def count_Vowels2(s):
    vowels= "aeiouAEIOU"
    vowel_Count= 0
    for char in s:
        if char in vowels:
            vowel_Count+=1
    return vowel_Count

print(count_Vowels2("RAMANA"))
