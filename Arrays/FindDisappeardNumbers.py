def findDisappearedNumbers(nums):
    n = len(nums)
    missing_nums = []
    for i in range(n):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    for i in range(n):
        if nums[i] > 0:
            missing_nums.append(i+1)
    return missing_nums

