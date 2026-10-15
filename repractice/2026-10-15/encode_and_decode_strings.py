"""
Problem: encode and decode strings
"""
def encode(strs):
    encoded_str = ""

    for s in strs:
        encoded_str += f"{len(s)}#{s}"
    return encoded_str

def decode(str):
    strs = []
    i = 0

    while i < len(str):
        if str[i] == "#":
            length = int(str[i - 1])
            extracted_str = str[i + 1: i + 1 + length]
            strs.append(extracted_str)
            i += length
        else:
            i += 1
    
    return strs



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

encoded = encode(strs)
print(encoded)

print(decode(encoded))
