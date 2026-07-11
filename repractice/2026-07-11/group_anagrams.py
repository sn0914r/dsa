# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

sortStr = lambda s: "".join(sorted(s))


def groupAnagrams(sArr):
    hash_map = {}

    for s in sArr:
        sortedStr = sortStr(s)

        if sortedStr not in hash_map:
            hash_map[sortedStr] = []

        hash_map[sortedStr].append(s)

    return list(hash_map.values())


testStrs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(testStrs))
