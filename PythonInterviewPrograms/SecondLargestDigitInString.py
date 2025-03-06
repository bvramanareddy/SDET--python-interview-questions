def find_Second_Largest_Digit(s):
    d= set()
    for ch in s:
        if ch.isdigit():
            d.add(int(ch))

    sorted_digits = sorted(d, reverse=True)

    if len(sorted_digits) >1:
        return sorted_digits[1]
    return -1


print("Second Largest is ",find_Second_Largest_Digit("str34ui89"))
