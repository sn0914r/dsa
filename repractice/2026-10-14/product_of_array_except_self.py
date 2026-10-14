"""
Problem: Product of Array Except Self
Approach: Prefix Products + Suffix Products

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

def product_of_array_except_self(nums):
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)
    result = [1] * len(nums)

    cur_product = 1
    for i in range(1, len(nums)):
        cur_product *= nums[i - 1]
        prefix[i] = cur_product

    cur_product = 1
    for i in range(len(nums) - 2, -1, -1):
        cur_product *= nums[i + 1]
        suffix[i] = cur_product
    
    for i in range(len(nums)):
        result[i] = prefix[i] * suffix[i]

    return result

nums = [1,2,3,4]
print(product_of_array_except_self(nums))

nums = [-1,1,0,-3,3]
print(product_of_array_except_self(nums))