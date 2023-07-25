# Odd Even Linked Lists: https://leetcode.com/problems/odd-even-linked-list/

# O(N) time, O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = odd = head
    even_head = even = head.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return odd_head
