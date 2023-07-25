# Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    def reverse_list(head):
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def find_middle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Find the middle of the linked list.
    middle = find_middle(head)

    # Reverse the second half of the linked list.
    reversed_second_half = reverse_list(middle)

    # Compare the values of the first half with the reversed second half.
    while reversed_second_half:
        if head.val != reversed_second_half.val:
            return False
        head = head.next
        reversed_second_half = reversed_second_half.next

    return True
