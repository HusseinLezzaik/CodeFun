# Squares of a Sorted Array: https://leetcode.com/problems/squares-of-a-sorted-array/

# Solution 1 | O(nlogn) time | O(n) space
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    return sortedSquares

# Solution 2 | O(n) time | O(n) space
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    
    # Initialize two pointers: left at the beginning and right at the end of the array
    left, right = 0, n - 1
    
    # Iterate through the result array from the end to the beginning
    for i in range(n - 1, -1, -1):
        # Compare the squares of the values at left and right pointers
        left_square, right_square = nums[left] ** 2, nums[right] ** 2
        
        # Add the larger square to the result array and move the corresponding pointer
        if left_square > right_square:
            result[i] = left_square
            left += 1
        else:
            result[i] = right_square
            right -= 1
    
    return result

# Test cases
print(sorted_squares([-4, -1, 0, 3, 10])) # Output: [0, 1, 9, 16, 100]
print(sorted_squares([-7, -3, 2, 3, 11])) # Output: [4, 9, 9, 49, 121]

