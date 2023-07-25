# Non-Overlapping Intervals: https://leetcode.com/problems/non-overlapping-intervals/

# O(NlogN) time, O(1) space
def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Sort intervals by the end time
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]
    count = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # Overlapping interval
            count += 1
        else:
            end = intervals[i][1]  # Update the end time

    return count

# Test Cases
print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # Expected output: 1
print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))  # Expected output: 2
print(eraseOverlapIntervals([[1, 2], [2, 3]]))  # Expected output: 0