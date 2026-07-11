# Problem: Contains Duplicates
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate
# Date: 15-06-2026
# Approach: Hash Set - track seen elements and return true when a duplicate is found
# Time: O(n) | Space: O(n)


def containsDuplicate(nums):
    seen = set()

    for i in nums:
        if i in seen:
            return True

        seen.add(i)

    return False


nums = [1, 2, 3]
print(containsDuplicate(nums))
