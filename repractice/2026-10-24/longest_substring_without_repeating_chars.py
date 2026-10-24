def longest_substring_without_repeating_chars_optimal(s):
    left = 0
    best = 0
    seen = set()
    
    for right in range(0, len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        best = max(best, right - left + 1)
    
    return best


s = "abcabcbb"
print(longest_substring_without_repeating_chars_optimal(s))