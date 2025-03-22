def find_the_factorial_of_number_using_recursion(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * find_the_factorial_of_number_using_recursion(number - 1)


num = 5
print(f"The Factorial of {num} is {find_the_factorial_of_number_using_recursion(num)}")
