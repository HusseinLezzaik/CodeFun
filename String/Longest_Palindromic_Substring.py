# Longest Palindromic Substring: https://leetcode.com/problems/longest-palindromic-substring/

"""
The time complexity is O(n^2), because we're filling up a nxn table.
The space complexity is also O(n ^2), because we're using a nxn table to store whether the substring is palindrome or not.
"""

def longestPalindrome(s):
    n = len(s)
    maxLength = 1
    start = 0
    table = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        table[i][i] = True
    
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            maxLength = 2
    
    for L in range(3, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if table[i + 1][j - 1] and s[i] == s[j]:
                table[i][j] = True
                if L > maxLength:
                    start = i
                    maxLength = L
    return s[start:start + maxLength]


# Test Cases
print(longestPalindrome("babad"))  # Expected output: "bab"
print(longestPalindrome("cbbd"))  # Expected output: "bb"
print(longestPalindrome("a"))  # Expected output: "a"
print(longestPalindrome("ac"))  # Expected output: "a"