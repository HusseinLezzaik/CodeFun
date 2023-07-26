# Merge K Sorted Lists: https://leetcode.com/problems/merge-k-sorted-lists/

"""
Time complexity: O(N log k), where N is the total number of nodes in all linked lists and k is the number of linked lists. This is because we process each node in the linked lists once and a heap operation takes log k time.
Space complexity: O(k), because we keep at most k pointers to nodes in the heap
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Now, let's define the mergeKLists function

import heapq

class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        curr = dummy
        heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heap.append((lists[i].val, i))
                lists[i] = lists[i].next

        heapq.heapify(heap)

        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            
            if lists[idx] is not None:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next

# Test the mergeKLists function
sol = Solution()

lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
merged_list = sol.mergeKLists(lists)
output = []
while merged_list is not None:
    output.append(merged_list.val)
    merged_list = merged_list.next
print("The merged list is:", output)  # Expected: [1, 1, 2, 3, 4, 4, 5, 6]