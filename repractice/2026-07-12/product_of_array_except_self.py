"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation
"""


def productOfArrayExceptSelf(numArr):
    l = len(numArr)
    prefix = [1] * l
    suffix = [1] * l
    output = [1] * l

    currentProduct = 1

    for i in range(1, l):
        currentProduct *= numArr[i - 1]
        prefix[i] = currentProduct

    currentProduct = 1

    for i in range(l - 2, -1, -1):
        currentProduct *= numArr[i + 1]
        suffix[i] = currentProduct

    for i in range(l):
        output[i] = prefix[i] * suffix[i]

    return output


testNumArr = [1, 2, 3, 4]
print(productOfArrayExceptSelf(testNumArr))

testNumArr2 = [-1, 1, 0, -3, 3]
print(productOfArrayExceptSelf(testNumArr2))
