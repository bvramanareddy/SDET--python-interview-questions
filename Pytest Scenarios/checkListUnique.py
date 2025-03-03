def checlListHavingUnique(data_list):
    if len(data_list) == len(set(data_list)):
        return True
    else:
        return False

print(checlListHavingUnique([1,3,4,6,7,8,8]))
print(checlListHavingUnique([1,3,4,5]))