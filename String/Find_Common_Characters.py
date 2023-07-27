# Find Common Characters: https://leetcode.com/problems/find-common-characters/

"""
The time complexity is O(NM), where N is the number of words and M is the average length of a word. This is because we're iterating over each character of each word.

The space complexity is O(1), because the Counter will hold a maximum of 26 keys (for each letter in the English alphabet), regardless of the size of the input.
"""

from collections import Counter

def commonChars(words):
    result = Counter(words[0])
    for word in words[1:]:
        result &= Counter(word)
    return list(result.elements())

# Test Cases
print(commonChars(["bella", "label", "roller"]))  # Expected output: ['b', 'e', 'l', 'l']
print(commonChars(["cool", "lock", "cook"]))  # Expected output: ['c', 'o']