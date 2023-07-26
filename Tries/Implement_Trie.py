# Implement Trie (Prefix Tree) - LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree/

"""
Time complexity: For both insert and search operations, it is O(k), where k is the length of the word. For the startsWith operation, it is O(p), where p is the length of the prefix. This is because in the worst case we have to visit each character of the word or prefix.
Space complexity: O(N), where N is the total number of characters in all the words that have been inserted into the Trie. This is because each node in the Trie could potentially store a link/reference to each character in the alphabet.
"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26  # For each letter of alphabet
        self.isEndOfWord = False   # True if node represents end of a word

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self,ch):
        return ord(ch)-ord('a')

    def insert(self, word: str) -> None:
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def search(self, word: str) -> bool:
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl is not None and pCrawl.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        pCrawl = self.root
        length = len(prefix)
        for level in range(length):
            index = self._charToIndex(prefix[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return True

# Test the Trie class
trie = Trie()

trie.insert("apple")
print(trie.search("apple"))  # returns True
print(trie.search("app"))    # returns False
print(trie.startsWith("app")) # returns True
trie.insert("app")
print(trie.search("app"))     # returns True
