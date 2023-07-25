# Minimum Window Substring: https://leetcode.com/problems/minimum-window-substring/

from collections import defaultdict

# O(m+n) time, O(m+n) space
def minWindow(s, t):
    dict_t = defaultdict(int)
    for c in t:
        dict_t[c] += 1

    start = 0
    min_length = float('inf')
    min_start = 0
    dict_window = defaultdict(int)
    matched = 0

    for end in range(len(s)):
        if s[end] in dict_t:
            dict_window[s[end]] += 1
            if dict_window[s[end]] <= dict_t[s[end]]:
                matched += 1

        while matched == len(t):
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_start = start

            if s[start] in dict_t:
                dict_window[s[start]] -= 1
                if dict_window[s[start]] < dict_t[s[start]]:
                    matched -= 1
            start += 1

    return "" if min_length == float('inf') else s[min_start:min_start+min_length]

# Test Cases
print(minWindow("ADOBECODEBANC", "ABC"))  # Expected output: "BANC"
print(minWindow("a", "a"))  # Expected output: "a"