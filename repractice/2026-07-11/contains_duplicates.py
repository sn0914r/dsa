# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def containsDuplicateValues(numsArr):
    hashSet = set()

    for num in numsArr:
        if num in hashSet:
            return True
        hashSet.add(num)

    return False


testNums = [1, 2, 3, 4, 5, 5, 6]
print(containsDuplicateValues(testNums))  # True
