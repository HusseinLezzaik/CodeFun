# Maximum XOR of Two Numbers in an Array: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

"""
Time complexity: O(N), where N is the number of elements in the input array. This is because we need to traverse the array twice, once to insert all the numbers into the Trie and once to find the maximum XOR for each number.
Space complexity: O(N), where N is the number of elements in the input array. This is because in the worst case scenario, each number would be stored in a separate path in the Trie, leading to a space complexity of O(N).
"""

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def findMaxXOR(self, num):
        node = self.root
        maxXOR = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggle_bit = 1 - bit
            if toggle_bit in node.children:
                maxXOR |= (1 << i)
                node = node.children[toggle_bit]
            else:
                node = node.children[bit]
        return maxXOR

class Solution:
    def findMaximumXOR(self, nums):
        trie = Trie()
        for num in nums:
            trie.insert(num)
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, trie.findMaxXOR(num))
        return max_xor

# Test the findMaximumXOR function
sol = Solution()

nums = [3, 10, 5, 25, 2, 8]
print("Maximum result of nums[i] XOR nums[j]:", sol.findMaximumXOR(nums))  # Expected: 28