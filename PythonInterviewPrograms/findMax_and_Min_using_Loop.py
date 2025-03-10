def find_the_max_min_using_Loop(numbers):
    max = 0
    min = 0
    for num in numbers:
        if num > max:
            max = num
        elif num < min:
            min = num
    return f"The Maximum, Minimum values from the given list are {max} and {min} "

def find_max_min_Simple_inbuilt(numss):
    maxx = max(numss)
    minn = min(numss)
    return f"{maxx} , {minn} are Maximum and Minimum from the list "

nums= [1,56,78,9,7,34,55,999]
print(find_the_max_min_using_Loop(nums))
print(find_max_min_Simple_inbuilt(nums))

