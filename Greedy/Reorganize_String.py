# Reorganize String: https://leetcode.com/problems/reorganize-string/

import heapq
import collections

# O(NlogK) time, O(K) space
def reorganizeString(s):
    # Count the frequency of each character
    count = collections.Counter(s)
    max_count = max(count.values())
    length = len(s)

    # If the number of the most frequent character is more than (n + 1) / 2,
    # a valid arrangement is not possible
    if max_count > (length + 1) // 2:
        return ""

    # Add all characters to a priority queue
    heap = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(heap)

    result = []

    while len(heap) > 1:
        freq1, char1 = heapq.heappop(heap)
        freq2, char2 = heapq.heappop(heap)
        result.extend([char1, char2])
        if freq1 + 1:
            heapq.heappush(heap, (freq1 + 1, char1))
        if freq2 + 1:
            heapq.heappush(heap, (freq2 + 1, char2))

    return "".join(result) + (heap[0][1] if heap else '')


# Test Cases
print(reorganizeString("aab"))  # Expected output: "aba"
print(reorganizeString("aaab"))  # Expected output: ""
print(reorganizeString("vvvlo"))  # Expected output: "vlvov"