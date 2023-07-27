# First Unique Character from String: https://leetcode.com/problems/first-unique-character-in-a-string/

"""
The time complexity is O(N), where N is the length of the string. 
This is because we're doing a single pass over the string to create the frequency counter, and another pass to find the first unique character.

The space complexity is O(1), because the Counter will hold a maximum of 26 keys (for each letter in the English alphabet), regardless of the size of the input.
"""

from collections import Counter

def firstUniqChar(s):
    frequency = Counter(s)
    for i, char in enumerate(s):
        if frequency[char] == 1:
            return i
    return -1

print(firstUniqChar("leetcode"))  # Expected output: 0
print(firstUniqChar("loveleetcode"))  # Expected output: 2
print(firstUniqChar("aabb"))  # Expected output: -1