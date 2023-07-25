# 56. Merge Intervals: https://leetcode.com/problems/merge-intervals/

# O(NlogN) time, O(N) space
def merge(intervals):
    if not intervals:
        return []

    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for current in intervals:
        previous = result[-1]
        # If the current interval overlaps with the previous one, merge them
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            # If not, add the current interval to the result
            result.append(current)

    return result


# Test Cases
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Expected output: [[1,6],[8,10],[15,18]]
print(merge([[1, 4], [4, 5]]))  # Expected output: [[1,5]]