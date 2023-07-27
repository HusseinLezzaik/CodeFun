# Longest Consecutive Sequence: https://leetcode.com/problems/longest-consecutive-sequence/

# O(n) time | O(n) space
def longest_consecutive(nums):
    num_set = set(nums)  # Store unique elements in a HashSet
    longest_streak = 0

    for num in num_set:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Iterate through the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Test 1: Normal case
nums1 = [100, 4, 200, 1, 3, 2]
streak1 = longest_consecutive(nums1)
print(f"For the input {nums1}, the longest consecutive streak is {streak1}. Expected: 4")

# Test 2: Another normal case
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
streak2 = longest_consecutive(nums2)
print(f"For the input {nums2}, the longest consecutive streak is {streak2}. Expected: 9")

# Test 3: Case with consecutive numbers
nums3 = [9, 2, 5, 1, 7, 3]
streak3 = longest_consecutive(nums3)
print(f"For the input {nums3}, the longest consecutive streak is {streak3}. Expected: 3")

(streak1, streak2, streak3)
