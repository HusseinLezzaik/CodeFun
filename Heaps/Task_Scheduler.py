# Task Scheduler: https://leetcode.com/problems/task-scheduler/

"""
Time complexity: O(N), where N is the number of tasks, because we process each task in the input list once.
Space complexity: O(1), because we use a heap to store the frequencies of the tasks, and there can be at most 26 tasks.
"""
import collections
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        frequencies = collections.Counter(tasks)
        heap = [-freq for freq in frequencies.values()]
        heapq.heapify(heap)
        
        time = 0
        while heap:
            temp = []
            for _ in range(n + 1):
                if heap:
                    task = heapq.heappop(heap)
                    if task < -1:
                        temp.append(task + 1)
                time += 1
                if not heap and not temp:
                    break
            for task in temp:
                heapq.heappush(heap, task)
        return time

# Test the leastInterval function
sol = Solution()

tasks = ["A","A","A","B","B","B"]
n = 2
print("The least number of units of times that the CPU will take to finish all the given tasks is:", sol.leastInterval(tasks, n))  # Expected: 8
