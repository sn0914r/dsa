# Problem: Three sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/3sum
# Date: 23-10-2026
# Approach(optimal): Two pointers
# Time: O(n^2)


nums = [0,0,0]

def three_sum_brute_force(nums):
    res = set()
    n = len(nums)

    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[k] + nums[j] == 0:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    
    return list(res)

print(three_sum_brute_force(nums))

def three_sum_optimal(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(0, n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return res

print(three_sum_optimal(nums))