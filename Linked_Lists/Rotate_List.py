# Rotate List: https://leetcode.com/problems/rotate-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or k == 0:
        return head

    # Step 1: Find the length of the linked list.
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Calculate the new rotation point k.
    k %= length

    if k == 0:
        return head

    # Step 3: Traverse to the kth node from the end.
    prev = None
    curr = head
    for _ in range(length - k):
        prev = curr
        curr = curr.next

    # Step 4: Perform the rotation.
    tail.next = head
    prev.next = None

    return curr

# Test Case 1
# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Rotate the linked list to the right by k = 2 places.
k = 2
result = rotateRight(head, k)

# Expected output: 4 -> 5 -> 1 -> 2 -> 3
while result:
    print(result.val, end=" -> ")
    result = result.next

# Test Case 2
# Create the linked list: 0 -> 1 -> 2
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)

# Rotate the linked list to the right by k = 4 places.
k = 4
result = rotateRight(head, k)

# Expected output: 2 -> 0 -> 1
while result:
    print(result.val, end=" -> ")
    result = result.next

# Test Case 3
# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Rotate the linked list to the right by k = 0 places.
k = 0
result = rotateRight(head, k)

# Expected output: 1 -> 2 -> 3 -> 4 -> 5
while result:
    print(result.val, end=" -> ")
    result = result.next
