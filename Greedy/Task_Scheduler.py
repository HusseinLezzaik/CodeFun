# Task Scheduler: https://leetcode.com/problems/task-scheduler/

import collections
import heapq

# O(N) time, O(1) space
def leastInterval(tasks, n):
    task_counts = collections.Counter(tasks)
    queue = [-count for count in task_counts.values()]
    heapq.heapify(queue)

    total_time = 0

    while queue:
        temp_list = []
        for _ in range(n+1):
            if queue:
                task = heapq.heappop(queue)
                if task < -1:
                    temp_list.append(task+1)
        for item in temp_list:
            heapq.heappush(queue, item)
        total_time += n+1 if queue else len(temp_list)
    
    return total_time

# Test Cases
print(leastInterval(["A","A","A","B","B","B"], 2))  # Expected output: 8
print(leastInterval(["A","A","A","B","B","B"], 0))  # Expected output: 6