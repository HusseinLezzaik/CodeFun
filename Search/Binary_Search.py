# Leetcode Problem 704
"""
questions around binary search often involve implementing this algorithm with a few math tricks in the problem of how to setup the search problem.
for example looking at leftmost or rightmost index of a target value in a sorted array. pretty easy and fun questions.
"""


# Iterative Solution: O(logn) time | O(1) space
def binarySearch(array, target):
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx <= rightIdx:
        middleIdx = rightIdx + leftIdx // 2
        potentialMatch = array[middleIdx]
        if target == potentialMatch:
            return middleIdx
        elif target > potentialMatch:
            leftIdx = middleIdx + 1
        else:
            rightIdx = middleIdx - 1
    return -1
  
# Recursive Solution: O(logn) time | O(1) space
def binarySearch(array, target):
  return binarySearchHelper(array, target, 0, len(array) -1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return - 1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle -1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)

# Test Cases
print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))  # Expected output: 3
print(binarySearch([1, 5, 23, 111], 111))  # Expected output: 3