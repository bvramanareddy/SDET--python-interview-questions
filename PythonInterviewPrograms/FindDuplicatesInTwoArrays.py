def find_duplicates_in_two_arrays(arr1, arr2):
    unique_set= set()
    duplicates= set()
    for i in arr1:
        unique_set.add(i)
    for i in arr2:
        if i in unique_set:
            duplicates.add(i)

    return duplicates

a1= [1,2,3,4,5,6]
a2= [5,6,7,8,9,10]
print(find_duplicates_in_two_arrays(a1,a2))