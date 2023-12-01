"""
leetcode: https://leetcode.com/problems/last-stone-weight/

time complexity: O(nlogn)

Heapifying the stones: heapq.heapify(stones) has a time complexity of O(n), where n is the number of stones.
Main loop: The while loop runs as long as there are more than one stone in the heap. In each iteration, two stones are popped from the heap, and possibly one new stone is pushed back. Popping from a heap (heapq.heappop) is O(log n) operation, and pushing onto a heap (heapq.heappush) is also O(log n). In the worst case, this loop runs for n-1 iterations (as each iteration effectively removes one stone from consideration).
Thus, each iteration has a time complexity of O(log n), and there are up to n-1 iterations, resulting in a total time complexity of O(n log n).
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

# There's a private _heapify_max method.
# https://github.com/python/cpython/blob/1170d5a292b46f754cd29c245a040f1602f70301/Lib/heapq.py#L198
class Solution(object):
    def lastStoneWeight(self, stones):
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)
        
        stones.append(0)
        return stones[0]
