# Reverse Linked List: LeetCode: https://leetcode.com/problems/reverse-linked-list/description/

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Iterative | O(n) time | O(1) space - n is depth of Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev = None
        while head != None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev

# Recursive | O(n) time | O(n) space (max depth of recursive stack)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head

"""
class Node:
    
    Node class to represent a single node in the linked list.
    
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    
    Reverses a linked list.

    :param head: The head node of the linked list.
    :return: The new head node of the reversed linked list.
    
    previous = None (*)
    current = head (*)
    while current is not None:
        next_node = current.next  # Remember next node
        current.next = previous  # Reverse the link
        previous = current       # Move previous to this node
        current = next_node      # Move to next node
    return previous

# Helper function to print the linked list
def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Create a simple linked list for demonstration 1->2->3->4->None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original Linked List:")
print_list(head)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

print("Reversed Linked List:")
print_list(reversed_head)

"""