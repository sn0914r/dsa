"""
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings
"""

def encode(str_arr):
    encoded_string = ""

    for s in str_arr:
        encoded_string += f"{len(s)}#{s}"
    
    return encoded_string
    

def decode(encoded_string):
    decoded_strings = []
    currentIndex = 0

    while currentIndex < len(encoded_string):
        delimiter = currentIndex

        while encoded_string[delimiter] != "#":
            delimiter += 1
        
        wordStartIndex = delimiter + 1
        wordEndIndex = wordStartIndex + int(encoded_string[currentIndex:delimiter])
        decoded_strings.append(encoded_string[wordStartIndex: wordEndIndex])
        currentIndex = wordEndIndex
    
    return decoded_strings
    

tc1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

encoded = encode(tc1)
print(encoded)

print(decode(encoded))