# Problem: Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Date: 14-07-2026
"""
Approach:
- store all numbers in a hash set for fast lookups.
- assume a number as the start of a sequence only if its previous number doesn't exist.
- from each starting number, keep moving forward util the next consecutive number exists.
- track the length of each sequence and return the maximum one.
"""
# Time: O(n) | Space: O(n)


def longestConsecutiveNumbersLength(numsArr):
    numsSet = set(numsArr)
    maxLength = 0

    for num in numsSet:
        if num - 1 not in numsSet:
            cur = num
            curLength = 0

            while cur in numsSet:
                cur += 1
                curLength += 1

            maxLength = max(curLength, maxLength)

    return maxLength


tc1 = [100, 4, 200, 1, 3, 2]
print(longestConsecutiveNumbersLength(tc1))
