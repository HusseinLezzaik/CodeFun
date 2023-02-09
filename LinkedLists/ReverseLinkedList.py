```
Reverse Linked List

LeetCode: https://leetcode.com/problems/reverse-linked-list/description/ 

```

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
