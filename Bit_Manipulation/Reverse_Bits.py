# Reverse Bits: https://leetcode.com/problems/reverse-bits/

# O(logn) time | O(1) space
def reverse_bits(n):
    result = 0
    while n > 0:
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Let's run some tests
test_cases = [0, 1, 6, 1234567890, 2**32 - 1]
results = [(n, bin(n), reverse_bits(n), bin(reverse_bits(n))) for n in test_cases]
results
