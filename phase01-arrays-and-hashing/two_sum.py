# Problem: Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# Date: 15-06-2026
# Approach: hashmap - store complement as we iterate
# Time: O(n) | Space: O(n)


def twoSum(nums, target):
    seen = {}

    for i in range(0, len(nums)):
        n = target - nums[i]
        if n in seen:
            return [i, seen[n]]
        seen[nums[i]] = i


nums = [2, 7, 11, 15]
print(twoSum(nums, 26))
