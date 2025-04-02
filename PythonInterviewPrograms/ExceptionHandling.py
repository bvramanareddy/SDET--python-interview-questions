#This one give errors, and we need to handle it to avoid termination in program
#x= 10/0

# This will handle the Error to some extent see below
#try:
#    x=10/0
#except:
#    print("This did not work!")

# To handle it gracefully we can use below implementation

try:
    answer = input("Enter a number to divide 10 by ")
    num =int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("you cant divide by zero")
except ValueError as e:
    print("you have not given a valid number")
    print(e)
finally:
    print("Your code always runs this part")


