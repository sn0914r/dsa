"""
Problem: Top K Frequent Elements
Approach: Hashmap - Store the frequencies in hashmap, then sort it by values and return first k elements

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

def top_k_frequent_elements(arr, k):
    hashmap = dict()

    for n in nums:
        if n in hashmap:
            hashmap[n] += 1
        else:
            hashmap[n] = 1
        
    entires = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for i in range(k):
        result.append(entires[i][0])

    return result    

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(top_k_frequent_elements(nums, k))