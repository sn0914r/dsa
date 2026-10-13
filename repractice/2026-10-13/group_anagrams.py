"""
Problem: Group anagrams - Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Approach: hashmap

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

def group_anagrams(strs):
    hashmap = dict()

    for e in strs:
        sorted_e = "".join(sorted(e))

        if sorted_e in hashmap:
            hashmap[sorted_e].append(e)
        else:
            hashmap[sorted_e] = [e]
    return list(hashmap.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))