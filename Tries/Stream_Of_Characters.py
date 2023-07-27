# Stream of Characters: https://leetcode.com/problems/stream-of-characters/description/

"""
The time complexity for the query operation is O(M), where M is the length of the longest word. This is because in the worst case, we would need to check for a match for the longest word in the list.

The space complexity is O(N), where N is the total number of characters in all the words. This is because we are storing all the words in the Trie.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class StreamChecker:
    def __init__(self, words):
        self.trie = TrieNode()
        self.stream = []
        for word in words:
            node = self.trie
            for ch in reversed(word):
                if not ch in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

    def query(self, letter):
        self.stream.append(letter)
        node = self.trie
        for ch in reversed(self.stream):
            if ch in node.children:
                node = node.children[ch]
                if node.is_word:
                    return True
            else:
                break
        return False

streamChecker = StreamChecker(["cd", "f", "kl"])
print(streamChecker.query("a"))  # Expected output: False
print(streamChecker.query("b"))  # Expected output: False
print(streamChecker.query("c"))  # Expected output: False
print(streamChecker.query("d"))  # Expected output: True
print(streamChecker.query("e"))  # Expected output: False
print(streamChecker.query("f"))  # Expected output: True
print(streamChecker.query("g"))  # Expected output: False
print(streamChecker.query("h"))  # Expected output: False
print(streamChecker.query("i"))  # Expected output: False
print(streamChecker.query("j"))  # Expected output: False
print(streamChecker.query("k"))  # Expected output: False
print(streamChecker.query("l"))  # Expected output: True