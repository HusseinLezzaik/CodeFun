# Next Greater Element I: https://leetcode.com/problems/next-greater-element-i/

# Time Complexity: O(n) | Space Complexity: O(n)
def nextGreaterElement(nums1, nums2):
    stack, hashmap = [], {}
    for num in nums2:
        while stack and stack[-1] < num:
            hashmap[stack.pop()] = num
        stack.append(num)
    return [hashmap.get(x, -1) for x in nums1]


nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))  # Outputs: [-1,3,-1]

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))  # Outputs: [3,-1]