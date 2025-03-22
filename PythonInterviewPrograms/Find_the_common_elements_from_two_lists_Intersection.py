def find_the_intersection_of_two_elements(list1, list2):
    return list(set(list1) & set(list2))  # The & operator will not directly work in list so we converted to set


num1 = [1, 2, 3, 4, 5]
num2 = [1, 2, 3, 7, 8]

intersection = find_the_intersection_of_two_elements(num1, num2)
print(intersection)
