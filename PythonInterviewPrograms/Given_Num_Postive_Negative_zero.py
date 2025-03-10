def find_the_number_is_positive_or_negative_zero(num):
    if num > 0:
        return f"Given Number -> {num} is a POSITIVE"
    elif num ==0:
        return f"Given Number -> {num} is ZERO"
    else: return f"Given Number -> {num} is a NEGATIVE"


number = 0
print(find_the_number_is_positive_or_negative_zero(number))