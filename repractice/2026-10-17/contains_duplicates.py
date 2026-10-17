"""
Problem: Contains Duplicates - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Approach: Hashset - track the elements in hashset and return False if we see already tracked element else return True

Example:
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
"""

def contains_duplicates(arr):
    hashset = set()

    for e in arr:
        if e in hashset:
            return True
        
        hashset.add(e)
    
    return False

nums = [1,2,3,1]
print(contains_duplicates(nums))

nums = [1,2,3,4]
print(contains_duplicates(nums))