# Problem: container with most water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/
# Date: 23-10-2026
# Approach(optimal): Two pointers -
# Time: O(n)| Space O(1)

def container_with_most_water_bruteforce(heights):
    max_water = 0
    n = len(heights)
    
    for i in range(0, n):
        for j in range(i + 1, n):
            cur_water = min(heights[i], heights[j]) * (j - i)
            max_water = max(max_water, cur_water)
    
    return max_water

def container_with_most_water_optimal(heights):
    left = 0
    right = len(heights) - 1
    max_water = 0

    while left < right:
        cur_water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, cur_water)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_water



heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(container_with_most_water_bruteforce(heights))
print(container_with_most_water_optimal(heights))