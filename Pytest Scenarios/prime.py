def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number*0.5)+1):
        if number % i == 0:
            return False
    return True


number= int(input("Enter the Number"))
print(is_prime(number))


def printDivBy5():
    for i in range(1,30):
        if i % 5 == 0:
            print(i)


printDivBy5()

