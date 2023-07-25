# Four Sum: https://leetcode.com/problems/4sum/

# Average: O(n^2) time and space
# Worst: O(n^3) time | O(n^2) space

def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array)- 1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets

# Test cases
array = [7, 6, 4, -1, 1, 2]
targetSum = 16
print(fourNumberSum(array, targetSum))  # Expected output: [[7, 6, 4, -1], [7, 6, 1, 2]]

array = [1, 2, 3, 4, 5, 6, 7]
targetSum = 10
print(fourNumberSum(array, targetSum))  # Expected output: [[1, 2, 3, 4]]