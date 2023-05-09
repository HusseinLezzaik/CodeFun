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

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4
