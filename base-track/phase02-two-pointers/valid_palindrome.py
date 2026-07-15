# Problem: Valid Palindrome
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-palindrome
# Date: 15-07-2026
# Approach: Two pointers - remove non-alphanumerics, convert to lower case then use two pointers from both end two compare the values
# Time: O(n)| Space O(n)


def validPalindrome(s):
    st = "".join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(st) - 1

    while left < right:
        if st[left] != st[right]:
            return False

        left += 1
        right -= 1

    return True


tc1 = "A man, a plan, a canal: Panama"
tc2 = "race a car"
tc3 = " "

print(validPalindrome(tc1))
print(validPalindrome(tc2))
print(validPalindrome(tc3))
