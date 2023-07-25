# Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# O(N) time, O(N) space
def lengthOfLongestSubstring(s):
    start = 0
    max_length = 0
    chars = set()

    for end in range(len(s)):
        while s[end] in chars:
            chars.remove(s[start])
            start += 1
        chars.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length

# Test Cases
print(lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
print(lengthOfLongestSubstring("bbbbb"))  # Expected output: 1