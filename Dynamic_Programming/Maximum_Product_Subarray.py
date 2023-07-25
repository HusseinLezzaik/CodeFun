# Maximum Prodcut Subarray: https://leetcode.com/problems/maximum-product-subarray/

# O(N) time, O(1) space
def maxProduct(nums):
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])

        result = max(result, max_prod)

    return result

# Test Cases
print(maxProduct([2, 3, -2, 4]))  # Expected output: 6
print(maxProduct([-2, 0, -1]))  # Expected output: 0
print(maxProduct([-2]))  # Expected output: -2