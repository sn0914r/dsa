"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def twoSum(numArr, target):
    hashMap = {}

    for i in range(0, len(numArr)):
        c = target - numArr[i]

        if c in hashMap:
            return [i, hashMap[c]]

        hashMap[numArr[i]] = i

    return False


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums,target))