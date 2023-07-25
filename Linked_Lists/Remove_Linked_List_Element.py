# Remove Linked List Element: https://leetcode.com/problems/remove-linked-list-elements/

# O(N) time, O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    # Create a dummy node to handle the case where the first node has the given value.
    dummy = ListNode(0)
    dummy.next = head

    prev, curr = dummy, head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return dummy.next

