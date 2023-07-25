# 442. Find All Duplicates in an Array: https://leetcode.com/problems/find-all-duplicates-in-an-array/

# O(n) time | O(1) space
def find_duplicates(nums):
    duplicates = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            duplicates.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return duplicates



print(find_duplicates([4,3,2,7,8,2,3,1]))  # Expected output: [2, 3]
print(find_duplicates([1,1,2]))  # Expected output: [1]
print(find_duplicates([1]))  # Expected output: []