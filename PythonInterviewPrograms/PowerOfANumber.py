def findPowerOfANumber(number, power):
    if number ==0:
        return 1
    if power == 1:
        return number
    return number * findPowerOfANumber(number, power-1)

num = 5
pow = 2
print(findPowerOfANumber(num, pow))
