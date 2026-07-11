# Problem: Top K Frequent Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-elements
# Date: 16-06-2026
# Approach: Hash Map - Count the frequencies of each num, sort the keys based on values in descending order and return the 1st k elements
# Time: O(n log n) | Space: O(n)
# Note: revisit for O(n) bucket sort approach


def topKFrequent(nums, k):
    freq_map = {}

    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    sorted_by_freq = sorted(freq_map, key=freq_map.get, reverse=True)

    return sorted_by_freq[:k]


nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2

print(topKFrequent(nums, k))
