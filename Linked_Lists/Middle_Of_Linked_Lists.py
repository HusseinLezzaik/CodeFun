# Middle of Linked List: https://leetcode.com/problems/middle-of-the-linked-list/

# O(N) time, O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # If there are two middle nodes, move the slow pointer one more step.
    if fast:
        slow = slow.next

    return slow

