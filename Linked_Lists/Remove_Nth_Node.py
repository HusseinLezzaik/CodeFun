"""
Remove Nth Node From End of List: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

The trick here is to use two pointers, and have the second pointer take N steps more than the first pointer.
That way when it hits the end of the linked list, the first pointer will be at the target point and all we need to do is do the swap.
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
