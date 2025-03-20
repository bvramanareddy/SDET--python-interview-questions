"""Use List Comprehensions instead of Loops"""
from multiprocessing import Pool

# using a Comprehension (FAST)
squares = [i ** 2 for i in range(10)]
print(squares)

# Using a Loop (SLOW)
squares1 = []
for i in range(10):
    squares1.append(i ** 2)
print(squares1)

""" Use Built-In Methods if available for faster execution"""
# Manual Summation (SLOW)
total1 = 0
for i in range(10):
    total1 += i
print(total1)

# using Buil-In SUM method
total = sum(range(10))
print(total)

""" Reduce overusing The variables"""
# Using An Extra Variable

name = "RAMANA Reddy"
length = len(name)
print(length)

# Using Directly in fucntion
print(len("Ramana REDDY Boda"))

"""Use MultiProcess for CPU Intensive Tasks and When Multiple cores improve efficiency"""


def square(n):
    return n ** 2


if __name__ == "__main__":
    with Pool(4) as p:  # Here we are using 4 worker Processes
        result = p.map(square, range(5))
    print(result)

"""The output of the above is except for the square will be executed 4 times as we are using 4 cores"""
