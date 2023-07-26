# Course Schedule III: https://leetcode.com/problems/course-schedule-iii/

"""
The time complexity of this solution is O(nlogn) due to the sorting of courses and the use of a heap data structure (where n is the number of courses).
The space complexity is O(n) because in the worst case, all courses will be added to the heap.
"""

class Solution:
    def scheduleCourse(self, courses):
        # Sort the courses by their ending day
        courses.sort(key=lambda x: x[1])
        
        # Initialize a max heap to keep track of the longest durations
        max_heap = []
        time = 0
        
        for course in courses:
            duration, end_day = course
            if time + duration <= end_day:
                # If we have enough time to finish this course, add it to the schedule
                time += duration
                heapq.heappush(max_heap, -duration)
            elif max_heap and -max_heap[0] > duration:
                # If this course can be finished quicker than the longest one in the schedule, replace it
                time += duration + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -duration)
        
        return len(max_heap)

# Test the scheduleCourse function
sol = Solution()

courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print("The maximum number of courses that can be taken is:", sol.scheduleCourse(courses))  # return 3
