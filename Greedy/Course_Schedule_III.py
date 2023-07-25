# Course Schedule III: https://leetcode.com/problems/course-schedule-iii/

import heapq

# O(NlogN) time, O(N) space
def scheduleCourse(courses):
    # Sort the courses by their end day
    courses.sort(key=lambda x: x[1])

    # Initialize a max heap for the durations of the courses
    heap = []
    time = 0

    for course in courses:
        duration, end = course
        # If we can finish the course before or on its end day, add it to the heap
        if time + duration <= end:
            time += duration
            heapq.heappush(heap, -duration)
        # If we cannot, but its duration is less than the max duration in the heap, replace the max duration with this one
        elif heap and -heap[0] > duration:
            time += duration + heapq.heappop(heap)
            heapq.heappush(heap, -duration)

    return len(heap)


# Test Cases
print(scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))  # Expected output: 3
print(scheduleCourse([[1, 2]]))  # Expected output: 1