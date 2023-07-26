# Populating Next Right Pointers in Each Node: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return None

        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()

                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

# Create a binary tree for testing
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Test the connect function
sol = Solution()
root = sol.connect(root)

# Print the values of the nodes next to each node
print("Node next to 1:", root.next)  # Expected: None
print("Node next to 2:", root.left.next.val)  # Expected: 3
print("Node next to 3:", root.right.next)  # Expected: None
print("Node next to 4:", root.left.left.next.val)  # Expected: 5
print("Node next to 5:", root.left.right.next.val)  # Expected: 6
print("Node next to 6:", root.right.left.next.val)  # Expected: 7
print("Node next to 7:", root.right.right.next)  # Expected: None