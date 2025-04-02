def is_palindrome(s):
    s1= s.lower()
    return s1 == s1[::-1]

def is_palindrome_withExactCharMach(s):
    return s == s[::-1]


print(is_palindrome("RAMmar"))
print(is_palindrome_withExactCharMach("RAMAR"))