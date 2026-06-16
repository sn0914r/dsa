# Problem: Group Anagrams
# Difficulty: Medium
# Link: https://leetcode.com/problems/group-anagrams
# Date: 16-06-2026
# Approach: Hash Map - Sort each string to create a key, then group all strings with the same sorted key into a list.
# Time: O(n * k log k)| Space O(n)


def groupAnagrams(strs):
    hash_map = {}

    for s in strs:
        key = "".join(sorted(s))
        hash_map.setdefault(key, []).append(s)

    return list(hash_map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
