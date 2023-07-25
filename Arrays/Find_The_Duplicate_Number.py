# Find the Duplicate Number: https://leetcode.com/problems/find-the-duplicate-number/

def findDuplicate(self, nums: List[int]) -> int:
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
