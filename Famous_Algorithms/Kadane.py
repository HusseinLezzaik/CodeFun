# Kadane's algorithm is a dynamic programming algorithm used to find the maximum sum of a contiguous subarray in an array of integers.

"""
The time complexity of Kadane's algorithm is O(n), where n is the length of the input array. This is because we traverse the array once.

The space complexity is O(1), because we only use a constant amount of space to store the variables max_global and max_current

"""

def kadanes_algorithm(array):
    max_global = max_current = array[0]
    for num in array[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

# Test cases
print(kadanes_algorithm([-2, -3, 4, -1, -2, 1, 5, -3]))  # Output: 7
print(kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
