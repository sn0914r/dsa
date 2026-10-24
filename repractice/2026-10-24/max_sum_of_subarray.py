arr = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum_of_subarray_bruteforce(nums, size):
    max_window_sum = 0
    for left in range(0, len(nums) - size + 1):
        window_sum = 0
        for right in range(left, left + size):
            window_sum += nums[right]
        max_window_sum = max(window_sum, max_window_sum)
    
    return max_window_sum
    


print(max_sum_of_subarray_bruteforce(arr, k))

def max_sum_of_subarray_optimal(nums, size):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - size]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(max_sum_of_subarray_optimal(arr, k))
