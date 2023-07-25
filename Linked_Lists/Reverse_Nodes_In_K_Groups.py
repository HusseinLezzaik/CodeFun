# Reverse Nodes in K Groups: https://leetcode.com/problems/reverse-nodes-in-k-group/

# O(N) time, O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    def reverse_list(head, k):
        prev, curr = None, head
        while k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1
        return prev

    def get_list_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    length = get_list_length(head)

    if length < k:
        return head

    # Reverse the first k nodes.
    new_head = reverse_list(head, k)

    # Recursively reverse the remaining part of the linked list.
    head.next = reverseKGroup(curr, k)

    return new_head
