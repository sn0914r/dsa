"""
Problem: Two Sum for sorted Array
Appraoch: Two pointers
"""

def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        cur_sum = nums[left] + nums[right]

        if cur_sum == target:
            return left, right
        elif cur_sum > target:
            right -= 1
        else:
            left += 1
    
    return False

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 3, 4]
target = 6
print(two_sum(nums, target))

nums = [2, 3, 4]
target = 100
print(two_sum(nums, target))

