# My approach: remove a whole distinct character group when needed
def longest_substring_with_almost_K_distinct_characters(arr, k):
    left = 0
    max_len = 0
    freq = {}
    unq_count = 0
    coords = ()

    for right in range(len(arr)):
        if arr[right] not in freq:
            unq_count += 1

        freq[arr[right]] = freq.get(arr[right], 0) + 1
        
        while unq_count > k:
            target = arr[left]

            while freq[target] > 0:
                freq[arr[left]] -= 1
                left += 1

            del freq[target] 
            unq_count -= 1
        
        if right - left + 1 > max_len:
            max_len = right - left + 1
            coords = (left, right)
    
    return max_len, coords

tc1 = ['t', 'h', 'i', 's', 'i', 's', 'a', 'l', 'o', 'i', 'n', 'g', 'x']
result = longest_substring_with_almost_K_distinct_characters(tc1, 4)
print(result)

# Standard approach: shrink the window one character at a time
def standard_approach(arr, k):
    left = 0
    max_size = 0
    coords = ()
    freq = {}

    for right in range(len(arr)):
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        while len(freq) > k:
            target = arr[left]
            freq[target] -= 1

            if freq[target] == 0:
                del freq[target]
            
            left += 1
        
        if right - left + 1 > max_size:
            max_size = right - left + 1
            coords = (left, right)
        
    
    return max_size, coords

result = standard_approach(tc1, 4)
print(result)
