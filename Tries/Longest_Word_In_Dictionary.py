# Longest Word In Dictionary: https://leetcode.com/problems/longest-word-in-dictionary/

"""
Time complexity: O(N), where N is the total number of characters in all the words. This is because we need to visit each character once when we insert the words into the Trie, and then again when we perform the DFS.
Space complexity: O(N), where N is the total number of characters in all the words. This is because each node in the Trie could potentially store a link/reference to each character in the alphabet, and we store all the words in the Trie.
"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.children[ord(ch) - ord('a')]:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node = node.children[ord(ch) - ord('a')]
        node.endOfWord = True
        node.word = word

class Solution:
    def longestWord(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        return self.dfs(trie.root)

    def dfs(self, node):
        res = node.word
        for child in node.children:
            if child and child.endOfWord:
                temp = self.dfs(child)
                if len(temp) > len(res) or len(temp) == len(res) and temp < res:
                    res = temp
        return res

# Test the longestWord function
sol = Solution()

words = ["w","wo","wor","worl", "world"]
print("Longest word that can be built one character at a time:", sol.longestWord(words))  # Expected: "world"
