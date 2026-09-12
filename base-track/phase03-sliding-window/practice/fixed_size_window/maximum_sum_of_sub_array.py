def maximum_sum_of_sub_array(arr, size):
    left = 0
    right = size - 1
    current_sum = sum(arr[left: right + 1])
    maximum_sum = current_sum

    while right < len(arr) - 1:
        current_sum -= arr[left]
        left += 1
        right += 1
        current_sum += arr[right]

        if maximum_sum < current_sum:
            maximum_sum = current_sum
    
    return maximum_sum

tc1 = [-2, -5, 6, 4, 3, 8, -1, 0, 9]
maximum_sum = maximum_sum_of_sub_array(tc1, 4)
print(maximum_sum)