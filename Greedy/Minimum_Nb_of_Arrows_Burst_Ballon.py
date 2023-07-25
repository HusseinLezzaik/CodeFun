# Minimum Number of Arrows to Burst Balloons: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# O(NlogN) time, O(1) space
def findMinArrowShots(points):
    if not points:
        return 0

    # Sort the balloons by the end point
    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for i in range(1, len(points)):
        # If the start point of the balloon is after the end of the last balloon
        if points[i][0] > end:
            # Shoot another arrow and update the end point
            arrows += 1
            end = points[i][1]

    return arrows


# Test Cases 
print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # Expected output: 2
print(findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))  # Expected output: 4