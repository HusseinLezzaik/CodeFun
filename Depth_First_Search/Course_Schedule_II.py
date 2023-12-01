# Course Schedule II: https://leetcode.com/problems/course-schedule-ii/
"""
the main element of this question is that it teaches how to do topological sort using DFS.

Time complexity: O(N + P), where N is the number of courses and P is the number of prerequisites. This is because we need to visit each course and each prerequisite once.
Space complexity: O(N + P), due to the space needed to store the course dictionary, the checked list, the path list, and the result list.
"""

from collections import defaultdict
from typing import List

# O(N + P) time | O(N + P) space - where N is the number of courses and P is the number of prerequisites
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        checked = [False] * numCourses
        path = [False] * numCourses
        res = []

        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path, res):
                return []
        return res[::-1]

    def isCyclic(self, currCourse, courseDict, checked, path, res):
        if checked[currCourse]: 
            return False
        if path[currCourse]: 
            return True

        path[currCourse] = True

        for nextCourse in courseDict[currCourse]:
            if self.isCyclic(nextCourse, courseDict, checked, path, res):
                return True

        path[currCourse] = False
        checked[currCourse] = True
        res.append(currCourse)
        return False

# Test the findOrder function
sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print("Ordering of courses:", sol.findOrder(numCourses, prerequisites))  # Expected: [0,1,2,3] or [0,2,1,3]