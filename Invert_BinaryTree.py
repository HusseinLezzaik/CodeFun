```
Invert Binary Tree 

LeetCode: https://leetcode.com/problems/invert-binary-tree/
```

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


# 1st Solution | O(n) time | O(n) space | Iterative
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
      current = queue.pop(0)
      if current is None:
        continue
      swapLeftAndRight(current)
      queue.append(current.left)
      queue.append(current.right)

# 2nd Solution | O(n) time | O(d) space | Recursive
def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
