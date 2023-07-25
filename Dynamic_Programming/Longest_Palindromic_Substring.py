# Longest Palindromic Substring: https://leetcode.com/problems/longest-palindromic-substring/

# O(N^2) time, O(N^2) space
def longestPalindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = max_len = 0

    for i in range(n):
        dp[i][i] = True
        for j in range(i):
            if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                dp[j][i] = True
                if i - j + 1 > max_len:
                    max_len = i - j + 1
                    start = j

    return s[start:start + max_len]


# Test Cases
print(longestPalindrome("babad"))  # Expected output: "bab"
print(longestPalindrome("cbbd"))  # Expected output: "bb"
print(longestPalindrome("a"))  # Expected output: "a"