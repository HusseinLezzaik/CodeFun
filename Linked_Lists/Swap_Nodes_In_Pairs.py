# Swap Nodes in Pairs: https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head or not head.next:
        return head

    # Store the next node.
    next_node = head.next

    # Recursively swap the remaining linked list.
    head.next = swapPairs(next_node.next)
    next_node.next = head

    # Return the new head of the swapped pair.
    return next_node

# Test Case 1
# Create the linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Swap every two adjacent nodes.
result = swapPairs(head)

# Expected output: 2 -> 1 -> 4 -> 3
while result:
    print(result.val, end=" -> ")
    result = result.next

# Test Case 2
# Create the linked list: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Swap every two adjacent nodes.
result = swapPairs(head)

# Expected output: 2 -> 1 -> 3
while result:
    print(result.val, end=" -> ")
    result = result.next

# Test Case 3
# Create an empty linked list.
head = None

# Swap every two adjacent nodes.
result = swapPairs(head)

# Expected output: None (Empty linked list)
print(result)