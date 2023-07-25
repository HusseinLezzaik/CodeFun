# 986. Interval List Intersections: https://leetcode.com/problems/interval-list-intersections/

# O(n + m) time, O(n + m) space
def intervalIntersection(firstList, secondList):
    i, j = 0, 0
    result = []

    while i < len(firstList) and j < len(secondList):
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])

        if start <= end:
            result.append([start, end])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result


# Test cases
print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
# Expected output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
print(intervalIntersection([[1,3],[5,9]], []))
# Expected output: []
print(intervalIntersection([[1,3],[5,7]], [[2,3],[5,6]]))
# Expected output: [[2,3],[5,6]]
print(intervalIntersection([[10,12],[18,19]], [[2,5],[6,8],[11,14]]))
# Expected output: [[11,12]]
print(intervalIntersection([[5,10]], [[5,6],[7,10]]))
# Expected output: [[5,6],[7,10]]
