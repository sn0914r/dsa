# Problem: Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram
# Date: 15-06-2026
# Approach: HashMap (Frequency Counting)
# Time: O(n) | Space: O(n)


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    seen = {}

    for i in s:
        seen[i] = seen.get(i, 0) + 1

    for i in t:
        if i not in seen:
            return False

        if seen[i] == 0:
            return False

        seen[i] -= 1

    return True

print(isAnagram("listen", "silent"))