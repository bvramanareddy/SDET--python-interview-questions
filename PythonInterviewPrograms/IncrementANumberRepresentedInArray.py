def increment_Number_givenInArray(input_array):
    num = int("".join(map(str, input_array)))
    num = num + 1
    return [int(digit) for digit in str(num)]


print(increment_Number_givenInArray([9, 9, 9]))
print(increment_Number_givenInArray([1, 0, 0]))
