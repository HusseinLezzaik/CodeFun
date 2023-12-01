# Linked List Cycle: https://leetcode.com/problems/linked-list-cycle/
"""
we can solve this problem using a hash table pretty easily, but the trick is to solve it using constant space.
We can do this by using two pointers, one that moves one node at a time, and one that moves two nodes at a time.

using floyd's cycle-finding algorithm, we can determine if there is a cycle in the linked list. 
they will always meet no matter where they start whenever we have a cycle and it happens in linear time!!

many problems involving linked lists can be solved using this two pointer technique, and that's usually the trick you need to know.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

# Test Cases
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(hasCycle(head))  # Expected output: True