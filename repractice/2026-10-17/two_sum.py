"""
Problem: Two Sum
Approach: Hashmap - calculate and store the complements in the hashmap while checking if the complement exists in the hashmap for every element during iteration

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

def two_sum(nums, target):
    hashmap = dict()

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [i, hashmap[complement]]
        
        hashmap[nums[i]] = i

nums = [2, 7, 11, 15]
target = 26

print(two_sum(nums, target))