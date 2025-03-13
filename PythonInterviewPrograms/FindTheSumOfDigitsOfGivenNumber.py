def find_the_sum_of_digits_of_given_number(number):
    sumOfDigits = 0
    while number>0:
        singleDigit = number%10
        sumOfDigits+= singleDigit
        number = number//10
    return sumOfDigits


number = 1234
print(f"The sum of Digits in given number {number}  is {find_the_sum_of_digits_of_given_number(number)}")