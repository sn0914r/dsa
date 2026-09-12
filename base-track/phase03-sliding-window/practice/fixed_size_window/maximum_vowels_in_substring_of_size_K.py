def is_vowel(ch):
    return ch.lower() in "aeiou"

def maximum_vowels_in_substring_of_size_K(arr, size):
    left = 0
    right = size - 1
    current_count = 0

    for ch in arr[left: right + 1]:
        if is_vowel(ch):
            current_count += 1

    max_count = current_count
    
    while right < len(arr) - 1:
        if is_vowel(arr[left]):
            current_count -= 1

        left += 1
        right += 1

        if is_vowel(arr[right]):
            current_count += 1

        if current_count > max_count:
            max_count = current_count
    
    return max_count


tc1 = ['t', 'h', 'i', 's', 'i', 's', 'a', 'l', 'o', 'i', 'n', 'g', 'x']
maximum_vowels_in_substring = maximum_vowels_in_substring_of_size_K(tc1, 4)
print(maximum_vowels_in_substring)