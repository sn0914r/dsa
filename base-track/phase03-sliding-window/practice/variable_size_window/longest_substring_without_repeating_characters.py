def longest_substring_without_repeating_characters(arr):
    left = 0
    max_size = 0
    visited_chars = set()

    for right in range(len(arr)):
        while arr[right] in visited_chars:
            visited_chars.remove(arr[left])
            left += 1
        
        visited_chars.add(arr[right])
        max_size = max(max_size, right - left + 1)
    
    return max_size


tc1 = ['t', 'h', 'i', 's', 'i', 's', 'a', 'l', 'o', 'i', 'n', 'g', 'x']
result = longest_substring_without_repeating_characters(tc1)
print(result)
