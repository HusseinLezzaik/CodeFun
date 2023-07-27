# Find the Duplicate Number: https://leetcode.com/problems/find-the-duplicate-number/

# O(n) time | O(1) space
def findDuplicate(nums):
    # Step 1: Find the intersection point of the two pointers
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Step 2: Find the entrance to the cycle (duplicate number)
    ptr1 = nums[0]
    ptr2 = tortoise

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

# Test 1: Normal case
nums1 = [3, 1, 3, 4, 2]
dup1 = findDuplicate(nums1)
print(f"For the input {nums1}, the duplicate number is {dup1}. Expected: 3")

# Test 2: Another normal case
nums2 = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
dup2 = findDuplicate(nums2)
print(f"For the input {nums2}, the duplicate number is {dup2}. Expected: 9")

# Test 3: Case with smallest possible list
nums3 = [1, 1]
dup3 = findDuplicate(nums3)
print(f"For the input {nums3}, the duplicate number is {dup3}. Expected: 1")

(dup1, dup2, dup3)