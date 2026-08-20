"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Approach: Hash Set - Iterate through the numbers array and track seen elements in a set and return True if a duplicate is found, otherwise return False.
"""
def contains_duplicates(numsArr):
    hash_set = set()

    for num in numsArr:
        if num in hash_set:
            return True
        hash_set.add(num)

    return False

tc1 = contains_duplicates([10, 3, 6, 3, 7, 8])
print(tc1)

tc2 = contains_duplicates([6, 7, 8, 20, 30, 67])
print(tc2)