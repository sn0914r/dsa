"""
Problem: Longest Consecutive Sequence
"""

def longest_consective_nums(nums):
    nums_set = set(nums)
    max_length = 0

    for num in nums:
        cur_length = 1
        next_num = num + 1

        while next_num in nums_set:
            cur_length += 1
            next_num += 1
        
        max_length = max(cur_length, max_length)
    
    return max_length

nums = [100, 4, 200, 1, 3, 2]
print(longest_consective_nums(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(longest_consective_nums(nums))
