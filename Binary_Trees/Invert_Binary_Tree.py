"""
Invert Binary Tree 

LeetCode: https://leetcode.com/problems/invert-binary-tree/

the trick with binary trees questions usually involves recursion, going bottom up instead of top down to save (O(n)) in complexity.
also more tricks involves computing heights, diameters and keeping track of them to use this meta data.

also you can use BFS or DFS to solve binary tree questions.

intuitively, you can see that DFS is a very efficient and easy to implement recursive algorithm - and many tree problems can be easily solved via recursion of patterns.
and so the solution ends up at the intersection of using DFS and recursion.

also some questions have binary search tree inputs, which opens up the tricks of binary search algorithms (makes time complexity o(logn)).
"""
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


# Test case 1
tree1 = BinaryTree(1)
tree1.left = BinaryTree(2)
tree1.right = BinaryTree(3)
tree1.left.left = BinaryTree(4)
tree1.left.right = BinaryTree(5)
tree1.right.left = BinaryTree(6)
tree1.right.right = BinaryTree(7)
tree1.left.left.left = BinaryTree(8)
tree1.left.left.right = BinaryTree(9)
tree1.left.right.left = BinaryTree(10)

invertBinaryTree(tree1)
print(tree1.value)
print(tree1.left.value)
print(tree1.right.value)
print(tree1.left.left.value)
print(tree1.left.right.value)
print(tree1.right.left.value)
print(tree1.right.right.value)
print(tree1.left.left.left.value)
print(tree1.left.left.right.value)
print(tree1.left.right.left.value)