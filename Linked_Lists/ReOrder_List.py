"""
LeetCode: https://leetcode.com/problems/reorder-list/

Main trick: using slow and fast pointers to find the middle of the linked list and then reversing the second half of the linked list.
The slow pointer will end up at the middle of the linked list when the fast pointer reaches the end of the linked list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
