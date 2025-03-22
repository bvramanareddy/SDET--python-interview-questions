def find_the_sum_of_digits_of_given_number(number):
    originalNumber= number
    digitsSum =0
    while number>0:
        num = number %10
        digitsSum+= num
        number = number//10
    return f"The Sum of digits from a Given number {originalNumber} is = {digitsSum}"

print(find_the_sum_of_digits_of_given_number(123))