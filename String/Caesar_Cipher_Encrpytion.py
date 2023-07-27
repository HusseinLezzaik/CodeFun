# Caesar Cipher Encryption

"""
The time complexity is O(NM), where N is the number of strings and M is the maximum length of a string.
This is because we're iterating over each character of each string.

The space complexity is O(NM), because in the worst case if all the strings are different then we need to store all of them in the hash map.
"""


from collections import defaultdict

def groupStrings(strings):
    groups = defaultdict(list)
    for s in strings:
        key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
        groups[key].append(s)
    return list(groups.values())

print(groupStrings(["abc", "bcd", "acd", "dfg"]))  # Expected output: [['abc', 'bcd'], ['acd', 'dfg']]