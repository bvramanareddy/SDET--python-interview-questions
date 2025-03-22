def find_smallest_SecondSmallest(nums):
    smallest = float('inf')
    secondSmallest = float('inf')
    for num in nums:
        if num < smallest:
            secondSmallest = smallest
            smallest = num
        elif num < secondSmallest and num!= smallest:
            secondSmallest = num
    return  smallest, secondSmallest

arr = [1,2,55,67,834,4,3]
print(f"Given array is {arr}")
print(f" Smallest and Second Smallest values are {find_smallest_SecondSmallest(arr)}")