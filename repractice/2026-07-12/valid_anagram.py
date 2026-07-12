# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isValidAnagram(s, t):
    if len(s) != len(t):
        return False

    hashMap = {}

    for i in s:
        if i in hashMap:
            hashMap[i] += 1
            continue
        hashMap[i] = 1

    for i in t:
        if i not in hashMap:
            return False

        hashMap[i] -= 1

        if hashMap[i] == 0:
            del hashMap[i]

    return True


print(isValidAnagram("anagram", "nagaram"))
print(isValidAnagram("siva", "nanda"))
print(isValidAnagram("ate", "eat"))
