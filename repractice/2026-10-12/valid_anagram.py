"""
Problem: Valid Anagram
Approach: Hashmap - Store the frequences of characters of first string in hashmap and then subtract the frequencies of characters of second string, if the frequency reaches 0 or below then return False else True

Example:
Input: s = "anagram", t = "nagaram"
Output: true
"""

def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    hashmap = dict()

    for ch in s:
        if ch in hashmap:
            hashmap[ch] += 1
        else:
            hashmap[ch] = 1
    
    for ch in t:
        if ch in hashmap:
            hashmap[ch] -= 1
            if hashmap[ch] == 0:
                del hashmap[ch]
        else:
            return False
    
    return True
        

s = "listen"
t = "silent"
print(valid_anagram(s, t))

s = "nagaram"
t = "anagram"
print(valid_anagram(s, t))