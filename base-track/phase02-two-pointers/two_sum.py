# Problem: Two pointers
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum
# Date: 15-07-2026
# Approach: Two pointers - use pointers at both ends of the sorted array. If sum < target then increment left pointer, if sum > target, decrement right pointer.
# Time: O(n)| Space O(1)


def twoSumInSortedArray(sortedNumsArr, target):
    left = 0
    right = len(sortedNumsArr) - 1

    while left < right:
        sum = sortedNumsArr[left] + sortedNumsArr[right]
        if sum == target:
            return left, right
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1


nums = [2, 7, 11, 15]
target = 9
print(twoSumInSortedArray(nums, target))

nums = [2, 3, 4]
target = 6
print(twoSumInSortedArray(nums, target))
