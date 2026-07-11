# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


def topKFrequentElements(numArr, k):
    hash_map = {}

    for num in numArr:
        if num not in hash_map:
            hash_map[num] = 0

        hash_map[num] += 1

    return sorted(hash_map, key=lambda k: hash_map[k], reverse=True)[:k]


testNums = [1, 2, 3, 1, 2, 1]
print(topKFrequentElements(testNums, 2))
