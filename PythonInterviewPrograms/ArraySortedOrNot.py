def check_array_is_sorted_or_not(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

arr = [1,2,3,5,7]
print(f"Is given array {arr} sorted: {check_array_is_sorted_or_not(arr)}")