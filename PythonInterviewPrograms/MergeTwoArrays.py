def merge_two_arrays(arr1, arr2):
    return arr1 + arr2


array1 = [1, 2, 4]
array2 = [5, 6, 9]

merged_Array = merge_two_arrays(array1, array2)
print("Printing the Merged Array using concat opertarr + ", merged_Array)


def merge_two_arrays_UsingExtend(arr1, arr2):
    return arr1.extend(arr2)


merge_two_arrays_UsingExtend(array1, array2)

print("Printing the MergedArray using the Extend method", array1)
