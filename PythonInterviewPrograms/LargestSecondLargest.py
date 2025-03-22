def find_largest_SecondLargest(nums):
    largest = 0
    secondLargest = 0
    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondSmallest = num
    return largest, secondLargest


arr = [1, 2, 3, 4, 55, 69, 99]
print(f"Given Array is {arr}")
print(f"Largest and SecondLargest are {find_largest_SecondLargest(arr)}")
