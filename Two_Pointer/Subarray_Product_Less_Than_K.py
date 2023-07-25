# Subarray Product Less Than K: https://leetcode.com/problems/subarray-product-less-than-k/

# O(n^2) time | O(1) space
def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    product = 1
    result = 0
    left = 0

    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product /= nums[left]
            left += 1
        result += (right - left + 1)

    return result

nums = [10, 5, 2, 6]
k = 100
print(num_subarray_product_less_than_k(nums, k))  # Expected output: 8

nums = [1, 2, 3]
k = 0
print(num_subarray_product_less_than_k(nums, k))  # Expected output: 0