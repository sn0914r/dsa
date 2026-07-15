def encode(strings):
    encodedStrings = ""

    for s in strings:
        encodedStrings += str(len(s)) + "#" + s

    return encodedStrings


def decode(s):
    decodedStrings = []
    currentIndex = 0

    while currentIndex < len(s):
        delimiter = currentIndex

        while s[delimiter] != "#":
            delimiter += 1

        wordStartIndex = delimiter + 1
        wordEndIndex = wordStartIndex + int(s[currentIndex:delimiter])
        decodedStrings.append(s[wordStartIndex:wordEndIndex])
        currentIndex = wordEndIndex


    return decodedStrings


tc1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

encoded = encode(tc1)
print(encoded)

print(decode(encoded))
