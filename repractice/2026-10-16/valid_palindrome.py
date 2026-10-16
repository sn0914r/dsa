"""
Problem: Valid Palindrome
Approach: Two pointers

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


def valid_palindrome(s):
    st = "".join(ch.lower() for ch in s if ch.isalnum())
    left = 0
    right = len(st) - 1

    while left < right:
        if st[left] != st[right]:
            return False
        
        left += 1
        right -= 1
    
    return True


s = "A man, a plan, a canal: Panama"
print(valid_palindrome(s))

s = "race a car"
print(valid_palindrome(s))

s = " "
print(valid_palindrome(s))