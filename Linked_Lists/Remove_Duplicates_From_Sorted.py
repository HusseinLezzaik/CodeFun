# Remove Duplicates from Sorted Lists: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# O(N) time, O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return head

    current = head

    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head