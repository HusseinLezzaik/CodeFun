# Maximum Height by Stacking Cuboids: https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

"""
The time complexity is O(n^2), where n is the number of cuboids. This is because we perform a double loop to calculate the longest increasing subsequence.

The space complexity is O(n), because we store the maximum height for each cuboid in the dp array.
"""

def maxHeight(cuboids):
    for cuboid in cuboids:
        cuboid.sort()
    cuboids.append([0, 0, 0])
    cuboids.sort()

    dp = [0] * len(cuboids)
    for i in range(len(cuboids)):
        for j in range(i):
            if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                dp[i] = max(dp[i], dp[j] + cuboids[i][2])
    return max(dp)

print(maxHeight([[50,45,20],[95,37,53],[45,23,12]]))  # Expected output: 190
print(maxHeight([[38,25,45],[76,35,3]]))  # Expected output: 76
print(maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))  # Expected output: 102