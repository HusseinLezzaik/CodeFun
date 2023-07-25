# Maximum Number of Vowels in a Substring of Given Length: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# O(N) time, O(1) space
def maxVowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    window_vowels = sum(1 for i in range(k) if s[i] in vowels)
    max_vowels = window_vowels

    for i in range(k, len(s)):
        window_vowels += (s[i] in vowels) - (s[i - k] in vowels)
        max_vowels = max(max_vowels, window_vowels)

    return max_vowels

# Test Cases
print(maxVowels("abciiidef", 3))  # Expected output: 3
print(maxVowels("aeiou", 2))  # Expected output: 2
print(maxVowels("leetcode", 3))  # Expected output: 2