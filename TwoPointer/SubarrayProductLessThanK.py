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

