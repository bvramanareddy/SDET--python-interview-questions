def find_smallest_largest_sec_largest_sec_smallest(nums):
    nums.sort()
    smallest = nums[0]
    largest = nums[len(nums)-1]
    secLargest = nums[len(nums)-2]
    secSmallest = nums[1]
    return smallest, secSmallest, largest, secLargest

arr = [1,2,344,6,56,8,88,3]
print(f"Given array is {arr}")
print(f"Smallest- Second Smallest,  Largest, Second Largest values are {find_smallest_largest_sec_largest_sec_smallest(arr)}")