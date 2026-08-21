"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

approach: 2 pointers
"""

def is_palindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
        
    return True


tc1 = "A man, a plan, a canal: Panama"
tc2 = "race a car"
tc3 = " "

print(is_palindrome(tc1))
print(is_palindrome(tc2))
print(is_palindrome(tc3))
