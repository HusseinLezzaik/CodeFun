# Concatenated Words: https://leetcode.com/problems/concatenated-words/

"""
Time complexity: O(NL^2), where N is the number of words and L is the maximum length of a word. This is because we iterate over each word, and for each character in a word, we could potentially be creating a new path in the Trie, which takes O(L) time. Additionally, we perform a DFS for each word, which takes O(L) time. Therefore, the total time complexity is O(NL^2).
Space complexity: O(N*L), where N is the number of words and L is the maximum length of a word. This is because we store all the words in a Trie, and the space complexity of a Trie is proportional to the sum of the lengths of the words it contains.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        trie = Trie()
        for word in words:
            if word:
                trie.addWord(word)

        res = []
        for word in words:
            if self.testWord(word, 0, trie.root, 0, trie):
                res.append(word)
        return res

    def testWord(self, word, index, node, count, trie):
        if index == len(word):
            return count >= 2 if node.endOfWord else False

        if node.endOfWord:
            if self.testWord(word, index, trie.root, count+1, trie):
                return True

        if word[index] not in node.children:
            return False

        return self.testWord(word, index+1, node.children[word[index]], count, trie)

# Test the findAllConcatenatedWordsInADict function
sol = Solution()

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatsdogcat"]
print("Concatenated words:", sol.findAllConcatenatedWordsInADict(words))  # Expected: ["catsdogcats", "dogcatsdog", "ratcatsdogcat"]