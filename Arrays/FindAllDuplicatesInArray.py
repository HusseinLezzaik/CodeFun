def findDuplicates(nums):
    result = []
    
    for num in nums:
        if nums[abs(num) - 1] < 0:
            result.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
            
    return result

