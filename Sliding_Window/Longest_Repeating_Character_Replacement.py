# 424. Longest Repeating Character Replacement: https://leetcode.com/problems/longest-repeating-character-replacement/

# O(N) time, O(1) space
def characterReplacement(s, k):
    count = [0]*26
    max_freq = 0
    window_start = 0
    max_length = 0

    for window_end in range(len(s)):
        count[ord(s[window_end]) - ord('A')] += 1
        max_freq = max(max_freq, count[ord(s[window_end]) - ord('A')])
        if (window_end - window_start + 1) - max_freq > k:
            count[ord(s[window_start]) - ord('A')] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


# Test cases
print(characterReplacement("ABAB", 2))  # Expected output: 4
print(characterReplacement("AABABBA", 1))  # Expected output: 4
print(characterReplacement("AAAB", 0))  # Expected output: 3
print(characterReplacement("BAAAB", 2))  # Expected output: 5
print(characterReplacement("AAB", 2))  # Expected output: 3
