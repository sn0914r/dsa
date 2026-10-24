def max_vowels_optimal(s, k):
    count = 0
    vowels = 'aeiou'

    for ch in s:
        if ch.lower() in vowels:
            count += 1
    best = count

    for right in range(k, len(s)):
        if s[right].lower() in vowels:
            count += 1
        if s[right - k].lower() in vowels:
            count -= 1
        
        best = max(count, best)
    
    return count


s = ['t', 'h', 'i', 's', 'i', 's', 'a', 'l', 'o', 'i', 'n', 'g', 'x']
k = 4

print(max_vowels_optimal(s, k))