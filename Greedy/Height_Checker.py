# Height Checker: https://leetcode.com/problems/height-checker/
"""
The time complexity is O(nlogn) because we sort the heights array, where n is the number of students.
The comparison of the two arrays then takes  O(n) time, so the total time complexity is O(nlogn).

The space complexity is O(n) because we create a new array to store the sorted heights
"""


def heightChecker(heights):
    expected = sorted(heights)
    return sum(h1 != h2 for h1, h2 in zip(heights, expected))

print(heightChecker([1,1,4,2,1,3]))  # Expected output: 3
print(heightChecker([5,1,2,3,4]))  # Expected output: 5
print(heightChecker([1,2,3,4,5]))  # Expected output: 0
