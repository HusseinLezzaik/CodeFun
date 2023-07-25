# Two Sum: https://leetcode.com/problems/two-sum/

# Solution 1 | O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []
  
# Solution 2 | O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        print("this is num value", num)
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []
  
# Solution 3 | O(nlogn)) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort() # increasing order
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

nums = [2,7,11,15]
target = 9
print(twoNumberSum(nums, target)) # [0,1]

nums = [3,2,4]
target = 6
print(twoNumberSum(nums, target)) # [1,2]