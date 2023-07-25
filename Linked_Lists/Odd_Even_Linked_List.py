# Odd Even Linked List: https://leetcode.com/problems/odd-even-linked-list/

# O(N) time, O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = head
    even_head = head.next

    odd_curr = odd_head
    even_curr = even_head

    while even_curr and even_curr.next:
        odd_curr.next = even_curr.next
        odd_curr = odd_curr.next
        even_curr.next = odd_curr.next
        even_curr = even_curr.next

    odd_curr.next = even_head
    return odd_head

# Test Case 1
# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Group nodes with odd indices together followed by nodes with even indices.
result = oddEvenList(head)

# Expected output: 1 -> 3 -> 5 -> 2 -> 4
while result:
    print(result.val, end=" -> ")
    result = result.next

# Test Case 2
# Create the linked list: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(7)

# Group nodes with odd indices together followed by nodes with even indices.
result = oddEvenList(head)

# Expected output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
while result:
    print(result.val, end=" -> ")
    result = result.next

# Test Case 3
# Create the linked list: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Group nodes with odd indices together followed by nodes with even indices.
result = oddEvenList(head)

# Expected output: 1 -> 3 -> 2
while result:
    print(result.val, end=" -> ")
    result = result.next