# Problem: Product of Array Except Self
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-array-except-self
# Date: 17-06-2026
# Approach: Prefix Product + Suffix Product
# Time: O(n) | Space: O(n)

# Notes:
# prefix[i] = product of all elements before i
# suffix[i] = product of all elements after i
# answer[i] = prefix[i] * suffix[i]

def productExceptSelf(nums):
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)

    curProduct = 1
    for i in range(1, len(nums)):
        curProduct *= nums[i - 1]
        prefix[i] = curProduct

    curProduct = 1
    for i in range(len(nums) - 2, -1, -1):
        curProduct *= nums[i + 1]
        suffix[i] = curProduct

    for i in range(0, len(nums)):
        nums[i] = prefix[i] * suffix[i]

    return nums


nums = [1, 2, 3, 4]
productExceptSelf(nums)
print(nums)
