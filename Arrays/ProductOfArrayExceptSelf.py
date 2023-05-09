def product_except_self(nums):
    n = len(nums)
    
    # Initialize the answer array
    answer = [1] * n

    # Calculate left_products and store them in answer
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Calculate right_products and store the final product in answer
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

