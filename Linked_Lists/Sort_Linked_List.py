'''
Sort Linked List

Time Complexity: The given code sorts the linked list using the merge sort algorithm, which has a time complexity ofvO(nlogn), where 
n is the number of nodes in the linked list. This is because the list is divided into halves until we reach individual elements (logn divisions), 
and then we merge them back together, comparing all n elements.

Space Complexity: The space complexity of this code is O(n) because of the recursive stack space used during the merge sort. 
In the worst case, there will be n function calls stored in the stack.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def sort_list(self):
        if not self.head or not self.head.next:
            return

        self.head = self._sort_list(self.head)

    def _sort_list(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._sort_list(head)
        right = self._sort_list(next_to_middle)

        return self._merge(left, right)

    def _get_middle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.value < right.value:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result


# Test case 1: Typical case with multiple elements
ll = LinkedList()
ll.append(4)
ll.append(2)
ll.append(1)
ll.append(3)
ll.sort_list()
ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> None

# Test case 2: Empty linked list
ll = LinkedList()
ll.sort_list()
ll.print_list()  # Output: None

# Test case 3: Single element linked list
ll = LinkedList()
ll.append(5)
ll.sort_list()
ll.print_list()  # Output: 5 -> None

# Test case 4: Already sorted linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.sort_list()
ll.print_list()  # Output: 1 -> 2 -> 3 -> None