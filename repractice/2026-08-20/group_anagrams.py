"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Approach: Hash Map - Sort each string to create a key, and append the original string to the corresponding list in the hash map.
"""
from collections import defaultdict

def group_anagrams(strArr):
    hash_map = defaultdict(list)

    for s in strArr:
        sorted_s = "".join(sorted(s))
        hash_map[sorted_s].append(s)
    
    return list(hash_map.values())

tc1 = group_anagrams(["eat","tea","tan","ate","nat","bat"])
print(tc1)