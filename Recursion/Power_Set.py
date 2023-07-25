# LeetCode Question Subsets: https://leetcode.com/problems/subsets/

# Iterative Solution: O(n*2^n) time | O(n*2^n) space
def powerset(array):
    subsets = [[]]
    for element in array:
        for i in  range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [element])
    return subsets
  
  # Recursive Solution: O(n*2^n) time | O(n*2^n) space
  def powerset(array, idx =None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx -1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets

# Test Cases
array = [1, 2, 3]
print(powerset(array))  # Expected output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

array = [1, 2, 3, 4]
print(powerset(array))  # Expected output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]