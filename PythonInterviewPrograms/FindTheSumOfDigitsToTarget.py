def findTheDigitsToMatchTheTarget(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return nums[left], nums[right]
        elif sum < target:
            left += 1
        else:
            right += 1

    return []


nums = [1, 2, 3, 4, 5]
target = 9
print(findTheDigitsToMatchTheTarget(nums, target))
