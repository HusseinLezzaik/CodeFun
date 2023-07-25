# Three Number Sum: https://leetcode.com/problems/3sum/

# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) -2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets
            
nums = [-1,0,1,2,-1,-4]
target = 0
print(threeNumberSum(nums, target)) # [[-1,-1,2],[-1,0,1]]

nums = [0,0,0,0]
target = 0
print(threeNumberSum(nums, target)) # [[0,0,0]]