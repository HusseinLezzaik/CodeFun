# Implement Trie (Prefix Tree) - LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree/

"""
Time complexity: For both insert and search operations, it is O(k), where k is the length of the word. For the startsWith operation, it is O(p), where p is the length of the prefix. This is because in the worst case we have to visit each character of the word or prefix.
Space complexity: O(N), where N is the total number of characters in all the words that have been inserted into the Trie. This is because each node in the Trie could potentially store a link/reference to each character in the alphabet.

the main advantage of using a trie is that we can search for a word in O(L) time, where L is the length of the word.
compare this to a hashset, where we would have to search through all the words in the set to see if the word exists.
so like if you have 10^6 words in a string, it would take forever whereas here its very fast..

that's why it's called a prefix tree.
"""
# Method 1: actually note that it's more efficient to use a list of 26 elements instead of a dictionary for children; but both work
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here, code in functions is pretty repetitive.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix. same as search except we don't need to check if curr.end == True
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True


# Method 2
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
