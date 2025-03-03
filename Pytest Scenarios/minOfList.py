def find_Min_Max(lst):
    min = lst[0]
    max = lst[0]
    for ele in lst:
        if ele < min:
            min = ele
        if ele > max:
            max = ele

    return min, max

list1= [1,78,43,97,234,7]
min_Ele, max_Ele = find_Min_Max(list1)
print(min_Ele, max_Ele)
