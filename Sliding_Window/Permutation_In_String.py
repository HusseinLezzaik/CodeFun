# Permutation in String: https://leetcode.com/problems/permutation-in-string/

from collections import Counter

# O(n) time | O(1) space
def checkInclusion(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 > len_s2:
        return False

    freq_s1 = Counter(s1)
    freq_window = Counter()

    for i in range(len_s2):
        freq_window[s2[i]] += 1
        if i >= len_s1:
            if freq_window[s2[i - len_s1]] == 1:
                del freq_window[s2[i - len_s1]]
            else:
                freq_window[s2[i - len_s1]] -= 1
        if freq_s1 == freq_window:
            return True

    return False


# Test Cases
print(checkInclusion("ab", "eidbaooo"))  # Expected output: True
print(checkInclusion("ab", "eidboaoo"))  # Expected output: False