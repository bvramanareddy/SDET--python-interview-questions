def find_largest_element_in_array(arr):
    arr.sort()
    print(f"Sorted Array is {arr}")
    thirdLargest = arr[len(arr)-3]
    return thirdLargest

array = [1,45,6,455,33,99]
print(f"Given Array is {array}")
print(f"Third Largest element from Sorted array is {find_largest_element_in_array(array)}")