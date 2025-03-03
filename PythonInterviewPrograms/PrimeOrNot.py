import math


def is_prime(num):
    if num <=1:
        return f"{num} is Not a Prime"
    for i in range(2, int(math.sqrt(num))+ 1):
    #We can also use >>> for i in range(2, int(num**0.5) + 1):
        if num % i ==0:
            return f"{num} is Not a Prime"
    return f"{num} is a Prime"

print(is_prime(4))