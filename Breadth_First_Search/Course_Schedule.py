# Course Schedule: https://leetcode.com/problems/course-schedule/
"""
Time complexity: O(N + P), where N is the number of courses and P is the number of prerequisites. This is because we first add all prerequisites to the adjacency list (which takes O(P) time), and then we process all nodes in the graph (which takes O(N) time).
Space complexity: O(N + P), due to the space needed to store the adjacency list and the in-degree array.
"""


from collections import deque

# O(N + P) time | O(N + P) space - where N is the number of courses and P is the number of prerequisites
class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degree[course] += 1

        stack = deque([node for node in range(numCourses) if in_degree[node] == 0])
        topological_order = []

        while stack:
            node = stack.pop()
            topological_order.append(node)

            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)

        return topological_order if len(topological_order) == numCourses else []

# Test the findOrder function
sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print("Ordering of courses:", sol.findOrder(numCourses, prerequisites))  # Expected: [0,1,2,3] or [0,2,1,3]
