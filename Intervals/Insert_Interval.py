# Insert Interval: https://leetcode.com/problems/insert-interval/

# O(N) time, O(N) space
def insert(intervals, newInterval):
    result = []
    i = 0

    # Add to the result all the intervals ending before newInterval starts
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge all overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add the merged interval
    result.append(newInterval)

    # Add all the rest
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result

# Test cases
print(insert([[1,3],[6,9]], [2,5]))
# Expected output: [[1,5],[6,9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# Expected output: [[1,2],[3,10],[12,16]]
print(insert([], [5,7]))
# Expected output: [[5,7]]
print(insert([[1,5]], [2,3]))
# Expected output: [[1,5]]
print(insert([[1,5]], [2,7]))
# Expected output: [[1,7]]