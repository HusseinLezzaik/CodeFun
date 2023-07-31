# Prefix and Sufix Search: https://leetcode.com/problems/prefix-and-suffix-search/

"""
Time complexity: O(N * L^2) for initialization, where N is the number of words and L is the maximum length of a word. This is because we iterate over each word, and for each character in a word, we could potentially be creating a new path in the Trie, which takes O(L) time. The f function has a time complexity of O(L), where L is the length of the prefix and suffix.
Space complexity: O(N * L^2), where N is the number of words and L is the maximum length of a word. This is because we store all the words in a Trie, and the space complexity of a Trie is proportional to the sum of the lengths of the words it contains.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class WordFilter:
    def __init__(self, words):
        self.trie = TrieNode()
        for index in range(len(words)):
            word = words[index]
            word = word + '#' + word
            for i in range(len(word)):
                node = self.trie
                node.index = index
                for j in range(i, len(word)):
                    node = node.children.setdefault(word[j], TrieNode())
                    node.index = index

    def f(self, prefix: str, suffix: str) -> int:
        node = self.trie
        for char in suffix + '#' + prefix:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.index

# Test the WordFilter class

words = ["apple"]
wordFilter = WordFilter(words)
print(wordFilter.f("a", "e"))  # Expected: 0
print(wordFilter.f("b", ""))  # Expected: -1
