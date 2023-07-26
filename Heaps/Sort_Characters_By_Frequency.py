# Sort Characters By Frequency: https://leetcode.com/problems/sort-characters-by-frequency/

"""
Time complexity: O(n log n), where n is the length of the string, because we perform a heap operation for each character in the string and a heap operation takes log n time.
Space complexity: O(n), because we use a heap and a counter to store the characters and their frequencies.
"""

import collections
import heapq

class Solution:
    def frequencySort(self, s):
        counter = collections.Counter(s)
        heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(heap)
        return ''.join([-freq * char for freq, char in heap])

# Test the frequencySort function
sol = Solution()

s = "tree"
print("The sorted string is:", sol.frequencySort(s))  # return "eert" or "eetr"