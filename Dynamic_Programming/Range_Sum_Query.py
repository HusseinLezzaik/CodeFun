# Range Sum Query: https://leetcode.com/problems/range-sum-query-immutable/

# O(N) time, O(N) space
class NumArray:
    def __init__(self, nums):
        self.presum = [0]
        for num in nums:
            self.presum.append(self.presum[-1] + num)

    def sumRange(self, left, right):
        return self.presum[right + 1] - self.presum[left]

# Test Cases
test = NumArray([-2, 0, 3, -5, 2, -1])
print(test.sumRange(0, 2))  # Expected output: 1
print(test.sumRange(2, 5))  # Expected output: -1
print(test.sumRange(0, 5))  # Expected output: -3