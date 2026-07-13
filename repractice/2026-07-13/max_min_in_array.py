# Find maximum and minimum in an array


def maxMinNumsInArr(numArr):
    maximum = float("-inf")
    minimum = float("inf")

    for num in numArr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


testNumArr = [2, 7, 11, 15, 6, 8]
print(maxMinNumsInArr(testNumArr))
