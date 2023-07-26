# Palindrome Pairs: https://leetcode.com/problems/palindrome-pairs/

"""
Time complexity: O(n * m^2), where n is the number of words and m is the average length of a word. This is because for each word, we check for each substring (including the word itself), which takes O(m^2) time, and we do this for all the words.
Space complexity: O(n * m), where n is the number of words and m is the average length of a word. This is because we store all the words in a dictionary, and the space complexity of a dictionary is proportional to the number of entries in it.
"""

class Solution:
    def palindromePairs(self, words):
        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right+1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            sub = s[left:right+1]
            return sub == sub[::-1]

        n = len(words)
        indices = {word[::-1]: i for i, word in enumerate(words)}

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m+1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret

# Test the palindromePairs function
sol = Solution()

words = ["abcd","dcba","lls","s","sssll"]
print("Palindrome pairs:", sol.palindromePairs(words))  # Expected: [[0, 1], [1, 0], [3, 2], [2, 4]]