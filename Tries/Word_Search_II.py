# Wordh Search II: https://leetcode.com/problems/word-search-ii/

"""
Time complexity: O(M*(4^L)), where M is the number of cells in the board and L is the maximum length of the words. This is because in the worst case scenario, for each cell in the board, we perform a DFS where the word could potentially be constructed from L cells, and at each cell, we could go in any of the four directions.
Space complexity: O(N), where N is the total number of letters in all the words. This is because we store all the words in a Trie, and the space complexity of a Trie is proportional to the sum of the lengths of the words it contains.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def findWords(board, words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.word = word

    def search(node, i, j):
        if node.word:
            res.append(node.word)
            node.word = None
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        char = board[i][j]
        child = node.children.get(char)
        if not child:
            return
        board[i][j] = None
        search(child, i + 1, j)
        search(child, i - 1, j)
        search(child, i, j + 1)
        search(child, i, j - 1)
        board[i][j] = char

    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            search(root, i, j)
    return res

# Test the findWords function

board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

print("Words on the board:", findWords(board, words))  # Expected: ["oath", "eat"]