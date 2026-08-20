"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

def two_sum(numsArr, target):
    hash_map = dict()

    for i in range(0, len(numsArr)):
        complement = target - numsArr[i]

        if complement in hash_map:
            return [i, hash_map[complement]]
        
        hash_map[numsArr[i]] = i
        

tc1 = two_sum([2,7,11,15], target = 9)
print(tc1)